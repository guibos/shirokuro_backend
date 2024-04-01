from context.shared.domain.criteria.criteria_schema import CriteriaSchema


class Criteria(list):
    @classmethod
    def from_schema(cls, criteria_schema: CriteriaSchema) -> 'Criteria':
        return cls(criteria_schema)
