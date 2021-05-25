class DocrunnerBaseException(Exception):
    def get_message(self) -> str:
        raise NotImplementedError()

    def get_output_color(self) -> str:
        raise NotImplementedError()
