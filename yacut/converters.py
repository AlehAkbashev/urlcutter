from werkzeug.routing import BaseConverter
from werkzeug.routing.map import Map
import yacut

class RegexConverter(BaseConverter):

    def __init__(self, urlmap: Map, *args) -> None:
        super(RegexConverter, self).__init__(urlmap)
        self.regex = yacut.app.config['USER_PATTERN']