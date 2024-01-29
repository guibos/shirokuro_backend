Feature: Account
    Tests related with account creation

    Scenario: Create account
        Given account_id
        And password
        And email

        When I put data to the api

        Then I get a 200 or 202 http response
