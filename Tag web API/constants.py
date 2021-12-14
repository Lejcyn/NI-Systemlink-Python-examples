USER_SVC_URLS = dict(
    base='http://{0}/niuser',
    base_sans_protocol='{0}://{1}/niuser',
    get_workspaces='/v1/workspaces?take={0}'
)


TAG_SVC_URLS = dict(
    base='http://{0}/nitag',
    base_sans_protocol='{0}://{1}/nitag',
    create_tag='/v2/tags',
    get_tag_value='/v2/tags-with-values/{0}/{1}',
    put_tag_value='/v2/update-current-values'
)
