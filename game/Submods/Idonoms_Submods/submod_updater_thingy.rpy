# This makes my submods compatable with the updater
# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="Idonom",
        name="Idonom's Submods",
        description=(
            "A collection of various submods that were created by idonom.\n"
            "If you have any suggestions for submods, please DM idonom on either reddit or Discord."
        )
        description=,
        version="1.0.0"
        
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Idonom's Submods",
            user_name="idonom",
            repository_name="MAS_Submods",
            update_dir="",
            attachment_id=None
        )
