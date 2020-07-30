from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

_transport = RequestsHTTPTransport(
    url="https://api.stackshare.io/graphql",
    headers={"x-api-key": "TO1vIHztc2Ig3XqiDeef_g"},
    use_json=True
)

client = Client(transport=_transport)
# fmt: off
import ipdb,os; ipdb.set_trace()  # noqa
# fmt: on
query = gql(
    """
{
    enrichment(domain: "airbnb.com"){
        domain
        companyId
        companyName
        companyTools {
            count
            pageInfo {
                hasNextPage
                endCursor
            }
            edges {
                node {
                    tool{
                    id
                    name
                    }
                    sourcesSummary
                    sources
                }
            }
        }
    }
}
"""
)

print(client.execute(query))
