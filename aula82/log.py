class LogMixin:
    @staticmethod
    def write(msg):
        with open('log_values.txt', 'a+') as file:
            file.write(msg)
            file.write('\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')
