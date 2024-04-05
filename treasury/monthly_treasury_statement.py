from typing import Dict, List

from treasury.session import FederalTreasurySession


class MonthlyTreasuryStatements:

    def __init__(self, session: FederalTreasurySession) -> None:

        self.treasury_session: FederalTreasurySession = session

    def __repr__(self) -> str:
        """String representation of the `FederalTreasuryClient.MonthlyTreasuryStatements` object."""

        # define the string representation
        str_representation = "<FederalTreasuryClient.MonthlyTreasuryStatements (active=True, connected=True)>"

        return str_representation

    def receipts_outlays_and_deficits(
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
            endpoint="/v1/accounting/mts/mts_table_1",
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

    def budgets_and_financing(
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
            endpoint="/v1/accounting/mts/mts_table_2",
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

    def receipts_and_outlays(
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
            filters = ",".join(fields)

        if sort:
            sort = ",".join(sort)

        content = self.treasury_session.make_request(
            method="get",
            endpoint="/v1/accounting/mts/mts_table_3",
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

    def receipts(
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
            endpoint="/v1/accounting/mts/mts_table_4",
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

    def outlays(
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
            endpoint="/v1/accounting/mts/mts_table_5",
            params={
                "format": "json",
                "page[numbero]": page_number,
                "page[size]": page_size,
                "fields": fields,
                "sort": sort,
                "filters": filters,
            },
        )

        return content

    def means_of_financing(
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
            endpoints="/v1/accounting/mts/mts_table_6",
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

    def analysis_change_in_liabilities(
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
            endpoint="/v1/accounting/mts/mts_table_6a",
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

    def securities_issued_special_financing(
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
            endpoint="/v1/accounting/mts/mts_table_6b",
            params={
                "format": "json",
                "page[number]": page_number,
                "page[size]": page_size,
                "field": fields,
                "sort": sort,
                "filters": filters,
            },
        )

        return content

    def borrowing_financed_treasury_securities(
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
            endpoint="/v1/accounting/mts/mts_table_6c",
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

    def investments_federal_securities(
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
            endpoint="/v1/accounting/mts/mts_table_6d",
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

    def direct_loan_financing(
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
            endpoint="/v1/accounting/mts/mts_table_6e",
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

    def receipts_and_outlay_by_month(
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
            endpoint="/v1/accounting/mts/mts_table_7",
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

    def trust_fund_impact(
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
            endpoint="/v1/accounting/mts/mts_table_8",
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

    def receipt_by_source_outlay_by_function(
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
            endpoint="/v1/accounting/mts/mts_table_9",
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
