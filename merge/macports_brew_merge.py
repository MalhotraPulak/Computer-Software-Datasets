import pandas as pd
from collections import defaultdict

brew_data = pd.read_csv('../brew/brew_data.csv', sep=',')
macports_data = pd.read_csv('../macports/macports_data.csv', sep=',')

# packages_dict = defaultdict(int)
# for i in macports_data['name']:
#     packages_dict[i]+=1
# for i in brew_data['name']:
#     packages_dict[i]+=1



brew_data.rename(columns = {
    'tap':'tap',
    'name':'name',
    'full_name':'full_name',
    'desc':'brew_description',
    'homepage':'brew_homepage',
    'urls|stable|url':'brew_stable_url',
    'generated_date':'generated_date',
    'versions|stable':'brew_stable_version',
    'bottle|stable|root_url':'brew_stable_root_url',
    'versions|bottle':'brew_bottle_version',
    'analytics|install|365d|command':'analytics|install|365d',
    'analytics|install_on_request|365d|command':'analytics|install_on_request|365d',
    'analytics|install|90d|command':'analytics|install|90d',
    'analytics|install_on_request|90d|command':'analytics|install_on_request|90d',
    'analytics|install|30d|command':'analytics|install|30d',
    'analytics|install_on_request|30d|command':'analytics|install_on_request|30d',
    'bottle|stable|files|catalina|cellar':'bottle|stable|files|catalina|cellar',
    'bottle|stable|files|catalina|url':'bottle|stable|files|catalina|url',
    'bottle|stable|files|catalina|sha256':'bottle|stable|files|catalina|sha256',
    'bottle|stable|files|mojave|cellar':'bottle|stable|files|mojave|cellar',
    'bottle|stable|files|mojave|url':'bottle|stable|files|mojave|url',
    'bottle|stable|files|mojave|sha256':'bottle|stable|files|mojave|sha256',
    'bottle|stable|files|big_sur|cellar':'bottle|stable|files|big_sur|cellar',
    'bottle|stable|files|big_sur|url':'bottle|stable|files|big_sur|url',
    'bottle|stable|files|big_sur|sha256':'bottle|stable|files|big_sur|sha256',
    'license':'brew_license',
    'bottle|stable|files|arm64_big_sur|cellar':'bottle|stable|files|arm64_big_sur|cellar',
    'bottle|stable|files|arm64_big_sur|url':'bottle|stable|files|arm64_big_sur|url',
    'bottle|stable|files|arm64_big_sur|sha256':'bottle|stable|files|arm64_big_sur|sha256',
    'bottle|stable|files|x86_64_linux|cellar':'bottle|stable|files|x86_64_linux|cellar',
    'bottle|stable|files|x86_64_linux|url':'bottle|stable|files|x86_64_linux|url',
    'bottle|stable|files|x86_64_linux|sha256':'bottle|stable|files|x86_64_linux|sha256',
    'dependencies|0':'brew_dependency_first',
    'build_dependencies|0':'brew_build_dependency_first',
    'versions|head':'brew_versions_head',
    'bottle|stable|files|high_sierra|cellar':'bottle|stable|files|high_sierra|cellar',
    'bottle|stable|files|high_sierra|url':'bottle|stable|files|high_sierra|url',
    'bottle|stable|files|high_sierra|sha256':'bottle|stable|files|high_sierra|sha256',
    'dependencies|1':'brew_dependency_second',
    'revision':'revision',
    'build_dependencies|1':'brew_build_dependency_second',
    'bottle|stable|files|sierra|cellar':'bottle|stable|files|sierra|cellar',
    'bottle|stable|files|sierra|url':'bottle|stable|files|sierra|url',
    'bottle|stable|files|sierra|sha256':'bottle|stable|files|sierra|sha256',
    'analytics|install_on_request|365d|command --HEAD':'analytics|install_on_request|365d|command --HEAD',
    'analytics|install|365d|command --HEAD':'analytics|install|365d|command --HEAD',
    'dependencies|2':'brew_dependency_third',
    'bottle|stable|files|el_capitan|cellar':'bottle|stable|files|el_capitan|cellar',
    'bottle|stable|files|el_capitan|url':'bottle|stable|files|el_capitan|url',
    'bottle|stable|files|el_capitan|sha256':'bottle|stable|files|el_capitan|sha256',
    'analytics|install|90d|command --HEAD':'analytics|install|90d|command --HEAD',
    'analytics|install_on_request|90d|command --HEAD':'analytics|install_on_request|90d|command --HEAD',
    'uses_from_macos|0':'brew_uses_from_macos_first',
    'bottle|stable|rebuild':'bottle|stable|rebuild',
    'bottle|stable|files|yosemite|cellar':'bottle|stable|files|yosemite|cellar',
    'bottle|stable|files|yosemite|url':'bottle|stable|files|yosemite|url',
    'bottle|stable|files|yosemite|sha256':'bottle|stable|files|yosemite|sha256',
    'build_dependencies|2':'brew_build_dependency_third',
    'dependencies|3':'brew_dependency_fourth',
    'bottle|stable|files|all|cellar':'bottle|stable|files|all|cellar',
    'bottle|stable|files|all|url':'bottle|stable|files|all|url',
    'bottle|stable|files|all|sha256':'bottle|stable|files|all|sha256',
    'analytics|install|30d|command --HEAD':'analytics|install|30d|command --HEAD',
    'analytics|install_on_request|30d|command --HEAD':'analytics|install_on_request|30d|command --HEAD',
    }, inplace = True)

