#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2024, Gaspard Micol (@gmicol) <gmicol@cisco.com>

# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {"metadata_version": "1.1", "status": ["preview"], "supported_by": "community"}

DOCUMENTATION = r"""
---
module: ndo_tenant_custom_qos_policy
short_description: Manage Custom QoS Policies in Tenant Policy Templates on Cisco Nexus Dashboard Orchestrator (NDO).
description:
- Manage Custom Quality of Service (QoS) Policies in Tenant Policy Templates on Cisco Nexus Dashboard Orchestrator (NDO).
- This module is only supported on ND v3.1 (NDO v4.3) and later.
author:
- Gaspard Micol (@gmicol)
options:
  template:
    description:
    - The name of the tenant template.
    type: str
    aliases: [ tenant_template ]
    required: true
  name:
    description:
    - The name of the Custom QoS Policy.
    type: str
    aliases: [ custom_qos_policy ]
  uuid:
    description:
    - The UUID of the Custom QoS Policy.
    - This parameter is required when the Custom QoS Policy O(name) needs to be updated.
    aliases: [ custom_qos_policy_uuid ]
    type: str
  description:
    description:
    - The description of the Custom QoS Policy.
    - Providing an empty string will remove the O(description="") from the Custom QoS Policy.
    type: str
  dscp_mappings:
    description:
    - The Differentiated Services Code Point (DSCP) mappings of the Custom QoS Policy.
    - Both O(dscp_mappings.dscp_from) and O(dscp_mappings.dscp_to) cannot be set to C(unspecified).
    type: list
    elements: dict
    suboptions:
      dscp_from:
        description:
        - The starting encoding point of the DSCP range.
        - Defaults to C(unspecified) when unset during creation.
        type: str
        choices:
          - af11
          - af12
          - af13
          - af21
          - af22
          - af23
          - af31
          - af32
          - af33
          - af41
          - af42
          - af43
          - cs0
          - cs1
          - cs2
          - cs3
          - cs4
          - cs5
          - cs6
          - cs7
          - expedited_forwarding
          - unspecified
          - voice_admit
        aliases: [ from ]
      dscp_to:
        description:
        - The ending encoding point of the DSCP range.
        - Defaults to C(unspecified) when unset during creation.
        type: str
        choices:
          - af11
          - af12
          - af13
          - af21
          - af22
          - af23
          - af31
          - af32
          - af33
          - af41
          - af42
          - af43
          - cs0
          - cs1
          - cs2
          - cs3
          - cs4
          - cs5
          - cs6
          - cs7
          - expedited_forwarding
          - unspecified
          - voice_admit
        aliases: [ to ]
      dscp_target:
        description:
        - The DSCP target encoding point for egressing traffic.
        - Defaults to C(unspecified) when unset during creation.
        type: str
        choices:
          - af11
          - af12
          - af13
          - af21
          - af22
          - af23
          - af31
          - af32
          - af33
          - af41
          - af42
          - af43
          - cs0
          - cs1
          - cs2
          - cs3
          - cs4
          - cs5
          - cs6
          - cs7
          - expedited_forwarding
          - unspecified
          - voice_admit
        aliases: [ target ]
      target_cos:
        description:
        - The target CoS traffic type for the egressing traffic.
        - Defaults to C(unspecified) when unset during creation.
        type: str
        choices: [ background, best_effort, excellent_effort, critical_applications, video, voice, internetwork_control, network_control, unspecified ]
      qos_priority:
        description:
        - The QoS priority level to which the DSCP values will be mapped.
        - Defaults to C(unspecified) when unset during creation.
        type: str
        choices: [ level1, level2, level3, level4, level5, level6, unspecified ]
        aliases: [ priority, prio ]
  cos_mappings:
    description:
    - The Class of Service (CoS) mappings of the Custom QoS Policy.
    - Both O(cos_mappings.dot1p_from) and O(cos_mappings.dot1p_to) cannot be set to C(unspecified).
    type: list
    elements: dict
    suboptions:
      dot1p_from:
        description:
        - The starting traffic type of the CoS range.
        - Defaults to C(unspecified) when unset during creation.
        type: str
        choices: [ background, best_effort, excellent_effort, critical_applications, video, voice, internetwork_control, network_control, unspecified ]
        aliases: [ from ]
      dot1p_to:
        description:
        - The encoding traffic type of the CoS range.
        - Defaults to C(unspecified) when unset during creation.
        type: str
        choices: [ background, best_effort, excellent_effort, critical_applications, video, voice, internetwork_control, network_control, unspecified ]
        aliases: [ to ]
      dscp_target:
        description:
        - The DSCP target encoding point for egressing traffic.
        - Defaults to C(unspecified) when unset during creation.
        type: str
        choices:
          - af11
          - af12
          - af13
          - af21
          - af22
          - af23
          - af31
          - af32
          - af33
          - af41
          - af42
          - af43
          - cs0
          - cs1
          - cs2
          - cs3
          - cs4
          - cs5
          - cs6
          - cs7
          - expedited_forwarding
          - unspecified
          - voice_admit
        aliases: [ target ]
      target_cos:
        description:
        - The target CoS traffic type for the egressing traffic.
        - Defaults to C(unspecified) when unset during creation.
        type: str
        choices: [ background, best_effort, excellent_effort, critical_applications, video, voice, internetwork_control, network_control, unspecified ]
      qos_priority:
        description:
        - The QoS priority level to which the DSCP values will be mapped.
        - Defaults to C(unspecified) when unset during creation.
        type: str
        choices: [ level1, level2, level3, level4, level5, level6, unspecified ]
        aliases: [ priority, prio ]
  state:
    description:
    - Use C(absent) for removing.
    - Use C(query) for listing an object or multiple objects.
    - Use C(present) for creating or updating.
    type: str
    choices: [ absent, query, present ]
    default: query
notes:
- The O(template) must exist before using this module in your playbook.
  Use M(cisco.mso.ndo_template) to create the Tenant template.
seealso:
- module: cisco.mso.ndo_template
extends_documentation_fragment: cisco.mso.modules
"""

