import justpy as jp
import definition

class API:
    """Handles requests at /api?w=word
    """
    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')  # returns the value of w

        defined = definition.Definition(word).get()

        wp.html = defined  # with div the source code is a full html web. With this the source code is just vad defined
        return wp


jp.Route("/api", API.serve)
jp.justpy()