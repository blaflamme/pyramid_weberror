import os.path
import logging
import sys

from weberror.evalexception import EvalException

log = logging.getLogger(__name__)

# Provides Mako template engine HTML error formatters for the Template tab of
# EvalException.

try:
    import mako.exceptions
except ImportError: # pragma: no cover
    mako = None

def handle_mako_error(context, exc):
    try:
        exc.is_mako_exception = True
    except:
        pass
    raise exc, None, sys.exc_info()[2]

template_error_formatters = []

if mako:
    def mako_html_data(exc_value):
        """Format a Mako exception as HTML"""
        if getattr(exc_value, 'is_mako_exception', False) or \
           isinstance(exc_value, (mako.exceptions.CompileException,
                                  mako.exceptions.SyntaxException)):
            return mako.exceptions.html_error_template().render(full=False,
                                                                css=False)
    template_error_formatters.append(mako_html_data)


# Setup pyramid vars for EvalException
    
medias_path = os.path.join(os.path.dirname(__file__), 'medias')

footer_html = """\
<div id="pyramid-footer" style="float: right; text-align: left;">
<img src="{{prefix}}/medias/pyramid/pyramid_148x45.png" alt="pyramid">
<h2 style="font-weight: bold; float: right;">
  Version %s
</h2>\
"""

report_libs = ['pyramid', 'mako', 'sqlalchemy']   

def make_eval_exception(app, global_conf, **kw):
    from pkg_resources import get_distribution
    info = get_distribution('pyramid')
    footer = footer_html % (kw.get(
                                'traceback_host', 
                                'pylonshq.com'),
                            info.version)
    media_paths = dict(pyramid=media_path)
    return EvalException(
        app,
        global_conf,
        templating_formatters=template_error_formatters,
        media_paths=media_paths,
        head_html=head_html, 
        footer_html=footer,
        libraries=report_libs
    )


def evalerror_filter_factory(global_conf, **kw):
    def factory(app):
        return make_eval_exception(app, global_conf, **kw)
    return factory