EXAMPLES = r"""
- name: Create a new Custom QoS Policy object
  cisco.mso.ndo_tenant_custom_qos_policy:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    template: tenant_template
    name: custom_qos_policy_1
    dscp_mappings:
      - dscp_from: af11
        dscp_to: af12
        dscp_target: af11
        target_cos: background
        qos_priority: level1
    cos_mappings:
      - dot1p_from: background
        dot1p_to: best_effort
        target: af11
        target_cos: background
        qos_priority: level1
    state: present
  register: custom_qos_policy_1

- name: Update a Custom QoS Policy object name with UUID
  cisco.mso.ndo_tenant_custom_qos_policy:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    template: tenant_template
    name: custom_qos_policy_2
    uuid: "{{ custom_qos_policy_1.current.uuid }}"
    state: present

- name: Query a Custom QoS Policy object with name
  cisco.mso.ndo_tenant_custom_qos_policy:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    template: tenant_template
    name: custom_qos_policy_1
    state: query
  register: query_name

- name: Query a Custom QoS Policy object with UUID
  cisco.mso.ndo_tenant_custom_qos_policy:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    template: tenant_template
    uuid: "{{ custom_qos_policy_1.current.uuid }}"
    state: query
  register: query_uuid

- name: Query all Custom QoS Policy objects in a Tenant Template
  cisco.mso.ndo_tenant_custom_qos_policy:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    template: tenant_template
    state: query
  register: query_all

- name: Delete a Custom QoS Policy object with name
  cisco.mso.ndo_tenant_custom_qos_policy:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    template: tenant_template
    name: custom_qos_policy_1
    state: absent

- name: Delete a Custom QoS Policy object with UUID
  cisco.mso.ndo_tenant_custom_qos_policy:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    template: tenant_template
    uuid: "{{ custom_qos_policy_1.current.uuid }}"
    state: absent
"""

RETURN = r"""
"""

import copy
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.mso.plugins.module_utils.mso import MSOModule, mso_argument_spec
from ansible_collections.cisco.mso.plugins.module_utils.template import MSOTemplate, KVPair
from ansible_collections.cisco.mso.plugins.module_utils.utils import format_list_dict
from ansible_collections.cisco.mso.plugins.module_utils.constants import (
    TARGET_DSCP_MAP,
    TARGET_COS_MAP,
    DSCP_KEYS_FORMAT_MAP,
    DOT1P_KEYS_FORMAT_MAP,
)


