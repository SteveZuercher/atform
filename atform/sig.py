"""Approval signature API."""

from . import error
from . import misc
from . import state


################################################################################
# Public API
#
# Items in this area are documented and exported for use by end users.
################################################################################


@error.exit_on_script_error
@misc.setup_only
def add_signature(title):
    """Adds an approval signature line.

    The signature entry contains title, name, signature, initials, and date
    fields that will appear at the conclusion of every test. Signatures
    will be presented in the order they are defined.

    .. seealso:: :ref:`setup`

    Args:
        title (str): A short description of the person signing; may not
            be blank.
    """
    state.signatures.append(misc.nonempty_string("signature title", title))


@error.exit_on_script_error
@misc.setup_only
def set_signature_name_plain():
    """Globally disables interactive text entry for the signature name.

    The name field will instead be rendered as a blank area. May only be
    called once in the setup area.
    """
    if state.sig_name_plain:
        raise error.UserScriptError(
            "Duplicate function call.",
            """
            This function can only be called once to disable interactive
            forms for the signature name field; remove one of the calls to
            this function.
            """,
        )
    state.sig_name_plain = True

@error.exit_on_script_error
@misc.setup_only
def set_signature_no_initials():
    """Globally disables the initials field from the signature.

    May only be called once in the setup area.
    """
    if state.sig_include_initials:
            raise error.UserScriptError(
                "Duplicate function call.",
                """
                This function can only be called once to remove the initials
                from the signature entry; remove one of the calls to
                this function.
                """,
            )
    state.sig_include_initials = True
