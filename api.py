import justpy as jp


class API:
    """Handles requests at /api?w=word
    """
    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')  # returns the value of w
        jp.Div(a=wp, text=word.title())
        return wp

jp.Route("/api", API.serve)
jp.justpy()