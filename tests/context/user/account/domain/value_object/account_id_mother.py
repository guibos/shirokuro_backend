from context.user.account.domain.value_object.account_id import AccountId


class AccountIdMother:
    @staticmethod
    def create() -> AccountId:
        return AccountId()
