import factory

from app.models.charts import Chart, Entry
from app.models.users import User


class UserFactory(factory.Factory):
    class Meta:
        model = User

    name = factory.Sequence(lambda n: f'teste{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.name}@teste.com')
    password = factory.LazyAttribute(lambda obj: f'{obj.name}@example.com')


class EntryFactory(factory.Factory):
    class Meta:
        model = Entry

    text = factory.Sequence(lambda n: f'entrada{n}')
    result = factory.Sequence(lambda n: n)


class ChartFactory(factory.Factory):
    class Meta:
        model = Chart

    name = factory.Sequence(lambda n: f'chart{n}')
    code = factory.Sequence(lambda n: f'A{n}')
    dice = 'd20'

    @factory.post_generation
    def entries_size(self, create, extracted, **kwargs):
        if not create:
            return

        size = extracted if isinstance(extracted, int) else 12

        if size > 0:
            entries = []
            for i in range(size):
                entry = EntryFactory(
                    text=f'entry{i + 1}',
                    result=str(i + 1),
                    chart_uuid=self.uuid,
                )
                entries.append(entry)
            self.entries = entries