def main():
    argument_spec = mso_argument_spec()
    argument_spec.update(
        template=dict(type="str", required=True, aliases=["tenant_template"]),
        name=dict(type="str", aliases=["custom_qos_policy"]),
        uuid=dict(type="str", aliases=["custom_qos_policy_uuid"]),
        description=dict(type="str"),
        dscp_mappings=dict(
            type="list",
            elements="dict",
            options=dict(
                dscp_from=dict(type="str", choices=list(TARGET_DSCP_MAP.keys()), aliases=["from"]),
                dscp_to=dict(type="str", choices=list(TARGET_DSCP_MAP.keys()), aliases=["to"]),
                dscp_target=dict(type="str", choices=list(TARGET_DSCP_MAP.keys()), aliases=["target"]),
                target_cos=dict(type="str", choices=list(TARGET_COS_MAP.keys())),
                qos_priority=dict(
                    type="str",
                    choices=["level1", "level2", "level3", "level4", "level5", "level6", "unspecified"],
                    aliases=["priority", "prio"],
                ),
            ),
        ),
        cos_mappings=dict(
            type="list",
            elements="dict",
            options=dict(
                dot1p_from=dict(type="str", choices=list(TARGET_COS_MAP.keys()), aliases=["from"]),
                dot1p_to=dict(type="str", choices=list(TARGET_COS_MAP.keys()), aliases=["to"]),
                dscp_target=dict(type="str", choices=list(TARGET_DSCP_MAP.keys()), aliases=["target"]),
                target_cos=dict(type="str", choices=list(TARGET_COS_MAP.keys())),
                qos_priority=dict(
                    type="str",
                    choices=["level1", "level2", "level3", "level4", "level5", "level6", "unspecified"],
                    aliases=["priority", "prio"],
                ),
            ),
        ),
        state=dict(type="str", default="query", choices=["absent", "query", "present"]),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[
            ["state", "absent", ["name", "uuid"], True],
            ["state", "present", ["name", "uuid"], True],
        ],
    )

    mso = MSOModule(module)

    template = module.params.get("template")
    name = module.params.get("name")
    uuid = module.params.get("uuid")
    description = module.params.get("description")
    dscp_mappings = format_list_dict(module.params.get("dscp_mappings"), DSCP_KEYS_FORMAT_MAP)
    cos_mappings = format_list_dict(module.params.get("cos_mappings"), DOT1P_KEYS_FORMAT_MAP)
    state = module.params.get("state")

    template_object = MSOTemplate(mso, "tenant", template)
    template_object.validate_template("tenantPolicy")

    custom_qos_policies = template_object.template.get("tenantPolicyTemplate", {}).get("template", {}).get("qosPolicies", [])
    object_description = "Custom QoS Policy"

    if state in ["query", "absent"] and custom_qos_policies == []:
        mso.exit_json()
    elif state == "query" and not (name or uuid):
        mso.existing = custom_qos_policies
    elif custom_qos_policies and (name or uuid):
        match = template_object.get_object_by_key_value_pairs(
            object_description, custom_qos_policies, [KVPair("uuid", uuid) if uuid else KVPair("name", name)]
        )
        if match:
            custom_qos_policy_attrs_path = "/tenantPolicyTemplate/template/qosPolicies/{0}".format(match.index)
            mso.existing = mso.previous = copy.deepcopy(match.details)

    ops = []

    if state == "present":
        if uuid and not mso.existing:
            mso.fail_json(msg="{0} with the UUID: '{1}' not found".format(object_description, uuid))

        if mso.existing:
            proposed_payload = copy.deepcopy(match.details)

            if name and mso.existing.get("name") != name:
                ops.append(dict(op="replace", path=custom_qos_policy_attrs_path + "/name", value=name))
                proposed_payload["name"] = name

            if description is not None and mso.existing.get("description") != description:
                ops.append(dict(op="replace", path=custom_qos_policy_attrs_path + "/description", value=description))
                proposed_payload["description"] = description

            if dscp_mappings and mso.existing.get("dscpMappings") != dscp_mappings:
                ops.append(dict(op="replace", path=custom_qos_policy_attrs_path + "/dscpMappings", value=dscp_mappings))
                proposed_payload["dscpMappings"] = dscp_mappings
            elif dscp_mappings == [] and mso.existing.get("dscpMappings"):
                ops.append(dict(op="remove", path=custom_qos_policy_attrs_path + "/dscpMappings"))
                proposed_payload["dscpMappings"] = []

            if cos_mappings and mso.existing.get("cosMappings") != cos_mappings:
                ops.append(dict(op="replace", path=custom_qos_policy_attrs_path + "/cosMappings", value=cos_mappings))
                proposed_payload["cosMappings"] = cos_mappings
            elif cos_mappings == [] and mso.existing.get("cosMappings"):
                ops.append(dict(op="remove", path=custom_qos_policy_attrs_path + "/cosMappings"))
                proposed_payload["cosMappings"] = []

            mso.sanitize(proposed_payload, collate=True)
        else:
            payload = dict(
                name=name,
                description=description,
                dscpMappings=dscp_mappings,
                cosMappings=cos_mappings,
            )

            mso.sanitize(payload)
            ops.append(dict(op="add", path="/tenantPolicyTemplate/template/qosPolicies/-", value=mso.sent))

    elif state == "absent":
        if mso.existing:
            ops.append(dict(op="remove", path=custom_qos_policy_attrs_path))

    if not module.check_mode and ops:
        response_object = mso.request(template_object.template_path, method="PATCH", data=ops)
        custom_qos_policies = response_object.get("tenantPolicyTemplate", {}).get("template", {}).get("qosPolicies", [])
        match = template_object.get_object_by_key_value_pairs(
            object_description, custom_qos_policies, [KVPair("uuid", uuid) if uuid else KVPair("name", name)]
        )
        if match:
            mso.existing = match.details  # When the state is present
        else:
            mso.existing = {}  # When the state is absent
    elif module.check_mode and state != "query":  # When the state is present/absent with check mode
        mso.existing = mso.proposed if state == "present" else {}

    mso.exit_json()


if __name__ == "__main__":
    main()