macports_data.rename(columns = {
    'name':'name',
    'portdir':'portdir',
    'version':'macports_version',
    'license':'macports_license',
    'platforms':'platforms',
    'dependencies|0|type':'macports_dependency_first_type',
    'dependencies|0|ports|0':'macports_dependency_first',
    'description':'macports_description',
    'long_description':'macports_long_description',
    'categories|0':'categories_first',
    'homepage':'macports_homepage',
    'active':'active',
    'dependencies|1|type':'macports_dependency_second_type',
    'dependencies|1|ports|0':'macports_dependency_second',
    'maintainers|0|ports_count':'macports_maintainers_first_ports_count',
    'maintainers|0|name':'macports_maintainers_first_name',
    'depends_on|0|type':'macports_depends_on_first_type',
    'depends_on|0|ports|0':'macports_depends_on_first',
    'dependencies|0|ports|1':'macports_dependency_first_port',
    'maintainers|0|github':'macports_maintainers_first_github',
    'dependencies|1|ports|1':'macports_dependency_second_port',
    'variants|0':'macports_variants_first',
    'categories|1':'macports_categories_second',
    'dependencies|1|ports|2':'macports_dependency_second_anotherport',
    'depends_on|0|ports|1':'macports_depends_on_first_port',
    'dependencies|1|ports|3':'macports_dependency_second_port_latest',
    'dependencies|0|ports|2':'macports_dependency_first_ports_anotherport',
    'dependencies|2|type':'macports_dependency_third_type',
    'dependencies|2|ports|0':'macports_dependency_third_port',
    'variants|1':'macports_variants_second',
}, inplace=True)


inner_merged_total = pd.merge(brew_data, macports_data, on=["name"])
print(brew_data.shape)
print(macports_data.shape)
print(inner_merged_total.shape)
print(inner_merged_total.fillna(0).astype(bool).sum(axis=0).to_string())

inner_merged_total.to_csv('macports_brew_merge_data.csv')

# i=0
# for items in inner_merged_total.fillna(0).astype(bool).sum(axis=0).iteritems():
#     if items[1]>1250:
#         print(items)
#         i+=1

# print(i)
# temp = []
# for k,v in packages_dict.items():
#     if v>1:
#         temp.append(k)

# print(len(temp))