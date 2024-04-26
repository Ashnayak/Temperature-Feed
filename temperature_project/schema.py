import graphene
from graphene_django.types import DjangoObjectType
from django.db.models import Min, Max
from temperature.models import TemperatureReading

class TemperatureReadingType(DjangoObjectType):
    class Meta:
        model = TemperatureReading

class TemperatureRangeType(graphene.ObjectType):
    min = graphene.Float()
    max = graphene.Float()

class Query(graphene.ObjectType):
    current_temperature = graphene.Field(TemperatureReadingType)
    temperature_statistics = graphene.Field(
        TemperatureRangeType,
        after=graphene.DateTime(required=True),
        before=graphene.DateTime(required=True)
    )

    def resolve_current_temperature(self, info):
        # Retrieve the most recent temperature reading based on the timestamp
        return TemperatureReading.objects.order_by('-timestamp').first()

    def resolve_temperature_statistics(self, info, after, before):
        # Aggregate the min and max temperatures within the specified timestamp range
        aggregation = TemperatureReading.objects.filter(
            timestamp__gte=after,
            timestamp__lte=before
        ).aggregate(
            min=Min('value'),
            max=Max('value')
        )
        return TemperatureRangeType(
            min=aggregation.get('min'),
            max=aggregation.get('max')
        )

schema = graphene.Schema(query=Query)
