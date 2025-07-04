# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T13:39:31+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity
from fastapi import Header

from models import (
    CreateSavingsPlanPostRequest,
    CreateSavingsPlanResponse,
    DeleteQueuedSavingsPlanPostRequest,
    DeleteQueuedSavingsPlanResponse,
    DescribeSavingsPlanRatesPostRequest,
    DescribeSavingsPlanRatesResponse,
    DescribeSavingsPlansOfferingRatesPostRequest,
    DescribeSavingsPlansOfferingRatesResponse,
    DescribeSavingsPlansOfferingsPostRequest,
    DescribeSavingsPlansOfferingsResponse,
    DescribeSavingsPlansPostRequest,
    DescribeSavingsPlansResponse,
    InternalServerException,
    ListTagsForResourcePostRequest,
    ListTagsForResourceResponse,
    ResourceNotFoundException,
    ServiceQuotaExceededException,
    TagResourcePostRequest,
    TagResourceResponse,
    UntagResourcePostRequest,
    UntagResourceResponse,
    ValidationException,
)

app = MCPProxy(
    contact={
        'email': 'mike.ralphson@gmail.com',
        'name': 'Mike Ralphson',
        'url': 'https://github.com/mermade/aws2openapi',
        'x-twitter': 'PermittedSoc',
    },
    description='Savings Plans are a pricing model that offer significant savings on AWS usage (for example, on Amazon EC2 instances). You commit to a consistent amount of usage, in USD per hour, for a term of 1 or 3 years, and receive a lower price for that usage. For more information, see the <a href="https://docs.aws.amazon.com/savingsplans/latest/userguide/">AWS Savings Plans User Guide</a>.',
    license={'name': 'Apache 2.0 License', 'url': 'http://www.apache.org/licenses/'},
    termsOfService='https://aws.amazon.com/service-terms/',
    title='AWS Savings Plans',
    version='2019-06-28',
    servers=[
        {
            'description': 'The AWSSavingsPlans multi-region endpoint',
            'url': 'http://savingsplans.{region}.amazonaws.com',
            'variables': {
                'region': {
                    'default': 'us-east-1',
                    'description': 'The AWS region',
                    'enum': [
                        'us-east-1',
                        'us-east-2',
                        'us-west-1',
                        'us-west-2',
                        'us-gov-west-1',
                        'us-gov-east-1',
                        'ca-central-1',
                        'eu-north-1',
                        'eu-west-1',
                        'eu-west-2',
                        'eu-west-3',
                        'eu-central-1',
                        'eu-south-1',
                        'af-south-1',
                        'ap-northeast-1',
                        'ap-northeast-2',
                        'ap-northeast-3',
                        'ap-southeast-1',
                        'ap-southeast-2',
                        'ap-east-1',
                        'ap-south-1',
                        'sa-east-1',
                        'me-south-1',
                    ],
                }
            },
        },
        {
            'description': 'The AWSSavingsPlans multi-region endpoint',
            'url': 'https://savingsplans.{region}.amazonaws.com',
            'variables': {
                'region': {
                    'default': 'us-east-1',
                    'description': 'The AWS region',
                    'enum': [
                        'us-east-1',
                        'us-east-2',
                        'us-west-1',
                        'us-west-2',
                        'us-gov-west-1',
                        'us-gov-east-1',
                        'ca-central-1',
                        'eu-north-1',
                        'eu-west-1',
                        'eu-west-2',
                        'eu-west-3',
                        'eu-central-1',
                        'eu-south-1',
                        'af-south-1',
                        'ap-northeast-1',
                        'ap-northeast-2',
                        'ap-northeast-3',
                        'ap-southeast-1',
                        'ap-southeast-2',
                        'ap-east-1',
                        'ap-south-1',
                        'sa-east-1',
                        'me-south-1',
                    ],
                }
            },
        },
        {
            'description': 'The AWSSavingsPlans endpoint for China (Beijing) and China (Ningxia)',
            'url': 'http://savingsplans.{region}.amazonaws.com.cn',
            'variables': {
                'region': {
                    'default': 'cn-north-1',
                    'description': 'The AWS region',
                    'enum': ['cn-north-1', 'cn-northwest-1'],
                }
            },
        },
        {
            'description': 'The AWSSavingsPlans endpoint for China (Beijing) and China (Ningxia)',
            'url': 'https://savingsplans.{region}.amazonaws.com.cn',
            'variables': {
                'region': {
                    'default': 'cn-north-1',
                    'description': 'The AWS region',
                    'enum': ['cn-north-1', 'cn-northwest-1'],
                }
            },
        },
    ],
)


@app.post(
    '/CreateSavingsPlan',
    description=""" Creates a Savings Plan. """,
    tags=['savings_plan_operations'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def create_savings_plan(
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: CreateSavingsPlanPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/DeleteQueuedSavingsPlan',
    description=""" Deletes the queued purchase for the specified Savings Plan. """,
    tags=['savings_plan_operations'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def delete_queued_savings_plan(
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: DeleteQueuedSavingsPlanPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/DescribeSavingsPlanRates',
    description=""" Describes the specified Savings Plans rates. """,
    tags=['savings_plan_operations'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def describe_savings_plan_rates(
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: DescribeSavingsPlanRatesPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/DescribeSavingsPlans',
    description=""" Describes the specified Savings Plans. """,
    tags=['savings_plan_operations'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def describe_savings_plans(
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: DescribeSavingsPlansPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/DescribeSavingsPlansOfferingRates',
    description=""" Describes the specified Savings Plans offering rates. """,
    tags=['savings_plan_operations'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def describe_savings_plans_offering_rates(
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: DescribeSavingsPlansOfferingRatesPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/DescribeSavingsPlansOfferings',
    description=""" Describes the specified Savings Plans offerings. """,
    tags=['savings_plan_operations'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def describe_savings_plans_offerings(
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: DescribeSavingsPlansOfferingsPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/ListTagsForResource',
    description=""" Lists the tags for the specified resource. """,
    tags=['resource_tag_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def list_tags_for_resource(
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: ListTagsForResourcePostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/TagResource',
    description=""" Adds the specified tags to the specified resource. """,
    tags=['resource_tag_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def tag_resource(
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: TagResourcePostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/UntagResource',
    description=""" Removes the specified tags from the specified resource. """,
    tags=['resource_tag_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def untag_resource(
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: UntagResourcePostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
