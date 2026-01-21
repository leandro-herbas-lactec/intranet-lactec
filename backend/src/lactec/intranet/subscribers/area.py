from lactec.intranet import logger
from lactec.intranet.content.area import Area
from plone import api
from zope.lifecycleevent import ObjectAddedEvent
from zope.lifecycleevent import ObjectModifiedEvent


def _add_editor_group(obj: Area):
    """Cria grupo de editores para a área criada"""
    uid = api.content.get_uuid(obj)

    group = api.group.create(
        groupname=f"editores-{uid}",
        title=f"Editores {obj.title}",
        description=f"Editores da área {obj.title}",
    )
    logger.info(f"Grupo {obj.title} criado")

    api.group.grant_roles(group=group, roles=["Editor"], obj=obj)
    logger.info(f"Grupo {obj.title} recebeu papel de Editor")


def _update_excluded_from_nav(obj: Area):
    """Update excluded_from_nav in the Area object."""
    description = obj.description
    obj.exclude_from_nav = not bool(description)
    logger.info(f"Atualizado o campo excluded_from_nav para {obj.title}")


def added(obj: Area, event: ObjectAddedEvent):
    """Post creation handler for Area."""
    _update_excluded_from_nav(obj)
    _add_editor_group(obj)


def modified(obj: Area, event: ObjectModifiedEvent):
    """Post modification handler for Area."""
    _update_excluded_from_nav(obj)
