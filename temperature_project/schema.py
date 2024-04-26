import graphene
from graphene_django.types import DjangoObjectType
from django.db.models import Min, Max
from temperature.models import TemperatureReading

class TemperatureReadingType(DjangoObjectType):
    class Meta:
        model = TemperatureReading

class TemperatureRangeType(graphene.ObjectType):
    min_temperature = graphene.Float()
    max_temperature = graphene.Float()

class Query(graphene.ObjectType):
    latest_temperature_reading = graphene.Field(TemperatureReadingType)
    temperature_range_stats = graphene.Field(
        TemperatureRangeType,
        after=graphene.DateTime(required=True),
        before=graphene.DateTime(required=True)
    )

    def resolve_latest_temperature_reading(self, info):
        # Retrieve the most recent temperature reading based on the timestamp
        return TemperatureReading.objects.order_by('-timestamp').first()

    def resolve_temperature_range_stats(self, info, after, before):
        # Aggregate the min and max temperatures within the specified timestamp range
        aggregation = TemperatureReading.objects.filter(
            timestamp__gte=after,
            timestamp__lte=before
        ).aggregate(
            min_temperature=Min('temperature'),
            max_temperature=Max('temperature')
        )
        return TemperatureRangeType(
            min_temperature=aggregation.get('min_temperature'),
            max_temperature=aggregation.get('max_temperature')
        )

schema = graphene.Schema(query=Query)
