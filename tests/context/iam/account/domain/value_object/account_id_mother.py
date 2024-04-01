from context.shared.domain.value_types.account.account_id import AccountId


class AccountIdMother:

    @staticmethod
    def create() -> AccountId:
        return AccountId()
