from .base import BaseCgi


class StatusJsonCgi(BaseCgi):
    def host_count(self) -> None:
        pass

    def host_list(self) -> None:
        pass

    def host(self) -> None:
        pass

    def service_count(self) -> None:
        pass

    def service_list(
        self,
        start=None,
        count=None,
        parent_host=None,
        child_host=None,
        show_details=False,
        date_format=None,
        host_name=None,
        host_group=None,
        host_status=None,
        service_group=None,
        service_status=None,
        parent_service=None,
        child_service=None,
        contact_group=None,
        service_description=None,
        check_timeperiod_name=None,
        service_notification_timeperiod_name=None,
        check_command_name=None,
        event_handler_name=None,
        contact_name=None,
        service_time_field=None,
        start_time=None,
        end_time=None,
    ) -> None:
        pass

    def service(self) -> None:
        pass

    def comment_count(self) -> None:
        pass

    def comment_list(self) -> None:
        pass

    def comment(self) -> None:
        pass

    def downtime_count(self) -> None:
        pass

    def downtime_list(self) -> None:
        pass

    def downtime(self) -> None:
        pass

    def program_status(self) -> None:
        pass

    def performance_data(self) -> None:
        pass

    def help(self) -> None:
        pass
