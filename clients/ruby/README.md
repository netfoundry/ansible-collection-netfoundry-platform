# openapi_client

OpenapiClient - the Ruby gem for the untitled API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 5229
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.RubyClientCodegen

## Installation

### Build a gem

To build the Ruby code into a gem:

```shell
gem build openapi_client.gemspec
```

Then either install the gem locally:

```shell
gem install ./openapi_client-1.0.0.gem
```

(for development, run `gem install --dev ./openapi_client-1.0.0.gem` to install the development dependencies)

or publish the gem to a gem hosting service, e.g. [RubyGems](https://rubygems.org/).

Finally add this to the Gemfile:

    gem 'openapi_client', '~> 1.0.0'

### Install from Git

If the Ruby gem is hosted at a git repository: https://github.com/GIT_USER_ID/GIT_REPO_ID, then add the following in the Gemfile:

    gem 'openapi_client', :git => 'https://github.com/GIT_USER_ID/GIT_REPO_ID.git'

### Include the Ruby code directly

Include the Ruby code directly using `-I` as follows:

```shell
ruby -Ilib script.rb
```

## Getting Started

Please follow the [installation](#installation) procedure and then run the following code:

```ruby
# Load the gem
require 'openapi_client'

api_instance = OpenapiClient::DefaultApi.new
edge_router_id = 'edge_router_id_example' # String | 

begin
  #Get an Edge Router
  result = api_instance.request4_q1q_u3c4dk(edge_router_id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Exception when calling DefaultApi->request4_q1q_u3c4dk: #{e}"
end

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*OpenapiClient::DefaultApi* | [**request4_q1q_u3c4dk**](docs/DefaultApi.md#request4_q1q_u3c4dk) | **GET** /core/v2/edge-routers/{edgeRouterId} | Get an Edge Router
*OpenapiClient::DefaultApi* | [**request9s_du_piz_ciu**](docs/DefaultApi.md#request9s_du_piz_ciu) | **POST** /core/v2/endpoints | Create an Endpoint
*OpenapiClient::DefaultApi* | [**request_a8syya_p_znw**](docs/DefaultApi.md#request_a8syya_p_znw) | **GET** /product-metadata/v2/download-urls.json | Get the list of Network product versions
*OpenapiClient::DefaultApi* | [**request_auar_cs_ihk_j**](docs/DefaultApi.md#request_auar_cs_ihk_j) | **POST** /core/v2/edge-routers/{edgeRouterId}/registration-key | Get the registration information for an Edge Router
*OpenapiClient::DefaultApi* | [**request_ay_fh_a_qd5pn**](docs/DefaultApi.md#request_ay_fh_a_qd5pn) | **GET** /core/v2/endpoints | Get an Endpoint
*OpenapiClient::DefaultApi* | [**request_btgg9_zl_c0e**](docs/DefaultApi.md#request_btgg9_zl_c0e) | **GET** /core/v2/edge-router-policies/{edgeRouterPolicyId} | Get an Edge Router Policy
*OpenapiClient::DefaultApi* | [**request_e1_iex_rfv_zg**](docs/DefaultApi.md#request_e1_iex_rfv_zg) | **GET** /core/v2/services | Get the list of Services
*OpenapiClient::DefaultApi* | [**request_f_wl_fmqidpx**](docs/DefaultApi.md#request_f_wl_fmqidpx) | **POST** /core/v2/networks | Create a Network
*OpenapiClient::DefaultApi* | [**request_gij_vc_eo_ml_m**](docs/DefaultApi.md#request_gij_vc_eo_ml_m) | **GET** /core/v2/app-wans | Get the list of AppWANs
*OpenapiClient::DefaultApi* | [**request_hp1b9_gi_lax**](docs/DefaultApi.md#request_hp1b9_gi_lax) | **GET** /core/v2/edge-router-policies | Get an Edge Router Policy
*OpenapiClient::DefaultApi* | [**request_iaj_vi_y_lviu**](docs/DefaultApi.md#request_iaj_vi_y_lviu) | **DELETE** /core/v2/networks/{networkId} | Delete a Network
*OpenapiClient::DefaultApi* | [**request_k9aj_dj8v_us**](docs/DefaultApi.md#request_k9aj_dj8v_us) | **GET** /rest/v1/network-groups | Get the list of Network Groups
*OpenapiClient::DefaultApi* | [**request_kke_r9g_ny25**](docs/DefaultApi.md#request_kke_r9g_ny25) | **GET** /core/v2/app-wans/{appWanId} | Get an AppWAN
*OpenapiClient::DefaultApi* | [**request_lg_kx_u4ph9t**](docs/DefaultApi.md#request_lg_kx_u4ph9t) | **POST** /core/v2/edge-router-policies | Create an Edge Router Policy
*OpenapiClient::DefaultApi* | [**request_lo_xf_q_ss8_ge**](docs/DefaultApi.md#request_lo_xf_q_ss8_ge) | **GET** /core/v2/network-configs | Get a Network Configuration profile
*OpenapiClient::DefaultApi* | [**request_lopo_ftq4ih**](docs/DefaultApi.md#request_lopo_ftq4ih) | **POST** /core/v2/services | Create a Service
*OpenapiClient::DefaultApi* | [**request_mpy_yt_ii_s6x**](docs/DefaultApi.md#request_mpy_yt_ii_s6x) | **GET** /identity/v1/api-account-identities/self | Get the identity of the caller's API account
*OpenapiClient::DefaultApi* | [**request_n6_gjg_plo4v**](docs/DefaultApi.md#request_n6_gjg_plo4v) | **GET** /identity/v1/organizations/{organizationId} | Get an Organization
*OpenapiClient::DefaultApi* | [**request_n_xo_v6_k2f0_q**](docs/DefaultApi.md#request_n_xo_v6_k2f0_q) | **POST** /core/v2/app-wans | Create an AppWAN
*OpenapiClient::DefaultApi* | [**request_oi_i_af_x2_v_us**](docs/DefaultApi.md#request_oi_i_af_x2_v_us) | **GET** /core/v2/networks | Get the list of Networks
*OpenapiClient::DefaultApi* | [**request_p_baai_o3_b0d**](docs/DefaultApi.md#request_p_baai_o3_b0d) | **DELETE** /core/v2/services/{serviceId} | Delete a Service
*OpenapiClient::DefaultApi* | [**request_py_r6a_up5mi**](docs/DefaultApi.md#request_py_r6a_up5mi) | **POST** /core/v2/edge-routers | Create an Edge Router
*OpenapiClient::DefaultApi* | [**request_q0b3cb_dw8_s**](docs/DefaultApi.md#request_q0b3cb_dw8_s) | **GET** /core/v2/posture-checks | Get the list of Posture Checks
*OpenapiClient::DefaultApi* | [**request_teq_m_ge_er5_f**](docs/DefaultApi.md#request_teq_m_ge_er5_f) | **GET** /core/v2/networks/{networkId} | Get a Network
*OpenapiClient::DefaultApi* | [**request_tsyuwl_aej_k**](docs/DefaultApi.md#request_tsyuwl_aej_k) | **GET** /core/v2/endpoints/{endpointId} | Get an Endpoint
*OpenapiClient::DefaultApi* | [**request_v_iz_b1k6_uqb**](docs/DefaultApi.md#request_v_iz_b1k6_uqb) | **PATCH** /core/v2/services/{serviceId} | Change some properties of a Service
*OpenapiClient::DefaultApi* | [**request_ve_jcbur9i_o**](docs/DefaultApi.md#request_ve_jcbur9i_o) | **GET** /rest/v1/network-groups/{networkGroupId} | Get a Network Group
*OpenapiClient::DefaultApi* | [**request_vfua_d_me_trp**](docs/DefaultApi.md#request_vfua_d_me_trp) | **GET** /core/v2/data-centers | Get the list of data centers
*OpenapiClient::DefaultApi* | [**request_y_lsf4m9_ttt**](docs/DefaultApi.md#request_y_lsf4m9_ttt) | **GET** /core/v2/services/{serviceId} | Get a Service
*OpenapiClient::DefaultApi* | [**request_yhz_d_aw1_ks4**](docs/DefaultApi.md#request_yhz_d_aw1_ks4) | **GET** /core/v2/edge-routers | Get an Edge Router


## Documentation for Models

 - [OpenapiClient::CoreV2EndpointsEnrollmentMethod](docs/CoreV2EndpointsEnrollmentMethod.md)
 - [OpenapiClient::CoreV2ServicesModel](docs/CoreV2ServicesModel.md)
 - [OpenapiClient::CoreV2ServicesModelClientIngress](docs/CoreV2ServicesModelClientIngress.md)
 - [OpenapiClient::CoreV2ServicesModelClientIngressPorts](docs/CoreV2ServicesModelClientIngressPorts.md)
 - [OpenapiClient::CoreV2ServicesModelEdgeRouterHosts](docs/CoreV2ServicesModelEdgeRouterHosts.md)
 - [OpenapiClient::CoreV2ServicesModelServerEgress](docs/CoreV2ServicesModelServerEgress.md)
 - [OpenapiClient::CoreV2ServicesServiceIdModel](docs/CoreV2ServicesServiceIdModel.md)
 - [OpenapiClient::CoreV2ServicesServiceIdModelClientIngress](docs/CoreV2ServicesServiceIdModelClientIngress.md)
 - [OpenapiClient::CoreV2ServicesServiceIdModelServerEgress](docs/CoreV2ServicesServiceIdModelServerEgress.md)
 - [OpenapiClient::InlineObject](docs/InlineObject.md)
 - [OpenapiClient::InlineObject1](docs/InlineObject1.md)
 - [OpenapiClient::InlineObject2](docs/InlineObject2.md)
 - [OpenapiClient::InlineObject3](docs/InlineObject3.md)
 - [OpenapiClient::InlineObject4](docs/InlineObject4.md)
 - [OpenapiClient::InlineObject5](docs/InlineObject5.md)
 - [OpenapiClient::InlineObject6](docs/InlineObject6.md)
 - [OpenapiClient::InlineResponse200](docs/InlineResponse200.md)
 - [OpenapiClient::InlineResponse2001](docs/InlineResponse2001.md)
 - [OpenapiClient::InlineResponse20010](docs/InlineResponse20010.md)
 - [OpenapiClient::InlineResponse20011](docs/InlineResponse20011.md)
 - [OpenapiClient::InlineResponse20011Links](docs/InlineResponse20011Links.md)
 - [OpenapiClient::InlineResponse20012](docs/InlineResponse20012.md)
 - [OpenapiClient::InlineResponse20013](docs/InlineResponse20013.md)
 - [OpenapiClient::InlineResponse20014](docs/InlineResponse20014.md)
 - [OpenapiClient::InlineResponse20014IdentityProviders](docs/InlineResponse20014IdentityProviders.md)
 - [OpenapiClient::InlineResponse20014UpdatedAt](docs/InlineResponse20014UpdatedAt.md)
 - [OpenapiClient::InlineResponse20015](docs/InlineResponse20015.md)
 - [OpenapiClient::InlineResponse20015Embedded](docs/InlineResponse20015Embedded.md)
 - [OpenapiClient::InlineResponse20015EmbeddedNetworkConfigMetadataList](docs/InlineResponse20015EmbeddedNetworkConfigMetadataList.md)
 - [OpenapiClient::InlineResponse20016](docs/InlineResponse20016.md)
 - [OpenapiClient::InlineResponse20017](docs/InlineResponse20017.md)
 - [OpenapiClient::InlineResponse20017Embedded](docs/InlineResponse20017Embedded.md)
 - [OpenapiClient::InlineResponse20017EmbeddedOrganizations](docs/InlineResponse20017EmbeddedOrganizations.md)
 - [OpenapiClient::InlineResponse20017Links](docs/InlineResponse20017Links.md)
 - [OpenapiClient::InlineResponse20018](docs/InlineResponse20018.md)
 - [OpenapiClient::InlineResponse20018Embedded](docs/InlineResponse20018Embedded.md)
 - [OpenapiClient::InlineResponse20019](docs/InlineResponse20019.md)
 - [OpenapiClient::InlineResponse20019710](docs/InlineResponse20019710.md)
 - [OpenapiClient::InlineResponse200197316](docs/InlineResponse200197316.md)
 - [OpenapiClient::InlineResponse20019734](docs/InlineResponse20019734.md)
 - [OpenapiClient::InlineResponse2001Embedded](docs/InlineResponse2001Embedded.md)
 - [OpenapiClient::InlineResponse2001EmbeddedLinks](docs/InlineResponse2001EmbeddedLinks.md)
 - [OpenapiClient::InlineResponse2001EmbeddedNetworkList](docs/InlineResponse2001EmbeddedNetworkList.md)
 - [OpenapiClient::InlineResponse2001Links](docs/InlineResponse2001Links.md)
 - [OpenapiClient::InlineResponse2001LinksSelf](docs/InlineResponse2001LinksSelf.md)
 - [OpenapiClient::InlineResponse2001Page](docs/InlineResponse2001Page.md)
 - [OpenapiClient::InlineResponse2002](docs/InlineResponse2002.md)
 - [OpenapiClient::InlineResponse2002Embedded](docs/InlineResponse2002Embedded.md)
 - [OpenapiClient::InlineResponse2002EmbeddedDataCenters](docs/InlineResponse2002EmbeddedDataCenters.md)
 - [OpenapiClient::InlineResponse2002EmbeddedLinks](docs/InlineResponse2002EmbeddedLinks.md)
 - [OpenapiClient::InlineResponse2003](docs/InlineResponse2003.md)
 - [OpenapiClient::InlineResponse2003Embedded](docs/InlineResponse2003Embedded.md)
 - [OpenapiClient::InlineResponse2003EmbeddedConfigIdByConfigTypeId](docs/InlineResponse2003EmbeddedConfigIdByConfigTypeId.md)
 - [OpenapiClient::InlineResponse2003EmbeddedModel](docs/InlineResponse2003EmbeddedModel.md)
 - [OpenapiClient::InlineResponse2003EmbeddedModelClientIngress](docs/InlineResponse2003EmbeddedModelClientIngress.md)
 - [OpenapiClient::InlineResponse2003EmbeddedModelClientIngressPorts](docs/InlineResponse2003EmbeddedModelClientIngressPorts.md)
 - [OpenapiClient::InlineResponse2003EmbeddedModelEdgeRouterHosts](docs/InlineResponse2003EmbeddedModelEdgeRouterHosts.md)
 - [OpenapiClient::InlineResponse2003EmbeddedModelServerEgress](docs/InlineResponse2003EmbeddedModelServerEgress.md)
 - [OpenapiClient::InlineResponse2003EmbeddedModelServerEgress1](docs/InlineResponse2003EmbeddedModelServerEgress1.md)
 - [OpenapiClient::InlineResponse2003EmbeddedServiceList](docs/InlineResponse2003EmbeddedServiceList.md)
 - [OpenapiClient::InlineResponse2004](docs/InlineResponse2004.md)
 - [OpenapiClient::InlineResponse2004Embedded](docs/InlineResponse2004Embedded.md)
 - [OpenapiClient::InlineResponse2004EmbeddedEdgeRouterPolicyList](docs/InlineResponse2004EmbeddedEdgeRouterPolicyList.md)
 - [OpenapiClient::InlineResponse2005](docs/InlineResponse2005.md)
 - [OpenapiClient::InlineResponse2005ConfigIdByConfigTypeId](docs/InlineResponse2005ConfigIdByConfigTypeId.md)
 - [OpenapiClient::InlineResponse2006](docs/InlineResponse2006.md)
 - [OpenapiClient::InlineResponse2006Embedded](docs/InlineResponse2006Embedded.md)
 - [OpenapiClient::InlineResponse2007](docs/InlineResponse2007.md)
 - [OpenapiClient::InlineResponse2007Embedded](docs/InlineResponse2007Embedded.md)
 - [OpenapiClient::InlineResponse2007EmbeddedEndpointList](docs/InlineResponse2007EmbeddedEndpointList.md)
 - [OpenapiClient::InlineResponse2008](docs/InlineResponse2008.md)
 - [OpenapiClient::InlineResponse2009](docs/InlineResponse2009.md)
 - [OpenapiClient::InlineResponse200Links](docs/InlineResponse200Links.md)
 - [OpenapiClient::InlineResponse200LinksNetwork](docs/InlineResponse200LinksNetwork.md)
 - [OpenapiClient::InlineResponse200LinksSelf](docs/InlineResponse200LinksSelf.md)
 - [OpenapiClient::InlineResponse202](docs/InlineResponse202.md)
 - [OpenapiClient::InlineResponse2021](docs/InlineResponse2021.md)
 - [OpenapiClient::InlineResponse2021ConfigIdByConfigTypeId](docs/InlineResponse2021ConfigIdByConfigTypeId.md)
 - [OpenapiClient::InlineResponse2021Links](docs/InlineResponse2021Links.md)
 - [OpenapiClient::InlineResponse2022](docs/InlineResponse2022.md)
 - [OpenapiClient::InlineResponse2022ConfigIdByConfigTypeId](docs/InlineResponse2022ConfigIdByConfigTypeId.md)
 - [OpenapiClient::InlineResponse2023](docs/InlineResponse2023.md)
 - [OpenapiClient::InlineResponse2023ConfigIdByConfigTypeId](docs/InlineResponse2023ConfigIdByConfigTypeId.md)
 - [OpenapiClient::InlineResponse2023Model](docs/InlineResponse2023Model.md)
 - [OpenapiClient::InlineResponse2023ModelClientIngress](docs/InlineResponse2023ModelClientIngress.md)
 - [OpenapiClient::InlineResponse2024](docs/InlineResponse2024.md)
 - [OpenapiClient::InlineResponse2024Links](docs/InlineResponse2024Links.md)
 - [OpenapiClient::InlineResponse2024NetworkController](docs/InlineResponse2024NetworkController.md)
 - [OpenapiClient::InlineResponse2025](docs/InlineResponse2025.md)
 - [OpenapiClient::InlineResponse202Links](docs/InlineResponse202Links.md)
 - [OpenapiClient::InlineResponse500](docs/InlineResponse500.md)
 - [OpenapiClient::InlineResponse5001](docs/InlineResponse5001.md)
 - [OpenapiClient::InlineResponse5001Status](docs/InlineResponse5001Status.md)


## Documentation for Authorization

 All endpoints do not require authorization.
