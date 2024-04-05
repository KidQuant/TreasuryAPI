from typing import Dict, List

from treasury.session import FederalTreasurySession


class DailyTreasuryStatement:
    def __init__(self, session: FederalTreasurySession) -> None:
        self.treasury_session: FederalTreasurySession = session

    def __repr__(self) -> str:
        str_representation = "<FederalTreasuryClient.DailyTreasuryStatements (active=True, connected=True)>"

        return str_representation

    def operating_cash_balance(
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

        content = self.treasury_session.make_requests(
            method="get",
            endpoint="/v1/accounting/dts/dts_table_1",
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

    def deposits_and_withdrawals_operating_cash(
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

        content = self.treasury_session.make_requests(
            method="get",
            endpoint="/v1/accounting/dts/dts_table_2",
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

    def public_debt_transactions(
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

        content = self.treasury_session.make_requests(
            method="get",
            endpoint="/v1/accounting/dts/dts_table_3a",
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

    def adjusted_public_debt_transaction(
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

        content = self.treasury_session.make_requests(
            method="get",
            endpoint="/v1/accounting/dts/dts_table_3b",
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

    def debt_subject_limit(
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

        content = self.treasury_session.make_requests(
            method="get",
            endpoint="/v1/accounting/dts/dts_table_3c",
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

    def federal_tax_deposits(
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

        content = self.treasury_session.make_requests(
            method="get",
            endpoint="/v1/accounting/dts/dts_table_4",
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

    def short_term_cash_investments(
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

        content = self.treasury_session.make_requests(
            method="get",
            endpoint="/v1/accounting/dts/dts_table_5",
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

    def income_tax_refunds_issued(
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

        content = self.treasury_session.make_requests(
            method="get",
            endpoint="/v1/accounting/dts/dts_table_6",
            params={
                "format": "json",
                "page[number]": page_number,
                "page[size]": page_size,
                "fields": fields,
                "filters": filters,
            },
        )

        return content
