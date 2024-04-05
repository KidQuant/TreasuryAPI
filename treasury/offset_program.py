from typing import Dict, List

from treasury.session import FederalTreasurySession


class OffsetProgram:
    """
    ## Overview:
    ----
    This dataset shows how Treasury offsets federal payments, such
    as tax refunds, to pay off delinquent debts such as unpaid
    child support.
    """

    def __init__(self, session: FederalTreasurySession) -> None:
        """Initialize the`OffsetProgram` object.

        ### Parameters
        ----
        session : `TreasurySession`
            An initialized session of the `TreasurySession.`

        ### Usage
        ----
            >>> treasury_client = FederalTreasuryClient()
            >>> offset_program_service = treasury_client.offset_program()
        """

        # Set the session
        self.treasury_session: FederalTreasurySession = session

    def __repr__(self) -> str:
        """String representation of the `FederalTreasuryClient.OffsetProgram` object."""

        # define the string representation
        str_representation = (
            "<FederalTreasuryClient.OffsetProgram (active=True, connected=True)>"
        )

        return str_representation

    def federal_collection(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100,
    ) -> Dict:

        if fields:
            fields = ",".join(fields)

        if filters:
            filters = ",".join(filters)

        if sort:
            sort = ",".join(sort)

        content = self.treasury_session.make_request(
            method="get",
            endpoint="/v1/debt/top/top_federal",
            params={
                "format": "json",
                "page[number]": page_number,
                "page[size]": page_size,
                "fields": fields,
                "sort": sort,
                "filters": filters,
            },
        )

        return content

    def state_program(
        self,
        fields: List[str] = None,
        sort: List[str] = None,
        filters: List[str] = None,
        page_number: int = 1,
        page_size: int = 100,
    ) -> Dict:

        if fields:
            fields = ",".join(fields)

        if filters:
            filters = ",".join(filters)

        if sort:
            sort = ",".join(sort)

        content = self.treasury_session.make_request(
            method="get",
            endpoint="/v1/debt/top/top_state",
            params={
                "format": "json",
                "page[number]": page_number,
                "page[size]": page_size,
                "fields": fields,
                "sort": sort,
                "filters": filters,
            },
        )
        return content
