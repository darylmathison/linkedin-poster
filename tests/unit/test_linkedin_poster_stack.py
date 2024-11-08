import aws_cdk as core
import aws_cdk.assertions as assertions

from linkedin_poster.linkedin_poster_stack import LinkedinPosterStack

# example tests. To run these tests, uncomment this file along with the example
# resource in linkedin_poster/linkedin_poster_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LinkedinPosterStack(app, "linkedin-poster")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
