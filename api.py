import justpy as jp
import definition
import json


class API:
    """Handles requests at /api?w=word
    """
    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')  # returns the value of w

        defined = definition.Definition(word).get()

        response = {
            "word": word,
            "definition": defined
        }

        wp.html = json.dumps(response)  # json it's a string that can be read by machines
        return wp



