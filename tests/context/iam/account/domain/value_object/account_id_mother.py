from context.iam.account.domain.value_object.account_id import AccountId


class AccountIdMother:
    @staticmethod
    def create() -> AccountId:
        return AccountId()
