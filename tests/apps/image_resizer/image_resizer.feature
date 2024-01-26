Feature: Controller
    Tests related with external requests

    Scenario: Resize image in AWS
        Given An URI of an image
        And Desired sizes

        When I post the URI of the image and desired sizes

        Then I get the image with desired sizes
