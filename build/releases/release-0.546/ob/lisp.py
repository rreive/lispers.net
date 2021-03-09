# -----------------------------------------------------------------------------
#             
# Copyright 2013-2019 lispers.net - Dino Farinacci <farinacci@gmail.com>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.    
# 
# -----------------------------------------------------------------------------
#
# lisp.py
#
# This file contains all constants, definitions, data structures, packet
# send and receive functions for the LISP protocol according to RFC 6830.
#
#------------------------------------------------------------------------------
if 64 - 64: i11iIiiIii
import socket
import time
import struct
import binascii
import hmac
import hashlib
import datetime
import os
import sys
import random
import threading
import operator
import netifaces
import platform
import Queue
import traceback
from Crypto . Cipher import AES
import ecdsa
import json
import commands
import copy
import chacha
import poly1305
from geopy . distance import vincenty
import curve25519
use_chacha = ( os . getenv ( "LISP_USE_CHACHA" ) != None )
use_poly = ( os . getenv ( "LISP_USE_POLY" ) != None )
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
lisp_print_rloc_probe_list = False
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
if 46 - 46: ooOoO0o * I11i - OoooooooOO
if 30 - 30: o0oOOo0O0Ooo - O0 % o0oOOo0O0Ooo - OoooooooOO * O0 * OoooooooOO
if 60 - 60: iIii1I11I1II1 / i1IIi * oO0o - I1ii11iIi11i + o0oOOo0O0Ooo
if 94 - 94: i1IIi % Oo0Ooo
if 68 - 68: Ii1I / O0
lisp_hostname = ""
lisp_version = ""
lisp_uptime = ""
lisp_i_am_core = False
lisp_i_am_itr = False
lisp_i_am_etr = False
lisp_i_am_rtr = False
lisp_i_am_mr = False
lisp_i_am_ms = False
lisp_i_am_ddt = False
lisp_log_id = ""
lisp_debug_logging = True
if 46 - 46: O0 * II111iiii / IiII * Oo0Ooo * iII111i . I11i
lisp_map_notify_queue = { }
lisp_map_servers_list = { }
lisp_ddt_map_requestQ = { }
lisp_db_list = [ ]
lisp_group_mapping_list = { }
lisp_map_resolvers_list = { }
lisp_rtr_list = { }
lisp_elp_list = { }
lisp_rle_list = { }
lisp_geo_list = { }
lisp_json_list = { }
lisp_myrlocs = [ None , None , None ]
lisp_mymacs = { }
if 62 - 62: i11iIiiIii - II111iiii % I1Ii111 - iIii1I11I1II1 . I1ii11iIi11i . II111iiii
if 61 - 61: oO0o / OoOoOO00 / iII111i * OoO0O00 . II111iiii
if 1 - 1: II111iiii - I1ii11iIi11i % i11iIiiIii + IiII . I1Ii111
if 55 - 55: iIii1I11I1II1 - I1IiiI . Ii1I * IiII * i1IIi / iIii1I11I1II1
if 79 - 79: oO0o + I1Ii111 . ooOoO0o * IiII % I11i . I1IiiI
lisp_myinterfaces = { }
lisp_iid_to_interface = { }
lisp_multi_tenant_interfaces = [ ]
if 94 - 94: iII111i * Ii1I / IiII . i1IIi * iII111i
lisp_test_mr_timer = None
lisp_rloc_probe_timer = None
if 47 - 47: i1IIi % i11iIiiIii
if 20 - 20: ooOoO0o * II111iiii
if 65 - 65: o0oOOo0O0Ooo * iIii1I11I1II1 * ooOoO0o
if 18 - 18: iIii1I11I1II1 / I11i + oO0o / Oo0Ooo - II111iiii - I11i
lisp_registered_count = 0
if 1 - 1: I11i - OOooOOo % O0 + I1IiiI - iII111i / I11i
if 31 - 31: OoO0O00 + II111iiii
if 13 - 13: OOooOOo * oO0o * I1IiiI
if 55 - 55: II111iiii
lisp_info_sources_by_address = { }
lisp_info_sources_by_nonce = { }
if 43 - 43: OoOoOO00 - i1IIi + I1Ii111 + Ii1I
if 17 - 17: o0oOOo0O0Ooo
if 64 - 64: Ii1I % i1IIi % OoooooooOO
if 3 - 3: iII111i + O0
if 42 - 42: OOooOOo / i1IIi + i11iIiiIii - Ii1I
if 78 - 78: OoO0O00
lisp_crypto_keys_by_nonce = { }
lisp_crypto_keys_by_rloc_encap = { }
lisp_crypto_keys_by_rloc_decap = { }
lisp_data_plane_security = False
lisp_search_decap_keys = True
if 18 - 18: O0 - iII111i / iII111i + ooOoO0o % ooOoO0o - IiII
lisp_data_plane_logging = False
lisp_frame_logging = False
lisp_flow_logging = False
if 62 - 62: iII111i - IiII - OoOoOO00 % i1IIi / oO0o
if 77 - 77: II111iiii - II111iiii . I1IiiI / o0oOOo0O0Ooo
if 14 - 14: I11i % O0
if 41 - 41: i1IIi + I1Ii111 + OOooOOo - IiII
if 77 - 77: Oo0Ooo . IiII % ooOoO0o
if 42 - 42: oO0o - i1IIi / i11iIiiIii + OOooOOo + OoO0O00
if 17 - 17: oO0o . Oo0Ooo . I1ii11iIi11i
lisp_crypto_ephem_port = None
if 3 - 3: OoOoOO00 . Oo0Ooo . I1IiiI / Ii1I
if 38 - 38: II111iiii % i11iIiiIii . ooOoO0o - OOooOOo + Ii1I
if 66 - 66: OoooooooOO * OoooooooOO . OOooOOo . i1IIi - OOooOOo
if 77 - 77: I11i - iIii1I11I1II1
lisp_pitr = False
if 82 - 82: i11iIiiIii . OOooOOo / Oo0Ooo * O0 % oO0o % iIii1I11I1II1
if 78 - 78: iIii1I11I1II1 - Ii1I * OoO0O00 + o0oOOo0O0Ooo + iII111i + iII111i
if 11 - 11: iII111i - OoO0O00 % ooOoO0o % iII111i / OoOoOO00 - OoO0O00
if 74 - 74: iII111i * O0
lisp_l2_overlay = False
if 89 - 89: oO0o + Oo0Ooo
if 3 - 3: i1IIi / I1IiiI % I11i * i11iIiiIii / O0 * I11i
if 49 - 49: oO0o % Ii1I + i1IIi . I1IiiI % I1ii11iIi11i
if 48 - 48: I11i + I11i / II111iiii / iIii1I11I1II1
if 20 - 20: o0oOOo0O0Ooo
lisp_rloc_probing = False
lisp_rloc_probe_list = { }
if 77 - 77: OoOoOO00 / I11i
if 98 - 98: iIii1I11I1II1 / i1IIi / i11iIiiIii / o0oOOo0O0Ooo
if 28 - 28: OOooOOo - IiII . IiII + OoOoOO00 - OoooooooOO + O0
if 95 - 95: OoO0O00 % oO0o . O0
if 15 - 15: ooOoO0o / Ii1I . Ii1I - i1IIi
if 53 - 53: IiII + I1IiiI * oO0o
lisp_register_all_rtrs = True
if 61 - 61: i1IIi * OOooOOo / OoooooooOO . i11iIiiIii . OoOoOO00
if 60 - 60: I11i / I11i
if 46 - 46: Ii1I * OOooOOo - OoO0O00 * oO0o - I1Ii111
if 83 - 83: OoooooooOO
lisp_nonce_echoing = False
lisp_nonce_echo_list = { }
if 31 - 31: II111iiii - OOooOOo . I1Ii111 % OoOoOO00 - O0
if 4 - 4: II111iiii / ooOoO0o . iII111i
if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - I1ii11iIi11i / oO0o
if 50 - 50: I1IiiI
lisp_nat_traversal = False
if 34 - 34: I1IiiI * II111iiii % iII111i * OoOoOO00 - I1IiiI
if 33 - 33: o0oOOo0O0Ooo + OOooOOo * OoO0O00 - Oo0Ooo / oO0o % Ii1I
if 21 - 21: OoO0O00 * iIii1I11I1II1 % oO0o * i1IIi
if 16 - 16: O0 - I1Ii111 * iIii1I11I1II1 + iII111i
if 50 - 50: II111iiii - ooOoO0o * I1ii11iIi11i / I1Ii111 + o0oOOo0O0Ooo
if 88 - 88: Ii1I / I1Ii111 + iII111i - II111iiii / ooOoO0o - OoOoOO00
if 15 - 15: I1ii11iIi11i + OoOoOO00 - OoooooooOO / OOooOOo
if 58 - 58: i11iIiiIii % I11i
lisp_program_hardware = False
if 71 - 71: OOooOOo + ooOoO0o % i11iIiiIii + I1ii11iIi11i - IiII
if 88 - 88: OoOoOO00 - OoO0O00 % OOooOOo
if 16 - 16: I1IiiI * oO0o % IiII
if 86 - 86: I1IiiI + Ii1I % i11iIiiIii * oO0o . ooOoO0o * I11i
lisp_checkpoint_map_cache = False
lisp_checkpoint_filename = "./lisp.checkpoint"
if 44 - 44: oO0o
if 88 - 88: I1Ii111 % Ii1I . II111iiii
if 38 - 38: o0oOOo0O0Ooo
if 57 - 57: O0 / oO0o * I1Ii111 / OoOoOO00 . II111iiii
lisp_ipc_data_plane = False
lisp_ipc_dp_socket = None
lisp_ipc_dp_socket_name = "lisp-ipc-data-plane"
if 26 - 26: iII111i
if 91 - 91: OoO0O00 . I1ii11iIi11i + OoO0O00 - iII111i / OoooooooOO
if 39 - 39: I1ii11iIi11i / ooOoO0o - II111iiii
if 98 - 98: I1ii11iIi11i / I11i % oO0o . OoOoOO00
if 91 - 91: oO0o % Oo0Ooo
lisp_ipc_lock = None
if 64 - 64: I11i % iII111i - I1Ii111 - oO0o
if 31 - 31: I11i - II111iiii . I11i
if 18 - 18: o0oOOo0O0Ooo
if 98 - 98: iII111i * iII111i / iII111i + I11i
if 34 - 34: ooOoO0o
if 15 - 15: I11i * ooOoO0o * Oo0Ooo % i11iIiiIii % OoOoOO00 - OOooOOo
lisp_default_iid = 0
lisp_default_secondary_iid = 0
if 68 - 68: I1Ii111 % i1IIi . IiII . I1ii11iIi11i
if 92 - 92: iII111i . I1Ii111
if 31 - 31: I1Ii111 . OoOoOO00 / O0
if 89 - 89: OoOoOO00
if 68 - 68: OoO0O00 * OoooooooOO % O0 + OoO0O00 + ooOoO0o
lisp_ms_rtr_list = [ ]
if 4 - 4: ooOoO0o + O0 * OOooOOo
if 55 - 55: Oo0Ooo + iIii1I11I1II1 / OoOoOO00 * oO0o - i11iIiiIii - Ii1I
if 25 - 25: I1ii11iIi11i
if 7 - 7: i1IIi / I1IiiI * I1Ii111 . IiII . iIii1I11I1II1
if 13 - 13: OOooOOo / i11iIiiIii
if 2 - 2: I1IiiI / O0 / o0oOOo0O0Ooo % OoOoOO00 % Ii1I
lisp_nat_state_info = { }
if 52 - 52: o0oOOo0O0Ooo
if 95 - 95: Ii1I
if 87 - 87: ooOoO0o + OoOoOO00 . OOooOOo + OoOoOO00
if 91 - 91: O0
if 61 - 61: II111iiii
if 64 - 64: ooOoO0o / OoOoOO00 - O0 - I11i
lisp_last_map_request_sent = None
lisp_no_map_request_rate_limit = time . time ( )
if 86 - 86: I11i % OoOoOO00 / I1IiiI / OoOoOO00
if 42 - 42: OoO0O00
if 67 - 67: I1Ii111 . iII111i . O0
if 10 - 10: I1ii11iIi11i % I1ii11iIi11i - iIii1I11I1II1 / OOooOOo + Ii1I
lisp_last_icmp_too_big_sent = 0
if 87 - 87: oO0o * I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / iII111i
if 37 - 37: iII111i - ooOoO0o * oO0o % i11iIiiIii - I1Ii111
if 83 - 83: I11i / I1IiiI
if 34 - 34: IiII
LISP_FLOW_LOG_SIZE = 100
lisp_flow_log = [ ]
if 57 - 57: oO0o . I11i . i1IIi
if 42 - 42: I11i + I1ii11iIi11i % O0
if 6 - 6: oO0o
if 68 - 68: OoOoOO00 - OoO0O00
lisp_policies = { }
if 28 - 28: OoO0O00 . OOooOOo / OOooOOo + Oo0Ooo . I1ii11iIi11i
if 1 - 1: iIii1I11I1II1 / II111iiii
if 33 - 33: I11i
if 18 - 18: o0oOOo0O0Ooo % iII111i * O0
if 87 - 87: i11iIiiIii
lisp_load_split_pings = False
if 93 - 93: I1ii11iIi11i - OoO0O00 % i11iIiiIii . iII111i / iII111i - I1Ii111
if 9 - 9: I1ii11iIi11i / Oo0Ooo - I1IiiI / OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
if 91 - 91: iII111i % i1IIi % iIii1I11I1II1
if 20 - 20: OOooOOo % Ii1I / Ii1I + Ii1I
if 45 - 45: oO0o - IiII - OoooooooOO - OoO0O00 . II111iiii / O0
if 51 - 51: O0 + iII111i
lisp_eid_hashes = [ ]
if 8 - 8: oO0o * OoOoOO00 - Ii1I - OoO0O00 * OOooOOo % I1IiiI
if 48 - 48: O0
if 11 - 11: I11i + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
if 41 - 41: Ii1I - O0 - O0
if 68 - 68: OOooOOo % I1Ii111
if 88 - 88: iIii1I11I1II1 - ooOoO0o + OOooOOo
if 40 - 40: I1IiiI * Ii1I + OOooOOo % iII111i
if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + I1Ii111 / OoOoOO00
lisp_reassembly_queue = { }
if 23 - 23: O0
if 85 - 85: Ii1I
if 84 - 84: I1IiiI . iIii1I11I1II1 % OoooooooOO + Ii1I % OoooooooOO % OoO0O00
if 42 - 42: OoO0O00 / I11i / o0oOOo0O0Ooo + iII111i / OoOoOO00
if 84 - 84: ooOoO0o * II111iiii + Oo0Ooo
if 53 - 53: iII111i % II111iiii . IiII - iIii1I11I1II1 - IiII * II111iiii
if 77 - 77: iIii1I11I1II1 * OoO0O00
lisp_pubsub_cache = { }
if 95 - 95: I1IiiI + i11iIiiIii
if 6 - 6: ooOoO0o / i11iIiiIii + iII111i * oO0o
if 80 - 80: II111iiii
if 83 - 83: I11i . i11iIiiIii + II111iiii . o0oOOo0O0Ooo * I11i
if 53 - 53: II111iiii
if 31 - 31: OoO0O00
lisp_decent_push_configured = False
if 80 - 80: I1Ii111 . i11iIiiIii - o0oOOo0O0Ooo
if 25 - 25: OoO0O00
if 62 - 62: OOooOOo + O0
if 98 - 98: o0oOOo0O0Ooo
if 51 - 51: Oo0Ooo - oO0o + II111iiii * Ii1I . I11i + oO0o
if 78 - 78: i11iIiiIii / iII111i - Ii1I / OOooOOo + oO0o
lisp_decent_modulus = 0
lisp_decent_dns_suffix = None
if 82 - 82: Ii1I
if 46 - 46: OoooooooOO . i11iIiiIii
if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
if 87 - 87: Oo0Ooo . IiII
if 75 - 75: ooOoO0o + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . iII111i
if 55 - 55: OOooOOo . I1IiiI
lisp_ipc_socket = None
if 61 - 61: Oo0Ooo % IiII . Oo0Ooo
if 100 - 100: I1Ii111 * O0
if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
if 79 - 79: O0
lisp_ms_encryption_keys = { }
lisp_ms_json_keys = { }
if 78 - 78: I1ii11iIi11i + OOooOOo - I1Ii111
if 38 - 38: o0oOOo0O0Ooo - oO0o + iIii1I11I1II1 / OoOoOO00 % Oo0Ooo
if 57 - 57: OoO0O00 / ooOoO0o
if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * OOooOOo . I1IiiI * I1IiiI
if 7 - 7: IiII * I1Ii111 % Ii1I - o0oOOo0O0Ooo
if 13 - 13: Ii1I . i11iIiiIii
if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
if 33 - 33: I1Ii111 + iII111i * oO0o / iIii1I11I1II1 - I1IiiI
if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
if 57 - 57: i11iIiiIii . I1ii11iIi11i - Ii1I - oO0o + OoOoOO00
if 63 - 63: OoOoOO00 * iII111i
if 69 - 69: O0 . OoO0O00
lisp_rtr_nat_trace_cache = { }
if 49 - 49: I1IiiI - I11i
if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
if 62 - 62: OoooooooOO * I1IiiI
if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
if 50 - 50: I1Ii111 . o0oOOo0O0Ooo
if 97 - 97: O0 + OoOoOO00
if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * I11i * Ii1I
if 37 - 37: OoooooooOO - O0 - o0oOOo0O0Ooo
if 77 - 77: OOooOOo * iIii1I11I1II1
if 98 - 98: I1IiiI % Ii1I * OoooooooOO
lisp_glean_mappings = [ ]
if 51 - 51: iIii1I11I1II1 . OoOoOO00 / oO0o + o0oOOo0O0Ooo
if 33 - 33: ooOoO0o . II111iiii % iII111i + o0oOOo0O0Ooo
if 71 - 71: Oo0Ooo % OOooOOo
if 98 - 98: I11i % i11iIiiIii % ooOoO0o + Ii1I
if 78 - 78: I1ii11iIi11i % oO0o / iII111i - iIii1I11I1II1
if 69 - 69: I1Ii111
if 11 - 11: I1IiiI
if 16 - 16: Ii1I + IiII * O0 % i1IIi . I1IiiI
if 67 - 67: OoooooooOO / I1IiiI * Ii1I + I11i
if 65 - 65: OoooooooOO - I1ii11iIi11i / ooOoO0o / II111iiii / i1IIi
if 71 - 71: I1Ii111 + Ii1I
if 28 - 28: OOooOOo
if 38 - 38: ooOoO0o % II111iiii % I11i / OoO0O00 + OoOoOO00 / i1IIi
if 54 - 54: iIii1I11I1II1 % I1ii11iIi11i - OOooOOo / oO0o - OoO0O00 . I11i
if 11 - 11: I1ii11iIi11i . OoO0O00 * IiII * OoooooooOO + ooOoO0o
if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
if 18 - 18: I1Ii111 / Oo0Ooo * I1Ii111 + I1Ii111 * i11iIiiIii * I1ii11iIi11i
if 11 - 11: ooOoO0o / OoOoOO00 - IiII * OoooooooOO + OoooooooOO . OoOoOO00
if 26 - 26: Ii1I % I1ii11iIi11i
lisp_gleaned_groups = { }
if 76 - 76: IiII * iII111i
if 52 - 52: OOooOOo
if 19 - 19: I1IiiI
if 25 - 25: Ii1I / ooOoO0o
if 31 - 31: OOooOOo . O0 % I1IiiI . o0oOOo0O0Ooo + IiII
lisp_icmp_raw_socket = None
if ( os . getenv ( "LISP_SEND_ICMP_TOO_BIG" ) != None ) :
 lisp_icmp_raw_socket = socket . socket ( socket . AF_INET , socket . SOCK_RAW ,
 socket . IPPROTO_ICMP )
 lisp_icmp_raw_socket . setsockopt ( socket . SOL_IP , socket . IP_HDRINCL , 1 )
 if 71 - 71: I1Ii111 . II111iiii
 if 62 - 62: OoooooooOO . I11i
lisp_ignore_df_bit = ( os . getenv ( "LISP_IGNORE_DF_BIT" ) != None )
if 61 - 61: OoOoOO00 - OOooOOo - i1IIi
if 25 - 25: O0 * I11i + I1ii11iIi11i . o0oOOo0O0Ooo . o0oOOo0O0Ooo
if 58 - 58: I1IiiI
if 53 - 53: i1IIi
if 59 - 59: o0oOOo0O0Ooo
if 81 - 81: OoOoOO00 - OoOoOO00 . iII111i
LISP_DATA_PORT = 4341
LISP_CTRL_PORT = 4342
LISP_L2_DATA_PORT = 8472
LISP_VXLAN_DATA_PORT = 4789
LISP_VXLAN_GPE_PORT = 4790
LISP_TRACE_PORT = 2434
if 73 - 73: I11i % i11iIiiIii - I1IiiI
if 7 - 7: O0 * i11iIiiIii * Ii1I + ooOoO0o % OoO0O00 - ooOoO0o
if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
if 23 - 23: i11iIiiIii
LISP_MAP_REQUEST = 1
LISP_MAP_REPLY = 2
LISP_MAP_REGISTER = 3
LISP_MAP_NOTIFY = 4
LISP_MAP_NOTIFY_ACK = 5
LISP_MAP_REFERRAL = 6
LISP_NAT_INFO = 7
LISP_ECM = 8
LISP_TRACE = 9
if 30 - 30: o0oOOo0O0Ooo - i1IIi % II111iiii + I11i * iIii1I11I1II1
if 81 - 81: IiII % i1IIi . iIii1I11I1II1
if 4 - 4: i11iIiiIii % OoO0O00 % i1IIi / IiII
if 6 - 6: iII111i / I1IiiI % OOooOOo - I1IiiI
LISP_NO_ACTION = 0
LISP_NATIVE_FORWARD_ACTION = 1
LISP_SEND_MAP_REQUEST_ACTION = 2
LISP_DROP_ACTION = 3
LISP_POLICY_DENIED_ACTION = 4
LISP_AUTH_FAILURE_ACTION = 5
LISP_SEND_PUBSUB_ACTION = 6
if 31 - 31: OOooOOo
lisp_map_reply_action_string = [ "no-action" , "native-forward" ,
 "send-map-request" , "drop-action" , "policy-denied" ,
 "auth-failure" , "send-subscribe" ]
if 23 - 23: I1Ii111 . IiII
if 92 - 92: OoOoOO00 + I1Ii111 * Ii1I % I1IiiI
if 42 - 42: Oo0Ooo
if 76 - 76: I1IiiI * iII111i % I1Ii111
LISP_NONE_ALG_ID = 0
LISP_SHA_1_96_ALG_ID = 1
LISP_SHA_256_128_ALG_ID = 2
LISP_MD5_AUTH_DATA_LEN = 16
LISP_SHA1_160_AUTH_DATA_LEN = 20
LISP_SHA2_256_AUTH_DATA_LEN = 32
if 57 - 57: iIii1I11I1II1 - i1IIi / I1Ii111 - O0 * OoooooooOO % II111iiii
if 68 - 68: OoooooooOO * I11i % OoOoOO00 - IiII
if 34 - 34: I1Ii111 . iIii1I11I1II1 * OoOoOO00 * oO0o / I1Ii111 / I1ii11iIi11i
if 78 - 78: Oo0Ooo - o0oOOo0O0Ooo / OoOoOO00
LISP_LCAF_NULL_TYPE = 0
LISP_LCAF_AFI_LIST_TYPE = 1
LISP_LCAF_INSTANCE_ID_TYPE = 2
LISP_LCAF_ASN_TYPE = 3
LISP_LCAF_APP_DATA_TYPE = 4
LISP_LCAF_GEO_COORD_TYPE = 5
LISP_LCAF_OPAQUE_TYPE = 6
LISP_LCAF_NAT_TYPE = 7
LISP_LCAF_NONCE_LOC_TYPE = 8
LISP_LCAF_MCAST_INFO_TYPE = 9
LISP_LCAF_ELP_TYPE = 10
LISP_LCAF_SECURITY_TYPE = 11
LISP_LCAF_SOURCE_DEST_TYPE = 12
LISP_LCAF_RLE_TYPE = 13
LISP_LCAF_JSON_TYPE = 14
LISP_LCAF_KV_TYPE = 15
LISP_LCAF_ENCAP_TYPE = 16
if 10 - 10: iII111i + Oo0Ooo * I1ii11iIi11i + iIii1I11I1II1 / I1Ii111 / I1ii11iIi11i
if 42 - 42: I1IiiI
if 38 - 38: OOooOOo + II111iiii % ooOoO0o % OoOoOO00 - Ii1I / OoooooooOO
if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
LISP_MR_TTL = ( 24 * 60 )
LISP_REGISTER_TTL = 3
LISP_SHORT_TTL = 1
LISP_NMR_TTL = 15
LISP_GLEAN_TTL = 15
LISP_MCAST_TTL = 15
LISP_IGMP_TTL = 240
if 85 - 85: Ii1I % iII111i + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
LISP_SITE_TIMEOUT_CHECK_INTERVAL = 60
LISP_PUBSUB_TIMEOUT_CHECK_INTERVAL = 60
LISP_REFERRAL_TIMEOUT_CHECK_INTERVAL = 60
LISP_TEST_MR_INTERVAL = 60
LISP_MAP_NOTIFY_INTERVAL = 2
LISP_DDT_MAP_REQUEST_INTERVAL = 2
LISP_MAX_MAP_NOTIFY_RETRIES = 3
LISP_INFO_INTERVAL = 15
LISP_MAP_REQUEST_RATE_LIMIT = .5
LISP_NO_MAP_REQUEST_RATE_LIMIT_TIME = 60
LISP_ICMP_TOO_BIG_RATE_LIMIT = 1
if 62 - 62: i11iIiiIii + i11iIiiIii - o0oOOo0O0Ooo
LISP_RLOC_PROBE_TTL = 128
LISP_RLOC_PROBE_INTERVAL = 10
LISP_RLOC_PROBE_REPLY_WAIT = 15
LISP_DEFAULT_DYN_EID_TIMEOUT = 15
LISP_NONCE_ECHO_INTERVAL = 10
LISP_IGMP_TIMEOUT_INTERVAL = 180
if 28 - 28: iII111i . iII111i % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iII111i
if 27 - 27: OoO0O00 + ooOoO0o - i1IIi
if 69 - 69: IiII - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
if 79 - 79: O0 * i11iIiiIii - IiII / IiII
if 48 - 48: O0
if 93 - 93: i11iIiiIii - I1IiiI * I1ii11iIi11i * I11i % O0 + OoooooooOO
if 25 - 25: IiII + Ii1I / ooOoO0o . o0oOOo0O0Ooo % O0 * OoO0O00
if 84 - 84: ooOoO0o % Ii1I + i11iIiiIii
if 28 - 28: Oo0Ooo + OoO0O00 * OOooOOo % oO0o . I11i % O0
if 16 - 16: I11i - iIii1I11I1II1 / I1IiiI . II111iiii + iIii1I11I1II1
if 19 - 19: OoO0O00 - Oo0Ooo . O0
if 60 - 60: II111iiii + Oo0Ooo
if 9 - 9: ooOoO0o * OoooooooOO - iIii1I11I1II1 + OoOoOO00 / OoO0O00 . OoO0O00
if 49 - 49: II111iiii
if 25 - 25: OoooooooOO - I1IiiI . I1IiiI * oO0o
if 81 - 81: iII111i + IiII
if 98 - 98: I1IiiI
if 95 - 95: ooOoO0o / ooOoO0o
if 30 - 30: I1ii11iIi11i + Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
if 55 - 55: ooOoO0o - I11i + II111iiii + iII111i % Ii1I
if 41 - 41: i1IIi - I11i - Ii1I
if 8 - 8: OoO0O00 + I1Ii111 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
if 9 - 9: Oo0Ooo - i11iIiiIii - OOooOOo * Ii1I + ooOoO0o
if 44 - 44: II111iiii
if 52 - 52: I1ii11iIi11i - Oo0Ooo + I1ii11iIi11i % o0oOOo0O0Ooo
if 35 - 35: iIii1I11I1II1
if 42 - 42: I1Ii111 . I1IiiI . i1IIi + OoOoOO00 + OOooOOo + I1IiiI
if 31 - 31: iII111i . OOooOOo - ooOoO0o . OoooooooOO / OoooooooOO
if 56 - 56: OoO0O00 / oO0o / i11iIiiIii + OoooooooOO - Oo0Ooo - I11i
if 21 - 21: O0 % IiII . I1IiiI / II111iiii + IiII
if 53 - 53: oO0o - I1IiiI - oO0o * iII111i
if 71 - 71: O0 - iIii1I11I1II1
if 12 - 12: OOooOOo / o0oOOo0O0Ooo
if 42 - 42: Oo0Ooo
if 19 - 19: oO0o % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
if 46 - 46: Oo0Ooo
if 1 - 1: iII111i
if 97 - 97: OOooOOo + iII111i + O0 + i11iIiiIii
if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . iII111i % iII111i + i11iIiiIii
if 72 - 72: iIii1I11I1II1 * Ii1I % ooOoO0o / OoO0O00
if 35 - 35: ooOoO0o + i1IIi % I1ii11iIi11i % I11i + oO0o
if 17 - 17: i1IIi
if 21 - 21: Oo0Ooo
if 29 - 29: I11i / II111iiii / ooOoO0o * OOooOOo
if 10 - 10: I1Ii111 % IiII * IiII . I11i / Ii1I % OOooOOo
if 49 - 49: OoO0O00 / oO0o + O0 * o0oOOo0O0Ooo
if 28 - 28: ooOoO0o + i11iIiiIii / I11i % OoOoOO00 % Oo0Ooo - O0
if 54 - 54: i1IIi + II111iiii
LISP_CS_1024 = 0
LISP_CS_1024_G = 2
LISP_CS_1024_P = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381FFFFFFFFFFFFFFFF
if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
LISP_CS_2048_CBC = 1
LISP_CS_2048_CBC_G = 2
LISP_CS_2048_CBC_P = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381FFFFFFFFFFFFFFFF
if 5 - 5: Ii1I
LISP_CS_25519_CBC = 2
LISP_CS_2048_GCM = 3
if 46 - 46: IiII
LISP_CS_3072 = 4
LISP_CS_3072_G = 2
LISP_CS_3072_P = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AAAC42DAD33170D04507A33A85521ABDF1CBA64ECFB850458DBEF0A8AEA71575D060C7DB3970F85A6E1E4C7ABF5AE8CDB0933D71E8C94E04A25619DCEE3D2261AD2EE6BF12FFA06D98A0864D87602733EC86A64521F2B18177B200CBBE117577A615D6C770988C0BAD946E208E24FA074E5AB3143DB5BFCE0FD108E4B82D120A93AD2CAFFFFFFFFFFFFFFFF
if 45 - 45: ooOoO0o
LISP_CS_25519_GCM = 5
LISP_CS_25519_CHACHA = 6
if 21 - 21: oO0o . I1Ii111 . OOooOOo / Oo0Ooo / I1Ii111
LISP_4_32_MASK = 0xFFFFFFFF
LISP_8_64_MASK = 0xFFFFFFFFFFFFFFFF
LISP_16_128_MASK = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
if 17 - 17: OOooOOo / OOooOOo / I11i
if 1 - 1: i1IIi . i11iIiiIii % OOooOOo
if 82 - 82: iIii1I11I1II1 + Oo0Ooo . iIii1I11I1II1 % IiII / Ii1I . Ii1I
if 14 - 14: o0oOOo0O0Ooo . OOooOOo . I11i + OoooooooOO - OOooOOo + IiII
if 9 - 9: Ii1I
if 59 - 59: I1IiiI * II111iiii . O0
if 56 - 56: Ii1I - iII111i % I1IiiI - o0oOOo0O0Ooo
if 51 - 51: O0 / ooOoO0o * iIii1I11I1II1 + I1ii11iIi11i + o0oOOo0O0Ooo
def lisp_record_traceback ( * args ) :
 if 98 - 98: iIii1I11I1II1 * I1ii11iIi11i * OOooOOo + ooOoO0o % i11iIiiIii % O0
 i1 = datetime . datetime . now ( ) . strftime ( "%m/%d/%y %H:%M:%S.%f" ) [ : - 3 ]
 OO0oOOoo = open ( "./logs/lisp-traceback.log" , "a" )
 OO0oOOoo . write ( "---------- Exception occurred: {} ----------\n" . format ( i1 ) )
 try :
  traceback . print_last ( file = OO0oOOoo )
 except :
  OO0oOOoo . write ( "traceback.print_last(file=fd) failed" )
  if 52 - 52: o0oOOo0O0Ooo % Oo0Ooo
 try :
  traceback . print_last ( )
 except :
  print ( "traceback.print_last() failed" )
  if 64 - 64: O0 % I11i % O0 * OoO0O00 . oO0o + I1IiiI
 OO0oOOoo . close ( )
 return
 if 75 - 75: I11i . OoooooooOO % o0oOOo0O0Ooo * I11i % OoooooooOO
 if 13 - 13: IiII / i11iIiiIii % II111iiii % I11i . I1ii11iIi11i
 if 8 - 8: OoOoOO00 + Oo0Ooo - II111iiii
 if 11 - 11: i1IIi % i11iIiiIii - i1IIi * OoOoOO00
 if 39 - 39: I1Ii111
 if 86 - 86: I11i * I1IiiI + I11i + II111iiii
 if 8 - 8: I1Ii111 - iII111i / ooOoO0o
def lisp_set_exception ( ) :
 sys . excepthook = lisp_record_traceback
 return
 if 96 - 96: OoOoOO00
 if 29 - 29: I1ii11iIi11i / i1IIi . I1IiiI - OoOoOO00 - OoOoOO00 - Ii1I
 if 20 - 20: i1IIi % OoO0O00 . I1IiiI / IiII * i11iIiiIii * OOooOOo
 if 85 - 85: o0oOOo0O0Ooo . OoOoOO00 / ooOoO0o . O0 % I1Ii111
 if 90 - 90: Oo0Ooo % O0 * iIii1I11I1II1 . iII111i
 if 8 - 8: ooOoO0o + II111iiii / iII111i / I11i
 if 74 - 74: O0 / i1IIi
def lisp_is_raspbian ( ) :
 if ( platform . dist ( ) [ 0 ] != "debian" ) : return ( False )
 return ( platform . machine ( ) in [ "armv6l" , "armv7l" ] )
 if 78 - 78: OoooooooOO . OoO0O00 + ooOoO0o - i1IIi
 if 31 - 31: OoooooooOO . OOooOOo
 if 83 - 83: iII111i . O0 / Oo0Ooo / OOooOOo - II111iiii
 if 100 - 100: OoO0O00
 if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iII111i . iIii1I11I1II1 * iII111i
 if 38 - 38: I1ii11iIi11i - iII111i / O0 . I1Ii111
 if 45 - 45: I1Ii111
def lisp_is_ubuntu ( ) :
 return ( platform . dist ( ) [ 0 ] == "Ubuntu" )
 if 83 - 83: OoOoOO00 . OoooooooOO
 if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / IiII / i11iIiiIii
 if 62 - 62: OoO0O00 / I1ii11iIi11i
 if 7 - 7: OoooooooOO . IiII
 if 53 - 53: Ii1I % Ii1I * o0oOOo0O0Ooo + OoOoOO00
 if 92 - 92: OoooooooOO + i1IIi / Ii1I * O0
 if 100 - 100: ooOoO0o % iIii1I11I1II1 * II111iiii - iII111i
def lisp_is_fedora ( ) :
 return ( platform . dist ( ) [ 0 ] == "fedora" )
 if 92 - 92: ooOoO0o
 if 22 - 22: Oo0Ooo % iII111i * I1ii11iIi11i / OOooOOo % i11iIiiIii * I11i
 if 95 - 95: OoooooooOO - IiII * I1IiiI + OoOoOO00
 if 10 - 10: o0oOOo0O0Ooo / i11iIiiIii
 if 92 - 92: I11i . I1Ii111
 if 85 - 85: I1ii11iIi11i . I1Ii111
 if 78 - 78: ooOoO0o * I1Ii111 + iIii1I11I1II1 + iIii1I11I1II1 / I1Ii111 . Ii1I
def lisp_is_centos ( ) :
 return ( platform . dist ( ) [ 0 ] == "centos" )
 if 97 - 97: ooOoO0o / I1Ii111 % i1IIi % I1ii11iIi11i
 if 18 - 18: iIii1I11I1II1 % I11i
 if 95 - 95: ooOoO0o + i11iIiiIii * I1Ii111 - i1IIi * I1Ii111 - iIii1I11I1II1
 if 75 - 75: OoooooooOO * IiII
 if 9 - 9: IiII - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
 if 39 - 39: IiII * Oo0Ooo + iIii1I11I1II1 - IiII + OOooOOo
 if 69 - 69: O0
def lisp_is_debian ( ) :
 return ( platform . dist ( ) [ 0 ] == "debian" )
 if 85 - 85: ooOoO0o / O0
 if 18 - 18: o0oOOo0O0Ooo % O0 * I1ii11iIi11i
 if 62 - 62: I1Ii111 . IiII . OoooooooOO
 if 11 - 11: OOooOOo / I11i
 if 73 - 73: i1IIi / i11iIiiIii
 if 58 - 58: Oo0Ooo . II111iiii + oO0o - i11iIiiIii / II111iiii / O0
 if 85 - 85: OoOoOO00 + OOooOOo
def lisp_is_debian_kali ( ) :
 return ( platform . dist ( ) [ 0 ] == "Kali" )
 if 10 - 10: IiII / OoO0O00 + OoOoOO00 / i1IIi
 if 27 - 27: Ii1I
 if 67 - 67: I1IiiI
 if 55 - 55: I1ii11iIi11i - iII111i * o0oOOo0O0Ooo + OoOoOO00 * OoOoOO00 * O0
 if 91 - 91: I1Ii111 - OOooOOo % iIii1I11I1II1 - OoooooooOO % ooOoO0o
 if 98 - 98: OoO0O00 . OoO0O00 * oO0o * II111iiii * I1Ii111
 if 92 - 92: Oo0Ooo
def lisp_is_macos ( ) :
 return ( platform . uname ( ) [ 0 ] == "Darwin" )
 if 40 - 40: OoOoOO00 / IiII
 if 79 - 79: OoO0O00 - iIii1I11I1II1 + Ii1I - I1Ii111
 if 93 - 93: II111iiii . I1IiiI - Oo0Ooo + OoOoOO00
 if 61 - 61: II111iiii
 if 15 - 15: i11iIiiIii % I1IiiI * I11i / I1Ii111
 if 90 - 90: iII111i
 if 31 - 31: OOooOOo + O0
def lisp_is_alpine ( ) :
 return ( os . path . exists ( "/etc/alpine-release" ) )
 if 87 - 87: ooOoO0o
 if 45 - 45: OoO0O00 / OoooooooOO - iII111i / Ii1I % IiII
 if 83 - 83: I1IiiI . iIii1I11I1II1 - IiII * i11iIiiIii
 if 20 - 20: i1IIi * I1Ii111 + II111iiii % o0oOOo0O0Ooo % oO0o
 if 13 - 13: Oo0Ooo
 if 60 - 60: I1ii11iIi11i * I1IiiI
 if 17 - 17: OOooOOo % Oo0Ooo / I1ii11iIi11i . IiII * OOooOOo - II111iiii
def lisp_is_x86 ( ) :
 i1i1IIii1i1 = platform . machine ( )
 return ( i1i1IIii1i1 in ( "x86" , "i686" , "x86_64" ) )
 if 65 - 65: I1IiiI + OoOoOO00 / OOooOOo
 if 83 - 83: o0oOOo0O0Ooo . iII111i - Oo0Ooo
 if 65 - 65: iIii1I11I1II1 / ooOoO0o . IiII - II111iiii
 if 72 - 72: iIii1I11I1II1 / IiII % iII111i % OOooOOo - I11i % OOooOOo
 if 100 - 100: Oo0Ooo + i11iIiiIii
 if 71 - 71: I11i / o0oOOo0O0Ooo / I1Ii111 % OOooOOo
 if 51 - 51: IiII * O0 / II111iiii . Ii1I % OOooOOo / I1IiiI
def lisp_is_linux ( ) :
 return ( platform . uname ( ) [ 0 ] == "Linux" )
 if 9 - 9: I1IiiI % I1IiiI % II111iiii
 if 30 - 30: IiII + I1Ii111 - IiII . IiII - II111iiii + O0
 if 86 - 86: i1IIi
 if 41 - 41: OoOoOO00 * I11i / OoOoOO00 % oO0o
 if 18 - 18: II111iiii . OoooooooOO % OoOoOO00 % Ii1I
 if 9 - 9: OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
 if 2 - 2: OoooooooOO % OOooOOo
def lisp_on_aws ( ) :
 oOoOOo0oo0 = commands . getoutput ( "sudo dmidecode -s bios-vendor" )
 if ( oOoOOo0oo0 . find ( "command not found" ) != - 1 and lisp_on_docker ( ) ) :
  o0O0Oo00Oo0o = bold ( "AWS check" , False )
  lprint ( "{} - dmidecode not installed in docker container" . format ( o0O0Oo00Oo0o ) )
  if 74 - 74: Oo0Ooo / i11iIiiIii - II111iiii * o0oOOo0O0Ooo
 return ( oOoOOo0oo0 . lower ( ) . find ( "amazon" ) != - 1 )
 if 5 - 5: OOooOOo - OOooOOo . Oo0Ooo + OoOoOO00 - OOooOOo . oO0o
 if 31 - 31: II111iiii - iIii1I11I1II1 - iIii1I11I1II1 % I11i
 if 12 - 12: iIii1I11I1II1
 if 20 - 20: o0oOOo0O0Ooo / i1IIi
 if 71 - 71: OoOoOO00 . i1IIi
 if 94 - 94: OOooOOo . I1Ii111
 if 84 - 84: O0 . I11i - II111iiii . ooOoO0o / II111iiii
def lisp_on_gcp ( ) :
 oOoOOo0oo0 = commands . getoutput ( "sudo dmidecode -s bios-version" )
 return ( oOoOOo0oo0 . lower ( ) . find ( "google" ) != - 1 )
 if 47 - 47: OoooooooOO
 if 4 - 4: I1IiiI % I11i
 if 10 - 10: IiII . OoooooooOO - OoO0O00 + IiII - O0
 if 82 - 82: ooOoO0o + II111iiii
 if 39 - 39: oO0o % iIii1I11I1II1 % O0 % OoooooooOO * I1ii11iIi11i + iII111i
 if 68 - 68: Oo0Ooo + i11iIiiIii
 if 69 - 69: iIii1I11I1II1 * iIii1I11I1II1 * i11iIiiIii + I1IiiI / OOooOOo % Ii1I
def lisp_on_docker ( ) :
 return ( os . path . exists ( "/.dockerenv" ) )
 if 58 - 58: OOooOOo * o0oOOo0O0Ooo + O0 % OOooOOo
 if 25 - 25: Oo0Ooo % I1ii11iIi11i * ooOoO0o
 if 6 - 6: iII111i . IiII * OoOoOO00 . i1IIi
 if 98 - 98: i1IIi
 if 65 - 65: OoOoOO00 / OoO0O00 % IiII
 if 45 - 45: OoOoOO00
 if 66 - 66: OoO0O00
 if 56 - 56: O0
def lisp_process_logfile ( ) :
 OOo00 = "./logs/lisp-{}.log" . format ( lisp_log_id )
 if ( os . path . exists ( OOo00 ) ) : return
 if 37 - 37: i1IIi
 sys . stdout . close ( )
 sys . stdout = open ( OOo00 , "a" )
 if 46 - 46: OoOoOO00 - I11i - Ii1I . i1IIi
 lisp_print_banner ( bold ( "logfile rotation" , False ) )
 return
 if 35 - 35: II111iiii * I11i - OoooooooOO . I11i . I11i
 if 11 - 11: I1Ii111 / OoOoOO00 + I11i % iIii1I11I1II1
 if 42 - 42: I1ii11iIi11i * OoOoOO00 % ooOoO0o - OoOoOO00 . i11iIiiIii - I1Ii111
 if 84 - 84: I1Ii111 - I1ii11iIi11i / I11i
 if 13 - 13: IiII - Oo0Ooo - ooOoO0o
 if 92 - 92: ooOoO0o / OoOoOO00 * OoO0O00 . I11i % II111iiii
 if 71 - 71: I1Ii111 % i1IIi - II111iiii - OOooOOo + OOooOOo * ooOoO0o
 if 51 - 51: iIii1I11I1II1 / OoOoOO00 + OOooOOo - I11i + iII111i
def lisp_i_am ( name ) :
 global lisp_log_id , lisp_i_am_itr , lisp_i_am_etr , lisp_i_am_rtr
 global lisp_i_am_mr , lisp_i_am_ms , lisp_i_am_ddt , lisp_i_am_core
 global lisp_hostname
 if 29 - 29: o0oOOo0O0Ooo % iIii1I11I1II1 . OoooooooOO % OoooooooOO % II111iiii / iII111i
 lisp_log_id = name
 if ( name == "itr" ) : lisp_i_am_itr = True
 if ( name == "etr" ) : lisp_i_am_etr = True
 if ( name == "rtr" ) : lisp_i_am_rtr = True
 if ( name == "mr" ) : lisp_i_am_mr = True
 if ( name == "ms" ) : lisp_i_am_ms = True
 if ( name == "ddt" ) : lisp_i_am_ddt = True
 if ( name == "core" ) : lisp_i_am_core = True
 if 70 - 70: i11iIiiIii % iII111i
 if 11 - 11: IiII % I1ii11iIi11i % Ii1I / II111iiii % I1Ii111 - Oo0Ooo
 if 96 - 96: I1ii11iIi11i / II111iiii . Ii1I - iII111i * I11i * oO0o
 if 76 - 76: Ii1I - II111iiii * OOooOOo / OoooooooOO
 if 18 - 18: OoO0O00 + iIii1I11I1II1 - II111iiii - I1IiiI
 lisp_hostname = socket . gethostname ( )
 ooo = lisp_hostname . find ( "." )
 if ( ooo != - 1 ) : lisp_hostname = lisp_hostname [ 0 : ooo ]
 return
 if 94 - 94: OoOoOO00 - Oo0Ooo - I1IiiI % i1IIi
 if 19 - 19: o0oOOo0O0Ooo
 if 42 - 42: i1IIi . I1IiiI / i1IIi + Ii1I
 if 54 - 54: ooOoO0o % OOooOOo . I1Ii111 + oO0o - OOooOOo * I1IiiI
 if 92 - 92: o0oOOo0O0Ooo + I1Ii111 / Oo0Ooo % OoO0O00 % IiII . OoooooooOO
 if 52 - 52: ooOoO0o / i11iIiiIii - OOooOOo . IiII % iIii1I11I1II1 + o0oOOo0O0Ooo
 if 71 - 71: oO0o % I11i * OoOoOO00 . O0 / Ii1I . I1ii11iIi11i
 if 58 - 58: Oo0Ooo / oO0o
 if 44 - 44: OOooOOo
def lprint ( * args ) :
 O0O0o0o0o = ( "force" in args )
 if ( lisp_debug_logging == False and O0O0o0o0o == False ) : return
 if 9 - 9: Oo0Ooo + OoOoOO00 - iIii1I11I1II1 - Ii1I + o0oOOo0O0Ooo
 lisp_process_logfile ( )
 i1 = datetime . datetime . now ( ) . strftime ( "%m/%d/%y %H:%M:%S.%f" )
 i1 = i1 [ : - 3 ]
 print "{}: {}:" . format ( i1 , lisp_log_id ) ,
 if 97 - 97: OOooOOo
 for OO0OOooOO0 in args :
  if ( OO0OOooOO0 == "force" ) : continue
  print OO0OOooOO0 ,
  if 31 - 31: I1IiiI * oO0o + OoooooooOO - iII111i / OoooooooOO
 print ""
 if 19 - 19: IiII * ooOoO0o * o0oOOo0O0Ooo + O0 / O0
 try : sys . stdout . flush ( )
 except : pass
 return
 if 73 - 73: iIii1I11I1II1 / iIii1I11I1II1 - oO0o
 if 91 - 91: oO0o + I1IiiI
 if 59 - 59: I1IiiI + i11iIiiIii + i1IIi / I11i
 if 44 - 44: I11i . OoOoOO00 * I1IiiI + OoooooooOO - iII111i - IiII
 if 15 - 15: IiII / O0 . o0oOOo0O0Ooo . i11iIiiIii
 if 59 - 59: I1Ii111 - o0oOOo0O0Ooo - ooOoO0o
 if 48 - 48: i1IIi + I11i % OoOoOO00 / Oo0Ooo - o0oOOo0O0Ooo
 if 67 - 67: oO0o % o0oOOo0O0Ooo . OoooooooOO + OOooOOo * I11i * OoOoOO00
def fprint ( * args ) :
 iiIii1I = args + ( "force" , )
 lprint ( * iiIii1I )
 return
 if 47 - 47: ooOoO0o . I11i / o0oOOo0O0Ooo
 if 83 - 83: o0oOOo0O0Ooo / OOooOOo / OOooOOo + o0oOOo0O0Ooo * I1Ii111 + o0oOOo0O0Ooo
 if 36 - 36: OoOoOO00 + o0oOOo0O0Ooo - OoooooooOO . oO0o . OoooooooOO / Oo0Ooo
 if 72 - 72: i1IIi
 if 82 - 82: OoOoOO00 + OoooooooOO / i11iIiiIii * I1ii11iIi11i . OoooooooOO
 if 63 - 63: I1ii11iIi11i
 if 6 - 6: ooOoO0o / I1ii11iIi11i
 if 57 - 57: I11i
def dprint ( * args ) :
 if ( lisp_data_plane_logging ) : lprint ( * args )
 return
 if 67 - 67: OoO0O00 . ooOoO0o
 if 87 - 87: oO0o % Ii1I
 if 83 - 83: II111iiii - I11i
 if 35 - 35: i1IIi - iIii1I11I1II1 + i1IIi
 if 86 - 86: iIii1I11I1II1 + OoOoOO00 . i11iIiiIii - Ii1I
 if 51 - 51: OoOoOO00
 if 14 - 14: IiII % oO0o % Oo0Ooo - i11iIiiIii
 if 53 - 53: Ii1I % Oo0Ooo
def debug ( * args ) :
 lisp_process_logfile ( )
 if 59 - 59: OOooOOo % iIii1I11I1II1 . i1IIi + II111iiii * IiII
 i1 = datetime . datetime . now ( ) . strftime ( "%m/%d/%y %H:%M:%S.%f" )
 i1 = i1 [ : - 3 ]
 if 41 - 41: Ii1I % I1ii11iIi11i
 print red ( ">>>" , False ) ,
 print "{}:" . format ( i1 ) ,
 for OO0OOooOO0 in args : print OO0OOooOO0 ,
 print red ( "<<<\n" , False )
 try : sys . stdout . flush ( )
 except : pass
 return
 if 12 - 12: OOooOOo
 if 69 - 69: OoooooooOO + OOooOOo
 if 26 - 26: Oo0Ooo + OOooOOo / OoO0O00 % OoOoOO00 % I1ii11iIi11i + II111iiii
 if 31 - 31: I11i % OOooOOo * I11i
 if 45 - 45: i1IIi . I1IiiI + OOooOOo - OoooooooOO % ooOoO0o
 if 1 - 1: iIii1I11I1II1
 if 93 - 93: i1IIi . i11iIiiIii . Oo0Ooo
def lisp_print_caller ( ) :
 fprint ( traceback . print_last ( ) )
 if 99 - 99: I11i - I1Ii111 - oO0o % OoO0O00
 if 21 - 21: II111iiii % I1ii11iIi11i . i1IIi - OoooooooOO
 if 4 - 4: OoooooooOO . ooOoO0o
 if 78 - 78: I1ii11iIi11i + I11i - O0
 if 10 - 10: I1Ii111 % I1IiiI
 if 97 - 97: OoooooooOO - I1Ii111
 if 58 - 58: iIii1I11I1II1 + O0
def lisp_print_banner ( string ) :
 global lisp_version , lisp_hostname
 if 30 - 30: ooOoO0o % iII111i * OOooOOo - I1ii11iIi11i * Ii1I % ooOoO0o
 if ( lisp_version == "" ) :
  lisp_version = commands . getoutput ( "cat lisp-version.txt" )
  if 46 - 46: i11iIiiIii - O0 . oO0o
 Oo0O = bold ( lisp_hostname , False )
 lprint ( "lispers.net LISP {} {}, version {}, hostname {}" . format ( string ,
 datetime . datetime . now ( ) , lisp_version , Oo0O ) )
 return
 if 1 - 1: O0 / iII111i % I1Ii111 . Oo0Ooo + IiII
 if 27 - 27: I1Ii111 % OoooooooOO + IiII % i1IIi / oO0o / OoooooooOO
 if 11 - 11: OOooOOo % Ii1I - i11iIiiIii - oO0o + ooOoO0o + IiII
 if 87 - 87: I1Ii111 * i1IIi / I1ii11iIi11i
 if 6 - 6: o0oOOo0O0Ooo + Oo0Ooo - OoooooooOO % OOooOOo * OoOoOO00
 if 69 - 69: i1IIi
 if 59 - 59: II111iiii - o0oOOo0O0Ooo
def green ( string , html ) :
 if ( html ) : return ( '<font color="green"><b>{}</b></font>' . format ( string ) )
 return ( bold ( "\033[92m" + string + "\033[0m" , html ) )
 if 24 - 24: Oo0Ooo - i1IIi + I11i
 if 38 - 38: OoooooooOO / I1ii11iIi11i . O0 / i1IIi / Oo0Ooo + iIii1I11I1II1
 if 96 - 96: iII111i
 if 18 - 18: iII111i * I11i - Ii1I
 if 31 - 31: Oo0Ooo - O0 % OoOoOO00 % oO0o
 if 45 - 45: I1ii11iIi11i + II111iiii * i11iIiiIii
 if 13 - 13: OoooooooOO * oO0o - Ii1I / OOooOOo + I11i + IiII
def green_last_sec ( string ) :
 return ( green ( string , True ) )
 if 39 - 39: iIii1I11I1II1 - OoooooooOO
 if 81 - 81: I1ii11iIi11i - O0 * OoooooooOO
 if 23 - 23: II111iiii / oO0o
 if 28 - 28: Oo0Ooo * ooOoO0o - OoO0O00
 if 19 - 19: I11i
 if 67 - 67: O0 % iIii1I11I1II1 / IiII . i11iIiiIii - Ii1I + O0
 if 27 - 27: OOooOOo
def green_last_min ( string ) :
 return ( '<font color="#58D68D"><b>{}</b></font>' . format ( string ) )
 if 89 - 89: II111iiii / oO0o
 if 14 - 14: OOooOOo . I1IiiI * ooOoO0o + II111iiii - ooOoO0o + OOooOOo
 if 18 - 18: oO0o - o0oOOo0O0Ooo - I1IiiI - I1IiiI
 if 54 - 54: Oo0Ooo + I1IiiI / iII111i . I1IiiI * OoOoOO00
 if 1 - 1: OoOoOO00 * OoO0O00 . i1IIi / Oo0Ooo . I1ii11iIi11i + Oo0Ooo
 if 17 - 17: Oo0Ooo + OoO0O00 / Ii1I / iII111i * OOooOOo
 if 29 - 29: OoO0O00 % OoooooooOO * oO0o / II111iiii - oO0o
def red ( string , html ) :
 if ( html ) : return ( '<font color="red"><b>{}</b></font>' . format ( string ) )
 return ( bold ( "\033[91m" + string + "\033[0m" , html ) )
 if 19 - 19: i11iIiiIii
 if 54 - 54: II111iiii . I11i
 if 73 - 73: OoOoOO00 . I1IiiI
 if 32 - 32: OoOoOO00 * I1IiiI % ooOoO0o * Ii1I . O0
 if 48 - 48: iII111i * iII111i
 if 13 - 13: Ii1I / I11i + OoOoOO00 . o0oOOo0O0Ooo % ooOoO0o
 if 48 - 48: I1IiiI / i11iIiiIii - o0oOOo0O0Ooo * oO0o / OoooooooOO
def blue ( string , html ) :
 if ( html ) : return ( '<font color="blue"><b>{}</b></font>' . format ( string ) )
 return ( bold ( "\033[94m" + string + "\033[0m" , html ) )
 if 89 - 89: iIii1I11I1II1 / I1IiiI - II111iiii / Ii1I . i11iIiiIii . Ii1I
 if 48 - 48: O0 + O0 . I1Ii111 - ooOoO0o
 if 63 - 63: oO0o
 if 71 - 71: i1IIi . Ii1I * iII111i % OoooooooOO + OOooOOo
 if 36 - 36: IiII
 if 49 - 49: OOooOOo / OoooooooOO / I1IiiI
 if 74 - 74: I1Ii111 % I1ii11iIi11i
def bold ( string , html ) :
 if ( html ) : return ( "<b>{}</b>" . format ( string ) )
 return ( "\033[1m" + string + "\033[0m" )
 if 7 - 7: II111iiii
 if 27 - 27: oO0o . OoooooooOO + i11iIiiIii
 if 86 - 86: I11i / o0oOOo0O0Ooo - o0oOOo0O0Ooo + I1ii11iIi11i + oO0o
 if 33 - 33: o0oOOo0O0Ooo . iII111i . IiII . i1IIi
 if 49 - 49: I1ii11iIi11i
 if 84 - 84: I11i - Oo0Ooo / O0 - I1Ii111
 if 21 - 21: O0 * O0 % I1ii11iIi11i
def convert_font ( string ) :
 o00ooo = [ [ "[91m" , red ] , [ "[92m" , green ] , [ "[94m" , blue ] , [ "[1m" , bold ] ]
 Ii1IiIiIi1IiI = "[0m"
 if 36 - 36: IiII - OoooooooOO / OoO0O00
 for iIIi1iI1I1IIi in o00ooo :
  O0OO0 = iIIi1iI1I1IIi [ 0 ]
  O0ooo0o0 = iIIi1iI1I1IIi [ 1 ]
  oO0ooOoO = len ( O0OO0 )
  ooo = string . find ( O0OO0 )
  if ( ooo != - 1 ) : break
  if 59 - 59: O0 % Oo0Ooo
  if 92 - 92: Ii1I % iII111i / I1ii11iIi11i % I1ii11iIi11i * I1IiiI
 while ( ooo != - 1 ) :
  Oo = string [ ooo : : ] . find ( Ii1IiIiIi1IiI )
  oO00oOOo0Oo = string [ ooo + oO0ooOoO : ooo + Oo ]
  string = string [ : ooo ] + O0ooo0o0 ( oO00oOOo0Oo , True ) + string [ ooo + Oo + oO0ooOoO : : ]
  if 5 - 5: o0oOOo0O0Ooo . O0 / Oo0Ooo % OoO0O00
  ooo = string . find ( O0OO0 )
  if 60 - 60: II111iiii / iIii1I11I1II1 + I1ii11iIi11i . i11iIiiIii
  if 40 - 40: o0oOOo0O0Ooo
  if 78 - 78: iIii1I11I1II1
  if 56 - 56: OoooooooOO - I11i - i1IIi
  if 8 - 8: I1Ii111 / OOooOOo . I1IiiI + I1ii11iIi11i / i11iIiiIii
 if ( string . find ( "[1m" ) != - 1 ) : string = convert_font ( string )
 return ( string )
 if 31 - 31: ooOoO0o - iIii1I11I1II1 + iII111i . Oo0Ooo / IiII % iIii1I11I1II1
 if 6 - 6: IiII * i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + o0oOOo0O0Ooo / i1IIi
 if 53 - 53: I11i + iIii1I11I1II1
 if 70 - 70: I1ii11iIi11i
 if 67 - 67: OoooooooOO
 if 29 - 29: O0 - i11iIiiIii - II111iiii + OOooOOo * IiII
 if 2 - 2: i1IIi - ooOoO0o + I1IiiI . o0oOOo0O0Ooo * o0oOOo0O0Ooo / OoOoOO00
def lisp_space ( num ) :
 oOOO = ""
 for iIi1I1 in range ( num ) : oOOO += "&#160;"
 return ( oOOO )
 if 63 - 63: iII111i * I1ii11iIi11i . OoooooooOO / OOooOOo * Oo0Ooo . ooOoO0o
 if 62 - 62: i1IIi / ooOoO0o . I1IiiI * o0oOOo0O0Ooo
 if 21 - 21: o0oOOo0O0Ooo
 if 81 - 81: I11i / iIii1I11I1II1 - ooOoO0o * I1Ii111 . I1IiiI * I1ii11iIi11i
 if 95 - 95: I1IiiI
 if 88 - 88: IiII % OoO0O00 + I1Ii111 + I1Ii111 * II111iiii
 if 78 - 78: OoooooooOO
def lisp_button ( string , url ) :
 OOoo0 = '<button style="background-color:transparent;border-radius:10px; ' + 'type="button">'
 if 36 - 36: o0oOOo0O0Ooo + I11i - IiII + iIii1I11I1II1 + OoooooooOO
 if 4 - 4: II111iiii . I11i + Ii1I * I1Ii111 . ooOoO0o
 if ( url == None ) :
  oOoOo = OOoo0 + string + "</button>"
 else :
  oO0OO = '<a href="{}">' . format ( url )
  OO0o0OO0 = lisp_space ( 2 )
  oOoOo = OO0o0OO0 + oO0OO + OOoo0 + string + "</button></a>" + OO0o0OO0
  if 56 - 56: i11iIiiIii - Oo0Ooo / iII111i / OoOoOO00
 return ( oOoOo )
 if 43 - 43: o0oOOo0O0Ooo . iII111i . I11i + iIii1I11I1II1
 if 78 - 78: iIii1I11I1II1 % OoOoOO00 + I1ii11iIi11i / i1IIi % II111iiii + OOooOOo
 if 91 - 91: iIii1I11I1II1 % OoO0O00 . o0oOOo0O0Ooo + Ii1I + o0oOOo0O0Ooo
 if 95 - 95: Ii1I + I1ii11iIi11i * OOooOOo
 if 16 - 16: I11i / I1IiiI + OoO0O00 % iIii1I11I1II1 - i1IIi . oO0o
 if 26 - 26: o0oOOo0O0Ooo * IiII . i1IIi
 if 59 - 59: O0 + i1IIi - o0oOOo0O0Ooo
def lisp_print_cour ( string ) :
 oOOO = '<font face="Courier New">{}</font>' . format ( string )
 return ( oOOO )
 if 62 - 62: i11iIiiIii % OOooOOo . IiII . OOooOOo
 if 84 - 84: i11iIiiIii * OoO0O00
 if 18 - 18: OOooOOo - Ii1I - OoOoOO00 / I1Ii111 - O0
 if 30 - 30: O0 + I1ii11iIi11i + II111iiii
 if 14 - 14: o0oOOo0O0Ooo / OOooOOo - iIii1I11I1II1 - oO0o % ooOoO0o
 if 49 - 49: ooOoO0o * oO0o / o0oOOo0O0Ooo / Oo0Ooo * iIii1I11I1II1
 if 57 - 57: OoOoOO00 - oO0o / ooOoO0o % i11iIiiIii
def lisp_print_sans ( string ) :
 oOOO = '<font face="Sans-Serif">{}</font>' . format ( string )
 return ( oOOO )
 if 3 - 3: iII111i . ooOoO0o % I1IiiI + I1ii11iIi11i
 if 64 - 64: i1IIi
 if 29 - 29: o0oOOo0O0Ooo / i11iIiiIii / I1IiiI % oO0o % i11iIiiIii
 if 18 - 18: OOooOOo + I1Ii111
 if 80 - 80: oO0o + o0oOOo0O0Ooo * Ii1I + OoO0O00
 if 75 - 75: I11i / o0oOOo0O0Ooo / OOooOOo / IiII % ooOoO0o + II111iiii
 if 4 - 4: iII111i - Oo0Ooo - IiII - I11i % i11iIiiIii / OoO0O00
def lisp_span ( string , hover_string ) :
 oOOO = '<span title="{}">{}</span>' . format ( hover_string , string )
 return ( oOOO )
 if 50 - 50: ooOoO0o + i1IIi
 if 31 - 31: Ii1I
 if 78 - 78: i11iIiiIii + o0oOOo0O0Ooo + I1Ii111 / o0oOOo0O0Ooo % iIii1I11I1II1 % IiII
 if 83 - 83: iIii1I11I1II1 % OoOoOO00 % o0oOOo0O0Ooo % I1Ii111 . I1ii11iIi11i % O0
 if 47 - 47: o0oOOo0O0Ooo
 if 66 - 66: I1IiiI - IiII
 if 33 - 33: I1IiiI / OoO0O00
def lisp_eid_help_hover ( output ) :
 iiIIi = '''Unicast EID format:
  For longest match lookups: 
    <address> or [<iid>]<address>
  For exact match lookups: 
    <prefix> or [<iid>]<prefix>
Multicast EID format:
  For longest match lookups:
    <address>-><group> or
    [<iid>]<address>->[<iid>]<group>'''
 if 36 - 36: I11i . II111iiii
 if 25 - 25: oO0o
 iI1 = lisp_span ( output , iiIIi )
 return ( iI1 )
 if 11 - 11: OoO0O00
 if 18 - 18: iII111i - oO0o % iII111i / I11i
 if 68 - 68: Ii1I * iIii1I11I1II1 + I1Ii111 % OoOoOO00
 if 46 - 46: OoOoOO00 % i1IIi / oO0o * Oo0Ooo * OOooOOo
 if 67 - 67: OoOoOO00 * OoOoOO00 . OoOoOO00 + Ii1I / oO0o
 if 13 - 13: iII111i
 if 80 - 80: Ii1I - o0oOOo0O0Ooo
def lisp_geo_help_hover ( output ) :
 iiIIi = '''EID format:
    <address> or [<iid>]<address>
    '<name>' or [<iid>]'<name>'
Geo-Point format:
    d-m-s-<N|S>-d-m-s-<W|E> or 
    [<iid>]d-m-s-<N|S>-d-m-s-<W|E>
Geo-Prefix format:
    d-m-s-<N|S>-d-m-s-<W|E>/<km> or
    [<iid>]d-m-s-<N|S>-d-m-s-<W|E>/<km>'''
 if 41 - 41: o0oOOo0O0Ooo - Oo0Ooo * I1IiiI
 if 82 - 82: OoO0O00 % o0oOOo0O0Ooo % OOooOOo / O0
 iI1 = lisp_span ( output , iiIIi )
 return ( iI1 )
 if 94 - 94: I1ii11iIi11i + I1ii11iIi11i + OoooooooOO % ooOoO0o
 if 7 - 7: iII111i
 if 78 - 78: OOooOOo + iII111i . IiII
 if 91 - 91: iIii1I11I1II1 . o0oOOo0O0Ooo . I1ii11iIi11i + OoooooooOO
 if 69 - 69: I1Ii111 - I1IiiI
 if 95 - 95: I1IiiI * i11iIiiIii . ooOoO0o
 if 41 - 41: II111iiii
def space ( num ) :
 oOOO = ""
 for iIi1I1 in range ( num ) : oOOO += "&#160;"
 return ( oOOO )
 if 37 - 37: I11i . Oo0Ooo % IiII * i1IIi
 if 71 - 71: Oo0Ooo / o0oOOo0O0Ooo + OOooOOo
 if 48 - 48: I1Ii111 + iII111i
 if 16 - 16: iIii1I11I1II1 % i11iIiiIii . OoOoOO00 % ooOoO0o + oO0o . OoO0O00
 if 46 - 46: OoO0O00 - o0oOOo0O0Ooo / OoOoOO00 - OoooooooOO + oO0o
 if 58 - 58: o0oOOo0O0Ooo / o0oOOo0O0Ooo + ooOoO0o + I11i - OoOoOO00 . OOooOOo
 if 15 - 15: ooOoO0o * OoOoOO00 % IiII . OoOoOO00 . I11i
 if 97 - 97: oO0o
def lisp_get_ephemeral_port ( ) :
 return ( random . randrange ( 32768 , 65535 ) )
 if 80 - 80: I1IiiI . Ii1I
 if 47 - 47: I11i + ooOoO0o + II111iiii % i11iIiiIii
 if 93 - 93: I1ii11iIi11i % OoOoOO00 . O0 / iII111i * oO0o
 if 29 - 29: o0oOOo0O0Ooo
 if 86 - 86: II111iiii . IiII
 if 2 - 2: OoooooooOO
 if 60 - 60: OoO0O00
def lisp_get_data_nonce ( ) :
 return ( random . randint ( 0 , 0xffffff ) )
 if 81 - 81: OoOoOO00 % Ii1I
 if 87 - 87: iIii1I11I1II1 . OoooooooOO * OoOoOO00
 if 100 - 100: OoO0O00 / i1IIi - I1IiiI % Ii1I - iIii1I11I1II1
 if 17 - 17: I11i / o0oOOo0O0Ooo % Oo0Ooo
 if 71 - 71: IiII . I1Ii111 . OoO0O00
 if 68 - 68: i11iIiiIii % oO0o * OoO0O00 * IiII * II111iiii + O0
 if 66 - 66: I11i % I1ii11iIi11i % OoooooooOO
def lisp_get_control_nonce ( ) :
 return ( random . randint ( 0 , ( 2 ** 64 ) - 1 ) )
 if 34 - 34: o0oOOo0O0Ooo / iII111i % O0 . OoO0O00 . i1IIi
 if 29 - 29: O0 . I1Ii111
 if 66 - 66: oO0o * iIii1I11I1II1 % iIii1I11I1II1 * IiII - ooOoO0o - IiII
 if 70 - 70: I1Ii111 + oO0o
 if 93 - 93: I1Ii111 + Ii1I
 if 33 - 33: O0
 if 78 - 78: O0 / II111iiii * OoO0O00
 if 50 - 50: OoooooooOO - iIii1I11I1II1 + i1IIi % I1Ii111 - iIii1I11I1II1 % O0
 if 58 - 58: IiII + iIii1I11I1II1
def lisp_hex_string ( integer_value ) :
 Oo00OO0OO = hex ( integer_value ) [ 2 : : ]
 if ( Oo00OO0OO [ - 1 ] == "L" ) : Oo00OO0OO = Oo00OO0OO [ 0 : - 1 ]
 return ( Oo00OO0OO )
 if 85 - 85: o0oOOo0O0Ooo % ooOoO0o . OoOoOO00 % I1Ii111 - Oo0Ooo
 if 69 - 69: ooOoO0o - o0oOOo0O0Ooo . ooOoO0o
 if 9 - 9: oO0o % i11iIiiIii / Oo0Ooo
 if 20 - 20: oO0o * O0 + I11i - OoooooooOO . I11i
 if 60 - 60: o0oOOo0O0Ooo . o0oOOo0O0Ooo / iII111i
 if 45 - 45: O0 . i11iIiiIii % iII111i . OoOoOO00 % IiII % iIii1I11I1II1
 if 58 - 58: iIii1I11I1II1 . OoOoOO00 - i11iIiiIii * iIii1I11I1II1 % i11iIiiIii / I1IiiI
def lisp_get_timestamp ( ) :
 return ( time . time ( ) )
 if 80 - 80: I1ii11iIi11i / iIii1I11I1II1 % OoOoOO00
 if 80 - 80: OoO0O00 % iII111i
 if 99 - 99: ooOoO0o / iIii1I11I1II1 - Ii1I * I1ii11iIi11i % I1IiiI
 if 13 - 13: OoO0O00
 if 70 - 70: I1Ii111 + O0 . oO0o * Ii1I
 if 2 - 2: OoooooooOO . OOooOOo . IiII
 if 42 - 42: OOooOOo % oO0o / OoO0O00 - oO0o * i11iIiiIii
def lisp_set_timestamp ( seconds ) :
 return ( time . time ( ) + seconds )
 if 19 - 19: oO0o * I1IiiI % i11iIiiIii
 if 24 - 24: o0oOOo0O0Ooo
 if 10 - 10: o0oOOo0O0Ooo % Ii1I / OOooOOo
 if 28 - 28: OOooOOo % ooOoO0o
 if 48 - 48: i11iIiiIii % oO0o
 if 29 - 29: iII111i + i11iIiiIii % I11i
 if 93 - 93: OoOoOO00 % iIii1I11I1II1
def lisp_print_elapsed ( ts ) :
 if ( ts == 0 or ts == None ) : return ( "never" )
 Ooo0o0oo0 = time . time ( ) - ts
 Ooo0o0oo0 = round ( Ooo0o0oo0 , 0 )
 return ( str ( datetime . timedelta ( seconds = Ooo0o0oo0 ) ) )
 if 87 - 87: OoOoOO00 / IiII + iIii1I11I1II1
 if 93 - 93: iIii1I11I1II1 + oO0o % ooOoO0o
 if 21 - 21: OOooOOo
 if 6 - 6: IiII
 if 46 - 46: IiII + oO0o
 if 79 - 79: OoooooooOO - IiII * IiII . OoOoOO00
 if 100 - 100: II111iiii * I11i % I1IiiI / I1ii11iIi11i
def lisp_print_future ( ts ) :
 if ( ts == 0 ) : return ( "never" )
 OOo = ts - time . time ( )
 if ( OOo < 0 ) : return ( "expired" )
 OOo = round ( OOo , 0 )
 return ( str ( datetime . timedelta ( seconds = OOo ) ) )
 if 99 - 99: OoOoOO00
 if 77 - 77: o0oOOo0O0Ooo
 if 48 - 48: OoOoOO00 % I1ii11iIi11i / I11i . iIii1I11I1II1 * II111iiii
 if 65 - 65: OoOoOO00
 if 31 - 31: I11i * OoOoOO00 . IiII % Ii1I + Oo0Ooo
 if 47 - 47: O0 * I1IiiI * OoO0O00 . II111iiii
 if 95 - 95: Ii1I % IiII . O0 % I1Ii111
 if 68 - 68: Oo0Ooo . Oo0Ooo - I1ii11iIi11i / I11i . ooOoO0o / i1IIi
 if 12 - 12: I1ii11iIi11i * i1IIi * I11i
 if 23 - 23: OOooOOo / O0 / I1IiiI
 if 49 - 49: I11i . o0oOOo0O0Ooo % oO0o / Ii1I
 if 95 - 95: O0 * OoOoOO00 * IiII . ooOoO0o / iIii1I11I1II1
 if 28 - 28: IiII + oO0o - ooOoO0o / iIii1I11I1II1 - I1IiiI
def lisp_print_eid_tuple ( eid , group ) :
 Ii1i1 = eid . print_prefix ( )
 if ( group . is_null ( ) ) : return ( Ii1i1 )
 if 65 - 65: oO0o + I1ii11iIi11i / OOooOOo
 oo0oo = group . print_prefix ( )
 IiIIi11i111 = group . instance_id
 if 67 - 67: i1IIi
 if ( eid . is_null ( ) or eid . is_exact_match ( group ) ) :
  ooo = oo0oo . find ( "]" ) + 1
  return ( "[{}](*, {})" . format ( IiIIi11i111 , oo0oo [ ooo : : ] ) )
  if 5 - 5: II111iiii . OoooooooOO
  if 57 - 57: I1IiiI
 iii1IIiI = eid . print_sg ( group )
 return ( iii1IIiI )
 if 33 - 33: I11i
 if 98 - 98: OoOoOO00 % II111iiii
 if 95 - 95: iIii1I11I1II1 - I1Ii111 - OOooOOo + I1Ii111 % I1ii11iIi11i . I1IiiI
 if 41 - 41: O0 + oO0o . i1IIi - II111iiii * o0oOOo0O0Ooo . OoO0O00
 if 68 - 68: o0oOOo0O0Ooo
 if 20 - 20: I1Ii111 - I1Ii111
 if 37 - 37: IiII
 if 37 - 37: Oo0Ooo / IiII * O0
def lisp_convert_6to4 ( addr_str ) :
 if ( addr_str . find ( "::ffff:" ) == - 1 ) : return ( addr_str )
 o0o00O0oOooO0 = addr_str . split ( ":" )
 return ( o0o00O0oOooO0 [ - 1 ] )
 if 99 - 99: ooOoO0o
 if 76 - 76: OoO0O00
 if 92 - 92: I11i - iIii1I11I1II1 % OoooooooOO
 if 39 - 39: iII111i . I1IiiI * OoOoOO00 - i11iIiiIii
 if 1 - 1: iII111i * OoOoOO00
 if 66 - 66: OoOoOO00 + i1IIi % II111iiii . O0 * I1ii11iIi11i % I1ii11iIi11i
 if 87 - 87: OOooOOo + o0oOOo0O0Ooo . iII111i - OoooooooOO
 if 6 - 6: iIii1I11I1II1 * OoooooooOO
 if 28 - 28: Oo0Ooo * o0oOOo0O0Ooo / I1Ii111
 if 52 - 52: O0 / o0oOOo0O0Ooo % iII111i * I1IiiI % OOooOOo
 if 69 - 69: I1ii11iIi11i
def lisp_convert_4to6 ( addr_str ) :
 o0o00O0oOooO0 = lisp_address ( LISP_AFI_IPV6 , "" , 128 , 0 )
 if ( o0o00O0oOooO0 . is_ipv4_string ( addr_str ) ) : addr_str = "::ffff:" + addr_str
 o0o00O0oOooO0 . store_address ( addr_str )
 return ( o0o00O0oOooO0 )
 if 83 - 83: o0oOOo0O0Ooo
 if 38 - 38: I1Ii111 + OoooooooOO . i1IIi
 if 19 - 19: iII111i - o0oOOo0O0Ooo - Ii1I - OoOoOO00 . iII111i . I1Ii111
 if 48 - 48: iII111i + IiII
 if 60 - 60: I11i + iII111i . IiII / i1IIi . iIii1I11I1II1
 if 14 - 14: OOooOOo
 if 79 - 79: Ii1I
 if 76 - 76: iIii1I11I1II1
 if 80 - 80: iIii1I11I1II1 . O0 / Ii1I % Ii1I
def lisp_gethostbyname ( string ) :
 ooOo000OoO0o = string . split ( "." )
 ooooo0O0 = string . split ( ":" )
 i1III1iI = string . split ( "-" )
 if 38 - 38: iIii1I11I1II1 / ooOoO0o
 if ( len ( ooOo000OoO0o ) == 4 ) :
  if ( ooOo000OoO0o [ 0 ] . isdigit ( ) and ooOo000OoO0o [ 1 ] . isdigit ( ) and ooOo000OoO0o [ 2 ] . isdigit ( ) and
 ooOo000OoO0o [ 3 ] . isdigit ( ) ) : return ( string )
  if 13 - 13: iIii1I11I1II1
 if ( len ( ooooo0O0 ) > 1 ) :
  try :
   int ( ooooo0O0 [ 0 ] , 16 )
   return ( string )
  except :
   pass
   if 77 - 77: i11iIiiIii - iIii1I11I1II1 / oO0o / ooOoO0o / OoO0O00
   if 56 - 56: OoooooooOO * O0
   if 85 - 85: OoooooooOO % OoOoOO00 * iIii1I11I1II1
   if 44 - 44: iIii1I11I1II1 . I1ii11iIi11i + I1Ii111 . ooOoO0o
   if 7 - 7: I1ii11iIi11i + iIii1I11I1II1 * I11i * I11i / II111iiii - Ii1I
   if 65 - 65: oO0o + OoOoOO00 + II111iiii
   if 77 - 77: II111iiii
 if ( len ( i1III1iI ) == 3 ) :
  for iIi1I1 in range ( 3 ) :
   try : int ( i1III1iI [ iIi1I1 ] , 16 )
   except : break
   if 50 - 50: O0 . O0 . ooOoO0o % Oo0Ooo
   if 68 - 68: oO0o
   if 10 - 10: Ii1I
 try :
  o0o00O0oOooO0 = socket . gethostbyname ( string )
  return ( o0o00O0oOooO0 )
 except :
  if ( lisp_is_alpine ( ) == False ) : return ( "" )
  if 77 - 77: OOooOOo / II111iiii + IiII + ooOoO0o - i11iIiiIii
  if 44 - 44: I1IiiI + OoOoOO00 + I1ii11iIi11i . I1IiiI * OoOoOO00 % iIii1I11I1II1
  if 72 - 72: OOooOOo . OOooOOo - I1ii11iIi11i
  if 48 - 48: Oo0Ooo - ooOoO0o + Oo0Ooo - I1IiiI * i11iIiiIii . iII111i
  if 35 - 35: IiII . O0 + Oo0Ooo + OOooOOo + i1IIi
 try :
  o0o00O0oOooO0 = socket . getaddrinfo ( string , 0 ) [ 0 ]
  if ( o0o00O0oOooO0 [ 3 ] != string ) : return ( "" )
  o0o00O0oOooO0 = o0o00O0oOooO0 [ 4 ] [ 0 ]
 except :
  o0o00O0oOooO0 = ""
  if 65 - 65: O0 * I1IiiI / I1IiiI . OoOoOO00
 return ( o0o00O0oOooO0 )
 if 87 - 87: II111iiii * I1ii11iIi11i % Oo0Ooo * Oo0Ooo
 if 58 - 58: OOooOOo . o0oOOo0O0Ooo + I1IiiI % Oo0Ooo - OoO0O00
 if 50 - 50: iII111i % II111iiii - ooOoO0o . i1IIi + O0 % iII111i
 if 10 - 10: iII111i . i1IIi + Ii1I
 if 66 - 66: OoO0O00 % o0oOOo0O0Ooo
 if 21 - 21: OoOoOO00 - OoooooooOO % i11iIiiIii
 if 71 - 71: i1IIi - I11i * I1Ii111 + oO0o - OoO0O00 % I1ii11iIi11i
 if 63 - 63: iIii1I11I1II1 + OOooOOo . OoO0O00 / I1IiiI
def lisp_ip_checksum ( data , hdrlen = 20 ) :
 if ( len ( data ) < hdrlen ) :
  lprint ( "IPv4 packet too short, length {}" . format ( len ( data ) ) )
  return ( data )
  if 84 - 84: i1IIi
  if 42 - 42: II111iiii - OoO0O00 - OoooooooOO . iII111i / OoOoOO00
 ooooo0Oo0 = binascii . hexlify ( data )
 if 97 - 97: IiII . oO0o . IiII
 if 91 - 91: OOooOOo + I1Ii111 . I11i
 if 15 - 15: I11i
 if 94 - 94: I1Ii111 % II111iiii * i1IIi * iIii1I11I1II1
 oO0oOoo0O = 0
 for iIi1I1 in range ( 0 , hdrlen * 2 , 4 ) :
  oO0oOoo0O += int ( ooooo0Oo0 [ iIi1I1 : iIi1I1 + 4 ] , 16 )
  if 26 - 26: Oo0Ooo + I1IiiI * OOooOOo + ooOoO0o
  if 88 - 88: I11i + i11iIiiIii % oO0o * OOooOOo * OOooOOo * Ii1I
  if 24 - 24: ooOoO0o / iII111i + IiII . IiII
  if 39 - 39: ooOoO0o + O0 / i1IIi % IiII / oO0o * IiII
  if 77 - 77: IiII . I1Ii111 % OoOoOO00
 oO0oOoo0O = ( oO0oOoo0O >> 16 ) + ( oO0oOoo0O & 0xffff )
 oO0oOoo0O += oO0oOoo0O >> 16
 oO0oOoo0O = socket . htons ( ~ oO0oOoo0O & 0xffff )
 if 42 - 42: IiII % iII111i % o0oOOo0O0Ooo % oO0o + I11i % OoOoOO00
 if 3 - 3: oO0o
 if 64 - 64: OoO0O00 . I1IiiI - OoooooooOO . ooOoO0o - iII111i
 if 77 - 77: Ii1I % OoOoOO00 / II111iiii % iII111i % OoooooooOO % OoO0O00
 oO0oOoo0O = struct . pack ( "H" , oO0oOoo0O )
 ooooo0Oo0 = data [ 0 : 10 ] + oO0oOoo0O + data [ 12 : : ]
 return ( ooooo0Oo0 )
 if 19 - 19: IiII * I1Ii111 / oO0o * I1Ii111 - OoooooooOO * I11i
 if 17 - 17: II111iiii + Oo0Ooo . I1Ii111
 if 12 - 12: I1Ii111 + OOooOOo + I11i . IiII / Ii1I
 if 29 - 29: IiII . ooOoO0o - II111iiii
 if 68 - 68: iIii1I11I1II1 + II111iiii / oO0o
 if 91 - 91: OoOoOO00 % iIii1I11I1II1 . I1IiiI
 if 70 - 70: I11i % II111iiii % O0 . i1IIi / I1Ii111
 if 100 - 100: I1ii11iIi11i * i11iIiiIii % oO0o / Oo0Ooo / ooOoO0o + I1ii11iIi11i
def lisp_icmp_checksum ( data ) :
 if ( len ( data ) < 36 ) :
  lprint ( "ICMP packet too short, length {}" . format ( len ( data ) ) )
  return ( data )
  if 59 - 59: I1Ii111 - IiII
  if 14 - 14: iIii1I11I1II1 - iIii1I11I1II1
 i111i1I1ii1i = binascii . hexlify ( data )
 if 100 - 100: IiII . Ii1I - iIii1I11I1II1 . i11iIiiIii / II111iiii
 if 71 - 71: I1Ii111 * Oo0Ooo . I11i
 if 49 - 49: IiII * O0 . IiII
 if 19 - 19: II111iiii - IiII
 oO0oOoo0O = 0
 for iIi1I1 in range ( 0 , 36 , 4 ) :
  oO0oOoo0O += int ( i111i1I1ii1i [ iIi1I1 : iIi1I1 + 4 ] , 16 )
  if 59 - 59: o0oOOo0O0Ooo * OoO0O00 - Ii1I . OOooOOo
  if 89 - 89: OOooOOo
  if 69 - 69: ooOoO0o - OoooooooOO * O0
  if 84 - 84: ooOoO0o + i11iIiiIii - OOooOOo * ooOoO0o
  if 33 - 33: ooOoO0o % i1IIi - oO0o . O0 / O0
 oO0oOoo0O = ( oO0oOoo0O >> 16 ) + ( oO0oOoo0O & 0xffff )
 oO0oOoo0O += oO0oOoo0O >> 16
 oO0oOoo0O = socket . htons ( ~ oO0oOoo0O & 0xffff )
 if 96 - 96: OoooooooOO + IiII * O0
 if 86 - 86: Ii1I
 if 29 - 29: iIii1I11I1II1 - OoO0O00 + I1IiiI % iIii1I11I1II1 % OOooOOo
 if 84 - 84: IiII + I1ii11iIi11i + Ii1I + iII111i
 oO0oOoo0O = struct . pack ( "H" , oO0oOoo0O )
 i111i1I1ii1i = data [ 0 : 2 ] + oO0oOoo0O + data [ 4 : : ]
 return ( i111i1I1ii1i )
 if 62 - 62: i11iIiiIii + OoOoOO00 + i1IIi
 if 69 - 69: OoOoOO00
 if 63 - 63: OoO0O00 / OoOoOO00 * iIii1I11I1II1 . I1Ii111
 if 85 - 85: i11iIiiIii / i11iIiiIii . OoO0O00 . O0
 if 67 - 67: II111iiii / o0oOOo0O0Ooo . OOooOOo . OoooooooOO
 if 19 - 19: IiII . I1ii11iIi11i / OoOoOO00
 if 68 - 68: ooOoO0o / OoooooooOO * I11i / oO0o
 if 88 - 88: o0oOOo0O0Ooo
 if 1 - 1: OoooooooOO
 if 48 - 48: ooOoO0o * OoOoOO00 - ooOoO0o - OOooOOo + OOooOOo
 if 40 - 40: i11iIiiIii . iIii1I11I1II1
 if 2 - 2: i1IIi * oO0o - oO0o + OoooooooOO % OoOoOO00 / OoOoOO00
 if 3 - 3: OoooooooOO
 if 71 - 71: IiII + i1IIi - iII111i - i11iIiiIii . I11i - ooOoO0o
 if 85 - 85: I1ii11iIi11i - OoOoOO00 / I1ii11iIi11i + OOooOOo - iII111i
 if 49 - 49: OoO0O00 - O0 / OoO0O00 * OoOoOO00 + I1Ii111
 if 35 - 35: II111iiii . I1IiiI / i1IIi / I1IiiI * oO0o
 if 85 - 85: II111iiii . ooOoO0o % OOooOOo % I11i
 if 80 - 80: oO0o * I11i / iIii1I11I1II1 % oO0o / iIii1I11I1II1
 if 42 - 42: i1IIi / i11iIiiIii . Oo0Ooo * iII111i . i11iIiiIii * O0
 if 44 - 44: i1IIi . I1IiiI / i11iIiiIii + IiII
 if 27 - 27: OOooOOo
 if 52 - 52: I1Ii111 % OoOoOO00 + iIii1I11I1II1 * oO0o . Ii1I
 if 95 - 95: iIii1I11I1II1 . IiII - OoooooooOO * OoO0O00 / o0oOOo0O0Ooo
 if 74 - 74: oO0o
 if 34 - 34: iII111i
 if 44 - 44: i1IIi % I1IiiI % o0oOOo0O0Ooo
 if 9 - 9: Oo0Ooo % OoooooooOO - Ii1I
 if 43 - 43: OoO0O00 % OoO0O00
 if 46 - 46: Oo0Ooo % iIii1I11I1II1 . iII111i . O0 * ooOoO0o / OoooooooOO
 if 7 - 7: oO0o - O0 * I11i - o0oOOo0O0Ooo - II111iiii
 if 41 - 41: I1IiiI - I1Ii111 % II111iiii . I1Ii111 - I11i
 if 45 - 45: Ii1I - OOooOOo
 if 70 - 70: OoO0O00 % I1IiiI / I1IiiI . I11i % ooOoO0o . II111iiii
 if 10 - 10: Ii1I - i11iIiiIii . I1ii11iIi11i % i1IIi
def lisp_udp_checksum ( source , dest , data ) :
 if 78 - 78: iIii1I11I1II1 * Oo0Ooo . Oo0Ooo - OOooOOo . iIii1I11I1II1
 if 30 - 30: ooOoO0o + ooOoO0o % IiII - o0oOOo0O0Ooo - I1ii11iIi11i
 if 36 - 36: I11i % OOooOOo
 if 72 - 72: I1IiiI / iII111i - O0 + I11i
 OO0o0OO0 = lisp_address ( LISP_AFI_IPV6 , source , LISP_IPV6_HOST_MASK_LEN , 0 )
 o0 = lisp_address ( LISP_AFI_IPV6 , dest , LISP_IPV6_HOST_MASK_LEN , 0 )
 iIIIIi = socket . htonl ( len ( data ) )
 i1I11ii = socket . htonl ( LISP_UDP_PROTOCOL )
 o0ooO00O0O = OO0o0OO0 . pack_address ( )
 o0ooO00O0O += o0 . pack_address ( )
 o0ooO00O0O += struct . pack ( "II" , iIIIIi , i1I11ii )
 if 41 - 41: I1ii11iIi11i
 if 5 - 5: Oo0Ooo
 if 100 - 100: Ii1I + iIii1I11I1II1
 if 59 - 59: IiII
 oOoO0OOO00O = binascii . hexlify ( o0ooO00O0O + data )
 OOOOO0o0OOo = len ( oOoO0OOO00O ) % 4
 for iIi1I1 in range ( 0 , OOOOO0o0OOo ) : oOoO0OOO00O += "0"
 if 40 - 40: IiII * oO0o % I11i * I1ii11iIi11i
 if 80 - 80: iIii1I11I1II1 - OoooooooOO - I1ii11iIi11i - I1ii11iIi11i . OoooooooOO
 if 48 - 48: I1Ii111 . i11iIiiIii / i1IIi % IiII % iII111i + oO0o
 if 41 - 41: IiII
 oO0oOoo0O = 0
 for iIi1I1 in range ( 0 , len ( oOoO0OOO00O ) , 4 ) :
  oO0oOoo0O += int ( oOoO0OOO00O [ iIi1I1 : iIi1I1 + 4 ] , 16 )
  if 3 - 3: IiII + II111iiii / iIii1I11I1II1
  if 10 - 10: II111iiii . O0
  if 31 - 31: oO0o / i11iIiiIii / O0
  if 39 - 39: I1IiiI + Oo0Ooo
  if 83 - 83: i1IIi
 oO0oOoo0O = ( oO0oOoo0O >> 16 ) + ( oO0oOoo0O & 0xffff )
 oO0oOoo0O += oO0oOoo0O >> 16
 oO0oOoo0O = socket . htons ( ~ oO0oOoo0O & 0xffff )
 if 76 - 76: Ii1I + iIii1I11I1II1 + OoOoOO00 . OoO0O00
 if 49 - 49: IiII / ooOoO0o / OOooOOo
 if 25 - 25: I1IiiI % O0 + i1IIi - ooOoO0o
 if 38 - 38: o0oOOo0O0Ooo % I1Ii111 + i11iIiiIii + iII111i + ooOoO0o / i11iIiiIii
 oO0oOoo0O = struct . pack ( "H" , oO0oOoo0O )
 oOoO0OOO00O = data [ 0 : 6 ] + oO0oOoo0O + data [ 8 : : ]
 return ( oOoO0OOO00O )
 if 94 - 94: iII111i - Oo0Ooo + oO0o
 if 59 - 59: I11i . I1IiiI - iIii1I11I1II1 + iIii1I11I1II1
 if 56 - 56: oO0o + ooOoO0o
 if 32 - 32: II111iiii + OoOoOO00 % ooOoO0o / OoOoOO00 + I1ii11iIi11i
 if 2 - 2: i11iIiiIii - I1Ii111 + OoO0O00 % I11i * Ii1I
 if 54 - 54: O0 - iII111i . OOooOOo % iII111i + iII111i
 if 36 - 36: OOooOOo % i11iIiiIii
 if 47 - 47: i1IIi + II111iiii . Oo0Ooo * oO0o . I11i / i1IIi
def lisp_igmp_checksum ( igmp ) :
 i11ii = binascii . hexlify ( igmp )
 if 83 - 83: I1ii11iIi11i * I1ii11iIi11i + OOooOOo
 if 57 - 57: O0 - O0 . I1ii11iIi11i / o0oOOo0O0Ooo / Ii1I
 if 20 - 20: OOooOOo * II111iiii - OoOoOO00 - oO0o * I1Ii111
 if 6 - 6: ooOoO0o + OOooOOo / Oo0Ooo + IiII % II111iiii / OoO0O00
 oO0oOoo0O = 0
 for iIi1I1 in range ( 0 , 24 , 4 ) :
  oO0oOoo0O += int ( i11ii [ iIi1I1 : iIi1I1 + 4 ] , 16 )
  if 45 - 45: OoooooooOO
  if 9 - 9: I11i . OoO0O00 * i1IIi . OoooooooOO
  if 32 - 32: OoOoOO00 . I1ii11iIi11i % I1IiiI - II111iiii
  if 11 - 11: O0 + I1IiiI
  if 80 - 80: oO0o % oO0o % O0 - i11iIiiIii . iII111i / O0
 oO0oOoo0O = ( oO0oOoo0O >> 16 ) + ( oO0oOoo0O & 0xffff )
 oO0oOoo0O += oO0oOoo0O >> 16
 oO0oOoo0O = socket . htons ( ~ oO0oOoo0O & 0xffff )
 if 13 - 13: I1IiiI + O0 - I1ii11iIi11i % Oo0Ooo / Ii1I . i1IIi
 if 60 - 60: Oo0Ooo . IiII % I1IiiI - I1Ii111
 if 79 - 79: OoooooooOO / I1ii11iIi11i . O0
 if 79 - 79: oO0o - II111iiii
 oO0oOoo0O = struct . pack ( "H" , oO0oOoo0O )
 igmp = igmp [ 0 : 2 ] + oO0oOoo0O + igmp [ 4 : : ]
 return ( igmp )
 if 43 - 43: i1IIi + O0 % OoO0O00 / Ii1I * I1IiiI
 if 89 - 89: I1IiiI . Oo0Ooo + I1ii11iIi11i . O0 % o0oOOo0O0Ooo
 if 84 - 84: OoooooooOO + I1Ii111 / I1IiiI % OOooOOo % I1ii11iIi11i * I1IiiI
 if 58 - 58: OoO0O00 - OoOoOO00 . i11iIiiIii % i11iIiiIii / i1IIi / oO0o
 if 24 - 24: I1IiiI * i1IIi % ooOoO0o / O0 + i11iIiiIii
 if 12 - 12: I1ii11iIi11i / Ii1I
 if 5 - 5: OoooooooOO
def lisp_get_interface_address ( device ) :
 if 18 - 18: I1IiiI % OoooooooOO - iII111i . i11iIiiIii * Oo0Ooo % Ii1I
 if 12 - 12: i1IIi / OOooOOo % ooOoO0o * IiII * O0 * iIii1I11I1II1
 if 93 - 93: Oo0Ooo / I1ii11iIi11i + i1IIi * oO0o . OoooooooOO
 if 54 - 54: O0 / IiII % ooOoO0o * i1IIi * O0
 if ( device not in netifaces . interfaces ( ) ) : return ( None )
 if 48 - 48: o0oOOo0O0Ooo . oO0o % OoOoOO00 - OoOoOO00
 if 33 - 33: I11i % II111iiii + OoO0O00
 if 93 - 93: i1IIi . IiII / I1IiiI + IiII
 if 58 - 58: I1ii11iIi11i + O0 . Oo0Ooo + OoOoOO00 - OoO0O00 - OoOoOO00
 IIiiI = netifaces . ifaddresses ( device )
 if ( IIiiI . has_key ( netifaces . AF_INET ) == False ) : return ( None )
 if 36 - 36: iII111i
 if 52 - 52: I1Ii111 % O0 . i1IIi . OoooooooOO
 if 33 - 33: OOooOOo % II111iiii
 if 71 - 71: Ii1I * I1Ii111 % II111iiii . Ii1I % OoO0O00 + I1ii11iIi11i
 o0oOo0OO = lisp_address ( LISP_AFI_IPV4 , "" , 32 , 0 )
 if 79 - 79: OoOoOO00 % I1IiiI % Ii1I / i1IIi % OoO0O00
 for o0o00O0oOooO0 in IIiiI [ netifaces . AF_INET ] :
  oo0o00OO = o0o00O0oOooO0 [ "addr" ]
  o0oOo0OO . store_address ( oo0o00OO )
  return ( o0oOo0OO )
  if 69 - 69: o0oOOo0O0Ooo % i11iIiiIii / Ii1I
 return ( None )
 if 93 - 93: ooOoO0o
 if 34 - 34: oO0o - ooOoO0o * Oo0Ooo / o0oOOo0O0Ooo
 if 19 - 19: I1ii11iIi11i
 if 46 - 46: iIii1I11I1II1 . i11iIiiIii - OoOoOO00 % O0 / II111iiii * i1IIi
 if 66 - 66: O0
 if 52 - 52: OoO0O00 * OoooooooOO
 if 12 - 12: O0 + IiII * i1IIi . OoO0O00
 if 71 - 71: I1Ii111 - o0oOOo0O0Ooo - OOooOOo
 if 28 - 28: iIii1I11I1II1
 if 7 - 7: o0oOOo0O0Ooo % IiII * OoOoOO00
 if 58 - 58: IiII / I11i + II111iiii % iII111i - OoooooooOO
 if 25 - 25: OoOoOO00 % OoooooooOO * Oo0Ooo - i1IIi * II111iiii * oO0o
def lisp_get_input_interface ( packet ) :
 I1iI1I1ii1 = lisp_format_packet ( packet [ 0 : 12 ] ) . replace ( " " , "" )
 iIIi1 = I1iI1I1ii1 [ 0 : 12 ]
 o0Ooo0o0Oo = I1iI1I1ii1 [ 12 : : ]
 if 55 - 55: iIii1I11I1II1 * iII111i
 try : oo = lisp_mymacs . has_key ( o0Ooo0o0Oo )
 except : oo = False
 if 30 - 30: O0 + OOooOOo % Oo0Ooo . i1IIi
 if ( lisp_mymacs . has_key ( iIIi1 ) ) : return ( lisp_mymacs [ iIIi1 ] , o0Ooo0o0Oo , iIIi1 , oo )
 if ( oo ) : return ( lisp_mymacs [ o0Ooo0o0Oo ] , o0Ooo0o0Oo , iIIi1 , oo )
 return ( [ "?" ] , o0Ooo0o0Oo , iIIi1 , oo )
 if 4 - 4: OOooOOo / iII111i * I11i - Oo0Ooo * I1IiiI
 if 6 - 6: Ii1I
 if 77 - 77: i1IIi + OoO0O00 . I1IiiI * OOooOOo / IiII / Ii1I
 if 84 - 84: OoO0O00 / iIii1I11I1II1
 if 33 - 33: i1IIi / I1Ii111 - i1IIi . Oo0Ooo
 if 18 - 18: Oo0Ooo / O0 + iII111i
 if 65 - 65: i1IIi . I1ii11iIi11i / ooOoO0o
 if 11 - 11: IiII * ooOoO0o / ooOoO0o - OOooOOo
def lisp_get_local_interfaces ( ) :
 for OoO0o0OOOO in netifaces . interfaces ( ) :
  II1i = lisp_interface ( OoO0o0OOOO )
  II1i . add_interface ( )
  if 62 - 62: I11i / oO0o % Oo0Ooo . OoooooooOO / i11iIiiIii / I1Ii111
 return
 if 60 - 60: I1IiiI % oO0o / o0oOOo0O0Ooo % oO0o * i11iIiiIii / iII111i
 if 34 - 34: I1Ii111 - OOooOOo
 if 25 - 25: oO0o % I1IiiI + i11iIiiIii + O0 * OoooooooOO
 if 64 - 64: i1IIi
 if 10 - 10: I1Ii111 % O0 / I1IiiI % I11i
 if 25 - 25: II111iiii / OoO0O00
 if 64 - 64: O0 % ooOoO0o
def lisp_get_loopback_address ( ) :
 for o0o00O0oOooO0 in netifaces . ifaddresses ( "lo" ) [ netifaces . AF_INET ] :
  if ( o0o00O0oOooO0 [ "peer" ] == "127.0.0.1" ) : continue
  return ( o0o00O0oOooO0 [ "peer" ] )
  if 40 - 40: o0oOOo0O0Ooo + I11i
 return ( None )
 if 77 - 77: i11iIiiIii % IiII + I1Ii111 % OoooooooOO - I11i
 if 26 - 26: Oo0Ooo + O0 - iIii1I11I1II1
 if 47 - 47: OoooooooOO
 if 2 - 2: OoOoOO00 % I1Ii111 * Oo0Ooo * OoOoOO00
 if 65 - 65: i11iIiiIii + Oo0Ooo * OoooooooOO - OoO0O00
 if 26 - 26: o0oOOo0O0Ooo % OOooOOo + OOooOOo % I11i * i11iIiiIii / iII111i
 if 64 - 64: oO0o % OoOoOO00 / II111iiii % ooOoO0o - iII111i
 if 2 - 2: I1Ii111 - I1ii11iIi11i + o0oOOo0O0Ooo * OoO0O00 / iII111i
def lisp_is_mac_string ( mac_str ) :
 i1III1iI = mac_str . split ( "/" )
 if ( len ( i1III1iI ) == 2 ) : mac_str = i1III1iI [ 0 ]
 return ( len ( mac_str ) == 14 and mac_str . count ( "-" ) == 2 )
 if 26 - 26: OOooOOo * Oo0Ooo
 if 31 - 31: I11i * oO0o . Ii1I
 if 35 - 35: I11i
 if 94 - 94: ooOoO0o / i11iIiiIii % O0
 if 70 - 70: I11i - Oo0Ooo / OoooooooOO % OoooooooOO
 if 95 - 95: OoooooooOO % OoooooooOO . Ii1I
 if 26 - 26: oO0o + IiII - II111iiii . II111iiii + I1ii11iIi11i + OoOoOO00
 if 68 - 68: O0
def lisp_get_local_macs ( ) :
 for OoO0o0OOOO in netifaces . interfaces ( ) :
  if 76 - 76: I1ii11iIi11i
  if 99 - 99: o0oOOo0O0Ooo
  if 1 - 1: Ii1I * OoOoOO00 * OoO0O00 + Oo0Ooo
  if 90 - 90: I1Ii111 % Oo0Ooo - Oo0Ooo . iIii1I11I1II1 / OOooOOo + I11i
  if 89 - 89: oO0o
  o0 = OoO0o0OOOO . replace ( ":" , "" )
  o0 = OoO0o0OOOO . replace ( "-" , "" )
  if ( o0 . isalnum ( ) == False ) : continue
  if 87 - 87: iII111i % Oo0Ooo
  if 62 - 62: OoO0O00 + ooOoO0o / iII111i * i11iIiiIii
  if 37 - 37: iII111i
  if 33 - 33: OoO0O00 - O0 - OoO0O00
  if 94 - 94: IiII * I11i * OoooooooOO / o0oOOo0O0Ooo . IiII - o0oOOo0O0Ooo
  try :
   I1I1i = netifaces . ifaddresses ( OoO0o0OOOO )
  except :
   continue
   if 45 - 45: OOooOOo
  if ( I1I1i . has_key ( netifaces . AF_LINK ) == False ) : continue
  i1III1iI = I1I1i [ netifaces . AF_LINK ] [ 0 ] [ "addr" ]
  i1III1iI = i1III1iI . replace ( ":" , "" )
  if 25 - 25: OOooOOo % O0
  if 44 - 44: I1Ii111 . Ii1I * II111iiii / IiII + iIii1I11I1II1
  if 14 - 14: O0 % IiII % Ii1I * oO0o
  if 65 - 65: I11i % oO0o + I1ii11iIi11i
  if 86 - 86: iIii1I11I1II1 / O0 . I1Ii111 % iIii1I11I1II1 % Oo0Ooo
  if ( len ( i1III1iI ) < 12 ) : continue
  if 86 - 86: i11iIiiIii - o0oOOo0O0Ooo . ooOoO0o * Oo0Ooo / Ii1I % o0oOOo0O0Ooo
  if ( lisp_mymacs . has_key ( i1III1iI ) == False ) : lisp_mymacs [ i1III1iI ] = [ ]
  lisp_mymacs [ i1III1iI ] . append ( OoO0o0OOOO )
  if 61 - 61: o0oOOo0O0Ooo + OoOoOO00
  if 15 - 15: OoOoOO00 * oO0o + OOooOOo . I11i % I1IiiI - ooOoO0o
 lprint ( "Local MACs are: {}" . format ( lisp_mymacs ) )
 return
 if 13 - 13: OoOoOO00 % OoOoOO00 % Oo0Ooo % I1IiiI * i1IIi % I11i
 if 82 - 82: IiII . OoOoOO00 / ooOoO0o + iII111i - ooOoO0o
 if 55 - 55: ooOoO0o % Oo0Ooo % o0oOOo0O0Ooo
 if 29 - 29: IiII / iIii1I11I1II1 + I1ii11iIi11i % iII111i % I11i
 if 46 - 46: iIii1I11I1II1
 if 70 - 70: i1IIi . I11i
 if 74 - 74: I11i
 if 58 - 58: iIii1I11I1II1 * OoO0O00 * I1Ii111 * ooOoO0o . OoooooooOO
def lisp_get_local_rloc ( ) :
 II1IIiiI1 = commands . getoutput ( "netstat -rn | egrep 'default|0.0.0.0'" )
 if ( II1IIiiI1 == "" ) : return ( lisp_address ( LISP_AFI_IPV4 , "" , 32 , 0 ) )
 if 96 - 96: OOooOOo + OOooOOo % IiII % OOooOOo
 if 28 - 28: iIii1I11I1II1 + OoOoOO00 . o0oOOo0O0Ooo % i11iIiiIii
 if 58 - 58: I11i / OoooooooOO % oO0o + OoO0O00
 if 58 - 58: O0
 II1IIiiI1 = II1IIiiI1 . split ( "\n" ) [ 0 ]
 OoO0o0OOOO = II1IIiiI1 . split ( ) [ - 1 ]
 if 91 - 91: iII111i / I1ii11iIi11i . iII111i - o0oOOo0O0Ooo + I1ii11iIi11i
 o0o00O0oOooO0 = ""
 O00 = lisp_is_macos ( )
 if ( O00 ) :
  II1IIiiI1 = commands . getoutput ( "ifconfig {} | egrep 'inet '" . format ( OoO0o0OOOO ) )
  if ( II1IIiiI1 == "" ) : return ( lisp_address ( LISP_AFI_IPV4 , "" , 32 , 0 ) )
 else :
  ooO0ooooO = 'ip addr show | egrep "inet " | egrep "{}"' . format ( OoO0o0OOOO )
  II1IIiiI1 = commands . getoutput ( ooO0ooooO )
  if ( II1IIiiI1 == "" ) :
   ooO0ooooO = 'ip addr show | egrep "inet " | egrep "global lo"'
   II1IIiiI1 = commands . getoutput ( ooO0ooooO )
   if 86 - 86: ooOoO0o
  if ( II1IIiiI1 == "" ) : return ( lisp_address ( LISP_AFI_IPV4 , "" , 32 , 0 ) )
  if 51 - 51: OoO0O00 - i11iIiiIii * I1IiiI
  if 95 - 95: OOooOOo % I1ii11iIi11i + o0oOOo0O0Ooo % ooOoO0o
  if 36 - 36: O0 / i1IIi % II111iiii / iII111i
  if 96 - 96: Oo0Ooo / oO0o . II111iiii . Oo0Ooo
  if 91 - 91: II111iiii . OOooOOo + o0oOOo0O0Ooo
  if 8 - 8: OOooOOo * Oo0Ooo / iII111i - OoO0O00 - OoooooooOO
 o0o00O0oOooO0 = ""
 II1IIiiI1 = II1IIiiI1 . split ( "\n" )
 if 100 - 100: oO0o . iIii1I11I1II1 . iIii1I11I1II1
 for oOOo0ooO0 in II1IIiiI1 :
  oO0OO = oOOo0ooO0 . split ( ) [ 1 ]
  if ( O00 == False ) : oO0OO = oO0OO . split ( "/" ) [ 0 ]
  ii1i1II11II1i = lisp_address ( LISP_AFI_IPV4 , oO0OO , 32 , 0 )
  return ( ii1i1II11II1i )
  if 95 - 95: I11i + o0oOOo0O0Ooo * I1ii11iIi11i
 return ( lisp_address ( LISP_AFI_IPV4 , o0o00O0oOooO0 , 32 , 0 ) )
 if 85 - 85: i11iIiiIii . OoooooooOO - iIii1I11I1II1
 if 38 - 38: I11i . I11i * oO0o / OoooooooOO % ooOoO0o
 if 80 - 80: OoO0O00 / IiII * I1IiiI % IiII
 if 95 - 95: O0 / I11i . I1Ii111
 if 17 - 17: I11i
 if 56 - 56: ooOoO0o * o0oOOo0O0Ooo + I11i
 if 48 - 48: IiII * OoO0O00 % I1Ii111 - I11i
 if 72 - 72: i1IIi % ooOoO0o % IiII % oO0o - oO0o
 if 97 - 97: o0oOOo0O0Ooo * O0 / o0oOOo0O0Ooo * OoO0O00 * Oo0Ooo
 if 38 - 38: I1Ii111
 if 25 - 25: iIii1I11I1II1 % II111iiii / I11i / I1ii11iIi11i
def lisp_get_local_addresses ( ) :
 global lisp_myrlocs
 if 22 - 22: oO0o * iII111i
 if 4 - 4: OoOoOO00 - oO0o + I1IiiI
 if 36 - 36: IiII
 if 19 - 19: OoOoOO00 . o0oOOo0O0Ooo . OoooooooOO
 if 13 - 13: OOooOOo . Oo0Ooo / II111iiii
 if 43 - 43: iIii1I11I1II1 % OoO0O00
 if 84 - 84: Oo0Ooo
 if 44 - 44: OoooooooOO * i11iIiiIii / Oo0Ooo
 if 75 - 75: OoooooooOO . OOooOOo + OoO0O00 / Ii1I - I1IiiI % Ii1I
 if 89 - 89: iII111i * iIii1I11I1II1 + i11iIiiIii . OoooooooOO
 O0O0 = None
 ooo = 1
 oO0oo = os . getenv ( "LISP_ADDR_SELECT" )
 if ( oO0oo != None and oO0oo != "" ) :
  oO0oo = oO0oo . split ( ":" )
  if ( len ( oO0oo ) == 2 ) :
   O0O0 = oO0oo [ 0 ]
   ooo = oO0oo [ 1 ]
  else :
   if ( oO0oo [ 0 ] . isdigit ( ) ) :
    ooo = oO0oo [ 0 ]
   else :
    O0O0 = oO0oo [ 0 ]
    if 52 - 52: IiII % ooOoO0o
    if 25 - 25: I11i / I11i % OoooooooOO - I1ii11iIi11i * oO0o
  ooo = 1 if ( ooo == "" ) else int ( ooo )
  if 23 - 23: i11iIiiIii
  if 100 - 100: oO0o + O0 . I1IiiI + i1IIi - OoOoOO00 + o0oOOo0O0Ooo
 ooOOo = [ None , None , None ]
 i1iii1IiiiI1i1 = lisp_address ( LISP_AFI_IPV4 , "" , 32 , 0 )
 IIIiI1i1 = lisp_address ( LISP_AFI_IPV6 , "" , 128 , 0 )
 IIi11iII11i1 = None
 if 5 - 5: II111iiii - IiII
 for OoO0o0OOOO in netifaces . interfaces ( ) :
  if ( O0O0 != None and O0O0 != OoO0o0OOOO ) : continue
  IIiiI = netifaces . ifaddresses ( OoO0o0OOOO )
  if ( IIiiI == { } ) : continue
  if 86 - 86: IiII * I11i + O0 * I1Ii111 + i11iIiiIii - I1ii11iIi11i
  if 70 - 70: i11iIiiIii
  if 57 - 57: I11i % OOooOOo + ooOoO0o * Ii1I . Oo0Ooo
  if 78 - 78: OoooooooOO / i1IIi . OOooOOo
  IIi11iII11i1 = lisp_get_interface_instance_id ( OoO0o0OOOO , None )
  if 88 - 88: I11i + I1IiiI - I11i / OoooooooOO - i11iIiiIii
  if 24 - 24: iIii1I11I1II1
  if 89 - 89: Ii1I / i1IIi - o0oOOo0O0Ooo % I1IiiI . Oo0Ooo - O0
  if 71 - 71: OoO0O00 % I1IiiI - iII111i . iII111i
  if ( IIiiI . has_key ( netifaces . AF_INET ) ) :
   ooOo000OoO0o = IIiiI [ netifaces . AF_INET ]
   I1I1 = 0
   for o0o00O0oOooO0 in ooOo000OoO0o :
    i1iii1IiiiI1i1 . store_address ( o0o00O0oOooO0 [ "addr" ] )
    if ( i1iii1IiiiI1i1 . is_ipv4_loopback ( ) ) : continue
    if ( i1iii1IiiiI1i1 . is_ipv4_link_local ( ) ) : continue
    if ( i1iii1IiiiI1i1 . address == 0 ) : continue
    I1I1 += 1
    i1iii1IiiiI1i1 . instance_id = IIi11iII11i1
    if ( O0O0 == None and
 lisp_db_for_lookups . lookup_cache ( i1iii1IiiiI1i1 , False ) ) : continue
    ooOOo [ 0 ] = i1iii1IiiiI1i1
    if ( I1I1 == ooo ) : break
    if 78 - 78: I11i . OOooOOo + oO0o * iII111i - i1IIi
    if 27 - 27: Ii1I % i1IIi . Oo0Ooo % I1Ii111
  if ( IIiiI . has_key ( netifaces . AF_INET6 ) ) :
   ooooo0O0 = IIiiI [ netifaces . AF_INET6 ]
   I1I1 = 0
   for o0o00O0oOooO0 in ooooo0O0 :
    oo0o00OO = o0o00O0oOooO0 [ "addr" ]
    IIIiI1i1 . store_address ( oo0o00OO )
    if ( IIIiI1i1 . is_ipv6_string_link_local ( oo0o00OO ) ) : continue
    if ( IIIiI1i1 . is_ipv6_loopback ( ) ) : continue
    I1I1 += 1
    IIIiI1i1 . instance_id = IIi11iII11i1
    if ( O0O0 == None and
 lisp_db_for_lookups . lookup_cache ( IIIiI1i1 , False ) ) : continue
    ooOOo [ 1 ] = IIIiI1i1
    if ( I1I1 == ooo ) : break
    if 10 - 10: IiII / OoooooooOO
    if 50 - 50: i11iIiiIii - OoooooooOO . oO0o + O0 . i1IIi
    if 91 - 91: o0oOOo0O0Ooo . iII111i % Oo0Ooo - iII111i . oO0o % i11iIiiIii
    if 25 - 25: iIii1I11I1II1
    if 63 - 63: ooOoO0o
    if 96 - 96: I11i
  if ( ooOOo [ 0 ] == None ) : continue
  if 34 - 34: OoOoOO00 / OoO0O00 - I1IiiI . O0 . OOooOOo
  ooOOo [ 2 ] = OoO0o0OOOO
  break
  if 63 - 63: iII111i
  if 11 - 11: iII111i - iIii1I11I1II1
 ooOo0O0 = ooOOo [ 0 ] . print_address_no_iid ( ) if ooOOo [ 0 ] else "none"
 ooo0 = ooOOo [ 1 ] . print_address_no_iid ( ) if ooOOo [ 1 ] else "none"
 OoO0o0OOOO = ooOOo [ 2 ] if ooOOo [ 2 ] else "none"
 if 36 - 36: I1Ii111 . IiII * OoooooooOO - o0oOOo0O0Ooo
 O0O0 = " (user selected)" if O0O0 != None else ""
 if 60 - 60: OOooOOo . iII111i / iIii1I11I1II1 + OOooOOo * I1Ii111
 ooOo0O0 = red ( ooOo0O0 , False )
 ooo0 = red ( ooo0 , False )
 OoO0o0OOOO = bold ( OoO0o0OOOO , False )
 lprint ( "Local addresses are IPv4: {}, IPv6: {} from device {}{}, iid {}" . format ( ooOo0O0 , ooo0 , OoO0o0OOOO , O0O0 , IIi11iII11i1 ) )
 if 82 - 82: i11iIiiIii . iIii1I11I1II1 * I1IiiI - I11i + Ii1I
 if 48 - 48: I1ii11iIi11i
 lisp_myrlocs = ooOOo
 return ( ( ooOOo [ 0 ] != None ) )
 if 96 - 96: ooOoO0o . OoooooooOO
 if 39 - 39: OOooOOo + OoO0O00
 if 80 - 80: OOooOOo % OoO0O00 / OoOoOO00
 if 54 - 54: Oo0Ooo % OoO0O00 - OOooOOo - I11i
 if 71 - 71: ooOoO0o . i11iIiiIii
 if 56 - 56: O0 * iII111i + iII111i * iIii1I11I1II1 / ooOoO0o * I1Ii111
 if 25 - 25: iIii1I11I1II1 . I11i * i11iIiiIii + Oo0Ooo * I11i
 if 67 - 67: iII111i
 if 88 - 88: Oo0Ooo
def lisp_get_all_addresses ( ) :
 i1ii111i = [ ]
 for II1i in netifaces . interfaces ( ) :
  try : i1ii1i1Ii11 = netifaces . ifaddresses ( II1i )
  except : continue
  if 88 - 88: I1Ii111 % I11i - OoooooooOO + ooOoO0o
  if ( i1ii1i1Ii11 . has_key ( netifaces . AF_INET ) ) :
   for o0o00O0oOooO0 in i1ii1i1Ii11 [ netifaces . AF_INET ] :
    oO0OO = o0o00O0oOooO0 [ "addr" ]
    if ( oO0OO . find ( "127.0.0.1" ) != - 1 ) : continue
    i1ii111i . append ( oO0OO )
    if 53 - 53: i1IIi . i1IIi - I11i / iII111i - OoOoOO00 % I1IiiI
    if 65 - 65: iII111i . OoooooooOO - O0 . iII111i - i11iIiiIii
  if ( i1ii1i1Ii11 . has_key ( netifaces . AF_INET6 ) ) :
   for o0o00O0oOooO0 in i1ii1i1Ii11 [ netifaces . AF_INET6 ] :
    oO0OO = o0o00O0oOooO0 [ "addr" ]
    if ( oO0OO == "::1" ) : continue
    if ( oO0OO [ 0 : 5 ] == "fe80:" ) : continue
    i1ii111i . append ( oO0OO )
    if 29 - 29: I1ii11iIi11i . I1IiiI % oO0o - i11iIiiIii
    if 27 - 27: I1ii11iIi11i - i11iIiiIii % I1Ii111 / Oo0Ooo . Oo0Ooo / OoooooooOO
    if 76 - 76: I11i * OoO0O00 . iIii1I11I1II1 % OoooooooOO % I1ii11iIi11i
 return ( i1ii111i )
 if 39 - 39: II111iiii * OoOoOO00 . O0 * I11i
 if 89 - 89: Ii1I - ooOoO0o . I11i - I1Ii111 - I1IiiI
 if 79 - 79: IiII + IiII + Ii1I
 if 39 - 39: O0 - OoooooooOO
 if 63 - 63: iIii1I11I1II1 % o0oOOo0O0Ooo * ooOoO0o
 if 79 - 79: O0
 if 32 - 32: II111iiii . O0 + Ii1I / OoOoOO00 / IiII / OOooOOo
 if 15 - 15: I1ii11iIi11i
def lisp_get_all_multicast_rles ( ) :
 I11iI1 = [ ]
 II1IIiiI1 = commands . getoutput ( 'egrep "rle-address =" ./lisp.config' )
 if ( II1IIiiI1 == "" ) : return ( I11iI1 )
 if 96 - 96: o0oOOo0O0Ooo % IiII / OOooOOo
 Oo0o0ooOoO = II1IIiiI1 . split ( "\n" )
 for oOOo0ooO0 in Oo0o0ooOoO :
  if ( oOOo0ooO0 [ 0 ] == "#" ) : continue
  iI1Ii11 = oOOo0ooO0 . split ( "rle-address = " ) [ 1 ]
  Ooo0 = int ( iI1Ii11 . split ( "." ) [ 0 ] )
  if ( Ooo0 >= 224 and Ooo0 < 240 ) : I11iI1 . append ( iI1Ii11 )
  if 49 - 49: II111iiii + OoooooooOO . oO0o + i11iIiiIii / oO0o
 return ( I11iI1 )
 if 39 - 39: OoO0O00 + O0 + ooOoO0o * II111iiii % O0 - O0
 if 41 - 41: IiII % o0oOOo0O0Ooo
 if 67 - 67: O0 % I1Ii111
 if 35 - 35: I1IiiI . OoOoOO00 + OoooooooOO % Oo0Ooo % OOooOOo
 if 39 - 39: Ii1I
 if 60 - 60: OOooOOo
 if 62 - 62: I1Ii111 * I11i
 if 74 - 74: OoOoOO00 . iIii1I11I1II1
class lisp_packet ( ) :
 def __init__ ( self , packet ) :
  self . outer_source = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . outer_dest = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . outer_tos = 0
  self . outer_ttl = 0
  self . udp_sport = 0
  self . udp_dport = 0
  self . udp_length = 0
  self . udp_checksum = 0
  self . inner_source = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . inner_dest = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . inner_tos = 0
  self . inner_ttl = 0
  self . inner_protocol = 0
  self . inner_sport = 0
  self . inner_dport = 0
  self . lisp_header = lisp_data_header ( )
  self . packet = packet
  self . inner_version = 0
  self . outer_version = 0
  self . encap_port = LISP_DATA_PORT
  self . inner_is_fragment = False
  self . packet_error = ""
  self . gleaned_dest = False
  if 87 - 87: ooOoO0o
  if 41 - 41: OoOoOO00 . iIii1I11I1II1 % ooOoO0o + O0
 def encode ( self , nonce ) :
  if 22 - 22: o0oOOo0O0Ooo + Oo0Ooo . ooOoO0o + I1ii11iIi11i * iII111i . i11iIiiIii
  if 90 - 90: OOooOOo * OoOoOO00 - Oo0Ooo + o0oOOo0O0Ooo
  if 53 - 53: OoooooooOO . OoooooooOO + o0oOOo0O0Ooo - iII111i + OOooOOo
  if 44 - 44: I1Ii111 - IiII
  if 100 - 100: oO0o . OoO0O00 - Ii1I + O0 * OoO0O00
  if ( self . outer_source . is_null ( ) ) : return ( None )
  if 59 - 59: II111iiii
  if 43 - 43: Oo0Ooo + OoooooooOO
  if 47 - 47: ooOoO0o
  if 92 - 92: I11i % i11iIiiIii % Oo0Ooo
  if 23 - 23: II111iiii * iII111i
  if 80 - 80: I1Ii111 / i11iIiiIii + OoooooooOO
  if ( nonce == None ) :
   self . lisp_header . nonce ( lisp_get_data_nonce ( ) )
  elif ( self . lisp_header . is_request_nonce ( nonce ) ) :
   self . lisp_header . request_nonce ( nonce )
  else :
   self . lisp_header . nonce ( nonce )
   if 38 - 38: I1ii11iIi11i % ooOoO0o + i1IIi * OoooooooOO * oO0o
  self . lisp_header . instance_id ( self . inner_dest . instance_id )
  if 83 - 83: iIii1I11I1II1 - ooOoO0o - I1Ii111 / OoO0O00 - O0
  if 81 - 81: Ii1I - oO0o * I1ii11iIi11i / I1Ii111
  if 21 - 21: OoO0O00
  if 63 - 63: I11i . O0 * I11i + iIii1I11I1II1
  if 46 - 46: i1IIi + II111iiii * i1IIi - Ii1I
  if 79 - 79: II111iiii - oO0o * I1ii11iIi11i - OoOoOO00 . I1ii11iIi11i
  self . lisp_header . key_id ( 0 )
  iiII1IIii1i1 = ( self . lisp_header . get_instance_id ( ) == 0xffffff )
  if ( lisp_data_plane_security and iiII1IIii1i1 == False ) :
   oo0o00OO = self . outer_dest . print_address_no_iid ( ) + ":" + str ( self . encap_port )
   if 38 - 38: iII111i * OoooooooOO
   if ( lisp_crypto_keys_by_rloc_encap . has_key ( oo0o00OO ) ) :
    iIi11III = lisp_crypto_keys_by_rloc_encap [ oo0o00OO ]
    if ( iIi11III [ 1 ] ) :
     iIi11III [ 1 ] . use_count += 1
     IiiiIi1iiii11 , iIIi1IIIii11i = self . encrypt ( iIi11III [ 1 ] , oo0o00OO )
     if ( iIIi1IIIii11i ) : self . packet = IiiiIi1iiii11
     if 40 - 40: I1IiiI % ooOoO0o % IiII + OoO0O00
     if 75 - 75: oO0o - I1ii11iIi11i + oO0o + OoooooooOO . i11iIiiIii
     if 52 - 52: iII111i / ooOoO0o - i11iIiiIii + OoooooooOO
     if 33 - 33: O0 + Oo0Ooo - iIii1I11I1II1 % i11iIiiIii / I1IiiI
     if 47 - 47: I1ii11iIi11i * oO0o + iIii1I11I1II1 - oO0o / IiII
     if 86 - 86: IiII
     if 43 - 43: I1IiiI / iII111i / ooOoO0o + iIii1I11I1II1 + OoooooooOO
     if 33 - 33: II111iiii - IiII - ooOoO0o
  self . udp_checksum = 0
  if ( self . encap_port == LISP_DATA_PORT ) :
   if ( lisp_crypto_ephem_port == None ) :
    if ( self . gleaned_dest ) :
     self . udp_sport = LISP_DATA_PORT
    else :
     self . hash_packet ( )
     if 92 - 92: OoO0O00 * IiII
   else :
    self . udp_sport = lisp_crypto_ephem_port
    if 92 - 92: oO0o
  else :
   self . udp_sport = LISP_DATA_PORT
   if 7 - 7: iII111i
  self . udp_dport = self . encap_port
  self . udp_length = len ( self . packet ) + 16
  if 73 - 73: OoO0O00 % I1ii11iIi11i
  if 32 - 32: OOooOOo + iII111i + iIii1I11I1II1 * Oo0Ooo
  if 62 - 62: i11iIiiIii
  if 2 - 2: I1IiiI
  if ( self . outer_version == 4 ) :
   oo0O = socket . htons ( self . udp_sport )
   O0o0o0ooO0ooo = socket . htons ( self . udp_dport )
  else :
   oo0O = self . udp_sport
   O0o0o0ooO0ooo = self . udp_dport
   if 47 - 47: IiII
   if 76 - 76: OoO0O00 * iIii1I11I1II1 + I1ii11iIi11i - ooOoO0o - I11i / i1IIi
  O0o0o0ooO0ooo = socket . htons ( self . udp_dport ) if self . outer_version == 4 else self . udp_dport
  if 27 - 27: I1ii11iIi11i . IiII
  if 66 - 66: O0 / O0 * i1IIi . OoooooooOO % iIii1I11I1II1
  oOoO0OOO00O = struct . pack ( "HHHH" , oo0O , O0o0o0ooO0ooo , socket . htons ( self . udp_length ) ,
 self . udp_checksum )
  if 21 - 21: IiII - I1IiiI % OoooooooOO + o0oOOo0O0Ooo
  if 92 - 92: ooOoO0o + IiII
  if 52 - 52: II111iiii / I1IiiI . oO0o * IiII . I11i
  if 25 - 25: i11iIiiIii / OoOoOO00 - I1Ii111 / OoO0O00 . o0oOOo0O0Ooo . o0oOOo0O0Ooo
  iI1iIIII1 = self . lisp_header . encode ( )
  if 65 - 65: O0 / II111iiii . iIii1I11I1II1 . oO0o / Oo0Ooo % iIii1I11I1II1
  if 74 - 74: i1IIi / I1IiiI % I1ii11iIi11i / O0 % I11i - OoOoOO00
  if 31 - 31: I1IiiI / OoooooooOO . iIii1I11I1II1 * OoOoOO00 . OoooooooOO + II111iiii
  if 8 - 8: I1ii11iIi11i * I1ii11iIi11i * i1IIi + iII111i . I1ii11iIi11i
  if 100 - 100: OoooooooOO - O0 . I11i / I11i + II111iiii * OoOoOO00
  if ( self . outer_version == 4 ) :
   i11111 = socket . htons ( self . udp_length + 20 )
   o0o00OoOo0 = socket . htons ( 0x4000 )
   oo0O0000O0 = struct . pack ( "BBHHHBBH" , 0x45 , self . outer_tos , i11111 , 0xdfdf ,
 o0o00OoOo0 , self . outer_ttl , 17 , 0 )
   oo0O0000O0 += self . outer_source . pack_address ( )
   oo0O0000O0 += self . outer_dest . pack_address ( )
   oo0O0000O0 = lisp_ip_checksum ( oo0O0000O0 )
  elif ( self . outer_version == 6 ) :
   oo0O0000O0 = ""
   if 53 - 53: IiII % Oo0Ooo
   if 42 - 42: i11iIiiIii / I1IiiI - OoO0O00 - ooOoO0o + II111iiii % ooOoO0o
   if 50 - 50: OoooooooOO + oO0o * I1IiiI - Ii1I / i11iIiiIii
   if 5 - 5: O0 - I1IiiI
   if 44 - 44: II111iiii . II111iiii + OOooOOo * Ii1I
   if 16 - 16: II111iiii
   if 100 - 100: O0 - i1IIi
  else :
   return ( None )
   if 48 - 48: oO0o % ooOoO0o + O0
   if 27 - 27: I1ii11iIi11i / OOooOOo
  self . packet = oo0O0000O0 + oOoO0OOO00O + iI1iIIII1 + self . packet
  return ( self )
  if 33 - 33: OoooooooOO % I1ii11iIi11i . O0 / I1ii11iIi11i
  if 63 - 63: IiII + iIii1I11I1II1 + I1IiiI + I1Ii111
 def cipher_pad ( self , packet ) :
  oOOoO0O = len ( packet )
  if ( ( oOOoO0O % 16 ) != 0 ) :
   OoOoO = ( ( oOOoO0O / 16 ) + 1 ) * 16
   packet = packet . ljust ( OoOoO )
   if 57 - 57: Oo0Ooo % OoO0O00
  return ( packet )
  if 1 - 1: OoOoOO00 * O0 . oO0o % O0 + II111iiii
  if 49 - 49: I11i . OOooOOo
 def encrypt ( self , key , addr_str ) :
  if ( key == None or key . shared_key == None ) :
   return ( [ self . packet , False ] )
   if 74 - 74: i1IIi
   if 15 - 15: i1IIi + IiII % I1IiiI / i11iIiiIii * OoOoOO00
   if 69 - 69: i11iIiiIii
   if 61 - 61: O0
   if 21 - 21: OoO0O00 % iIii1I11I1II1 . OoO0O00
  IiiiIi1iiii11 = self . cipher_pad ( self . packet )
  OO000OOOo0Oo = key . get_iv ( )
  if 75 - 75: II111iiii + ooOoO0o % OOooOOo + Oo0Ooo
  i1 = lisp_get_timestamp ( )
  oOoOOoo = None
  if ( key . cipher_suite == LISP_CS_25519_CHACHA ) :
   Oo00O0o0O = chacha . ChaCha ( key . encrypt_key , OO000OOOo0Oo ) . encrypt
  elif ( key . cipher_suite == LISP_CS_25519_GCM ) :
   O0OoOO = binascii . unhexlify ( key . encrypt_key )
   try :
    o0o0oO0OOO = AES . new ( O0OoOO , AES . MODE_GCM , OO000OOOo0Oo )
    Oo00O0o0O = o0o0oO0OOO . encrypt
    oOoOOoo = o0o0oO0OOO . digest
   except :
    lprint ( "You need AES-GCM, do a 'pip install pycryptodome'" )
    return ( [ self . packet , False ] )
    if 66 - 66: Ii1I * iIii1I11I1II1 - ooOoO0o / I1IiiI
  else :
   O0OoOO = binascii . unhexlify ( key . encrypt_key )
   Oo00O0o0O = AES . new ( O0OoOO , AES . MODE_CBC , OO000OOOo0Oo ) . encrypt
   if 62 - 62: IiII . O0 . iIii1I11I1II1
   if 94 - 94: ooOoO0o % I11i % i1IIi
  o0OoOo0o0O00 = Oo00O0o0O ( IiiiIi1iiii11 )
  if 33 - 33: ooOoO0o + OoooooooOO - OoO0O00 / i1IIi / OoooooooOO
  if ( o0OoOo0o0O00 == None ) : return ( [ self . packet , False ] )
  i1 = int ( str ( time . time ( ) - i1 ) . split ( "." ) [ 1 ] [ 0 : 6 ] )
  if 82 - 82: I1ii11iIi11i / OOooOOo - iII111i / Oo0Ooo * OoO0O00
  if 55 - 55: OoooooooOO
  if 73 - 73: OoOoOO00 - I1ii11iIi11i % Oo0Ooo + I1ii11iIi11i - O0 . OoO0O00
  if 38 - 38: O0
  if 79 - 79: i1IIi . oO0o
  if 34 - 34: I1Ii111 * II111iiii
  if ( oOoOOoo != None ) : o0OoOo0o0O00 += oOoOOoo ( )
  if 71 - 71: IiII
  if 97 - 97: I1ii11iIi11i
  if 86 - 86: Oo0Ooo - OOooOOo . OoOoOO00 . II111iiii * I1IiiI . II111iiii
  if 34 - 34: o0oOOo0O0Ooo . I1Ii111 % IiII - O0 / I1Ii111
  if 91 - 91: i11iIiiIii % I1Ii111 * oO0o - I1ii11iIi11i . I1Ii111
  self . lisp_header . key_id ( key . key_id )
  iI1iIIII1 = self . lisp_header . encode ( )
  if 28 - 28: i11iIiiIii
  Oo00oo0 = key . do_icv ( iI1iIIII1 + OO000OOOo0Oo + o0OoOo0o0O00 , OO000OOOo0Oo )
  if 82 - 82: OOooOOo * I1ii11iIi11i % Ii1I . OOooOOo
  iI1oOoo = 4 if ( key . do_poly ) else 8
  if 59 - 59: IiII % Ii1I
  O0ooo = bold ( "Encrypt" , False )
  IiIIiII1I = bold ( key . cipher_suite_string , False )
  addr_str = "RLOC: " + red ( addr_str , False )
  o00oOOo0Oo = "poly" if key . do_poly else "sha256"
  o00oOOo0Oo = bold ( o00oOOo0Oo , False )
  Oooo0o0oO = "ICV({}): 0x{}...{}" . format ( o00oOOo0Oo , Oo00oo0 [ 0 : iI1oOoo ] , Oo00oo0 [ - iI1oOoo : : ] )
  dprint ( "{} for key-id: {}, {}, {}, {}-time: {} usec" . format ( O0ooo , key . key_id , addr_str , Oooo0o0oO , IiIIiII1I , i1 ) )
  if 82 - 82: ooOoO0o
  if 70 - 70: iIii1I11I1II1 + i11iIiiIii + Oo0Ooo / iII111i
  Oo00oo0 = int ( Oo00oo0 , 16 )
  if ( key . do_poly ) :
   iI1IiiiIi = byte_swap_64 ( ( Oo00oo0 >> 64 ) & LISP_8_64_MASK )
   IiI111 = byte_swap_64 ( Oo00oo0 & LISP_8_64_MASK )
   Oo00oo0 = struct . pack ( "QQ" , iI1IiiiIi , IiI111 )
  else :
   iI1IiiiIi = byte_swap_64 ( ( Oo00oo0 >> 96 ) & LISP_8_64_MASK )
   IiI111 = byte_swap_64 ( ( Oo00oo0 >> 32 ) & LISP_8_64_MASK )
   OO0OO00ooO0 = socket . htonl ( Oo00oo0 & 0xffffffff )
   Oo00oo0 = struct . pack ( "QQI" , iI1IiiiIi , IiI111 , OO0OO00ooO0 )
   if 68 - 68: OoOoOO00 * I1ii11iIi11i - OoooooooOO - I11i + iIii1I11I1II1 * i11iIiiIii
   if 80 - 80: i1IIi . I1IiiI - oO0o + OOooOOo + iII111i % oO0o
  return ( [ OO000OOOo0Oo + o0OoOo0o0O00 + Oo00oo0 , True ] )
  if 13 - 13: II111iiii / OoOoOO00 / OoOoOO00 + ooOoO0o
  if 49 - 49: O0 / II111iiii * I1IiiI - OoooooooOO . II111iiii % IiII
 def decrypt ( self , packet , header_length , key , addr_str ) :
  if 13 - 13: oO0o . iIii1I11I1II1 . OOooOOo . IiII
  if 58 - 58: I11i
  if 7 - 7: II111iiii / IiII % I11i + I1IiiI - O0
  if 45 - 45: I1IiiI / iII111i + oO0o + IiII
  if 15 - 15: I1IiiI % OoO0O00
  if 66 - 66: oO0o * i11iIiiIii . I1Ii111
  if ( key . do_poly ) :
   iI1IiiiIi , IiI111 = struct . unpack ( "QQ" , packet [ - 16 : : ] )
   o0O0OOOo0 = byte_swap_64 ( iI1IiiiIi ) << 64
   o0O0OOOo0 |= byte_swap_64 ( IiI111 )
   o0O0OOOo0 = lisp_hex_string ( o0O0OOOo0 ) . zfill ( 32 )
   packet = packet [ 0 : - 16 ]
   iI1oOoo = 4
   I1ii1i = bold ( "poly" , False )
  else :
   iI1IiiiIi , IiI111 , OO0OO00ooO0 = struct . unpack ( "QQI" , packet [ - 20 : : ] )
   o0O0OOOo0 = byte_swap_64 ( iI1IiiiIi ) << 96
   o0O0OOOo0 |= byte_swap_64 ( IiI111 ) << 32
   o0O0OOOo0 |= socket . htonl ( OO0OO00ooO0 )
   o0O0OOOo0 = lisp_hex_string ( o0O0OOOo0 ) . zfill ( 40 )
   packet = packet [ 0 : - 20 ]
   iI1oOoo = 8
   I1ii1i = bold ( "sha" , False )
   if 51 - 51: OoO0O00 - iII111i % O0 - OoOoOO00
  iI1iIIII1 = self . lisp_header . encode ( )
  if 53 - 53: iII111i / i1IIi / i1IIi
  if 77 - 77: I11i + i1IIi . I11i
  if 89 - 89: o0oOOo0O0Ooo + OOooOOo * oO0o
  if 45 - 45: iII111i - o0oOOo0O0Ooo . Ii1I
  if ( key . cipher_suite == LISP_CS_25519_CHACHA ) :
   Iii = 8
   IiIIiII1I = bold ( "chacha" , False )
  elif ( key . cipher_suite == LISP_CS_25519_GCM ) :
   Iii = 12
   IiIIiII1I = bold ( "aes-gcm" , False )
  else :
   Iii = 16
   IiIIiII1I = bold ( "aes-cbc" , False )
   if 32 - 32: OoO0O00
  OO000OOOo0Oo = packet [ 0 : Iii ]
  if 99 - 99: Ii1I - IiII * iIii1I11I1II1 . II111iiii
  if 56 - 56: iIii1I11I1II1 % OoO0O00 . ooOoO0o % IiII . I1Ii111 * Oo0Ooo
  if 41 - 41: iIii1I11I1II1 % IiII * oO0o - ooOoO0o
  if 5 - 5: OoO0O00 + OoO0O00 + II111iiii * iIii1I11I1II1 + OoooooooOO
  Oo0OOOOOOO0oo = key . do_icv ( iI1iIIII1 + packet , OO000OOOo0Oo )
  if 35 - 35: I1ii11iIi11i * OoO0O00 * I1IiiI / OoooooooOO
  I1iIIIiiii = "0x{}...{}" . format ( o0O0OOOo0 [ 0 : iI1oOoo ] , o0O0OOOo0 [ - iI1oOoo : : ] )
  I1111 = "0x{}...{}" . format ( Oo0OOOOOOO0oo [ 0 : iI1oOoo ] , Oo0OOOOOOO0oo [ - iI1oOoo : : ] )
  if 67 - 67: i1IIi
  if ( Oo0OOOOOOO0oo != o0O0OOOo0 ) :
   self . packet_error = "ICV-error"
   O0Oo0oo0O0O0o = IiIIiII1I + "/" + I1ii1i
   IIIi111iIi11 = bold ( "ICV failed ({})" . format ( O0Oo0oo0O0O0o ) , False )
   Oooo0o0oO = "packet-ICV {} != computed-ICV {}" . format ( I1iIIIiiii , I1111 )
   dprint ( ( "{} from RLOC {}, receive-port: {}, key-id: {}, " + "packet dropped, {}" ) . format ( IIIi111iIi11 , red ( addr_str , False ) ,
   # II111iiii - oO0o
 self . udp_sport , key . key_id , Oooo0o0oO ) )
   dprint ( "{}" . format ( key . print_keys ( ) ) )
   if 52 - 52: I1IiiI % OoO0O00 * Ii1I * iII111i / OOooOOo
   if 88 - 88: oO0o
   if 1 - 1: Oo0Ooo
   if 95 - 95: OoooooooOO / I11i % OoooooooOO / ooOoO0o * IiII
   if 75 - 75: O0
   if 56 - 56: OoO0O00 / II111iiii
   lisp_retry_decap_keys ( addr_str , iI1iIIII1 + packet , OO000OOOo0Oo , o0O0OOOo0 )
   return ( [ None , False ] )
   if 39 - 39: OoOoOO00 - OoooooooOO - i1IIi / II111iiii
   if 49 - 49: Oo0Ooo + O0 + IiII . II111iiii % ooOoO0o
   if 33 - 33: OoOoOO00 . iIii1I11I1II1 / I11i % Ii1I
   if 49 - 49: OoO0O00 + II111iiii / IiII - O0 % Ii1I
   if 27 - 27: OoO0O00 + Oo0Ooo
  packet = packet [ Iii : : ]
  if 92 - 92: I1IiiI % iII111i
  if 31 - 31: OoooooooOO - oO0o / I1Ii111
  if 62 - 62: i11iIiiIii - I11i
  if 81 - 81: I11i
  i1 = lisp_get_timestamp ( )
  if ( key . cipher_suite == LISP_CS_25519_CHACHA ) :
   OOOOooO0 = chacha . ChaCha ( key . encrypt_key , OO000OOOo0Oo ) . decrypt
  elif ( key . cipher_suite == LISP_CS_25519_GCM ) :
   O0OoOO = binascii . unhexlify ( key . encrypt_key )
   try :
    OOOOooO0 = AES . new ( O0OoOO , AES . MODE_GCM , OO000OOOo0Oo ) . decrypt
   except :
    self . packet_error = "no-decrypt-key"
    lprint ( "You need AES-GCM, do a 'pip install pycryptodome'" )
    return ( [ None , False ] )
    if 23 - 23: I1IiiI * I11i / i11iIiiIii * I1Ii111 . iIii1I11I1II1
  else :
   if ( ( len ( packet ) % 16 ) != 0 ) :
    dprint ( "Ciphertext not multiple of 16 bytes, packet dropped" )
    return ( [ None , False ] )
    if 40 - 40: I1IiiI . Ii1I / i1IIi
   O0OoOO = binascii . unhexlify ( key . encrypt_key )
   OOOOooO0 = AES . new ( O0OoOO , AES . MODE_CBC , OO000OOOo0Oo ) . decrypt
   if 28 - 28: Ii1I
   if 66 - 66: I11i
  i1o0 = OOOOooO0 ( packet )
  i1 = int ( str ( time . time ( ) - i1 ) . split ( "." ) [ 1 ] [ 0 : 6 ] )
  if 61 - 61: I11i
  if 80 - 80: I1IiiI - I1IiiI
  if 52 - 52: II111iiii
  if 21 - 21: OoOoOO00 - II111iiii
  O0ooo = bold ( "Decrypt" , False )
  addr_str = "RLOC: " + red ( addr_str , False )
  o00oOOo0Oo = "poly" if key . do_poly else "sha256"
  o00oOOo0Oo = bold ( o00oOOo0Oo , False )
  Oooo0o0oO = "ICV({}): {}" . format ( o00oOOo0Oo , I1iIIIiiii )
  dprint ( "{} for key-id: {}, {}, {} (good), {}-time: {} usec" . format ( O0ooo , key . key_id , addr_str , Oooo0o0oO , IiIIiII1I , i1 ) )
  if 10 - 10: OoOoOO00 - o0oOOo0O0Ooo * i11iIiiIii / Oo0Ooo + o0oOOo0O0Ooo + iIii1I11I1II1
  if 23 - 23: i1IIi + I1ii11iIi11i + I1IiiI - ooOoO0o % OoooooooOO . IiII
  if 49 - 49: oO0o . OoOoOO00
  if 73 - 73: Ii1I / I1IiiI / OoooooooOO + I1IiiI
  if 57 - 57: OOooOOo . Ii1I % o0oOOo0O0Ooo
  if 32 - 32: I11i / IiII - O0 * iIii1I11I1II1
  if 70 - 70: OoooooooOO % OoooooooOO % OoO0O00
  self . packet = self . packet [ 0 : header_length ]
  return ( [ i1o0 , True ] )
  if 98 - 98: OoO0O00
  if 18 - 18: I11i + Oo0Ooo - OoO0O00 / I1Ii111 / OOooOOo
 def fragment_outer ( self , outer_hdr , inner_packet ) :
  OOoOoO = 1000
  if 72 - 72: OoOoOO00 / I1Ii111 * IiII % iIii1I11I1II1
  if 53 - 53: OoO0O00 . O0 . I1IiiI * OOooOOo / o0oOOo0O0Ooo
  if 34 - 34: OoOoOO00
  if 16 - 16: i1IIi - I1Ii111 - II111iiii
  if 83 - 83: I1IiiI - OoO0O00 - o0oOOo0O0Ooo / O0 - I11i . II111iiii
  iI1i1Ii111I = [ ]
  oO0ooOoO = 0
  oOOoO0O = len ( inner_packet )
  while ( oO0ooOoO < oOOoO0O ) :
   o0o00OoOo0 = inner_packet [ oO0ooOoO : : ]
   if ( len ( o0o00OoOo0 ) > OOoOoO ) : o0o00OoOo0 = o0o00OoOo0 [ 0 : OOoOoO ]
   iI1i1Ii111I . append ( o0o00OoOo0 )
   oO0ooOoO += len ( o0o00OoOo0 )
   if 17 - 17: O0 * iIii1I11I1II1 % IiII . IiII / O0
   if 52 - 52: I1IiiI - iIii1I11I1II1 - I1ii11iIi11i
   if 38 - 38: I1IiiI + o0oOOo0O0Ooo - IiII
   if 85 - 85: iII111i * iII111i % OoOoOO00 - OOooOOo % OoO0O00 - I1IiiI
   if 3 - 3: OOooOOo + i1IIi % I1ii11iIi11i
   if 100 - 100: OoooooooOO + i11iIiiIii % o0oOOo0O0Ooo + I1IiiI . Oo0Ooo . II111iiii
  OoiiI11111II = [ ]
  oO0ooOoO = 0
  for o0o00OoOo0 in iI1i1Ii111I :
   if 48 - 48: iII111i % i11iIiiIii . OoooooooOO * IiII % OoO0O00 . iII111i
   if 6 - 6: O0 . ooOoO0o - oO0o / i11iIiiIii
   if 84 - 84: I11i / I1ii11iIi11i * o0oOOo0O0Ooo * OoO0O00 * OOooOOo * O0
   if 83 - 83: O0 % II111iiii + o0oOOo0O0Ooo / OoooooooOO
   Ooi1IIii1i = oO0ooOoO if ( o0o00OoOo0 == iI1i1Ii111I [ - 1 ] ) else 0x2000 + oO0ooOoO
   Ooi1IIii1i = socket . htons ( Ooi1IIii1i )
   outer_hdr = outer_hdr [ 0 : 6 ] + struct . pack ( "H" , Ooi1IIii1i ) + outer_hdr [ 8 : : ]
   if 60 - 60: Ii1I % Oo0Ooo / I11i . iII111i / I1Ii111 - OoooooooOO
   if 76 - 76: O0
   if 71 - 71: I1IiiI . i1IIi
   if 19 - 19: II111iiii / II111iiii % I1ii11iIi11i + oO0o + oO0o + iII111i
   IIi1I1 = socket . htons ( len ( o0o00OoOo0 ) + 20 )
   outer_hdr = outer_hdr [ 0 : 2 ] + struct . pack ( "H" , IIi1I1 ) + outer_hdr [ 4 : : ]
   outer_hdr = lisp_ip_checksum ( outer_hdr )
   OoiiI11111II . append ( outer_hdr + o0o00OoOo0 )
   oO0ooOoO += len ( o0o00OoOo0 ) / 8
   if 80 - 80: o0oOOo0O0Ooo % iII111i
  return ( OoiiI11111II )
  if 80 - 80: Ii1I
  if 26 - 26: iIii1I11I1II1 . OoooooooOO - iIii1I11I1II1
 def send_icmp_too_big ( self , inner_packet ) :
  global lisp_last_icmp_too_big_sent
  global lisp_icmp_raw_socket
  if 59 - 59: I1ii11iIi11i + I11i . oO0o
  Ooo0o0oo0 = time . time ( ) - lisp_last_icmp_too_big_sent
  if ( Ooo0o0oo0 < LISP_ICMP_TOO_BIG_RATE_LIMIT ) :
   lprint ( "Rate limit sending ICMP Too-Big to {}" . format ( self . inner_source . print_address_no_iid ( ) ) )
   if 87 - 87: OoO0O00
   return ( False )
   if 34 - 34: I1Ii111 . OoOoOO00 / i11iIiiIii / iII111i
   if 46 - 46: Oo0Ooo + II111iiii * I1IiiI + OOooOOo
   if 31 - 31: Ii1I * o0oOOo0O0Ooo * Ii1I + OoO0O00 * o0oOOo0O0Ooo . I1Ii111
   if 89 - 89: OoooooooOO * Ii1I * I1IiiI . ooOoO0o * Ii1I / iII111i
   if 46 - 46: i11iIiiIii
   if 15 - 15: O0 / i1IIi / i1IIi . iII111i % OoOoOO00 + I1IiiI
   if 48 - 48: I1Ii111 % iII111i % Ii1I % iIii1I11I1II1 . Ii1I
   if 14 - 14: iII111i * OoO0O00 % O0 + I11i + I1ii11iIi11i
   if 23 - 23: Oo0Ooo % iII111i + Ii1I - I1Ii111
   if 65 - 65: OoooooooOO
   if 22 - 22: OOooOOo + II111iiii + Oo0Ooo
   if 83 - 83: ooOoO0o
   if 43 - 43: OOooOOo
   if 84 - 84: OOooOOo . IiII . iII111i
   if 2 - 2: Oo0Ooo - OoOoOO00
  I1iiII = socket . htons ( 1400 )
  i111i1I1ii1i = struct . pack ( "BBHHH" , 3 , 4 , 0 , 0 , I1iiII )
  i111i1I1ii1i += inner_packet [ 0 : 20 + 8 ]
  i111i1I1ii1i = lisp_icmp_checksum ( i111i1I1ii1i )
  if 81 - 81: OoOoOO00 + o0oOOo0O0Ooo + Oo0Ooo
  if 79 - 79: Oo0Ooo - OoooooooOO % I1Ii111 + OoooooooOO - I11i % OoOoOO00
  if 5 - 5: OoOoOO00 . Oo0Ooo
  if 89 - 89: I1IiiI / iII111i / OoooooooOO - i11iIiiIii + I1IiiI
  if 64 - 64: i11iIiiIii + i1IIi % O0 . I11i
  if 64 - 64: ooOoO0o / i1IIi % iII111i
  if 84 - 84: OoOoOO00 - Oo0Ooo . ooOoO0o . IiII - Oo0Ooo
  o0Oo0oO00Oooo = inner_packet [ 12 : 16 ]
  Ii1II1I11i1I = self . inner_source . print_address_no_iid ( )
  OOoOo = self . outer_source . pack_address ( )
  if 27 - 27: I1IiiI * i11iIiiIii / O0 / II111iiii
  if 72 - 72: oO0o - Oo0Ooo / i11iIiiIii * I1IiiI + OoO0O00
  if 47 - 47: OOooOOo / II111iiii % IiII . oO0o * I1ii11iIi11i
  if 35 - 35: Oo0Ooo * II111iiii
  if 32 - 32: oO0o . Oo0Ooo / ooOoO0o + ooOoO0o . I1ii11iIi11i
  if 50 - 50: iIii1I11I1II1 * oO0o
  if 85 - 85: i1IIi
  if 100 - 100: OoooooooOO / I11i % OoO0O00 + Ii1I
  i11111 = socket . htons ( 20 + 36 )
  ooooo0Oo0 = struct . pack ( "BBHHHBBH" , 0x45 , 0 , i11111 , 0 , 0 , 32 , 1 , 0 ) + OOoOo + o0Oo0oO00Oooo
  ooooo0Oo0 = lisp_ip_checksum ( ooooo0Oo0 )
  ooooo0Oo0 = self . fix_outer_header ( ooooo0Oo0 )
  ooooo0Oo0 += i111i1I1ii1i
  IIi11 = bold ( "Too-Big" , False )
  lprint ( "Send ICMP {} to {}, mtu 1400: {}" . format ( IIi11 , Ii1II1I11i1I ,
 lisp_format_packet ( ooooo0Oo0 ) ) )
  if 77 - 77: Oo0Ooo - IiII
  try :
   lisp_icmp_raw_socket . sendto ( ooooo0Oo0 , ( Ii1II1I11i1I , 0 ) )
  except socket . error , iIIi1iI1I1IIi :
   lprint ( "lisp_icmp_raw_socket.sendto() failed: {}" . format ( iIIi1iI1I1IIi ) )
   return ( False )
   if 50 - 50: OoO0O00 % OoooooooOO * II111iiii
   if 54 - 54: OoooooooOO + Oo0Ooo * OOooOOo
   if 98 - 98: oO0o - oO0o . ooOoO0o
   if 60 - 60: I1IiiI * I1ii11iIi11i / O0 + I11i + IiII
   if 66 - 66: IiII * Oo0Ooo . OoooooooOO * I1Ii111
   if 93 - 93: IiII / i1IIi
  lisp_last_icmp_too_big_sent = lisp_get_timestamp ( )
  return ( True )
  if 47 - 47: ooOoO0o - Ii1I
 def fragment ( self ) :
  global lisp_icmp_raw_socket
  global lisp_ignore_df_bit
  if 98 - 98: oO0o . I1Ii111 / OoOoOO00 . ooOoO0o
  IiiiIi1iiii11 = self . fix_outer_header ( self . packet )
  if 1 - 1: OOooOOo
  if 87 - 87: O0 * II111iiii + iIii1I11I1II1 % oO0o % i11iIiiIii - OoOoOO00
  if 73 - 73: iII111i + Ii1I
  if 37 - 37: oO0o - iIii1I11I1II1 + II111iiii . Ii1I % iIii1I11I1II1
  if 17 - 17: I1Ii111 + i1IIi % O0
  if 65 - 65: IiII
  oOOoO0O = len ( IiiiIi1iiii11 )
  if ( oOOoO0O <= 1500 ) : return ( [ IiiiIi1iiii11 ] , "Fragment-None" )
  if 50 - 50: II111iiii / OoO0O00
  IiiiIi1iiii11 = self . packet
  if 79 - 79: I1ii11iIi11i - iIii1I11I1II1 % i1IIi / Oo0Ooo + II111iiii
  if 95 - 95: oO0o
  if 48 - 48: I11i / iIii1I11I1II1 % II111iiii
  if 39 - 39: i1IIi . I1ii11iIi11i / I11i / I11i
  if 100 - 100: OoooooooOO - OoooooooOO + IiII
  if ( self . inner_version != 4 ) :
   iIiIi1i1Iiii = random . randint ( 0 , 0xffff )
   OOO00000O = IiiiIi1iiii11 [ 0 : 4 ] + struct . pack ( "H" , iIiIi1i1Iiii ) + IiiiIi1iiii11 [ 6 : 20 ]
   iIiiiII11 = IiiiIi1iiii11 [ 20 : : ]
   OoiiI11111II = self . fragment_outer ( OOO00000O , iIiiiII11 )
   return ( OoiiI11111II , "Fragment-Outer" )
   if 98 - 98: I1ii11iIi11i
   if 25 - 25: OOooOOo % OOooOOo
   if 25 - 25: i11iIiiIii + I1ii11iIi11i - OoooooooOO . O0 % I1Ii111
   if 53 - 53: i1IIi
   if 59 - 59: o0oOOo0O0Ooo + I1IiiI % OoooooooOO - iIii1I11I1II1
  iiIII1i1 = 56 if ( self . outer_version == 6 ) else 36
  OOO00000O = IiiiIi1iiii11 [ 0 : iiIII1i1 ]
  oOOo0OOoOO0 = IiiiIi1iiii11 [ iiIII1i1 : iiIII1i1 + 20 ]
  iIiiiII11 = IiiiIi1iiii11 [ iiIII1i1 + 20 : : ]
  if 30 - 30: II111iiii / I1IiiI - ooOoO0o + OoOoOO00 * ooOoO0o / OoOoOO00
  if 17 - 17: OoO0O00
  if 31 - 31: oO0o + OoooooooOO - Ii1I % o0oOOo0O0Ooo / o0oOOo0O0Ooo / iIii1I11I1II1
  if 31 - 31: OoooooooOO - Ii1I . IiII % oO0o
  if 16 - 16: OOooOOo * Ii1I % I1Ii111 / IiII + iIii1I11I1II1 / I1IiiI
  IIII1I1 = struct . unpack ( "H" , oOOo0OOoOO0 [ 6 : 8 ] ) [ 0 ]
  IIII1I1 = socket . ntohs ( IIII1I1 )
  if ( IIII1I1 & 0x4000 ) :
   if ( lisp_icmp_raw_socket != None ) :
    I1i1i1iIi1iIi = IiiiIi1iiii11 [ iiIII1i1 : : ]
    if ( self . send_icmp_too_big ( I1i1i1iIi1iIi ) ) : return ( [ ] , None )
    if 22 - 22: iIii1I11I1II1 * I1IiiI / I11i + OoOoOO00
   if ( lisp_ignore_df_bit ) :
    IIII1I1 &= ~ 0x4000
   else :
    o00OoOOoO = bold ( "DF-bit set" , False )
    dprint ( "{} in inner header, packet discarded" . format ( o00OoOOoO ) )
    return ( [ ] , "Fragment-None-DF-bit" )
    if 28 - 28: iIii1I11I1II1 * I11i . I1IiiI
    if 78 - 78: OoooooooOO . OoooooooOO / O0
    if 25 - 25: II111iiii % II111iiii - Ii1I . O0
  oO0ooOoO = 0
  oOOoO0O = len ( iIiiiII11 )
  OoiiI11111II = [ ]
  while ( oO0ooOoO < oOOoO0O ) :
   OoiiI11111II . append ( iIiiiII11 [ oO0ooOoO : oO0ooOoO + 1400 ] )
   oO0ooOoO += 1400
   if 79 - 79: IiII / OoO0O00 * OoooooooOO * OoOoOO00 + I1IiiI
   if 68 - 68: I11i / iIii1I11I1II1 . Oo0Ooo + i11iIiiIii + o0oOOo0O0Ooo
   if 92 - 92: OoO0O00 . o0oOOo0O0Ooo . Ii1I % OoOoOO00
   if 58 - 58: I1ii11iIi11i % Ii1I * Ii1I - iII111i
   if 9 - 9: ooOoO0o - Ii1I % II111iiii + IiII + OOooOOo % O0
  iI1i1Ii111I = OoiiI11111II
  OoiiI11111II = [ ]
  o00OoOo0 = True if IIII1I1 & 0x2000 else False
  IIII1I1 = ( IIII1I1 & 0x1fff ) * 8
  for o0o00OoOo0 in iI1i1Ii111I :
   if 2 - 2: II111iiii + i1IIi
   if 68 - 68: OOooOOo + Ii1I
   if 58 - 58: IiII * Ii1I . i1IIi
   if 19 - 19: oO0o
   O0oooooO = IIII1I1 / 8
   if ( o00OoOo0 ) :
    O0oooooO |= 0x2000
   elif ( o0o00OoOo0 != iI1i1Ii111I [ - 1 ] ) :
    O0oooooO |= 0x2000
    if 28 - 28: Oo0Ooo / IiII . iII111i + OoO0O00 + I11i % Oo0Ooo
   O0oooooO = socket . htons ( O0oooooO )
   oOOo0OOoOO0 = oOOo0OOoOO0 [ 0 : 6 ] + struct . pack ( "H" , O0oooooO ) + oOOo0OOoOO0 [ 8 : : ]
   if 45 - 45: Oo0Ooo / O0 % OoooooooOO
   if 92 - 92: Ii1I . OoOoOO00 . I11i - OoooooooOO / ooOoO0o
   if 80 - 80: iIii1I11I1II1 / i11iIiiIii + iII111i
   if 41 - 41: I1Ii111 + OoO0O00 * I1IiiI * O0 * Oo0Ooo - OoOoOO00
   if 96 - 96: I1IiiI - iIii1I11I1II1
   if 25 - 25: OoooooooOO . Ii1I % iII111i . IiII
   oOOoO0O = len ( o0o00OoOo0 )
   IIII1I1 += oOOoO0O
   IIi1I1 = socket . htons ( oOOoO0O + 20 )
   oOOo0OOoOO0 = oOOo0OOoOO0 [ 0 : 2 ] + struct . pack ( "H" , IIi1I1 ) + oOOo0OOoOO0 [ 4 : 10 ] + struct . pack ( "H" , 0 ) + oOOo0OOoOO0 [ 12 : : ]
   if 67 - 67: OoooooooOO + I1Ii111 / ooOoO0o
   oOOo0OOoOO0 = lisp_ip_checksum ( oOOo0OOoOO0 )
   O0oo = oOOo0OOoOO0 + o0o00OoOo0
   if 50 - 50: I1Ii111 - II111iiii
   if 33 - 33: IiII / IiII . i11iIiiIii * I1ii11iIi11i + o0oOOo0O0Ooo
   if 16 - 16: IiII
   if 10 - 10: OoOoOO00 . IiII * iIii1I11I1II1 - oO0o - OoOoOO00 / I1Ii111
   if 13 - 13: oO0o + OoOoOO00 % IiII % OoooooooOO
   oOOoO0O = len ( O0oo )
   if ( self . outer_version == 4 ) :
    IIi1I1 = oOOoO0O + iiIII1i1
    oOOoO0O += 16
    OOO00000O = OOO00000O [ 0 : 2 ] + struct . pack ( "H" , IIi1I1 ) + OOO00000O [ 4 : : ]
    if 22 - 22: I1Ii111
    OOO00000O = lisp_ip_checksum ( OOO00000O )
    O0oo = OOO00000O + O0oo
    O0oo = self . fix_outer_header ( O0oo )
    if 23 - 23: O0
    if 41 - 41: i1IIi . OOooOOo / ooOoO0o / o0oOOo0O0Ooo % IiII - Ii1I
    if 14 - 14: I1ii11iIi11i - i11iIiiIii * I1Ii111
    if 39 - 39: OoooooooOO
    if 19 - 19: i11iIiiIii
   oOOOO = iiIII1i1 - 12
   IIi1I1 = socket . htons ( oOOoO0O )
   O0oo = O0oo [ 0 : oOOOO ] + struct . pack ( "H" , IIi1I1 ) + O0oo [ oOOOO + 2 : : ]
   if 82 - 82: i1IIi + o0oOOo0O0Ooo - II111iiii . Ii1I
   OoiiI11111II . append ( O0oo )
   if 93 - 93: II111iiii * OoOoOO00 % o0oOOo0O0Ooo
  return ( OoiiI11111II , "Fragment-Inner" )
  if 67 - 67: o0oOOo0O0Ooo + Oo0Ooo . ooOoO0o - i1IIi . OoOoOO00
  if 12 - 12: IiII / OoO0O00 / O0 * IiII
 def fix_outer_header ( self , packet ) :
  if 51 - 51: ooOoO0o * iII111i / i1IIi
  if 2 - 2: oO0o + IiII . iII111i - i1IIi + I1Ii111
  if 54 - 54: OoooooooOO . oO0o - iII111i
  if 76 - 76: I1Ii111
  if 61 - 61: ooOoO0o / II111iiii * ooOoO0o * OoOoOO00 * I1Ii111 . i11iIiiIii
  if 26 - 26: I1Ii111 / ooOoO0o - OoO0O00 . iIii1I11I1II1
  if 83 - 83: ooOoO0o % Ii1I / Oo0Ooo - iII111i / O0
  if 97 - 97: iIii1I11I1II1 * I11i
  if ( self . outer_version == 4 or self . inner_version == 4 ) :
   if ( lisp_is_macos ( ) ) :
    packet = packet [ 0 : 2 ] + packet [ 3 ] + packet [ 2 ] + packet [ 4 : 6 ] + packet [ 7 ] + packet [ 6 ] + packet [ 8 : : ]
    if 95 - 95: OoO0O00
   else :
    packet = packet [ 0 : 2 ] + packet [ 3 ] + packet [ 2 ] + packet [ 4 : : ]
    if 68 - 68: iIii1I11I1II1 . iIii1I11I1II1 / OoOoOO00 - II111iiii - iIii1I11I1II1
    if 75 - 75: ooOoO0o . I1IiiI * II111iiii
  return ( packet )
  if 99 - 99: iIii1I11I1II1 * I1ii11iIi11i + IiII
  if 70 - 70: i1IIi % ooOoO0o . I1ii11iIi11i - IiII + OOooOOo
 def send_packet ( self , lisp_raw_socket , dest ) :
  if ( lisp_flow_logging and dest != self . inner_dest ) : self . log_flow ( True )
  if 84 - 84: oO0o + II111iiii * II111iiii % o0oOOo0O0Ooo / iII111i + ooOoO0o
  dest = dest . print_address_no_iid ( )
  OoiiI11111II , iiIIIi11I1I = self . fragment ( )
  if 52 - 52: oO0o + Ii1I - I1ii11iIi11i * Ii1I . OOooOOo + I1Ii111
  for O0oo in OoiiI11111II :
   if ( len ( OoiiI11111II ) != 1 ) :
    self . packet = O0oo
    self . print_packet ( iiIIIi11I1I , True )
    if 43 - 43: I1IiiI % IiII % I1ii11iIi11i
    if 53 - 53: oO0o % OOooOOo % I1ii11iIi11i . I1Ii111 . I1Ii111 . iII111i
   try : lisp_raw_socket . sendto ( O0oo , ( dest , 0 ) )
   except socket . error , iIIi1iI1I1IIi :
    lprint ( "socket.sendto() failed: {}" . format ( iIIi1iI1I1IIi ) )
    if 73 - 73: iII111i / ooOoO0o + OoO0O00 / OoOoOO00 . II111iiii * Ii1I
    if 21 - 21: I1IiiI - I1IiiI + iII111i % I1IiiI * oO0o
    if 74 - 74: iII111i / I11i . I1IiiI - OoooooooOO + II111iiii + I11i
    if 36 - 36: Ii1I * I1IiiI * I1ii11iIi11i . I11i * I1ii11iIi11i
 def send_l2_packet ( self , l2_socket , mac_header ) :
  if ( l2_socket == None ) :
   lprint ( "No layer-2 socket, drop IPv6 packet" )
   return
   if 76 - 76: OOooOOo + O0 / IiII - OoO0O00
  if ( mac_header == None ) :
   lprint ( "Could not build MAC header, drop IPv6 packet" )
   return
   if 27 - 27: Oo0Ooo - iIii1I11I1II1 * iII111i * II111iiii * I1ii11iIi11i
   if 9 - 9: i11iIiiIii + OOooOOo - OoOoOO00 / ooOoO0o % i1IIi / oO0o
  IiiiIi1iiii11 = mac_header + self . packet
  if 22 - 22: i1IIi
  if 3 - 3: OoO0O00 * I1ii11iIi11i - iII111i + I1ii11iIi11i
  if 63 - 63: I11i * ooOoO0o % II111iiii % I1Ii111 + I1IiiI * Oo0Ooo
  if 96 - 96: IiII
  if 99 - 99: iIii1I11I1II1 - ooOoO0o
  if 79 - 79: I1IiiI + oO0o % I11i % oO0o
  if 56 - 56: I1ii11iIi11i + oO0o . OoO0O00 + OoooooooOO * I1ii11iIi11i - O0
  if 35 - 35: OOooOOo . I11i . I1Ii111 - I11i % I11i + I1Ii111
  if 99 - 99: o0oOOo0O0Ooo + OOooOOo
  if 34 - 34: I1Ii111 * o0oOOo0O0Ooo . I1IiiI % i11iIiiIii
  if 61 - 61: iIii1I11I1II1 + oO0o * I11i - i1IIi % oO0o
  l2_socket . write ( IiiiIi1iiii11 )
  return
  if 76 - 76: oO0o / OoOoOO00
  if 12 - 12: I1Ii111
 def bridge_l2_packet ( self , eid , db ) :
  try : OO0oOo = db . dynamic_eids [ eid . print_address_no_iid ( ) ]
  except : return
  try : II1i = lisp_myinterfaces [ OO0oOo . interface ]
  except : return
  try :
   socket = II1i . get_bridge_socket ( )
   if ( socket == None ) : return
  except : return
  if 36 - 36: OoOoOO00 * OoO0O00 / ooOoO0o / I1IiiI - Ii1I
  try : socket . send ( self . packet )
  except socket . error , iIIi1iI1I1IIi :
   lprint ( "bridge_l2_packet(): socket.send() failed: {}" . format ( iIIi1iI1I1IIi ) )
   if 53 - 53: oO0o
   if 99 - 99: Oo0Ooo
   if 17 - 17: i11iIiiIii - i11iIiiIii + I1ii11iIi11i * ooOoO0o * oO0o / OoooooooOO
 def is_lisp_packet ( self , packet ) :
  oOoO0OOO00O = ( struct . unpack ( "B" , packet [ 9 ] ) [ 0 ] == LISP_UDP_PROTOCOL )
  if ( oOoO0OOO00O == False ) : return ( False )
  if 22 - 22: I1Ii111 * I1ii11iIi11i - IiII
  Oo0o = struct . unpack ( "H" , packet [ 22 : 24 ] ) [ 0 ]
  if ( socket . ntohs ( Oo0o ) == LISP_DATA_PORT ) : return ( True )
  Oo0o = struct . unpack ( "H" , packet [ 20 : 22 ] ) [ 0 ]
  if ( socket . ntohs ( Oo0o ) == LISP_DATA_PORT ) : return ( True )
  return ( False )
  if 4 - 4: I1Ii111 * I1IiiI % I1IiiI / OoooooooOO
  if 52 - 52: oO0o + I1Ii111 * I1Ii111 * Oo0Ooo - iIii1I11I1II1 + I1ii11iIi11i
 def decode ( self , is_lisp_packet , lisp_ipc_socket , stats ) :
  self . packet_error = ""
  IiiiIi1iiii11 = self . packet
  i1iI = len ( IiiiIi1iiii11 )
  I1111iIIiIIII = oOo0O = True
  if 44 - 44: i11iIiiIii
  if 11 - 11: I1IiiI - Ii1I * OOooOOo % o0oOOo0O0Ooo
  if 5 - 5: I1ii11iIi11i / o0oOOo0O0Ooo * I11i - i11iIiiIii - OoooooooOO / ooOoO0o
  if 6 - 6: I11i * OoooooooOO - OOooOOo + O0 * I1Ii111
  OoI1 = 0
  IiIIi11i111 = 0
  if ( is_lisp_packet ) :
   IiIIi11i111 = self . lisp_header . get_instance_id ( )
   Iii11111I1iii = struct . unpack ( "B" , IiiiIi1iiii11 [ 0 : 1 ] ) [ 0 ]
   self . outer_version = Iii11111I1iii >> 4
   if ( self . outer_version == 4 ) :
    if 67 - 67: I1ii11iIi11i + oO0o * IiII / II111iiii % OoO0O00 % OoO0O00
    if 28 - 28: OoOoOO00 % oO0o - OOooOOo + OOooOOo + oO0o / iIii1I11I1II1
    if 91 - 91: I1IiiI / II111iiii * OOooOOo
    if 94 - 94: II111iiii - iIii1I11I1II1 - iIii1I11I1II1
    if 83 - 83: I1ii11iIi11i * iIii1I11I1II1 + OoOoOO00 * i1IIi . OoooooooOO % Ii1I
    oOoOo00oo = struct . unpack ( "H" , IiiiIi1iiii11 [ 10 : 12 ] ) [ 0 ]
    IiiiIi1iiii11 = lisp_ip_checksum ( IiiiIi1iiii11 )
    oO0oOoo0O = struct . unpack ( "H" , IiiiIi1iiii11 [ 10 : 12 ] ) [ 0 ]
    if ( oO0oOoo0O != 0 ) :
     if ( oOoOo00oo != 0 or lisp_is_macos ( ) == False ) :
      self . packet_error = "checksum-error"
      if ( stats ) :
       stats [ self . packet_error ] . increment ( i1iI )
       if 32 - 32: I1IiiI * I1Ii111 * i1IIi + oO0o
       if 40 - 40: II111iiii
      lprint ( "IPv4 header checksum failed for outer header" )
      if ( lisp_flow_logging ) : self . log_flow ( False )
      return ( None )
      if 7 - 7: OOooOOo / OoO0O00
      if 88 - 88: i1IIi
      if 53 - 53: ooOoO0o . OOooOOo . o0oOOo0O0Ooo + oO0o
    IiiiII = LISP_AFI_IPV4
    oO0ooOoO = 12
    self . outer_tos = struct . unpack ( "B" , IiiiIi1iiii11 [ 1 : 2 ] ) [ 0 ]
    self . outer_ttl = struct . unpack ( "B" , IiiiIi1iiii11 [ 8 : 9 ] ) [ 0 ]
    OoI1 = 20
   elif ( self . outer_version == 6 ) :
    IiiiII = LISP_AFI_IPV6
    oO0ooOoO = 8
    OoO = struct . unpack ( "H" , IiiiIi1iiii11 [ 0 : 2 ] ) [ 0 ]
    self . outer_tos = ( socket . ntohs ( OoO ) >> 4 ) & 0xff
    self . outer_ttl = struct . unpack ( "B" , IiiiIi1iiii11 [ 7 : 8 ] ) [ 0 ]
    OoI1 = 40
   else :
    self . packet_error = "outer-header-error"
    if ( stats ) : stats [ self . packet_error ] . increment ( i1iI )
    lprint ( "Cannot decode outer header" )
    return ( None )
    if 57 - 57: oO0o
    if 92 - 92: II111iiii - OoO0O00 - OOooOOo % I1IiiI - OoOoOO00 * I1Ii111
   self . outer_source . afi = IiiiII
   self . outer_dest . afi = IiiiII
   IiIi11 = self . outer_source . addr_length ( )
   if 89 - 89: iII111i . OoOoOO00 . I11i
   self . outer_source . unpack_address ( IiiiIi1iiii11 [ oO0ooOoO : oO0ooOoO + IiIi11 ] )
   oO0ooOoO += IiIi11
   self . outer_dest . unpack_address ( IiiiIi1iiii11 [ oO0ooOoO : oO0ooOoO + IiIi11 ] )
   IiiiIi1iiii11 = IiiiIi1iiii11 [ OoI1 : : ]
   self . outer_source . mask_len = self . outer_source . host_mask_len ( )
   self . outer_dest . mask_len = self . outer_dest . host_mask_len ( )
   if 55 - 55: iII111i + Oo0Ooo
   if 95 - 95: I11i + Oo0Ooo + Oo0Ooo
   if 33 - 33: i1IIi % OoooooooOO / OoooooooOO
   if 88 - 88: I1Ii111 - Ii1I - oO0o + i1IIi
   ii11IiiIi = struct . unpack ( "H" , IiiiIi1iiii11 [ 0 : 2 ] ) [ 0 ]
   self . udp_sport = socket . ntohs ( ii11IiiIi )
   ii11IiiIi = struct . unpack ( "H" , IiiiIi1iiii11 [ 2 : 4 ] ) [ 0 ]
   self . udp_dport = socket . ntohs ( ii11IiiIi )
   ii11IiiIi = struct . unpack ( "H" , IiiiIi1iiii11 [ 4 : 6 ] ) [ 0 ]
   self . udp_length = socket . ntohs ( ii11IiiIi )
   ii11IiiIi = struct . unpack ( "H" , IiiiIi1iiii11 [ 6 : 8 ] ) [ 0 ]
   self . udp_checksum = socket . ntohs ( ii11IiiIi )
   IiiiIi1iiii11 = IiiiIi1iiii11 [ 8 : : ]
   if 39 - 39: OoO0O00 / Oo0Ooo % II111iiii % I11i
   if 57 - 57: OoO0O00
   if 79 - 79: OoOoOO00 + IiII
   if 14 - 14: I1Ii111 / I11i - OOooOOo * O0 % IiII . O0
   I1111iIIiIIII = ( self . udp_dport == LISP_DATA_PORT or
 self . udp_sport == LISP_DATA_PORT )
   oOo0O = ( self . udp_dport in ( LISP_L2_DATA_PORT , LISP_VXLAN_DATA_PORT ) )
   if 86 - 86: i1IIi * OoooooooOO
   if 22 - 22: I1Ii111 + iII111i - I11i + iIii1I11I1II1 / I1Ii111 - OoooooooOO
   if 42 - 42: OoooooooOO - OoOoOO00 - OOooOOo * I1Ii111
   if 98 - 98: OoO0O00 . iIii1I11I1II1 % Oo0Ooo + OoooooooOO
   if ( self . lisp_header . decode ( IiiiIi1iiii11 ) == False ) :
    self . packet_error = "lisp-header-error"
    if ( stats ) : stats [ self . packet_error ] . increment ( i1iI )
    if 2 - 2: I1Ii111 % OoooooooOO - ooOoO0o * I1ii11iIi11i * IiII
    if ( lisp_flow_logging ) : self . log_flow ( False )
    lprint ( "Cannot decode LISP header" )
    return ( None )
    if 99 - 99: iIii1I11I1II1 . Oo0Ooo / ooOoO0o . OOooOOo % I1IiiI * I11i
   IiiiIi1iiii11 = IiiiIi1iiii11 [ 8 : : ]
   IiIIi11i111 = self . lisp_header . get_instance_id ( )
   OoI1 += 16
   if 95 - 95: oO0o
  if ( IiIIi11i111 == 0xffffff ) : IiIIi11i111 = 0
  if 80 - 80: IiII
  if 42 - 42: OoooooooOO * II111iiii
  if 53 - 53: I1Ii111 + i1IIi . OoO0O00 / i11iIiiIii + Ii1I % OoOoOO00
  if 9 - 9: ooOoO0o . I11i - Oo0Ooo . I1Ii111
  i1I111II11 = False
  o00oO = self . lisp_header . k_bits
  if ( o00oO ) :
   oo0o00OO = lisp_get_crypto_decap_lookup_key ( self . outer_source ,
 self . udp_sport )
   if ( oo0o00OO == None ) :
    self . packet_error = "no-decrypt-key"
    if ( stats ) : stats [ self . packet_error ] . increment ( i1iI )
    if 32 - 32: iII111i . iIii1I11I1II1 % Oo0Ooo . OoooooooOO
    self . print_packet ( "Receive" , is_lisp_packet )
    Ooo00OoO0O00 = bold ( "No key available" , False )
    dprint ( "{} for key-id {} to decrypt packet" . format ( Ooo00OoO0O00 , o00oO ) )
    if ( lisp_flow_logging ) : self . log_flow ( False )
    return ( None )
    if 11 - 11: I11i
    if 20 - 20: O0 . i11iIiiIii * i1IIi % O0 . I1IiiI
   o0Oo = lisp_crypto_keys_by_rloc_decap [ oo0o00OO ] [ o00oO ]
   if ( o0Oo == None ) :
    self . packet_error = "no-decrypt-key"
    if ( stats ) : stats [ self . packet_error ] . increment ( i1iI )
    if 29 - 29: O0 * i11iIiiIii / OoooooooOO / o0oOOo0O0Ooo . ooOoO0o
    self . print_packet ( "Receive" , is_lisp_packet )
    Ooo00OoO0O00 = bold ( "No key available" , False )
    dprint ( "{} to decrypt packet from RLOC {}" . format ( Ooo00OoO0O00 ,
 red ( oo0o00OO , False ) ) )
    if ( lisp_flow_logging ) : self . log_flow ( False )
    return ( None )
    if 70 - 70: OoooooooOO . ooOoO0o / oO0o . oO0o - o0oOOo0O0Ooo
    if 29 - 29: I11i % OOooOOo - ooOoO0o
    if 26 - 26: O0 . I11i + iII111i - Ii1I . I11i
    if 2 - 2: I1ii11iIi11i . Oo0Ooo * OOooOOo % II111iiii . iII111i
    if 46 - 46: OoOoOO00 + I1IiiI % OoooooooOO * i11iIiiIii - Oo0Ooo
   o0Oo . use_count += 1
   IiiiIi1iiii11 , i1I111II11 = self . decrypt ( IiiiIi1iiii11 , OoI1 , o0Oo ,
 oo0o00OO )
   if ( i1I111II11 == False ) :
    if ( stats ) : stats [ self . packet_error ] . increment ( i1iI )
    if ( lisp_flow_logging ) : self . log_flow ( False )
    return ( None )
    if 47 - 47: iII111i * OoOoOO00 * IiII
    if 46 - 46: Ii1I
    if 42 - 42: iIii1I11I1II1
    if 32 - 32: Oo0Ooo - Ii1I . OoooooooOO - OoooooooOO - Oo0Ooo . iIii1I11I1II1
    if 34 - 34: Oo0Ooo
    if 31 - 31: i1IIi - I11i + I1Ii111 + ooOoO0o . ooOoO0o . O0
  Iii11111I1iii = struct . unpack ( "B" , IiiiIi1iiii11 [ 0 : 1 ] ) [ 0 ]
  self . inner_version = Iii11111I1iii >> 4
  if ( I1111iIIiIIII and self . inner_version == 4 and Iii11111I1iii >= 0x45 ) :
   ii11I = socket . ntohs ( struct . unpack ( "H" , IiiiIi1iiii11 [ 2 : 4 ] ) [ 0 ] )
   self . inner_tos = struct . unpack ( "B" , IiiiIi1iiii11 [ 1 : 2 ] ) [ 0 ]
   self . inner_ttl = struct . unpack ( "B" , IiiiIi1iiii11 [ 8 : 9 ] ) [ 0 ]
   self . inner_protocol = struct . unpack ( "B" , IiiiIi1iiii11 [ 9 : 10 ] ) [ 0 ]
   self . inner_source . afi = LISP_AFI_IPV4
   self . inner_dest . afi = LISP_AFI_IPV4
   self . inner_source . unpack_address ( IiiiIi1iiii11 [ 12 : 16 ] )
   self . inner_dest . unpack_address ( IiiiIi1iiii11 [ 16 : 20 ] )
   IIII1I1 = socket . ntohs ( struct . unpack ( "H" , IiiiIi1iiii11 [ 6 : 8 ] ) [ 0 ] )
   self . inner_is_fragment = ( IIII1I1 & 0x2000 or IIII1I1 != 0 )
   if ( self . inner_protocol == LISP_UDP_PROTOCOL ) :
    self . inner_sport = struct . unpack ( "H" , IiiiIi1iiii11 [ 20 : 22 ] ) [ 0 ]
    self . inner_sport = socket . ntohs ( self . inner_sport )
    self . inner_dport = struct . unpack ( "H" , IiiiIi1iiii11 [ 22 : 24 ] ) [ 0 ]
    self . inner_dport = socket . ntohs ( self . inner_dport )
    if 2 - 2: oO0o . OOooOOo
  elif ( I1111iIIiIIII and self . inner_version == 6 and Iii11111I1iii >= 0x60 ) :
   ii11I = socket . ntohs ( struct . unpack ( "H" , IiiiIi1iiii11 [ 4 : 6 ] ) [ 0 ] ) + 40
   OoO = struct . unpack ( "H" , IiiiIi1iiii11 [ 0 : 2 ] ) [ 0 ]
   self . inner_tos = ( socket . ntohs ( OoO ) >> 4 ) & 0xff
   self . inner_ttl = struct . unpack ( "B" , IiiiIi1iiii11 [ 7 : 8 ] ) [ 0 ]
   self . inner_protocol = struct . unpack ( "B" , IiiiIi1iiii11 [ 6 : 7 ] ) [ 0 ]
   self . inner_source . afi = LISP_AFI_IPV6
   self . inner_dest . afi = LISP_AFI_IPV6
   self . inner_source . unpack_address ( IiiiIi1iiii11 [ 8 : 24 ] )
   self . inner_dest . unpack_address ( IiiiIi1iiii11 [ 24 : 40 ] )
   if ( self . inner_protocol == LISP_UDP_PROTOCOL ) :
    self . inner_sport = struct . unpack ( "H" , IiiiIi1iiii11 [ 40 : 42 ] ) [ 0 ]
    self . inner_sport = socket . ntohs ( self . inner_sport )
    self . inner_dport = struct . unpack ( "H" , IiiiIi1iiii11 [ 42 : 44 ] ) [ 0 ]
    self . inner_dport = socket . ntohs ( self . inner_dport )
    if 43 - 43: iIii1I11I1II1
  elif ( oOo0O ) :
   ii11I = len ( IiiiIi1iiii11 )
   self . inner_tos = 0
   self . inner_ttl = 0
   self . inner_protocol = 0
   self . inner_source . afi = LISP_AFI_MAC
   self . inner_dest . afi = LISP_AFI_MAC
   self . inner_dest . unpack_address ( self . swap_mac ( IiiiIi1iiii11 [ 0 : 6 ] ) )
   self . inner_source . unpack_address ( self . swap_mac ( IiiiIi1iiii11 [ 6 : 12 ] ) )
  elif ( self . lisp_header . get_instance_id ( ) == 0xffffff ) :
   if ( lisp_flow_logging ) : self . log_flow ( False )
   return ( self )
  else :
   self . packet_error = "bad-inner-version"
   if ( stats ) : stats [ self . packet_error ] . increment ( i1iI )
   if 29 - 29: IiII % ooOoO0o + OoO0O00 . i1IIi + I1IiiI
   lprint ( "Cannot decode encapsulation, header version {}" . format ( hex ( Iii11111I1iii ) ) )
   if 24 - 24: I1Ii111 / Ii1I * I1ii11iIi11i - OoooooooOO / I1IiiI . oO0o
   IiiiIi1iiii11 = lisp_format_packet ( IiiiIi1iiii11 [ 0 : 20 ] )
   lprint ( "Packet header: {}" . format ( IiiiIi1iiii11 ) )
   if ( lisp_flow_logging and is_lisp_packet ) : self . log_flow ( False )
   return ( None )
   if 98 - 98: i1IIi - iII111i
  self . inner_source . mask_len = self . inner_source . host_mask_len ( )
  self . inner_dest . mask_len = self . inner_dest . host_mask_len ( )
  self . inner_source . instance_id = IiIIi11i111
  self . inner_dest . instance_id = IiIIi11i111
  if 49 - 49: o0oOOo0O0Ooo . Ii1I . oO0o
  if 9 - 9: IiII - II111iiii * OoO0O00
  if 78 - 78: iIii1I11I1II1 / O0 * oO0o / iII111i / OoOoOO00
  if 15 - 15: ooOoO0o / oO0o
  if 54 - 54: ooOoO0o - iIii1I11I1II1 - I11i % Ii1I / II111iiii
  if ( lisp_nonce_echoing and is_lisp_packet ) :
   oooooO0oO0o = lisp_get_echo_nonce ( self . outer_source , None )
   if ( oooooO0oO0o == None ) :
    O0ooo0Ooo = self . outer_source . print_address_no_iid ( )
    oooooO0oO0o = lisp_echo_nonce ( O0ooo0Ooo )
    if 96 - 96: IiII
   o0OOO = self . lisp_header . get_nonce ( )
   if ( self . lisp_header . is_e_bit_set ( ) ) :
    oooooO0oO0o . receive_request ( lisp_ipc_socket , o0OOO )
   elif ( oooooO0oO0o . request_nonce_sent ) :
    oooooO0oO0o . receive_echo ( lisp_ipc_socket , o0OOO )
    if 40 - 40: i11iIiiIii * II111iiii
    if 57 - 57: O0 * iIii1I11I1II1 % O0 . OoooooooOO
    if 53 - 53: Ii1I / I1IiiI * Ii1I + o0oOOo0O0Ooo + oO0o - Oo0Ooo
    if 16 - 16: OoO0O00 % I1Ii111 . i1IIi / I1ii11iIi11i - O0
    if 85 - 85: i1IIi . i1IIi
    if 16 - 16: I1IiiI - OOooOOo % Ii1I . OOooOOo + I1ii11iIi11i % i11iIiiIii
    if 59 - 59: i11iIiiIii - I11i
  if ( i1I111II11 ) : self . packet += IiiiIi1iiii11 [ : ii11I ]
  if 59 - 59: OoooooooOO * o0oOOo0O0Ooo / I1Ii111
  if 75 - 75: o0oOOo0O0Ooo - OoooooooOO
  if 21 - 21: I1IiiI + iIii1I11I1II1 / i11iIiiIii / oO0o
  if 66 - 66: OoooooooOO + iII111i . IiII % i1IIi
  if ( lisp_flow_logging and is_lisp_packet ) : self . log_flow ( False )
  return ( self )
  if 58 - 58: OOooOOo % iII111i * O0 + I1ii11iIi11i - IiII
  if 26 - 26: i1IIi / I1IiiI / I11i + I11i
 def swap_mac ( self , mac ) :
  return ( mac [ 1 ] + mac [ 0 ] + mac [ 3 ] + mac [ 2 ] + mac [ 5 ] + mac [ 4 ] )
  if 46 - 46: I1Ii111 % I1ii11iIi11i + Ii1I
  if 67 - 67: iIii1I11I1II1 . i11iIiiIii . i11iIiiIii . i11iIiiIii / I11i + ooOoO0o
 def strip_outer_headers ( self ) :
  oO0ooOoO = 16
  oO0ooOoO += 20 if ( self . outer_version == 4 ) else 40
  self . packet = self . packet [ oO0ooOoO : : ]
  return ( self )
  if 10 - 10: ooOoO0o - Oo0Ooo % II111iiii
  if 66 - 66: iIii1I11I1II1 . iIii1I11I1II1
 def hash_ports ( self ) :
  IiiiIi1iiii11 = self . packet
  Iii11111I1iii = self . inner_version
  I1iI1111ii1I1 = 0
  if ( Iii11111I1iii == 4 ) :
   oO = struct . unpack ( "B" , IiiiIi1iiii11 [ 9 ] ) [ 0 ]
   if ( self . inner_is_fragment ) : return ( oO )
   if ( oO in [ 6 , 17 ] ) :
    I1iI1111ii1I1 = oO
    I1iI1111ii1I1 += struct . unpack ( "I" , IiiiIi1iiii11 [ 20 : 24 ] ) [ 0 ]
    I1iI1111ii1I1 = ( I1iI1111ii1I1 >> 16 ) ^ ( I1iI1111ii1I1 & 0xffff )
    if 7 - 7: Oo0Ooo / i11iIiiIii + OoOoOO00 + i11iIiiIii / IiII
    if 66 - 66: I11i * i1IIi % OOooOOo / OoooooooOO * iII111i % ooOoO0o
  if ( Iii11111I1iii == 6 ) :
   oO = struct . unpack ( "B" , IiiiIi1iiii11 [ 6 ] ) [ 0 ]
   if ( oO in [ 6 , 17 ] ) :
    I1iI1111ii1I1 = oO
    I1iI1111ii1I1 += struct . unpack ( "I" , IiiiIi1iiii11 [ 40 : 44 ] ) [ 0 ]
    I1iI1111ii1I1 = ( I1iI1111ii1I1 >> 16 ) ^ ( I1iI1111ii1I1 & 0xffff )
    if 5 - 5: I1ii11iIi11i * Ii1I % I11i % II111iiii
    if 9 - 9: o0oOOo0O0Ooo % I1Ii111 + I11i
  return ( I1iI1111ii1I1 )
  if 55 - 55: OoO0O00 - I1ii11iIi11i
  if 38 - 38: iIii1I11I1II1 % IiII % OoO0O00 % O0 * iIii1I11I1II1 / I1Ii111
 def hash_packet ( self ) :
  I1iI1111ii1I1 = self . inner_source . address ^ self . inner_dest . address
  I1iI1111ii1I1 += self . hash_ports ( )
  if ( self . inner_version == 4 ) :
   I1iI1111ii1I1 = ( I1iI1111ii1I1 >> 16 ) ^ ( I1iI1111ii1I1 & 0xffff )
  elif ( self . inner_version == 6 ) :
   I1iI1111ii1I1 = ( I1iI1111ii1I1 >> 64 ) ^ ( I1iI1111ii1I1 & 0xffffffffffffffff )
   I1iI1111ii1I1 = ( I1iI1111ii1I1 >> 32 ) ^ ( I1iI1111ii1I1 & 0xffffffff )
   I1iI1111ii1I1 = ( I1iI1111ii1I1 >> 16 ) ^ ( I1iI1111ii1I1 & 0xffff )
   if 65 - 65: OOooOOo - I1IiiI * I1Ii111
  self . udp_sport = 0xf000 | ( I1iI1111ii1I1 & 0xfff )
  if 99 - 99: I1IiiI
  if 64 - 64: I1ii11iIi11i * Ii1I * Oo0Ooo % IiII % ooOoO0o
 def print_packet ( self , s_or_r , is_lisp_packet ) :
  if ( is_lisp_packet == False ) :
   OoO0000O = "{} -> {}" . format ( self . inner_source . print_address ( ) ,
 self . inner_dest . print_address ( ) )
   dprint ( ( "{} {}, tos/ttl: {}/{}, length: {}, packet: {} ..." ) . format ( bold ( s_or_r , False ) ,
   # Oo0Ooo * I1Ii111
 green ( OoO0000O , False ) , self . inner_tos ,
 self . inner_ttl , len ( self . packet ) ,
 lisp_format_packet ( self . packet [ 0 : 60 ] ) ) )
   return
   if 53 - 53: Oo0Ooo / Ii1I + oO0o . iII111i + IiII
   if 19 - 19: Ii1I
  if ( s_or_r . find ( "Receive" ) != - 1 ) :
   oo0 = "decap"
   oo0 += "-vxlan" if self . udp_dport == LISP_VXLAN_DATA_PORT else ""
  else :
   oo0 = s_or_r
   if ( oo0 in [ "Send" , "Replicate" ] or oo0 . find ( "Fragment" ) != - 1 ) :
    oo0 = "encap"
    if 25 - 25: o0oOOo0O0Ooo % iII111i . i11iIiiIii
    if 4 - 4: OoooooooOO
  o0OOOooOOOO = "{} -> {}" . format ( self . outer_source . print_address_no_iid ( ) ,
 self . outer_dest . print_address_no_iid ( ) )
  if 5 - 5: I1IiiI . I11i . IiII
  if 39 - 39: OOooOOo . Oo0Ooo - OoOoOO00 * i11iIiiIii
  if 4 - 4: OoOoOO00 * O0 - I11i
  if 72 - 72: I11i + ooOoO0o / I1IiiI . IiII % OoO0O00 / i11iIiiIii
  if 13 - 13: I1Ii111 % o0oOOo0O0Ooo + OOooOOo + I1Ii111 + i11iIiiIii - I1ii11iIi11i
  if ( self . lisp_header . get_instance_id ( ) == 0xffffff ) :
   oOOo0ooO0 = ( "{} LISP packet, outer RLOCs: {}, outer tos/ttl: " + "{}/{}, outer UDP: {} -> {}, " )
   if 70 - 70: II111iiii * II111iiii . I1IiiI
   oOOo0ooO0 += bold ( "control-packet" , False ) + ": {} ..."
   if 11 - 11: iII111i
   dprint ( oOOo0ooO0 . format ( bold ( s_or_r , False ) , red ( o0OOOooOOOO , False ) ,
 self . outer_tos , self . outer_ttl , self . udp_sport ,
 self . udp_dport , lisp_format_packet ( self . packet [ 0 : 56 ] ) ) )
   return
  else :
   oOOo0ooO0 = ( "{} LISP packet, outer RLOCs: {}, outer tos/ttl: " + "{}/{}, outer UDP: {} -> {}, inner EIDs: {}, " + "inner tos/ttl: {}/{}, length: {}, {}, packet: {} ..." )
   if 20 - 20: Ii1I . I1Ii111 % Ii1I
   if 5 - 5: OOooOOo + iII111i
   if 23 - 23: I1Ii111 % iIii1I11I1II1 . I11i
   if 95 - 95: Oo0Ooo + i11iIiiIii % OOooOOo - oO0o
  if ( self . lisp_header . k_bits ) :
   if ( oo0 == "encap" ) : oo0 = "encrypt/encap"
   if ( oo0 == "decap" ) : oo0 = "decap/decrypt"
   if 11 - 11: I1ii11iIi11i / O0 + II111iiii
   if 95 - 95: I1Ii111 + IiII * iIii1I11I1II1
  OoO0000O = "{} -> {}" . format ( self . inner_source . print_address ( ) ,
 self . inner_dest . print_address ( ) )
  if 17 - 17: OoO0O00 - Oo0Ooo * O0 / Ii1I
  dprint ( oOOo0ooO0 . format ( bold ( s_or_r , False ) , red ( o0OOOooOOOO , False ) ,
 self . outer_tos , self . outer_ttl , self . udp_sport , self . udp_dport ,
 green ( OoO0000O , False ) , self . inner_tos , self . inner_ttl ,
 len ( self . packet ) , self . lisp_header . print_header ( oo0 ) ,
 lisp_format_packet ( self . packet [ 0 : 56 ] ) ) )
  if 19 - 19: i1IIi - iIii1I11I1II1 . I11i
  if 2 - 2: Ii1I
 def print_eid_tuple ( self ) :
  return ( lisp_print_eid_tuple ( self . inner_source , self . inner_dest ) )
  if 12 - 12: i11iIiiIii - iIii1I11I1II1 * IiII * iII111i
  if 19 - 19: O0 + oO0o + o0oOOo0O0Ooo
 def get_raw_socket ( self ) :
  IiIIi11i111 = str ( self . lisp_header . get_instance_id ( ) )
  if ( IiIIi11i111 == "0" ) : return ( None )
  if ( lisp_iid_to_interface . has_key ( IiIIi11i111 ) == False ) : return ( None )
  if 81 - 81: iIii1I11I1II1
  II1i = lisp_iid_to_interface [ IiIIi11i111 ]
  OO0o0OO0 = II1i . get_socket ( )
  if ( OO0o0OO0 == None ) :
   O0ooo = bold ( "SO_BINDTODEVICE" , False )
   OO = ( os . getenv ( "LISP_ENFORCE_BINDTODEVICE" ) != None )
   lprint ( "{} required for multi-tenancy support, {} packet" . format ( O0ooo , "drop" if OO else "forward" ) )
   if 99 - 99: Ii1I / Oo0Ooo * II111iiii / O0
   if ( OO ) : return ( None )
   if 44 - 44: i11iIiiIii % I1Ii111 % oO0o + I11i * oO0o . Ii1I
   if 89 - 89: OoooooooOO % II111iiii - OoO0O00 % i11iIiiIii
  IiIIi11i111 = bold ( IiIIi11i111 , False )
  o0 = bold ( II1i . device , False )
  dprint ( "Send packet on instance-id {} interface {}" . format ( IiIIi11i111 , o0 ) )
  return ( OO0o0OO0 )
  if 7 - 7: IiII
  if 15 - 15: Oo0Ooo + iII111i + I1IiiI * o0oOOo0O0Ooo
 def log_flow ( self , encap ) :
  global lisp_flow_log
  if 33 - 33: o0oOOo0O0Ooo * Oo0Ooo
  O0OOOOoOOO = os . path . exists ( "./log-flows" )
  if ( len ( lisp_flow_log ) == LISP_FLOW_LOG_SIZE or O0OOOOoOOO ) :
   oooOo = [ lisp_flow_log ]
   lisp_flow_log = [ ]
   threading . Thread ( target = lisp_write_flow_log , args = oooOo ) . start ( )
   if ( O0OOOOoOOO ) : os . system ( "rm ./log-flows" )
   return
   if 91 - 91: I1IiiI - iII111i / OoO0O00 - OoO0O00 / Ii1I - IiII
   if 14 - 14: OOooOOo / o0oOOo0O0Ooo + Ii1I / OoooooooOO - I11i
  i1 = datetime . datetime . now ( )
  lisp_flow_log . append ( [ i1 , encap , self . packet , self ] )
  if 88 - 88: Ii1I / OoooooooOO % OoOoOO00 - i1IIi
  if 49 - 49: o0oOOo0O0Ooo - iIii1I11I1II1
 def print_flow ( self , ts , encap , packet ) :
  ts = ts . strftime ( "%m/%d/%y %H:%M:%S.%f" ) [ : - 3 ]
  o00oo00O0OoOo = "{}: {}" . format ( ts , "encap" if encap else "decap" )
  if 6 - 6: I1ii11iIi11i * Oo0Ooo + iIii1I11I1II1
  ii1iIi111i1 = red ( self . outer_source . print_address_no_iid ( ) , False )
  oOoOoO = red ( self . outer_dest . print_address_no_iid ( ) , False )
  o0oOoo00 = green ( self . inner_source . print_address ( ) , False )
  Ii11iIi1iIiii = green ( self . inner_dest . print_address ( ) , False )
  if 11 - 11: I1ii11iIi11i / I1ii11iIi11i
  if ( self . lisp_header . get_instance_id ( ) == 0xffffff ) :
   o00oo00O0OoOo += " {}:{} -> {}:{}, LISP control message type {}\n"
   o00oo00O0OoOo = o00oo00O0OoOo . format ( ii1iIi111i1 , self . udp_sport , oOoOoO , self . udp_dport ,
 self . inner_version )
   return ( o00oo00O0OoOo )
   if 39 - 39: O0 . I11i
   if 45 - 45: oO0o + o0oOOo0O0Ooo + IiII / Ii1I + o0oOOo0O0Ooo
  if ( self . outer_dest . is_null ( ) == False ) :
   o00oo00O0OoOo += " {}:{} -> {}:{}, len/tos/ttl {}/{}/{}"
   o00oo00O0OoOo = o00oo00O0OoOo . format ( ii1iIi111i1 , self . udp_sport , oOoOoO , self . udp_dport ,
 len ( packet ) , self . outer_tos , self . outer_ttl )
   if 33 - 33: iII111i - Oo0Ooo - I11i
   if 61 - 61: Ii1I + I1IiiI / i1IIi + i1IIi / oO0o
   if 47 - 47: I1Ii111
   if 25 - 25: iII111i + I1IiiI + OoOoOO00 + I1Ii111 % O0
   if 26 - 26: ooOoO0o + OoOoOO00
  if ( self . lisp_header . k_bits != 0 ) :
   II111I1i1 = "\n"
   if ( self . packet_error != "" ) :
    II111I1i1 = " ({})" . format ( self . packet_error ) + II111I1i1
    if 10 - 10: O0 . OoOoOO00 * IiII / I1Ii111 / i1IIi
   o00oo00O0OoOo += ", encrypted" + II111I1i1
   return ( o00oo00O0OoOo )
   if 32 - 32: O0 / OOooOOo . ooOoO0o % I1Ii111
   if 18 - 18: IiII * iII111i / I11i / O0
   if 11 - 11: iIii1I11I1II1 / Ii1I + OoooooooOO % i1IIi * i11iIiiIii
   if 86 - 86: i11iIiiIii - O0 - i11iIiiIii . iIii1I11I1II1 . IiII
   if 84 - 84: i1IIi / iIii1I11I1II1 / oO0o / Ii1I
  if ( self . outer_dest . is_null ( ) == False ) :
   packet = packet [ 36 : : ] if self . outer_version == 4 else packet [ 56 : : ]
   if 7 - 7: OoOoOO00 . OOooOOo % Oo0Ooo
   if 55 - 55: ooOoO0o - Oo0Ooo * oO0o
  oO = packet [ 9 ] if self . inner_version == 4 else packet [ 6 ]
  oO = struct . unpack ( "B" , oO ) [ 0 ]
  if 72 - 72: o0oOOo0O0Ooo % o0oOOo0O0Ooo + iII111i + I1ii11iIi11i / Oo0Ooo
  o00oo00O0OoOo += " {} -> {}, len/tos/ttl/prot {}/{}/{}/{}"
  o00oo00O0OoOo = o00oo00O0OoOo . format ( o0oOoo00 , Ii11iIi1iIiii , len ( packet ) , self . inner_tos ,
 self . inner_ttl , oO )
  if 30 - 30: Oo0Ooo + I1IiiI + i11iIiiIii / OoO0O00
  if 64 - 64: IiII
  if 80 - 80: I1IiiI - i11iIiiIii / OoO0O00 / OoOoOO00 + OoOoOO00
  if 89 - 89: O0 + IiII * I1Ii111
  if ( oO in [ 6 , 17 ] ) :
   iIIIIII = packet [ 20 : 24 ] if self . inner_version == 4 else packet [ 40 : 44 ]
   if ( len ( iIIIIII ) == 4 ) :
    iIIIIII = socket . ntohl ( struct . unpack ( "I" , iIIIIII ) [ 0 ] )
    o00oo00O0OoOo += ", ports {} -> {}" . format ( iIIIIII >> 16 , iIIIIII & 0xffff )
    if 48 - 48: OoOoOO00 * OoooooooOO + OoooooooOO * iIii1I11I1II1 * II111iiii % i11iIiiIii
  elif ( oO == 1 ) :
   II = packet [ 26 : 28 ] if self . inner_version == 4 else packet [ 46 : 48 ]
   if ( len ( II ) == 2 ) :
    II = socket . ntohs ( struct . unpack ( "H" , II ) [ 0 ] )
    o00oo00O0OoOo += ", icmp-seq {}" . format ( II )
    if 80 - 80: II111iiii - o0oOOo0O0Ooo . iIii1I11I1II1
    if 44 - 44: i11iIiiIii % I11i % I1ii11iIi11i
  if ( self . packet_error != "" ) :
   o00oo00O0OoOo += " ({})" . format ( self . packet_error )
   if 7 - 7: Oo0Ooo * OoO0O00 - II111iiii % I1Ii111 . Oo0Ooo . Oo0Ooo
  o00oo00O0OoOo += "\n"
  return ( o00oo00O0OoOo )
  if 5 - 5: OoooooooOO * I1ii11iIi11i
  if 42 - 42: o0oOOo0O0Ooo . I1Ii111 / O0 . II111iiii * OoOoOO00
 def is_trace ( self ) :
  iIIIIII = [ self . inner_sport , self . inner_dport ]
  return ( self . inner_protocol == LISP_UDP_PROTOCOL and
 LISP_TRACE_PORT in iIIIIII )
  if 7 - 7: I1Ii111 * O0 + OoOoOO00
  if 90 - 90: IiII * II111iiii * IiII - iII111i
  if 34 - 34: OOooOOo - I1ii11iIi11i * iII111i % Ii1I
  if 25 - 25: II111iiii + I1IiiI * ooOoO0o * I1ii11iIi11i . iII111i
  if 26 - 26: iII111i - ooOoO0o / OoooooooOO + o0oOOo0O0Ooo . Oo0Ooo
  if 75 - 75: O0 / OoOoOO00 . I1Ii111
  if 7 - 7: OoO0O00 * iII111i
  if 16 - 16: I1Ii111 . i1IIi . IiII
  if 50 - 50: OoO0O00 - II111iiii * OoooooooOO - I1IiiI . O0 + O0
  if 80 - 80: o0oOOo0O0Ooo
  if 50 - 50: ooOoO0o
  if 81 - 81: i11iIiiIii * iIii1I11I1II1 / Oo0Ooo * OOooOOo
  if 83 - 83: i11iIiiIii - I1IiiI * i11iIiiIii
  if 59 - 59: iII111i - OoooooooOO / ooOoO0o + I1ii11iIi11i . o0oOOo0O0Ooo - iII111i
  if 29 - 29: oO0o
  if 26 - 26: O0 % OOooOOo - IiII . OOooOOo
LISP_N_BIT = 0x80000000
LISP_L_BIT = 0x40000000
LISP_E_BIT = 0x20000000
LISP_V_BIT = 0x10000000
LISP_I_BIT = 0x08000000
LISP_P_BIT = 0x04000000
LISP_K_BITS = 0x03000000
if 70 - 70: o0oOOo0O0Ooo + I11i / iII111i + ooOoO0o / I1IiiI
class lisp_data_header ( ) :
 def __init__ ( self ) :
  self . first_long = 0
  self . second_long = 0
  self . k_bits = 0
  if 33 - 33: OoooooooOO . O0
  if 59 - 59: iIii1I11I1II1
 def print_header ( self , e_or_d ) :
  i1OOoO0OO0oO = lisp_hex_string ( self . first_long & 0xffffff )
  iii1 = lisp_hex_string ( self . second_long ) . zfill ( 8 )
  if 26 - 26: OOooOOo + Oo0Ooo
  oOOo0ooO0 = ( "{} LISP-header -> flags: {}{}{}{}{}{}{}{}, nonce: {}, " + "iid/lsb: {}" )
  if 71 - 71: I1IiiI . ooOoO0o
  return ( oOOo0ooO0 . format ( bold ( e_or_d , False ) ,
 "N" if ( self . first_long & LISP_N_BIT ) else "n" ,
 "L" if ( self . first_long & LISP_L_BIT ) else "l" ,
 "E" if ( self . first_long & LISP_E_BIT ) else "e" ,
 "V" if ( self . first_long & LISP_V_BIT ) else "v" ,
 "I" if ( self . first_long & LISP_I_BIT ) else "i" ,
 "P" if ( self . first_long & LISP_P_BIT ) else "p" ,
 "K" if ( self . k_bits in [ 2 , 3 ] ) else "k" ,
 "K" if ( self . k_bits in [ 1 , 3 ] ) else "k" ,
 i1OOoO0OO0oO , iii1 ) )
  if 43 - 43: I1ii11iIi11i * OOooOOo
  if 1 - 1: OoO0O00 * ooOoO0o + IiII . oO0o / ooOoO0o
 def encode ( self ) :
  O0O00Oo = "II"
  i1OOoO0OO0oO = socket . htonl ( self . first_long )
  iii1 = socket . htonl ( self . second_long )
  if 49 - 49: i1IIi - OOooOOo / o0oOOo0O0Ooo % IiII - ooOoO0o
  O00O0OO = struct . pack ( O0O00Oo , i1OOoO0OO0oO , iii1 )
  return ( O00O0OO )
  if 76 - 76: I1IiiI
  if 41 - 41: OoOoOO00 % I1Ii111 * oO0o * i1IIi
 def decode ( self , packet ) :
  O0O00Oo = "II"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( False )
  if 27 - 27: ooOoO0o . Oo0Ooo + ooOoO0o + iII111i
  i1OOoO0OO0oO , iii1 = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  if 28 - 28: OoO0O00 - ooOoO0o - oO0o % oO0o / O0
  if 99 - 99: II111iiii - iIii1I11I1II1
  self . first_long = socket . ntohl ( i1OOoO0OO0oO )
  self . second_long = socket . ntohl ( iii1 )
  self . k_bits = ( self . first_long & LISP_K_BITS ) >> 24
  return ( True )
  if 24 - 24: I1IiiI - i1IIi - O0 % I1Ii111 - iIii1I11I1II1 . I11i
  if 26 - 26: OoO0O00 % i1IIi * O0 . I1Ii111
 def key_id ( self , key_id ) :
  self . first_long &= ~ ( 0x3 << 24 )
  self . first_long |= ( ( key_id & 0x3 ) << 24 )
  self . k_bits = key_id
  if 31 - 31: O0 - IiII * i11iIiiIii * i1IIi
  if 78 - 78: ooOoO0o * OoOoOO00 . Ii1I . OoOoOO00 % iIii1I11I1II1
 def nonce ( self , nonce ) :
  self . first_long |= LISP_N_BIT
  self . first_long |= nonce
  if 67 - 67: Ii1I . Oo0Ooo
  if 39 - 39: I11i * I1Ii111
 def map_version ( self , version ) :
  self . first_long |= LISP_V_BIT
  self . first_long |= version
  if 63 - 63: ooOoO0o % I1IiiI . OOooOOo - ooOoO0o / Oo0Ooo % I1IiiI
  if 39 - 39: o0oOOo0O0Ooo . i1IIi % oO0o / I11i % O0
 def instance_id ( self , iid ) :
  if ( iid == 0 ) : return
  self . first_long |= LISP_I_BIT
  self . second_long &= 0xff
  self . second_long |= ( iid << 8 )
  if 100 - 100: I1Ii111 - OoOoOO00
  if 78 - 78: OoooooooOO - OoOoOO00 . i11iIiiIii
 def get_instance_id ( self ) :
  return ( ( self . second_long >> 8 ) & 0xffffff )
  if 36 - 36: oO0o * iII111i + IiII * iII111i . I1ii11iIi11i - iIii1I11I1II1
  if 14 - 14: I11i * oO0o + i11iIiiIii
 def locator_status_bits ( self , lsbs ) :
  self . first_long |= LISP_L_BIT
  self . second_long &= 0xffffff00
  self . second_long |= ( lsbs & 0xff )
  if 84 - 84: iII111i / II111iiii
  if 86 - 86: I1IiiI
 def is_request_nonce ( self , nonce ) :
  return ( nonce & 0x80000000 )
  if 97 - 97: II111iiii
  if 38 - 38: I1IiiI
 def request_nonce ( self , nonce ) :
  self . first_long |= LISP_E_BIT
  self . first_long |= LISP_N_BIT
  self . first_long |= ( nonce & 0xffffff )
  if 42 - 42: o0oOOo0O0Ooo
  if 8 - 8: i11iIiiIii / ooOoO0o
 def is_e_bit_set ( self ) :
  return ( self . first_long & LISP_E_BIT )
  if 33 - 33: I1Ii111 * IiII - O0 + I1IiiI / IiII
  if 19 - 19: i1IIi % II111iiii
 def get_nonce ( self ) :
  return ( self . first_long & 0xffffff )
  if 85 - 85: IiII - o0oOOo0O0Ooo % OOooOOo - II111iiii
  if 56 - 56: Ii1I * i11iIiiIii
  if 92 - 92: II111iiii - O0 . I1Ii111
class lisp_echo_nonce ( ) :
 def __init__ ( self , rloc_str ) :
  self . rloc_str = rloc_str
  self . rloc = lisp_address ( LISP_AFI_NONE , rloc_str , 0 , 0 )
  self . request_nonce_sent = None
  self . echo_nonce_sent = None
  self . last_request_nonce_sent = None
  self . last_new_request_nonce_sent = None
  self . last_echo_nonce_sent = None
  self . last_new_echo_nonce_sent = None
  self . request_nonce_rcvd = None
  self . echo_nonce_rcvd = None
  self . last_request_nonce_rcvd = None
  self . last_echo_nonce_rcvd = None
  self . last_good_echo_nonce_rcvd = None
  lisp_nonce_echo_list [ rloc_str ] = self
  if 59 - 59: OoOoOO00
  if 47 - 47: II111iiii - I1ii11iIi11i - Ii1I
 def send_ipc ( self , ipc_socket , ipc ) :
  iI1Iii1i1 = "lisp-itr" if lisp_i_am_itr else "lisp-etr"
  Ii1II1I11i1I = "lisp-etr" if lisp_i_am_itr else "lisp-itr"
  ipc = lisp_command_ipc ( ipc , iI1Iii1i1 )
  lisp_ipc ( ipc , ipc_socket , Ii1II1I11i1I )
  if 87 - 87: i11iIiiIii * II111iiii - Ii1I % OoooooooOO
  if 55 - 55: i1IIi
 def send_request_ipc ( self , ipc_socket , nonce ) :
  nonce = lisp_hex_string ( nonce )
  oOOO0oo0 = "nonce%R%{}%{}" . format ( self . rloc_str , nonce )
  self . send_ipc ( ipc_socket , oOOO0oo0 )
  if 13 - 13: OoOoOO00 - OoO0O00 * OoooooooOO
  if 26 - 26: OoooooooOO
 def send_echo_ipc ( self , ipc_socket , nonce ) :
  nonce = lisp_hex_string ( nonce )
  oOOO0oo0 = "nonce%E%{}%{}" . format ( self . rloc_str , nonce )
  self . send_ipc ( ipc_socket , oOOO0oo0 )
  if 65 - 65: OOooOOo
  if 14 - 14: ooOoO0o
 def receive_request ( self , ipc_socket , nonce ) :
  Ooo0OO00oo = self . request_nonce_rcvd
  self . request_nonce_rcvd = nonce
  self . last_request_nonce_rcvd = lisp_get_timestamp ( )
  if ( lisp_i_am_rtr ) : return
  if ( Ooo0OO00oo != nonce ) : self . send_request_ipc ( ipc_socket , nonce )
  if 21 - 21: I11i
  if 79 - 79: OoO0O00 / OOooOOo - i1IIi + i1IIi - IiII + IiII
 def receive_echo ( self , ipc_socket , nonce ) :
  if ( self . request_nonce_sent != nonce ) : return
  self . last_echo_nonce_rcvd = lisp_get_timestamp ( )
  if ( self . echo_nonce_rcvd == nonce ) : return
  if 67 - 67: OoO0O00 * OoO0O00 / OoooooooOO
  self . echo_nonce_rcvd = nonce
  if ( lisp_i_am_rtr ) : return
  self . send_echo_ipc ( ipc_socket , nonce )
  if 79 - 79: o0oOOo0O0Ooo % iIii1I11I1II1 / II111iiii / Ii1I / Ii1I + O0
  if 46 - 46: i1IIi / IiII
 def get_request_or_echo_nonce ( self , ipc_socket , remote_rloc ) :
  if 84 - 84: OoOoOO00 / iIii1I11I1II1 + oO0o % ooOoO0o + oO0o - iIii1I11I1II1
  if 27 - 27: O0 / o0oOOo0O0Ooo * I1IiiI
  if 41 - 41: ooOoO0o
  if 11 - 11: i1IIi / I1Ii111 * I1ii11iIi11i * I1Ii111 * ooOoO0o - i11iIiiIii
  if 96 - 96: I1ii11iIi11i % I1ii11iIi11i
  if ( self . request_nonce_sent and self . echo_nonce_sent and remote_rloc ) :
   ii1 = lisp_myrlocs [ 0 ] if remote_rloc . is_ipv4 ( ) else lisp_myrlocs [ 1 ]
   if 26 - 26: oO0o - ooOoO0o % Oo0Ooo - oO0o + IiII
   if 33 - 33: Ii1I + OoOoOO00 - I1ii11iIi11i + iIii1I11I1II1 % i1IIi * IiII
   if ( remote_rloc . address > ii1 . address ) :
    oO0OO = "exit"
    self . request_nonce_sent = None
   else :
    oO0OO = "stay in"
    self . echo_nonce_sent = None
    if 21 - 21: O0 * ooOoO0o % OoO0O00
    if 14 - 14: O0 / I1Ii111 / ooOoO0o + IiII - IiII
   IiiI11iIi = bold ( "collision" , False )
   IIi1I1 = red ( ii1 . print_address_no_iid ( ) , False )
   I1I111iIiI = red ( remote_rloc . print_address_no_iid ( ) , False )
   lprint ( "Echo nonce {}, {} -> {}, {} request-nonce mode" . format ( IiiI11iIi ,
 IIi1I1 , I1I111iIiI , oO0OO ) )
   if 1 - 1: Ii1I * OoooooooOO - ooOoO0o % OOooOOo - OoooooooOO
   if 83 - 83: OoooooooOO . iII111i
   if 20 - 20: OoO0O00 . oO0o
   if 4 - 4: Oo0Ooo % Ii1I % OoO0O00 * iII111i % OoooooooOO
   if 38 - 38: OoooooooOO . iII111i
  if ( self . echo_nonce_sent != None ) :
   o0OOO = self . echo_nonce_sent
   iIIi1iI1I1IIi = bold ( "Echoing" , False )
   lprint ( "{} nonce 0x{} to {}" . format ( iIIi1iI1I1IIi ,
 lisp_hex_string ( o0OOO ) , red ( self . rloc_str , False ) ) )
   self . last_echo_nonce_sent = lisp_get_timestamp ( )
   self . echo_nonce_sent = None
   return ( o0OOO )
   if 43 - 43: OoooooooOO
   if 8 - 8: OOooOOo + I11i . I11i
   if 89 - 89: I1ii11iIi11i * I1ii11iIi11i * OoOoOO00 / iII111i
   if 60 - 60: OoO0O00 / iII111i / I1IiiI + oO0o
   if 93 - 93: OoooooooOO * Ii1I / O0 + Ii1I - iIii1I11I1II1
   if 6 - 6: IiII - Oo0Ooo - I11i - O0 % OoooooooOO
   if 88 - 88: O0 / o0oOOo0O0Ooo * o0oOOo0O0Ooo . o0oOOo0O0Ooo . O0
  o0OOO = self . request_nonce_sent
  IiI1i11iiII = self . last_request_nonce_sent
  if ( o0OOO and IiI1i11iiII != None ) :
   if ( time . time ( ) - IiI1i11iiII >= LISP_NONCE_ECHO_INTERVAL ) :
    self . request_nonce_sent = None
    lprint ( "Stop request-nonce mode for {}, nonce 0x{}" . format ( red ( self . rloc_str , False ) , lisp_hex_string ( o0OOO ) ) )
    if 64 - 64: Ii1I
    return ( None )
    if 47 - 47: I1IiiI * i11iIiiIii . OOooOOo . iII111i . i11iIiiIii
    if 33 - 33: I1ii11iIi11i % OoooooooOO . O0 * o0oOOo0O0Ooo % Oo0Ooo
    if 79 - 79: I11i - I1IiiI * Ii1I % II111iiii - II111iiii
    if 16 - 16: OOooOOo . II111iiii - Ii1I - OoooooooOO
    if 83 - 83: i11iIiiIii - Oo0Ooo
    if 5 - 5: I1ii11iIi11i . II111iiii . i1IIi
    if 35 - 35: o0oOOo0O0Ooo + OoO0O00 - I1ii11iIi11i
    if 24 - 24: II111iiii
    if 23 - 23: Oo0Ooo - iII111i
  if ( o0OOO == None ) :
   o0OOO = lisp_get_data_nonce ( )
   if ( self . recently_requested ( ) ) : return ( o0OOO )
   if 79 - 79: I11i . O0 - i1IIi
   self . request_nonce_sent = o0OOO
   lprint ( "Start request-nonce mode for {}, nonce 0x{}" . format ( red ( self . rloc_str , False ) , lisp_hex_string ( o0OOO ) ) )
   if 42 - 42: oO0o - i11iIiiIii % oO0o - I1Ii111 * O0 / II111iiii
   self . last_new_request_nonce_sent = lisp_get_timestamp ( )
   if 5 - 5: Oo0Ooo
   if 84 - 84: I1ii11iIi11i
   if 53 - 53: oO0o
   if 26 - 26: I1Ii111 / I1Ii111 + Oo0Ooo - o0oOOo0O0Ooo % II111iiii . OoooooooOO
   if 7 - 7: II111iiii - I1ii11iIi11i / I11i % OoooooooOO + i1IIi
   if ( lisp_i_am_itr == False ) : return ( o0OOO | 0x80000000 )
   self . send_request_ipc ( ipc_socket , o0OOO )
  else :
   lprint ( "Continue request-nonce mode for {}, nonce 0x{}" . format ( red ( self . rloc_str , False ) , lisp_hex_string ( o0OOO ) ) )
   if 42 - 42: I11i + i1IIi - Ii1I / IiII . iII111i
   if 30 - 30: Oo0Ooo + Ii1I % i11iIiiIii * i1IIi + I1IiiI % OOooOOo
   if 30 - 30: i11iIiiIii * Oo0Ooo . II111iiii + I1ii11iIi11i / o0oOOo0O0Ooo % I1Ii111
   if 78 - 78: I1ii11iIi11i + OoooooooOO - I1IiiI * OoOoOO00 * iII111i
   if 7 - 7: OOooOOo . IiII . I1Ii111 / Ii1I / Oo0Ooo
   if 83 - 83: I11i / Oo0Ooo
   if 23 - 23: iIii1I11I1II1
  self . last_request_nonce_sent = lisp_get_timestamp ( )
  return ( o0OOO | 0x80000000 )
  if 10 - 10: I11i - o0oOOo0O0Ooo % OoooooooOO - I1ii11iIi11i
  if 64 - 64: OoO0O00 / I1IiiI
 def request_nonce_timeout ( self ) :
  if ( self . request_nonce_sent == None ) : return ( False )
  if ( self . request_nonce_sent == self . echo_nonce_rcvd ) : return ( False )
  if 23 - 23: I11i * I1Ii111 * o0oOOo0O0Ooo - I1IiiI % OoOoOO00 + o0oOOo0O0Ooo
  Ooo0o0oo0 = time . time ( ) - self . last_request_nonce_sent
  I1ii11ii1iiI = self . last_echo_nonce_rcvd
  return ( Ooo0o0oo0 >= LISP_NONCE_ECHO_INTERVAL and I1ii11ii1iiI == None )
  if 93 - 93: OoOoOO00 + I11i
  if 27 - 27: iIii1I11I1II1 * I11i
 def recently_requested ( self ) :
  I1ii11ii1iiI = self . last_request_nonce_sent
  if ( I1ii11ii1iiI == None ) : return ( False )
  if 42 - 42: oO0o
  Ooo0o0oo0 = time . time ( ) - I1ii11ii1iiI
  return ( Ooo0o0oo0 <= LISP_NONCE_ECHO_INTERVAL )
  if 22 - 22: iIii1I11I1II1 % I1IiiI . O0
  if 13 - 13: II111iiii % i1IIi - OoOoOO00 + iII111i
 def recently_echoed ( self ) :
  if ( self . request_nonce_sent == None ) : return ( True )
  if 59 - 59: OoooooooOO + I1Ii111 % o0oOOo0O0Ooo - OoOoOO00 . I1IiiI
  if 42 - 42: I1Ii111
  if 70 - 70: o0oOOo0O0Ooo / I11i + oO0o % I1IiiI % Oo0Ooo + OoO0O00
  if 80 - 80: OOooOOo
  I1ii11ii1iiI = self . last_good_echo_nonce_rcvd
  if ( I1ii11ii1iiI == None ) : I1ii11ii1iiI = 0
  Ooo0o0oo0 = time . time ( ) - I1ii11ii1iiI
  if ( Ooo0o0oo0 <= LISP_NONCE_ECHO_INTERVAL ) : return ( True )
  if 12 - 12: Ii1I
  if 2 - 2: OoooooooOO
  if 100 - 100: Oo0Ooo / O0 * i11iIiiIii * OoooooooOO
  if 46 - 46: O0 % OoooooooOO
  if 22 - 22: iII111i + OoooooooOO - OoOoOO00 - OoO0O00 * I1Ii111 - oO0o
  if 99 - 99: ooOoO0o / I1IiiI . Ii1I - Ii1I * I1IiiI
  I1ii11ii1iiI = self . last_new_request_nonce_sent
  if ( I1ii11ii1iiI == None ) : I1ii11ii1iiI = 0
  Ooo0o0oo0 = time . time ( ) - I1ii11ii1iiI
  return ( Ooo0o0oo0 <= LISP_NONCE_ECHO_INTERVAL )
  if 24 - 24: I11i * OoO0O00 - oO0o / iIii1I11I1II1 - Oo0Ooo . OOooOOo
  if 2 - 2: ooOoO0o - O0 - I1ii11iIi11i / I11i * OoOoOO00
 def change_state ( self , rloc ) :
  if ( rloc . up_state ( ) and self . recently_echoed ( ) == False ) :
   III1II = bold ( "down" , False )
   O0O00000o = lisp_print_elapsed ( self . last_good_echo_nonce_rcvd )
   lprint ( "Take {} {}, last good echo: {}" . format ( red ( self . rloc_str , False ) , III1II , O0O00000o ) )
   if 53 - 53: Ii1I
   rloc . state = LISP_RLOC_NO_ECHOED_NONCE_STATE
   rloc . last_state_change = lisp_get_timestamp ( )
   return
   if 58 - 58: iIii1I11I1II1 - II111iiii - IiII % I1ii11iIi11i
   if 80 - 80: IiII * iII111i . i1IIi % Ii1I % I1ii11iIi11i + ooOoO0o
  if ( rloc . no_echoed_nonce_state ( ) == False ) : return
  if 6 - 6: I1ii11iIi11i . oO0o . OoO0O00 + IiII
  if ( self . recently_requested ( ) == False ) :
   oO0oo0O0OOOo0 = bold ( "up" , False )
   lprint ( "Bring {} {}, retry request-nonce mode" . format ( red ( self . rloc_str , False ) , oO0oo0O0OOOo0 ) )
   if 29 - 29: I1IiiI
   rloc . state = LISP_RLOC_UP_STATE
   rloc . last_state_change = lisp_get_timestamp ( )
   if 41 - 41: I1Ii111 * OoO0O00 - iII111i . Ii1I
   if 41 - 41: iIii1I11I1II1 - O0 - I1ii11iIi11i - oO0o + I1Ii111
   if 22 - 22: O0 % IiII % iII111i % I1IiiI
 def print_echo_nonce ( self ) :
  I11 = lisp_print_elapsed ( self . last_request_nonce_sent )
  i11i111i1 = lisp_print_elapsed ( self . last_good_echo_nonce_rcvd )
  if 1 - 1: oO0o - Oo0Ooo * iIii1I11I1II1 * Oo0Ooo * i1IIi
  i11i1IiIi = lisp_print_elapsed ( self . last_echo_nonce_sent )
  ooOoOoOOOo = lisp_print_elapsed ( self . last_request_nonce_rcvd )
  OO0o0OO0 = space ( 4 )
  if 73 - 73: i11iIiiIii / OoOoOO00
  oOOO = "Nonce-Echoing:\n"
  oOOO += ( "{}Last request-nonce sent: {}\n{}Last echo-nonce " + "received: {}\n" ) . format ( OO0o0OO0 , I11 , OO0o0OO0 , i11i111i1 )
  if 45 - 45: I11i . OoO0O00
  oOOO += ( "{}Last request-nonce received: {}\n{}Last echo-nonce " + "sent: {}" ) . format ( OO0o0OO0 , ooOoOoOOOo , OO0o0OO0 , i11i1IiIi )
  if 14 - 14: OOooOOo * I1IiiI - I1ii11iIi11i
  if 10 - 10: iII111i % I1Ii111 * I1ii11iIi11i * O0 * i11iIiiIii % I1Ii111
  return ( oOOO )
  if 68 - 68: OoooooooOO * OoOoOO00
  if 9 - 9: I1Ii111
  if 36 - 36: I1Ii111 / OoOoOO00 + OoOoOO00 * ooOoO0o / OOooOOo * O0
  if 17 - 17: OoO0O00 / ooOoO0o % I1IiiI
  if 47 - 47: Oo0Ooo * OoO0O00 / o0oOOo0O0Ooo * I1IiiI
  if 60 - 60: I1ii11iIi11i / IiII . i11iIiiIii / OoO0O00 % II111iiii
  if 6 - 6: iII111i % o0oOOo0O0Ooo + I1Ii111
  if 91 - 91: o0oOOo0O0Ooo + O0 * oO0o * IiII * I1ii11iIi11i
  if 83 - 83: OoooooooOO
class lisp_keys ( ) :
 def __init__ ( self , key_id , do_curve = True , do_chacha = use_chacha ,
 do_poly = use_poly ) :
  self . uptime = lisp_get_timestamp ( )
  self . last_rekey = None
  self . rekey_count = 0
  self . use_count = 0
  self . key_id = key_id
  self . cipher_suite = LISP_CS_1024
  self . dh_g_value = LISP_CS_1024_G
  self . dh_p_value = LISP_CS_1024_P
  self . curve25519 = None
  self . cipher_suite_string = ""
  if ( do_curve ) :
   if ( do_chacha ) :
    self . cipher_suite = LISP_CS_25519_CHACHA
    self . cipher_suite_string = "chacha"
   elif ( os . getenv ( "LISP_USE_AES_GCM" ) != None ) :
    self . cipher_suite = LISP_CS_25519_GCM
    self . cipher_suite_string = "aes-gcm"
   else :
    self . cipher_suite = LISP_CS_25519_CBC
    self . cipher_suite_string = "aes-cbc"
    if 52 - 52: o0oOOo0O0Ooo / OoOoOO00 % oO0o % OoO0O00 / IiII % o0oOOo0O0Ooo
   self . local_private_key = random . randint ( 0 , 2 ** 128 - 1 )
   o0Oo = lisp_hex_string ( self . local_private_key ) . zfill ( 32 )
   self . curve25519 = curve25519 . Private ( o0Oo )
  else :
   self . local_private_key = random . randint ( 0 , 0x1fff )
   if 88 - 88: OOooOOo / i11iIiiIii / Ii1I / i11iIiiIii * I1ii11iIi11i % I11i
  self . local_public_key = self . compute_public_key ( )
  self . remote_public_key = None
  self . shared_key = None
  self . encrypt_key = None
  self . icv_key = None
  self . icv = poly1305 if do_poly else hashlib . sha256
  self . iv = None
  self . get_iv ( )
  self . do_poly = do_poly
  if 43 - 43: OoOoOO00 * OoO0O00 % i1IIi * Ii1I + iIii1I11I1II1
  if 80 - 80: o0oOOo0O0Ooo . iII111i . OoooooooOO
 def copy_keypair ( self , key ) :
  self . local_private_key = key . local_private_key
  self . local_public_key = key . local_public_key
  self . curve25519 = key . curve25519
  if 63 - 63: ooOoO0o . OOooOOo
  if 66 - 66: I1IiiI
 def get_iv ( self ) :
  if ( self . iv == None ) :
   self . iv = random . randint ( 0 , LISP_16_128_MASK )
  else :
   self . iv += 1
   if 99 - 99: OoO0O00 % O0 . I1Ii111 - I1ii11iIi11i . Oo0Ooo / OoOoOO00
  OO000OOOo0Oo = self . iv
  if ( self . cipher_suite == LISP_CS_25519_CHACHA ) :
   OO000OOOo0Oo = struct . pack ( "Q" , OO000OOOo0Oo & LISP_8_64_MASK )
  elif ( self . cipher_suite == LISP_CS_25519_GCM ) :
   o0oOOoOoo = struct . pack ( "I" , ( OO000OOOo0Oo >> 64 ) & LISP_4_32_MASK )
   ooO0O = struct . pack ( "Q" , OO000OOOo0Oo & LISP_8_64_MASK )
   OO000OOOo0Oo = o0oOOoOoo + ooO0O
  else :
   OO000OOOo0Oo = struct . pack ( "QQ" , OO000OOOo0Oo >> 64 , OO000OOOo0Oo & LISP_8_64_MASK )
  return ( OO000OOOo0Oo )
  if 55 - 55: OOooOOo - II111iiii - IiII . I11i + oO0o - oO0o
  if 29 - 29: OoOoOO00 - I1Ii111 % OOooOOo
 def key_length ( self , key ) :
  if ( type ( key ) != str ) : key = self . normalize_pub_key ( key )
  return ( len ( key ) / 2 )
  if 45 - 45: IiII / Oo0Ooo + OoooooooOO
  if 77 - 77: oO0o . Ii1I / O0 * oO0o
 def print_key ( self , key ) :
  O0OoOO = self . normalize_pub_key ( key )
  return ( "0x{}...{}({})" . format ( O0OoOO [ 0 : 4 ] , O0OoOO [ - 4 : : ] , self . key_length ( O0OoOO ) ) )
  if 98 - 98: Oo0Ooo - oO0o . I1Ii111
  if 51 - 51: iII111i . I1ii11iIi11i / I11i + o0oOOo0O0Ooo % OOooOOo
 def normalize_pub_key ( self , key ) :
  if ( type ( key ) == str ) :
   if ( self . curve25519 ) : return ( binascii . hexlify ( key ) )
   return ( key )
   if 1 - 1: Ii1I % OOooOOo + OOooOOo * IiII
  key = lisp_hex_string ( key ) . zfill ( 256 )
  return ( key )
  if 76 - 76: I1IiiI % i11iIiiIii + OOooOOo
  if 17 - 17: I11i / II111iiii * o0oOOo0O0Ooo / Oo0Ooo + iII111i . oO0o
 def print_keys ( self , do_bold = True ) :
  IIi1I1 = bold ( "local-key: " , False ) if do_bold else "local-key: "
  if ( self . local_public_key == None ) :
   IIi1I1 += "none"
  else :
   IIi1I1 += self . print_key ( self . local_public_key )
   if 19 - 19: OOooOOo * I11i
  I1I111iIiI = bold ( "remote-key: " , False ) if do_bold else "remote-key: "
  if ( self . remote_public_key == None ) :
   I1I111iIiI += "none"
  else :
   I1I111iIiI += self . print_key ( self . remote_public_key )
   if 85 - 85: i1IIi % o0oOOo0O0Ooo * I1ii11iIi11i * OoO0O00 . II111iiii
  O000 = "ECDH" if ( self . curve25519 ) else "DH"
  I1i1i1 = self . cipher_suite
  return ( "{} cipher-suite: {}, {}, {}" . format ( O000 , I1i1i1 , IIi1I1 , I1I111iIiI ) )
  if 35 - 35: iIii1I11I1II1 % I1Ii111 * I11i . Oo0Ooo
  if 3 - 3: ooOoO0o - I1ii11iIi11i * I1IiiI . OoOoOO00
 def compare_keys ( self , keys ) :
  if ( self . dh_g_value != keys . dh_g_value ) : return ( False )
  if ( self . dh_p_value != keys . dh_p_value ) : return ( False )
  if ( self . remote_public_key != keys . remote_public_key ) : return ( False )
  return ( True )
  if 69 - 69: OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo % I1Ii111 - iIii1I11I1II1
  if 49 - 49: o0oOOo0O0Ooo . I1ii11iIi11i % II111iiii
 def compute_public_key ( self ) :
  if ( self . curve25519 ) : return ( self . curve25519 . get_public ( ) . public )
  if 4 - 4: I1IiiI / OoOoOO00 / I1IiiI / I11i . IiII + iII111i
  o0Oo = self . local_private_key
  i11ii = self . dh_g_value
  IiI1i1i1 = self . dh_p_value
  return ( int ( ( i11ii ** o0Oo ) % IiI1i1i1 ) )
  if 70 - 70: ooOoO0o . i11iIiiIii % OoOoOO00 + oO0o
  if 95 - 95: I1ii11iIi11i
 def compute_shared_key ( self , ed , print_shared = False ) :
  o0Oo = self . local_private_key
  iiIii1I1Ii = self . remote_public_key
  if 14 - 14: iII111i % OoO0O00
  iI1IIiiIII1 = bold ( "Compute {} shared-key" . format ( ed ) , False )
  lprint ( "{}, key-material: {}" . format ( iI1IIiiIII1 , self . print_keys ( ) ) )
  if 67 - 67: I1ii11iIi11i + Ii1I * I11i / oO0o
  if ( self . curve25519 ) :
   i111Iii11i1Ii = curve25519 . Public ( iiIii1I1Ii )
   self . shared_key = self . curve25519 . get_shared_key ( i111Iii11i1Ii )
  else :
   IiI1i1i1 = self . dh_p_value
   self . shared_key = ( iiIii1I1Ii ** o0Oo ) % IiI1i1i1
   if 65 - 65: iIii1I11I1II1 * IiII
   if 89 - 89: IiII % i11iIiiIii . i11iIiiIii + oO0o / I1ii11iIi11i
   if 19 - 19: I1IiiI
   if 86 - 86: I1ii11iIi11i + OoOoOO00 * IiII + ooOoO0o
   if 23 - 23: OoO0O00 - oO0o * iIii1I11I1II1
   if 1 - 1: I11i - Oo0Ooo / i1IIi
   if 96 - 96: OoooooooOO % iII111i - OoooooooOO % O0
  if ( print_shared ) :
   O0OoOO = self . print_key ( self . shared_key )
   lprint ( "Computed shared-key: {}" . format ( O0OoOO ) )
   if 21 - 21: iII111i
   if 1 - 1: Oo0Ooo . i11iIiiIii
   if 9 - 9: OoooooooOO / I11i
   if 47 - 47: OoooooooOO
   if 48 - 48: OoOoOO00 . IiII % I1IiiI + I11i
  self . compute_encrypt_icv_keys ( )
  if 37 - 37: Oo0Ooo + I1Ii111 * oO0o / o0oOOo0O0Ooo
  if 78 - 78: IiII + I11i - o0oOOo0O0Ooo + OoO0O00 / iIii1I11I1II1
  if 47 - 47: OOooOOo
  if 20 - 20: I1Ii111 % ooOoO0o - I1Ii111 * OoooooooOO / I1ii11iIi11i
  self . rekey_count += 1
  self . last_rekey = lisp_get_timestamp ( )
  if 57 - 57: IiII % I11i * OOooOOo % I1ii11iIi11i
  if 65 - 65: i1IIi - OoooooooOO
 def compute_encrypt_icv_keys ( self ) :
  OO0o = hashlib . sha256
  if ( self . curve25519 ) :
   oOO00o0 = self . shared_key
  else :
   oOO00o0 = lisp_hex_string ( self . shared_key )
   if 29 - 29: II111iiii - iII111i / oO0o % OoooooooOO % iII111i + IiII
   if 44 - 44: O0 / O0
   if 25 - 25: o0oOOo0O0Ooo + iIii1I11I1II1 + IiII + I1ii11iIi11i / I1Ii111 - i1IIi
   if 15 - 15: O0 % Oo0Ooo % IiII % OoooooooOO - IiII
   if 27 - 27: I1Ii111 - o0oOOo0O0Ooo * I1ii11iIi11i - I1IiiI
  IIi1I1 = self . local_public_key
  if ( type ( IIi1I1 ) != long ) : IIi1I1 = int ( binascii . hexlify ( IIi1I1 ) , 16 )
  I1I111iIiI = self . remote_public_key
  if ( type ( I1I111iIiI ) != long ) : I1I111iIiI = int ( binascii . hexlify ( I1I111iIiI ) , 16 )
  IIIiIIi111 = "0001" + "lisp-crypto" + lisp_hex_string ( IIi1I1 ^ I1I111iIiI ) + "0100"
  if 77 - 77: I1IiiI / I1Ii111
  OOoo0oo000oo = hmac . new ( IIIiIIi111 , oOO00o0 , OO0o ) . hexdigest ( )
  OOoo0oo000oo = int ( OOoo0oo000oo , 16 )
  if 58 - 58: I1ii11iIi11i % i11iIiiIii + OoOoOO00 / I11i - OoooooooOO
  if 62 - 62: OoO0O00 . OoOoOO00
  if 22 - 22: ooOoO0o . i11iIiiIii . OoooooooOO . i1IIi
  if 12 - 12: OoOoOO00 % OOooOOo + oO0o . O0 % iIii1I11I1II1
  ii1I = ( OOoo0oo000oo >> 128 ) & LISP_16_128_MASK
  O00oO0oOOOOOO = OOoo0oo000oo & LISP_16_128_MASK
  self . encrypt_key = lisp_hex_string ( ii1I ) . zfill ( 32 )
  Oo0ooo00OoO = 32 if self . do_poly else 40
  self . icv_key = lisp_hex_string ( O00oO0oOOOOOO ) . zfill ( Oo0ooo00OoO )
  if 1 - 1: OoooooooOO * iIii1I11I1II1 / I1ii11iIi11i * I11i
  if 37 - 37: iII111i % I11i . iII111i - OOooOOo / iIii1I11I1II1 - OOooOOo
 def do_icv ( self , packet , nonce ) :
  if ( self . icv_key == None ) : return ( "" )
  if ( self . do_poly ) :
   i1i = self . icv . poly1305aes
   iiIi1i = self . icv . binascii . hexlify
   nonce = iiIi1i ( nonce )
   I1i11IIiiIiI = i1i ( self . encrypt_key , self . icv_key , nonce , packet )
   I1i11IIiiIiI = iiIi1i ( I1i11IIiiIiI )
  else :
   o0Oo = binascii . unhexlify ( self . icv_key )
   I1i11IIiiIiI = hmac . new ( o0Oo , packet , self . icv ) . hexdigest ( )
   I1i11IIiiIiI = I1i11IIiiIiI [ 0 : 40 ]
   if 7 - 7: OoO0O00 * i11iIiiIii * iIii1I11I1II1 / OOooOOo / I1Ii111
  return ( I1i11IIiiIiI )
  if 35 - 35: iII111i * OOooOOo
  if 65 - 65: II111iiii % i1IIi
 def add_key_by_nonce ( self , nonce ) :
  if ( lisp_crypto_keys_by_nonce . has_key ( nonce ) == False ) :
   lisp_crypto_keys_by_nonce [ nonce ] = [ None , None , None , None ]
   if 13 - 13: OoO0O00 * I1Ii111 + Oo0Ooo - IiII
  lisp_crypto_keys_by_nonce [ nonce ] [ self . key_id ] = self
  if 31 - 31: OoO0O00
  if 68 - 68: OoO0O00 + i1IIi / iIii1I11I1II1 + II111iiii * iIii1I11I1II1 + I1ii11iIi11i
 def delete_key_by_nonce ( self , nonce ) :
  if ( lisp_crypto_keys_by_nonce . has_key ( nonce ) == False ) : return
  lisp_crypto_keys_by_nonce . pop ( nonce )
  if 77 - 77: i11iIiiIii - I1Ii111 . I1ii11iIi11i % Oo0Ooo . Ii1I
  if 9 - 9: o0oOOo0O0Ooo
 def add_key_by_rloc ( self , addr_str , encap ) :
  O0Ooo000Ooo = lisp_crypto_keys_by_rloc_encap if encap else lisp_crypto_keys_by_rloc_decap
  if 46 - 46: i1IIi + O0
  if 5 - 5: o0oOOo0O0Ooo + I1IiiI / OoooooooOO % i11iIiiIii % OoooooooOO - o0oOOo0O0Ooo
  if ( O0Ooo000Ooo . has_key ( addr_str ) == False ) :
   O0Ooo000Ooo [ addr_str ] = [ None , None , None , None ]
   if 53 - 53: OoO0O00 + i11iIiiIii / iIii1I11I1II1
  O0Ooo000Ooo [ addr_str ] [ self . key_id ] = self
  if 1 - 1: IiII % i1IIi
  if 41 - 41: OoO0O00 * OoO0O00 / iII111i + I1ii11iIi11i . o0oOOo0O0Ooo
  if 84 - 84: i11iIiiIii + OoO0O00 * I1IiiI + I1ii11iIi11i / Ii1I
  if 80 - 80: I1ii11iIi11i
  if 67 - 67: II111iiii
  if ( encap == False ) :
   lisp_write_ipc_decap_key ( addr_str , O0Ooo000Ooo [ addr_str ] )
   if 2 - 2: o0oOOo0O0Ooo - O0 * Ii1I % IiII
   if 64 - 64: i1IIi . ooOoO0o
   if 7 - 7: oO0o . iII111i - iII111i / I1Ii111 % Oo0Ooo
 def encode_lcaf ( self , rloc_addr ) :
  OOoO00OOo = self . normalize_pub_key ( self . local_public_key )
  iii = self . key_length ( OOoO00OOo )
  iiiii = ( 6 + iii + 2 )
  if ( rloc_addr != None ) : iiiii += rloc_addr . addr_length ( )
  if 74 - 74: I1ii11iIi11i % I1Ii111 - OoO0O00 * I11i . OoooooooOO * OoO0O00
  IiiiIi1iiii11 = struct . pack ( "HBBBBHBB" , socket . htons ( LISP_AFI_LCAF ) , 0 , 0 ,
 LISP_LCAF_SECURITY_TYPE , 0 , socket . htons ( iiiii ) , 1 , 0 )
  if 99 - 99: OoOoOO00 . iII111i - OoooooooOO - O0
  if 6 - 6: OOooOOo
  if 3 - 3: O0 - I1Ii111 * Ii1I * OOooOOo / Ii1I
  if 58 - 58: Ii1I * iIii1I11I1II1 + ooOoO0o . ooOoO0o
  if 74 - 74: ooOoO0o - o0oOOo0O0Ooo * IiII % ooOoO0o
  if 93 - 93: iIii1I11I1II1 / OoOoOO00 % Oo0Ooo * I1Ii111 - OoO0O00 - o0oOOo0O0Ooo
  I1i1i1 = self . cipher_suite
  IiiiIi1iiii11 += struct . pack ( "BBH" , I1i1i1 , 0 , socket . htons ( iii ) )
  if 44 - 44: OoooooooOO
  if 82 - 82: OoOoOO00 . OoOoOO00
  if 10 - 10: Oo0Ooo * I1ii11iIi11i . oO0o . OoooooooOO . OOooOOo * I1ii11iIi11i
  if 80 - 80: I1Ii111 + I11i . I1Ii111 + OOooOOo
  for iIi1I1 in range ( 0 , iii * 2 , 16 ) :
   o0Oo = int ( OOoO00OOo [ iIi1I1 : iIi1I1 + 16 ] , 16 )
   IiiiIi1iiii11 += struct . pack ( "Q" , byte_swap_64 ( o0Oo ) )
   if 85 - 85: i11iIiiIii . I11i + Ii1I / Ii1I
   if 43 - 43: IiII . OoooooooOO - II111iiii
   if 90 - 90: I1IiiI - iIii1I11I1II1 + I1ii11iIi11i * OOooOOo * oO0o
   if 19 - 19: I1Ii111 * II111iiii % Oo0Ooo - i1IIi
   if 27 - 27: OoOoOO00 . O0 / I1ii11iIi11i . iIii1I11I1II1
  if ( rloc_addr ) :
   IiiiIi1iiii11 += struct . pack ( "H" , socket . htons ( rloc_addr . afi ) )
   IiiiIi1iiii11 += rloc_addr . pack_address ( )
   if 15 - 15: Ii1I + OoO0O00 % iIii1I11I1II1 - I1ii11iIi11i - i1IIi % o0oOOo0O0Ooo
  return ( IiiiIi1iiii11 )
  if 54 - 54: IiII - II111iiii . ooOoO0o + Ii1I
  if 45 - 45: oO0o + II111iiii . iII111i / I1ii11iIi11i
 def decode_lcaf ( self , packet , lcaf_len ) :
  if 76 - 76: Ii1I + iII111i - IiII * iIii1I11I1II1 % i1IIi
  if 72 - 72: ooOoO0o + II111iiii . O0 - iII111i / OoooooooOO . I1Ii111
  if 28 - 28: iIii1I11I1II1 . O0
  if 32 - 32: OoooooooOO
  if ( lcaf_len == 0 ) :
   O0O00Oo = "HHBBH"
   IiIii1i = struct . calcsize ( O0O00Oo )
   if ( len ( packet ) < IiIii1i ) : return ( None )
   if 29 - 29: I1ii11iIi11i
   IiiiII , iI111iiI1II , OOOoooO000O0 , iI111iiI1II , lcaf_len = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
   if 63 - 63: oO0o - iII111i - ooOoO0o / oO0o + I1Ii111 + Oo0Ooo
   if 32 - 32: I1IiiI . I1IiiI / iIii1I11I1II1 - I11i - O0 % OOooOOo
   if ( OOOoooO000O0 != LISP_LCAF_SECURITY_TYPE ) :
    packet = packet [ lcaf_len + 6 : : ]
    return ( packet )
    if 48 - 48: Oo0Ooo % Oo0Ooo % O0
   lcaf_len = socket . ntohs ( lcaf_len )
   packet = packet [ IiIii1i : : ]
   if 8 - 8: iII111i . Ii1I - i1IIi % OoO0O00 / I11i
   if 13 - 13: Oo0Ooo / OoOoOO00 . I1ii11iIi11i . OOooOOo
   if 31 - 31: o0oOOo0O0Ooo
   if 59 - 59: Oo0Ooo / Oo0Ooo
   if 87 - 87: I1ii11iIi11i % OoOoOO00 + Ii1I . i11iIiiIii / Ii1I
   if 32 - 32: Ii1I + IiII + I1ii11iIi11i
  OOOoooO000O0 = LISP_LCAF_SECURITY_TYPE
  O0O00Oo = "BBBBH"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 79 - 79: i1IIi / Ii1I
  o0O , iI111iiI1II , I1i1i1 , iI111iiI1II , iii = struct . unpack ( O0O00Oo ,
 packet [ : IiIii1i ] )
  if 80 - 80: IiII % OoO0O00 / O0 % I1IiiI + i1IIi - O0
  if 70 - 70: OoooooooOO . II111iiii / Ii1I * IiII + OOooOOo
  if 48 - 48: oO0o % iIii1I11I1II1 + OoooooooOO
  if 71 - 71: Oo0Ooo
  if 98 - 98: o0oOOo0O0Ooo * Oo0Ooo - Ii1I . ooOoO0o
  if 2 - 2: Oo0Ooo - ooOoO0o % iIii1I11I1II1
  packet = packet [ IiIii1i : : ]
  iii = socket . ntohs ( iii )
  if ( len ( packet ) < iii ) : return ( None )
  if 88 - 88: I1Ii111 - OoO0O00
  if 79 - 79: iII111i
  if 45 - 45: II111iiii + iII111i . I11i . O0 * i1IIi - Ii1I
  if 48 - 48: I1ii11iIi11i + Oo0Ooo
  o0OOoOoo = [ LISP_CS_25519_CBC , LISP_CS_25519_GCM , LISP_CS_25519_CHACHA ,
 LISP_CS_1024 ]
  if ( I1i1i1 not in o0OOoOoo ) :
   lprint ( "Cipher-suites {} supported, received {}" . format ( o0OOoOoo ,
 I1i1i1 ) )
   packet = packet [ iii : : ]
   return ( packet )
   if 56 - 56: IiII - Ii1I + i11iIiiIii * OoO0O00 % I1IiiI
   if 37 - 37: iIii1I11I1II1 + IiII / I1Ii111 . OoooooooOO
  self . cipher_suite = I1i1i1
  if 72 - 72: oO0o % ooOoO0o % OOooOOo
  if 63 - 63: OoO0O00 . Ii1I % II111iiii / I11i - OoOoOO00
  if 4 - 4: Oo0Ooo - O0 / I11i + O0 - oO0o * Oo0Ooo
  if 25 - 25: I1IiiI
  if 64 - 64: oO0o
  OOoO00OOo = 0
  for iIi1I1 in range ( 0 , iii , 8 ) :
   o0Oo = byte_swap_64 ( struct . unpack ( "Q" , packet [ iIi1I1 : iIi1I1 + 8 ] ) [ 0 ] )
   OOoO00OOo <<= 64
   OOoO00OOo |= o0Oo
   if 80 - 80: o0oOOo0O0Ooo % iIii1I11I1II1
  self . remote_public_key = OOoO00OOo
  if 63 - 63: IiII * i11iIiiIii
  if 86 - 86: I11i % I11i - OoOoOO00 + I1Ii111 / I1IiiI * OoooooooOO
  if 26 - 26: II111iiii * iII111i + o0oOOo0O0Ooo / O0 + i1IIi - I11i
  if 56 - 56: OOooOOo
  if 76 - 76: i1IIi % iIii1I11I1II1 - o0oOOo0O0Ooo + IiII - I11i
  if ( self . curve25519 ) :
   o0Oo = lisp_hex_string ( self . remote_public_key )
   o0Oo = o0Oo . zfill ( 64 )
   OOOo00o = ""
   for iIi1I1 in range ( 0 , len ( o0Oo ) , 2 ) :
    OOOo00o += chr ( int ( o0Oo [ iIi1I1 : iIi1I1 + 2 ] , 16 ) )
    if 100 - 100: iIii1I11I1II1 - OoOoOO00
   self . remote_public_key = OOOo00o
   if 28 - 28: Oo0Ooo . O0 . I11i
   if 60 - 60: II111iiii + I1Ii111 / oO0o % OoooooooOO - i1IIi
  packet = packet [ iii : : ]
  return ( packet )
  if 57 - 57: ooOoO0o
  if 99 - 99: Oo0Ooo + I1Ii111 % ooOoO0o - o0oOOo0O0Ooo
  if 52 - 52: I1ii11iIi11i
  if 93 - 93: iII111i . i11iIiiIii
  if 24 - 24: OOooOOo . OoO0O00 + I1Ii111 . oO0o - I1ii11iIi11i % iII111i
  if 49 - 49: O0 . Oo0Ooo / Ii1I
  if 29 - 29: I1ii11iIi11i / oO0o * O0 - i11iIiiIii - OoO0O00 + Ii1I
  if 86 - 86: I1IiiI / I1ii11iIi11i * Ii1I % i11iIiiIii
class lisp_thread ( ) :
 def __init__ ( self , name ) :
  self . thread_name = name
  self . thread_number = - 1
  self . number_of_pcap_threads = 0
  self . number_of_worker_threads = 0
  self . input_queue = Queue . Queue ( )
  self . input_stats = lisp_stats ( )
  self . lisp_packet = lisp_packet ( None )
  if 20 - 20: iII111i . OoooooooOO + iII111i + ooOoO0o * I1ii11iIi11i
  if 44 - 44: i11iIiiIii
  if 69 - 69: OOooOOo * O0 + i11iIiiIii
  if 65 - 65: O0 / iII111i . i1IIi * iII111i / iIii1I11I1II1 - oO0o
  if 93 - 93: OoOoOO00 % i11iIiiIii - Ii1I % OoO0O00
  if 55 - 55: o0oOOo0O0Ooo . I1ii11iIi11i
  if 63 - 63: oO0o
  if 79 - 79: I1ii11iIi11i - oO0o - o0oOOo0O0Ooo . OOooOOo
  if 65 - 65: i11iIiiIii . OoO0O00 % iII111i + IiII - i11iIiiIii
  if 60 - 60: I1Ii111
  if 14 - 14: Oo0Ooo % oO0o * iII111i - i11iIiiIii / I1ii11iIi11i * i11iIiiIii
  if 95 - 95: iIii1I11I1II1 + OoOoOO00 . I1IiiI + OoOoOO00 * I11i + OOooOOo
  if 14 - 14: Ii1I - O0
  if 68 - 68: II111iiii - I1ii11iIi11i - OoO0O00 * iIii1I11I1II1 / I1IiiI * I1ii11iIi11i
  if 45 - 45: I1Ii111 * I11i / iIii1I11I1II1 / I1IiiI % II111iiii
  if 49 - 49: Ii1I / iII111i . iII111i . iII111i + i11iIiiIii % I11i
  if 7 - 7: IiII * ooOoO0o + OoOoOO00
  if 22 - 22: iII111i
class lisp_control_header ( ) :
 def __init__ ( self ) :
  self . type = 0
  self . record_count = 0
  self . nonce = 0
  self . rloc_probe = False
  self . smr_bit = False
  self . smr_invoked_bit = False
  self . ddt_bit = False
  self . to_etr = False
  self . to_ms = False
  self . info_reply = False
  if 48 - 48: I1ii11iIi11i . I1IiiI
  if 73 - 73: O0 . I1Ii111 - OoooooooOO % I11i % i1IIi
 def decode ( self , packet ) :
  O0O00Oo = "BBBBQ"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( False )
  if 14 - 14: I1Ii111 + Ii1I * Oo0Ooo
  iI11iI , O0o0ooo00o00 , IiiI , self . record_count , self . nonce = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  if 32 - 32: ooOoO0o
  if 26 - 26: O0 * Ii1I - I1IiiI - iII111i / iIii1I11I1II1
  self . type = iI11iI >> 4
  if ( self . type == LISP_MAP_REQUEST ) :
   self . smr_bit = True if ( iI11iI & 0x01 ) else False
   self . rloc_probe = True if ( iI11iI & 0x02 ) else False
   self . smr_invoked_bit = True if ( O0o0ooo00o00 & 0x40 ) else False
   if 57 - 57: I1ii11iIi11i - OoO0O00 * iIii1I11I1II1
  if ( self . type == LISP_ECM ) :
   self . ddt_bit = True if ( iI11iI & 0x04 ) else False
   self . to_etr = True if ( iI11iI & 0x02 ) else False
   self . to_ms = True if ( iI11iI & 0x01 ) else False
   if 26 - 26: OoO0O00 % ooOoO0o % o0oOOo0O0Ooo % OoOoOO00 . iII111i % O0
  if ( self . type == LISP_NAT_INFO ) :
   self . info_reply = True if ( iI11iI & 0x08 ) else False
   if 91 - 91: II111iiii . Oo0Ooo . oO0o - OoooooooOO / OoOoOO00
  return ( True )
  if 30 - 30: I11i % o0oOOo0O0Ooo + i1IIi * OoooooooOO * OoO0O00 - II111iiii
  if 55 - 55: OoO0O00
 def is_info_request ( self ) :
  return ( ( self . type == LISP_NAT_INFO and self . is_info_reply ( ) == False ) )
  if 20 - 20: ooOoO0o * I1Ii111 * o0oOOo0O0Ooo - ooOoO0o
  if 32 - 32: Ii1I * oO0o
 def is_info_reply ( self ) :
  return ( True if self . info_reply else False )
  if 85 - 85: i11iIiiIii . OoO0O00 + OoO0O00
  if 28 - 28: Oo0Ooo
 def is_rloc_probe ( self ) :
  return ( True if self . rloc_probe else False )
  if 62 - 62: Oo0Ooo + OoooooooOO / iII111i
  if 60 - 60: Ii1I / OoOoOO00 . I11i % OOooOOo
 def is_smr ( self ) :
  return ( True if self . smr_bit else False )
  if 61 - 61: O0 . Ii1I . O0 * i11iIiiIii * II111iiii / I1Ii111
  if 69 - 69: I11i
 def is_smr_invoked ( self ) :
  return ( True if self . smr_invoked_bit else False )
  if 17 - 17: I11i
  if 38 - 38: I1Ii111 % OOooOOo
 def is_ddt ( self ) :
  return ( True if self . ddt_bit else False )
  if 9 - 9: O0 . iIii1I11I1II1
  if 44 - 44: I1ii11iIi11i % IiII
 def is_to_etr ( self ) :
  return ( True if self . to_etr else False )
  if 6 - 6: OoO0O00
  if 82 - 82: iIii1I11I1II1 . I11i / IiII / OOooOOo * II111iiii % oO0o
 def is_to_ms ( self ) :
  return ( True if self . to_ms else False )
  if 62 - 62: II111iiii
  if 96 - 96: I11i % OoOoOO00 * I1ii11iIi11i
  if 94 - 94: Oo0Ooo - i1IIi . O0 % Oo0Ooo . ooOoO0o
  if 63 - 63: i11iIiiIii % I1ii11iIi11i % I1IiiI . IiII * o0oOOo0O0Ooo + OOooOOo
  if 77 - 77: o0oOOo0O0Ooo
  if 63 - 63: ooOoO0o * oO0o + ooOoO0o * Ii1I + Oo0Ooo / I1ii11iIi11i
  if 15 - 15: O0 . I1ii11iIi11i * I1ii11iIi11i
  if 65 - 65: I1Ii111 + O0 % o0oOOo0O0Ooo
  if 72 - 72: OOooOOo . OoOoOO00 / II111iiii
  if 69 - 69: OOooOOo * II111iiii - ooOoO0o - i1IIi + i11iIiiIii
  if 50 - 50: OoooooooOO * i1IIi / oO0o
  if 83 - 83: i1IIi
  if 38 - 38: OoooooooOO * iIii1I11I1II1
  if 54 - 54: OoooooooOO . I1Ii111
  if 71 - 71: Ii1I
  if 31 - 31: I11i . i11iIiiIii . OoO0O00 * Oo0Ooo % Ii1I . o0oOOo0O0Ooo
  if 92 - 92: OoooooooOO / O0 * i1IIi + iIii1I11I1II1
  if 93 - 93: ooOoO0o % I1Ii111
  if 46 - 46: I1ii11iIi11i * OoOoOO00 * IiII * I1ii11iIi11i . I1ii11iIi11i
  if 43 - 43: ooOoO0o . i1IIi
  if 68 - 68: IiII % Oo0Ooo . O0 - OoOoOO00 + I1ii11iIi11i . i11iIiiIii
  if 45 - 45: I1IiiI
  if 17 - 17: OoooooooOO - ooOoO0o + Ii1I . OoooooooOO % Oo0Ooo
  if 92 - 92: I1Ii111 - OOooOOo % OoO0O00 - o0oOOo0O0Ooo % i1IIi
  if 38 - 38: I1ii11iIi11i . I11i / OoOoOO00 % I11i
  if 10 - 10: O0 . I1IiiI * o0oOOo0O0Ooo / iII111i
  if 61 - 61: Oo0Ooo - I1Ii111
  if 51 - 51: iII111i * ooOoO0o / O0 / O0
  if 52 - 52: OoooooooOO % O0
  if 56 - 56: oO0o - i1IIi * OoooooooOO - II111iiii
  if 28 - 28: i1IIi / I11i . o0oOOo0O0Ooo
  if 11 - 11: Oo0Ooo * OoooooooOO - i11iIiiIii
  if 13 - 13: i11iIiiIii . O0 / OOooOOo * i1IIi
  if 14 - 14: IiII + IiII . I11i / Ii1I . iIii1I11I1II1
  if 10 - 10: II111iiii . OOooOOo / iII111i
  if 35 - 35: iII111i / Oo0Ooo + O0 * iIii1I11I1II1 - O0
  if 3 - 3: I1ii11iIi11i
  if 42 - 42: I11i % Oo0Ooo + IiII - I11i . iIii1I11I1II1 - Ii1I
  if 27 - 27: iII111i % Oo0Ooo . I1ii11iIi11i . i1IIi % OoOoOO00 . o0oOOo0O0Ooo
  if 37 - 37: iII111i + I1Ii111 * Ii1I + IiII
  if 39 - 39: O0 * Oo0Ooo - I1IiiI + Ii1I / II111iiii
  if 66 - 66: ooOoO0o + oO0o % OoooooooOO
  if 23 - 23: oO0o . OoOoOO00 + iIii1I11I1II1
  if 17 - 17: IiII
  if 12 - 12: i1IIi . OoO0O00
  if 14 - 14: OOooOOo + II111iiii % OOooOOo . oO0o * ooOoO0o
  if 54 - 54: ooOoO0o * I11i - I1Ii111
  if 15 - 15: iII111i / O0
  if 61 - 61: i1IIi / i1IIi + ooOoO0o . I1Ii111 * ooOoO0o
class lisp_map_register ( ) :
 def __init__ ( self ) :
  self . proxy_reply_requested = False
  self . lisp_sec_present = False
  self . xtr_id_present = False
  self . map_notify_requested = False
  self . mobile_node = False
  self . merge_register_requested = False
  self . use_ttl_for_timeout = False
  self . map_register_refresh = False
  self . record_count = 0
  self . nonce = 0
  self . alg_id = 0
  self . key_id = 0
  self . auth_len = 0
  self . auth_data = 0
  self . xtr_id = 0
  self . site_id = 0
  self . record_count = 0
  self . sport = 0
  self . encrypt_bit = 0
  self . encryption_key_id = None
  if 19 - 19: o0oOOo0O0Ooo . II111iiii / i1IIi
  if 82 - 82: O0 / iII111i * OoO0O00 - I11i + Oo0Ooo
 def print_map_register ( self ) :
  IIiiII11i11I = lisp_hex_string ( self . xtr_id )
  if 95 - 95: Oo0Ooo / IiII + Oo0Ooo
  oOOo0ooO0 = ( "{} -> flags: {}{}{}{}{}{}{}{}{}, record-count: " +
 "{}, nonce: 0x{}, key/alg-id: {}/{}{}, auth-len: {}, xtr-id: " +
 "0x{}, site-id: {}" )
  if 94 - 94: ooOoO0o - i1IIi . O0 / I1IiiI
  lprint ( oOOo0ooO0 . format ( bold ( "Map-Register" , False ) , "P" if self . proxy_reply_requested else "p" ,
  # I1Ii111 - I1Ii111 - I1Ii111
 "S" if self . lisp_sec_present else "s" ,
 "I" if self . xtr_id_present else "i" ,
 "T" if self . use_ttl_for_timeout else "t" ,
 "R" if self . merge_register_requested else "r" ,
 "M" if self . mobile_node else "m" ,
 "N" if self . map_notify_requested else "n" ,
 "F" if self . map_register_refresh else "f" ,
 "E" if self . encrypt_bit else "e" ,
 self . record_count , lisp_hex_string ( self . nonce ) , self . key_id ,
 self . alg_id , " (sha1)" if ( self . key_id == LISP_SHA_1_96_ALG_ID ) else ( " (sha2)" if ( self . key_id == LISP_SHA_256_128_ALG_ID ) else "" ) , self . auth_len , IIiiII11i11I , self . site_id ) )
  if 92 - 92: I1IiiI . Ii1I
  if 60 - 60: I1ii11iIi11i * Oo0Ooo
  if 85 - 85: i1IIi * OoOoOO00
  if 99 - 99: Oo0Ooo
 def encode ( self ) :
  i1OOoO0OO0oO = ( LISP_MAP_REGISTER << 28 ) | self . record_count
  if ( self . proxy_reply_requested ) : i1OOoO0OO0oO |= 0x08000000
  if ( self . lisp_sec_present ) : i1OOoO0OO0oO |= 0x04000000
  if ( self . xtr_id_present ) : i1OOoO0OO0oO |= 0x02000000
  if ( self . map_register_refresh ) : i1OOoO0OO0oO |= 0x1000
  if ( self . use_ttl_for_timeout ) : i1OOoO0OO0oO |= 0x800
  if ( self . merge_register_requested ) : i1OOoO0OO0oO |= 0x400
  if ( self . mobile_node ) : i1OOoO0OO0oO |= 0x200
  if ( self . map_notify_requested ) : i1OOoO0OO0oO |= 0x100
  if ( self . encryption_key_id != None ) :
   i1OOoO0OO0oO |= 0x2000
   i1OOoO0OO0oO |= self . encryption_key_id << 14
   if 72 - 72: Oo0Ooo / II111iiii * ooOoO0o * I1ii11iIi11i - IiII / I1Ii111
   if 82 - 82: I1IiiI / I11i
   if 6 - 6: Ii1I / ooOoO0o / i11iIiiIii % o0oOOo0O0Ooo
   if 69 - 69: I1Ii111
   if 83 - 83: iIii1I11I1II1 . o0oOOo0O0Ooo + I1Ii111 . OoooooooOO / ooOoO0o + II111iiii
  if ( self . alg_id == LISP_NONE_ALG_ID ) :
   self . auth_len = 0
  else :
   if ( self . alg_id == LISP_SHA_1_96_ALG_ID ) :
    self . auth_len = LISP_SHA1_160_AUTH_DATA_LEN
    if 90 - 90: Ii1I * iII111i / OOooOOo
   if ( self . alg_id == LISP_SHA_256_128_ALG_ID ) :
    self . auth_len = LISP_SHA2_256_AUTH_DATA_LEN
    if 68 - 68: OoOoOO00
    if 65 - 65: oO0o
    if 82 - 82: o0oOOo0O0Ooo
  IiiiIi1iiii11 = struct . pack ( "I" , socket . htonl ( i1OOoO0OO0oO ) )
  IiiiIi1iiii11 += struct . pack ( "QBBH" , self . nonce , self . key_id , self . alg_id ,
 socket . htons ( self . auth_len ) )
  if 80 - 80: i1IIi % OoOoOO00 + OoO0O00 - OoooooooOO / iIii1I11I1II1 + I1Ii111
  IiiiIi1iiii11 = self . zero_auth ( IiiiIi1iiii11 )
  return ( IiiiIi1iiii11 )
  if 65 - 65: Ii1I
  if 71 - 71: I1Ii111 % I1Ii111 . oO0o + i11iIiiIii - i11iIiiIii
 def zero_auth ( self , packet ) :
  oO0ooOoO = struct . calcsize ( "I" ) + struct . calcsize ( "QHH" )
  Iiii = ""
  Ooo = 0
  if ( self . alg_id == LISP_NONE_ALG_ID ) : return ( packet )
  if ( self . alg_id == LISP_SHA_1_96_ALG_ID ) :
   Iiii = struct . pack ( "QQI" , 0 , 0 , 0 )
   Ooo = struct . calcsize ( "QQI" )
   if 97 - 97: I1Ii111 . o0oOOo0O0Ooo % O0 - I1Ii111 * OoooooooOO
  if ( self . alg_id == LISP_SHA_256_128_ALG_ID ) :
   Iiii = struct . pack ( "QQQQ" , 0 , 0 , 0 , 0 )
   Ooo = struct . calcsize ( "QQQQ" )
   if 20 - 20: OoooooooOO + OoooooooOO % oO0o % OoooooooOO
  packet = packet [ 0 : oO0ooOoO ] + Iiii + packet [ oO0ooOoO + Ooo : : ]
  return ( packet )
  if 73 - 73: I1IiiI % ooOoO0o % IiII + i1IIi - OoooooooOO / oO0o
  if 78 - 78: OoooooooOO % oO0o - i11iIiiIii
 def encode_auth ( self , packet ) :
  oO0ooOoO = struct . calcsize ( "I" ) + struct . calcsize ( "QHH" )
  Ooo = self . auth_len
  Iiii = self . auth_data
  packet = packet [ 0 : oO0ooOoO ] + Iiii + packet [ oO0ooOoO + Ooo : : ]
  return ( packet )
  if 37 - 37: IiII % Ii1I % i1IIi
  if 23 - 23: ooOoO0o - O0 + i11iIiiIii
 def decode ( self , packet ) :
  oO0ooOoOooO00o00 = packet
  O0O00Oo = "I"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( [ None , None ] )
  if 64 - 64: IiII . OOooOOo
  i1OOoO0OO0oO = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  i1OOoO0OO0oO = socket . ntohl ( i1OOoO0OO0oO [ 0 ] )
  packet = packet [ IiIii1i : : ]
  if 85 - 85: II111iiii % Ii1I * OoOoOO00
  O0O00Oo = "QBBH"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( [ None , None ] )
  if 33 - 33: i1IIi . i1IIi * OoooooooOO % I1Ii111 * o0oOOo0O0Ooo
  self . nonce , self . key_id , self . alg_id , self . auth_len = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  if 64 - 64: ooOoO0o / ooOoO0o + I1ii11iIi11i * OOooOOo % OOooOOo
  if 87 - 87: OoO0O00 * Oo0Ooo
  self . nonce = byte_swap_64 ( self . nonce )
  self . auth_len = socket . ntohs ( self . auth_len )
  self . proxy_reply_requested = True if ( i1OOoO0OO0oO & 0x08000000 ) else False
  if 83 - 83: i1IIi * I1Ii111 - IiII / Ii1I
  self . lisp_sec_present = True if ( i1OOoO0OO0oO & 0x04000000 ) else False
  self . xtr_id_present = True if ( i1OOoO0OO0oO & 0x02000000 ) else False
  self . use_ttl_for_timeout = True if ( i1OOoO0OO0oO & 0x800 ) else False
  self . map_register_refresh = True if ( i1OOoO0OO0oO & 0x1000 ) else False
  self . merge_register_requested = True if ( i1OOoO0OO0oO & 0x400 ) else False
  self . mobile_node = True if ( i1OOoO0OO0oO & 0x200 ) else False
  self . map_notify_requested = True if ( i1OOoO0OO0oO & 0x100 ) else False
  self . record_count = i1OOoO0OO0oO & 0xff
  if 48 - 48: oO0o . II111iiii - OoOoOO00 % i1IIi . OoOoOO00
  if 32 - 32: Ii1I * I1IiiI - OOooOOo . Oo0Ooo / O0 + Ii1I
  if 67 - 67: OoOoOO00 % Oo0Ooo
  if 7 - 7: i11iIiiIii % I1ii11iIi11i / I1Ii111 % Oo0Ooo - OoO0O00
  self . encrypt_bit = True if i1OOoO0OO0oO & 0x2000 else False
  if ( self . encrypt_bit ) :
   self . encryption_key_id = ( i1OOoO0OO0oO >> 14 ) & 0x7
   if 73 - 73: I1ii11iIi11i
   if 92 - 92: i11iIiiIii + O0 * I11i
   if 60 - 60: o0oOOo0O0Ooo / Oo0Ooo
   if 19 - 19: iIii1I11I1II1 . OoO0O00 / OoooooooOO
   if 2 - 2: O0 - O0 % I1Ii111 / I1ii11iIi11i
  if ( self . xtr_id_present ) :
   if ( self . decode_xtr_id ( oO0ooOoOooO00o00 ) == False ) : return ( [ None , None ] )
   if 76 - 76: OoO0O00 * oO0o - OoO0O00
   if 57 - 57: OoooooooOO / OoOoOO00 + oO0o . Ii1I
  packet = packet [ IiIii1i : : ]
  if 14 - 14: i11iIiiIii % OOooOOo * o0oOOo0O0Ooo * OoOoOO00
  if 55 - 55: I1Ii111 * OOooOOo * I1Ii111
  if 70 - 70: O0 . Ii1I
  if 33 - 33: OOooOOo * Ii1I
  if ( self . auth_len != 0 ) :
   if ( len ( packet ) < self . auth_len ) : return ( [ None , None ] )
   if 64 - 64: i11iIiiIii . iIii1I11I1II1
   if ( self . alg_id not in ( LISP_NONE_ALG_ID , LISP_SHA_1_96_ALG_ID ,
 LISP_SHA_256_128_ALG_ID ) ) :
    lprint ( "Invalid authentication alg-id: {}" . format ( self . alg_id ) )
    return ( [ None , None ] )
    if 7 - 7: OoOoOO00 % ooOoO0o + OoOoOO00 - OoOoOO00 * i11iIiiIii % OoO0O00
    if 57 - 57: OOooOOo / OoO0O00 + I1ii11iIi11i
   Ooo = self . auth_len
   if ( self . alg_id == LISP_SHA_1_96_ALG_ID ) :
    IiIii1i = struct . calcsize ( "QQI" )
    if ( Ooo < IiIii1i ) :
     lprint ( "Invalid sha1-96 authentication length" )
     return ( [ None , None ] )
     if 60 - 60: O0 * Oo0Ooo % OOooOOo + IiII . OoO0O00 . Oo0Ooo
    o0O0OoOOo0o , I1iIiiIii , O0OOOOO0O = struct . unpack ( "QQI" , packet [ : Ooo ] )
    ii111 = ""
   elif ( self . alg_id == LISP_SHA_256_128_ALG_ID ) :
    IiIii1i = struct . calcsize ( "QQQQ" )
    if ( Ooo < IiIii1i ) :
     lprint ( "Invalid sha2-256 authentication length" )
     return ( [ None , None ] )
     if 31 - 31: IiII . oO0o
    o0O0OoOOo0o , I1iIiiIii , O0OOOOO0O , ii111 = struct . unpack ( "QQQQ" ,
 packet [ : Ooo ] )
   else :
    lprint ( "Unsupported authentication alg-id value {}" . format ( self . alg_id ) )
    if 40 - 40: Ii1I - I11i / II111iiii * i1IIi + IiII * II111iiii
    return ( [ None , None ] )
    if 53 - 53: I1ii11iIi11i - i11iIiiIii . OoO0O00 / OoOoOO00 - I1Ii111
   self . auth_data = lisp_concat_auth_data ( self . alg_id , o0O0OoOOo0o , I1iIiiIii ,
 O0OOOOO0O , ii111 )
   oO0ooOoOooO00o00 = self . zero_auth ( oO0ooOoOooO00o00 )
   packet = packet [ self . auth_len : : ]
   if 99 - 99: Ii1I - IiII - i1IIi / i11iIiiIii . IiII
  return ( [ oO0ooOoOooO00o00 , packet ] )
  if 58 - 58: OOooOOo
  if 12 - 12: I1IiiI . o0oOOo0O0Ooo * OoooooooOO
 def encode_xtr_id ( self , packet ) :
  OOO0oo = self . xtr_id >> 64
  ii1iII1 = self . xtr_id & 0xffffffffffffffff
  OOO0oo = byte_swap_64 ( OOO0oo )
  ii1iII1 = byte_swap_64 ( ii1iII1 )
  Iii1I1 = byte_swap_64 ( self . site_id )
  packet += struct . pack ( "QQQ" , OOO0oo , ii1iII1 , Iii1I1 )
  return ( packet )
  if 87 - 87: OoooooooOO - oO0o - ooOoO0o * I1ii11iIi11i
  if 44 - 44: oO0o * II111iiii * II111iiii + I1IiiI / Oo0Ooo
 def decode_xtr_id ( self , packet ) :
  IiIii1i = struct . calcsize ( "QQQ" )
  if ( len ( packet ) < IiIii1i ) : return ( [ None , None ] )
  packet = packet [ len ( packet ) - IiIii1i : : ]
  OOO0oo , ii1iII1 , Iii1I1 = struct . unpack ( "QQQ" ,
 packet [ : IiIii1i ] )
  OOO0oo = byte_swap_64 ( OOO0oo )
  ii1iII1 = byte_swap_64 ( ii1iII1 )
  self . xtr_id = ( OOO0oo << 64 ) | ii1iII1
  self . site_id = byte_swap_64 ( Iii1I1 )
  return ( True )
  if 9 - 9: Oo0Ooo - IiII
  if 30 - 30: OoooooooOO % OOooOOo
  if 14 - 14: OoOoOO00 / OoO0O00 / i11iIiiIii - OoOoOO00 / o0oOOo0O0Ooo - OOooOOo
  if 81 - 81: iII111i % Ii1I . ooOoO0o
  if 66 - 66: I1ii11iIi11i * Ii1I / OoooooooOO * O0 % OOooOOo
  if 49 - 49: II111iiii . I1IiiI * O0 * Ii1I / I1Ii111 * OoooooooOO
  if 82 - 82: Oo0Ooo / Ii1I / Ii1I % Ii1I
  if 20 - 20: ooOoO0o
  if 63 - 63: iIii1I11I1II1 . OoO0O00
  if 100 - 100: i1IIi * i1IIi
  if 26 - 26: OOooOOo . OoO0O00 % OoOoOO00
  if 94 - 94: IiII
  if 15 - 15: Ii1I - IiII / O0
  if 28 - 28: I1Ii111 . i1IIi / I1ii11iIi11i
  if 77 - 77: i11iIiiIii / I1Ii111 / i11iIiiIii % OoOoOO00 - I1Ii111
  if 80 - 80: I1Ii111 % OoOoOO00 . OoooooooOO . II111iiii % IiII
  if 6 - 6: I1Ii111 % IiII / Ii1I + I1Ii111 . oO0o
  if 70 - 70: iIii1I11I1II1 / Ii1I
  if 61 - 61: O0 * o0oOOo0O0Ooo + I1Ii111 - OOooOOo . I1IiiI - IiII
  if 7 - 7: I1ii11iIi11i
  if 81 - 81: Oo0Ooo % II111iiii % o0oOOo0O0Ooo / I11i
  if 95 - 95: OoOoOO00 - O0 % OoooooooOO
  if 13 - 13: i11iIiiIii
  if 54 - 54: OOooOOo . I1ii11iIi11i * I11i % I1Ii111 . O0 * IiII
  if 87 - 87: Ii1I % I1ii11iIi11i * Oo0Ooo
  if 59 - 59: Oo0Ooo / I11i - iIii1I11I1II1 * iIii1I11I1II1
  if 18 - 18: I11i * I1ii11iIi11i / i11iIiiIii / iIii1I11I1II1 * OoooooooOO . OOooOOo
  if 69 - 69: Oo0Ooo * ooOoO0o
  if 91 - 91: o0oOOo0O0Ooo . ooOoO0o / OoO0O00 / i11iIiiIii * o0oOOo0O0Ooo
  if 52 - 52: I1IiiI - i11iIiiIii / IiII . oO0o
  if 38 - 38: oO0o + OoooooooOO * OoOoOO00 % oO0o
  if 91 - 91: i1IIi - I1ii11iIi11i * I1IiiI
  if 24 - 24: OoOoOO00 * Ii1I
class lisp_map_notify ( ) :
 def __init__ ( self , lisp_sockets ) :
  self . etr = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . etr_port = 0
  self . retransmit_timer = None
  self . lisp_sockets = lisp_sockets
  self . retry_count = 0
  self . record_count = 0
  self . alg_id = LISP_NONE_ALG_ID
  self . key_id = 0
  self . auth_len = 0
  self . auth_data = ""
  self . nonce = 0
  self . nonce_key = ""
  self . packet = None
  self . site = ""
  self . map_notify_ack = False
  self . eid_records = ""
  self . eid_list = [ ]
  if 17 - 17: OoO0O00 . I1IiiI * O0
  if 81 - 81: OOooOOo
 def print_notify ( self ) :
  Iiii = binascii . hexlify ( self . auth_data )
  if ( self . alg_id == LISP_SHA_1_96_ALG_ID and len ( Iiii ) != 40 ) :
   Iiii = self . auth_data
  elif ( self . alg_id == LISP_SHA_256_128_ALG_ID and len ( Iiii ) != 64 ) :
   Iiii = self . auth_data
   if 58 - 58: II111iiii . I1Ii111 . Ii1I * OoooooooOO / Ii1I / I11i
  oOOo0ooO0 = ( "{} -> record-count: {}, nonce: 0x{}, key/alg-id: " +
 "{}{}{}, auth-len: {}, auth-data: {}" )
  lprint ( oOOo0ooO0 . format ( bold ( "Map-Notify-Ack" , False ) if self . map_notify_ack else bold ( "Map-Notify" , False ) ,
  # OoOoOO00 + OoooooooOO % OoO0O00
 self . record_count , lisp_hex_string ( self . nonce ) , self . key_id ,
 self . alg_id , " (sha1)" if ( self . key_id == LISP_SHA_1_96_ALG_ID ) else ( " (sha2)" if ( self . key_id == LISP_SHA_256_128_ALG_ID ) else "" ) , self . auth_len , Iiii ) )
  if 83 - 83: ooOoO0o - Oo0Ooo . II111iiii + oO0o - I1ii11iIi11i
  if 10 - 10: OOooOOo . Ii1I
  if 5 - 5: IiII - I11i
  if 16 - 16: IiII . iII111i . Oo0Ooo % OOooOOo / IiII
 def zero_auth ( self , packet ) :
  if ( self . alg_id == LISP_NONE_ALG_ID ) : return ( packet )
  if ( self . alg_id == LISP_SHA_1_96_ALG_ID ) :
   Iiii = struct . pack ( "QQI" , 0 , 0 , 0 )
   if 72 - 72: o0oOOo0O0Ooo * ooOoO0o - i11iIiiIii / Ii1I
  if ( self . alg_id == LISP_SHA_256_128_ALG_ID ) :
   Iiii = struct . pack ( "QQQQ" , 0 , 0 , 0 , 0 )
   if 11 - 11: O0 - I1IiiI
  packet += Iiii
  return ( packet )
  if 31 - 31: iII111i
  if 1 - 1: I1Ii111 / OoOoOO00 * OoOoOO00 - o0oOOo0O0Ooo % Ii1I
 def encode ( self , eid_records , password ) :
  if ( self . map_notify_ack ) :
   i1OOoO0OO0oO = ( LISP_MAP_NOTIFY_ACK << 28 ) | self . record_count
  else :
   i1OOoO0OO0oO = ( LISP_MAP_NOTIFY << 28 ) | self . record_count
   if 96 - 96: IiII / Ii1I % OoO0O00 . iIii1I11I1II1
  IiiiIi1iiii11 = struct . pack ( "I" , socket . htonl ( i1OOoO0OO0oO ) )
  IiiiIi1iiii11 += struct . pack ( "QBBH" , self . nonce , self . key_id , self . alg_id ,
 socket . htons ( self . auth_len ) )
  if 30 - 30: I11i - OoO0O00
  if ( self . alg_id == LISP_NONE_ALG_ID ) :
   self . packet = IiiiIi1iiii11 + eid_records
   return ( self . packet )
   if 15 - 15: OoooooooOO
   if 31 - 31: II111iiii
   if 62 - 62: iIii1I11I1II1 % I1Ii111 % I1ii11iIi11i * IiII
   if 87 - 87: IiII
   if 45 - 45: oO0o + II111iiii * O0 % OOooOOo . iIii1I11I1II1
  IiiiIi1iiii11 = self . zero_auth ( IiiiIi1iiii11 )
  IiiiIi1iiii11 += eid_records
  if 55 - 55: IiII
  I1iI1111ii1I1 = lisp_hash_me ( IiiiIi1iiii11 , self . alg_id , password , False )
  if 43 - 43: OOooOOo
  oO0ooOoO = struct . calcsize ( "I" ) + struct . calcsize ( "QHH" )
  Ooo = self . auth_len
  self . auth_data = I1iI1111ii1I1
  IiiiIi1iiii11 = IiiiIi1iiii11 [ 0 : oO0ooOoO ] + I1iI1111ii1I1 + IiiiIi1iiii11 [ oO0ooOoO + Ooo : : ]
  self . packet = IiiiIi1iiii11
  return ( IiiiIi1iiii11 )
  if 17 - 17: i11iIiiIii
  if 94 - 94: OoooooooOO - IiII + oO0o . OoooooooOO / i1IIi
 def decode ( self , packet ) :
  oO0ooOoOooO00o00 = packet
  O0O00Oo = "I"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 53 - 53: I1Ii111 % I1ii11iIi11i
  i1OOoO0OO0oO = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  i1OOoO0OO0oO = socket . ntohl ( i1OOoO0OO0oO [ 0 ] )
  self . map_notify_ack = ( ( i1OOoO0OO0oO >> 28 ) == LISP_MAP_NOTIFY_ACK )
  self . record_count = i1OOoO0OO0oO & 0xff
  packet = packet [ IiIii1i : : ]
  if 17 - 17: OoooooooOO % Ii1I % O0
  O0O00Oo = "QBBH"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 46 - 46: iII111i + I1Ii111 % OoooooooOO * I1ii11iIi11i
  self . nonce , self . key_id , self . alg_id , self . auth_len = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  if 89 - 89: IiII - IiII % iII111i / I11i + oO0o - IiII
  self . nonce_key = lisp_hex_string ( self . nonce )
  self . auth_len = socket . ntohs ( self . auth_len )
  packet = packet [ IiIii1i : : ]
  self . eid_records = packet [ self . auth_len : : ]
  if 97 - 97: Ii1I % OoOoOO00 / I1ii11iIi11i / iIii1I11I1II1 * OoooooooOO * OOooOOo
  if ( self . auth_len == 0 ) : return ( self . eid_records )
  if 80 - 80: oO0o / O0
  if 55 - 55: I1IiiI * I11i / O0 % OoOoOO00
  if 71 - 71: i11iIiiIii * OoOoOO00 * OOooOOo + oO0o + Oo0Ooo
  if 59 - 59: IiII
  if ( len ( packet ) < self . auth_len ) : return ( None )
  if 54 - 54: OOooOOo
  Ooo = self . auth_len
  if ( self . alg_id == LISP_SHA_1_96_ALG_ID ) :
   o0O0OoOOo0o , I1iIiiIii , O0OOOOO0O = struct . unpack ( "QQI" , packet [ : Ooo ] )
   ii111 = ""
   if 27 - 27: OoOoOO00 - OoO0O00 + o0oOOo0O0Ooo + ooOoO0o . OoO0O00
  if ( self . alg_id == LISP_SHA_256_128_ALG_ID ) :
   o0O0OoOOo0o , I1iIiiIii , O0OOOOO0O , ii111 = struct . unpack ( "QQQQ" ,
 packet [ : Ooo ] )
   if 86 - 86: II111iiii - OoooooooOO - ooOoO0o % iII111i
  self . auth_data = lisp_concat_auth_data ( self . alg_id , o0O0OoOOo0o , I1iIiiIii ,
 O0OOOOO0O , ii111 )
  if 16 - 16: ooOoO0o + Oo0Ooo + OoooooooOO
  IiIii1i = struct . calcsize ( "I" ) + struct . calcsize ( "QHH" )
  packet = self . zero_auth ( oO0ooOoOooO00o00 [ : IiIii1i ] )
  IiIii1i += Ooo
  packet += oO0ooOoOooO00o00 [ IiIii1i : : ]
  return ( packet )
  if 87 - 87: I1IiiI . oO0o / IiII - OoooooooOO
  if 33 - 33: oO0o % OoO0O00 . iIii1I11I1II1 / IiII
  if 3 - 3: Ii1I + OoO0O00
  if 60 - 60: OoO0O00 . OoOoOO00 - I1ii11iIi11i - I1IiiI - II111iiii % Oo0Ooo
  if 62 - 62: O0 + iII111i - iII111i % iIii1I11I1II1
  if 47 - 47: I1Ii111 + I1IiiI
  if 40 - 40: iIii1I11I1II1 % Ii1I + II111iiii - I1IiiI
  if 80 - 80: oO0o
  if 81 - 81: OoooooooOO / ooOoO0o * iIii1I11I1II1 . Oo0Ooo + oO0o / O0
  if 84 - 84: II111iiii - o0oOOo0O0Ooo
  if 78 - 78: IiII
  if 58 - 58: i11iIiiIii - OoOoOO00
  if 67 - 67: I1ii11iIi11i / iII111i + iIii1I11I1II1 % I1IiiI
  if 99 - 99: ooOoO0o . Ii1I
  if 92 - 92: i1IIi
  if 68 - 68: OoO0O00 % IiII - oO0o - ooOoO0o . Oo0Ooo
  if 30 - 30: OoooooooOO % o0oOOo0O0Ooo + ooOoO0o * OoO0O00
  if 57 - 57: I11i + iIii1I11I1II1 . OoO0O00 + oO0o
  if 4 - 4: Ii1I
  if 43 - 43: i1IIi . I1IiiI * iIii1I11I1II1 * i11iIiiIii - OOooOOo + ooOoO0o
  if 56 - 56: Oo0Ooo % i11iIiiIii / Ii1I . I1Ii111 . OoO0O00 - OoOoOO00
  if 32 - 32: I1Ii111 / oO0o / I1IiiI
  if 22 - 22: OoO0O00 - OoOoOO00 . Oo0Ooo + o0oOOo0O0Ooo
  if 69 - 69: oO0o - I1IiiI
  if 10 - 10: i1IIi / iII111i . II111iiii * i1IIi % OoooooooOO
  if 83 - 83: I11i . OOooOOo + I1Ii111 * I11i . I1Ii111 + oO0o
  if 64 - 64: Ii1I . o0oOOo0O0Ooo - i1IIi
  if 35 - 35: I1ii11iIi11i % OoooooooOO
  if 59 - 59: I1IiiI % I11i
  if 32 - 32: I1IiiI * O0 + O0
  if 34 - 34: IiII
  if 5 - 5: OoO0O00 . I1IiiI
  if 48 - 48: Oo0Ooo - OoO0O00 . I11i - iIii1I11I1II1 % Ii1I
  if 47 - 47: iII111i / OoooooooOO - II111iiii
  if 91 - 91: OoOoOO00 + o0oOOo0O0Ooo
  if 23 - 23: i1IIi
  if 9 - 9: i1IIi % I1Ii111 - OoO0O00 * OoOoOO00 . o0oOOo0O0Ooo
  if 18 - 18: Ii1I . OoOoOO00 + iII111i . I1IiiI + OoooooooOO . OoO0O00
  if 31 - 31: I1Ii111 - I11i
  if 49 - 49: iIii1I11I1II1 - iIii1I11I1II1 - OoOoOO00 + IiII / OoOoOO00
  if 74 - 74: OoooooooOO + I1ii11iIi11i % O0
  if 32 - 32: I1ii11iIi11i + I1ii11iIi11i
  if 89 - 89: ooOoO0o + oO0o + Ii1I - OOooOOo
  if 12 - 12: OoOoOO00 - o0oOOo0O0Ooo - I1Ii111 / I11i
  if 17 - 17: OoO0O00 - I1Ii111 - II111iiii / I1Ii111 / Ii1I
  if 30 - 30: OOooOOo * I1ii11iIi11i % I1ii11iIi11i + iII111i * IiII
  if 33 - 33: o0oOOo0O0Ooo + I11i * O0 * OoO0O00 . I1ii11iIi11i
  if 74 - 74: iII111i * iII111i * o0oOOo0O0Ooo / oO0o
  if 91 - 91: i11iIiiIii . I1ii11iIi11i / II111iiii
  if 97 - 97: Ii1I % i1IIi % IiII + Oo0Ooo - O0 - I11i
class lisp_map_request ( ) :
 def __init__ ( self ) :
  self . auth_bit = False
  self . map_data_present = False
  self . rloc_probe = False
  self . smr_bit = False
  self . pitr_bit = False
  self . smr_invoked_bit = False
  self . mobile_node = False
  self . xtr_id_present = False
  self . local_xtr = False
  self . dont_reply_bit = False
  self . itr_rloc_count = 0
  self . record_count = 0
  self . nonce = 0
  self . signature_eid = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . source_eid = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . target_eid = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . target_group = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . itr_rlocs = [ ]
  self . keys = None
  self . privkey_filename = None
  self . map_request_signature = None
  self . subscribe_bit = False
  self . xtr_id = None
  self . json_telemetry = None
  if 64 - 64: Ii1I - iII111i
  if 12 - 12: i1IIi
 def print_prefix ( self ) :
  if ( self . target_group . is_null ( ) ) :
   return ( green ( self . target_eid . print_prefix ( ) , False ) )
   if 99 - 99: II111iiii - I1ii11iIi11i * IiII
  return ( green ( self . target_eid . print_sg ( self . target_group ) , False ) )
  if 3 - 3: IiII - I1ii11iIi11i * iII111i * I1ii11iIi11i + Oo0Ooo
  if 15 - 15: I1ii11iIi11i * Ii1I / iII111i . o0oOOo0O0Ooo / Ii1I % OoOoOO00
 def print_map_request ( self ) :
  IIiiII11i11I = ""
  if ( self . xtr_id != None and self . subscribe_bit ) :
   IIiiII11i11I = "subscribe, xtr-id: 0x{}, " . format ( lisp_hex_string ( self . xtr_id ) )
   if 75 - 75: OoooooooOO % i11iIiiIii % iIii1I11I1II1 % I1ii11iIi11i / i11iIiiIii
   if 96 - 96: ooOoO0o * oO0o / iIii1I11I1II1 / I11i
   if 5 - 5: o0oOOo0O0Ooo
  oOOo0ooO0 = ( "{} -> flags: {}{}{}{}{}{}{}{}{}{}, itr-rloc-" +
 "count: {} (+1), record-count: {}, nonce: 0x{}, source-eid: " +
 "afi {}, {}{}, target-eid: afi {}, {}, {}ITR-RLOCs:" )
  if 83 - 83: I11i * I1IiiI . II111iiii * i1IIi % O0
  lprint ( oOOo0ooO0 . format ( bold ( "Map-Request" , False ) , "A" if self . auth_bit else "a" ,
  # Ii1I % Oo0Ooo + OoO0O00
 "D" if self . map_data_present else "d" ,
 "R" if self . rloc_probe else "r" ,
 "S" if self . smr_bit else "s" ,
 "P" if self . pitr_bit else "p" ,
 "I" if self . smr_invoked_bit else "i" ,
 "M" if self . mobile_node else "m" ,
 "X" if self . xtr_id_present else "x" ,
 "L" if self . local_xtr else "l" ,
 "D" if self . dont_reply_bit else "d" , self . itr_rloc_count ,
 self . record_count , lisp_hex_string ( self . nonce ) ,
 self . source_eid . afi , green ( self . source_eid . print_address ( ) , False ) ,
 " (with sig)" if self . map_request_signature != None else "" ,
 self . target_eid . afi , green ( self . print_prefix ( ) , False ) , IIiiII11i11I ) )
  if 92 - 92: OOooOOo
  iIi11III = self . keys
  for OooO0OO0 in self . itr_rlocs :
   if ( OooO0OO0 . afi == LISP_AFI_LCAF and self . json_telemetry != None ) :
    continue
    if 98 - 98: Oo0Ooo + OoOoOO00 * OOooOOo / iII111i * OoOoOO00 / OoooooooOO
   IiI = red ( OooO0OO0 . print_address_no_iid ( ) , False )
   lprint ( "  itr-rloc: afi {} {}{}" . format ( OooO0OO0 . afi , IiI ,
 "" if ( iIi11III == None ) else ", " + iIi11III [ 1 ] . print_keys ( ) ) )
   iIi11III = None
   if 68 - 68: iIii1I11I1II1
  if ( self . json_telemetry != None ) :
   lprint ( "  itr-rloc: afi {} telemetry: {}" . format ( LISP_AFI_LCAF ,
 self . json_telemetry ) )
   if 51 - 51: OoOoOO00 + IiII
   if 55 - 55: Oo0Ooo % I1Ii111 . II111iiii
   if 53 - 53: O0 / OoO0O00 % i11iIiiIii
 def sign_map_request ( self , privkey ) :
  I1IiI11 = self . signature_eid . print_address ( )
  i1i1Ii1iiII1I = self . source_eid . print_address ( )
  IIIII11IIi = self . target_eid . print_address ( )
  i11I1iiI1iI = lisp_hex_string ( self . nonce ) + i1i1Ii1iiII1I + IIIII11IIi
  self . map_request_signature = privkey . sign ( i11I1iiI1iI )
  i1i11 = binascii . b2a_base64 ( self . map_request_signature )
  i1i11 = { "source-eid" : i1i1Ii1iiII1I , "signature-eid" : I1IiI11 ,
 "signature" : i1i11 }
  return ( json . dumps ( i1i11 ) )
  if 77 - 77: iIii1I11I1II1 * OoOoOO00 + i11iIiiIii * ooOoO0o
  if 81 - 81: Ii1I * iII111i % Ii1I % i11iIiiIii % i1IIi / o0oOOo0O0Ooo
 def verify_map_request_sig ( self , pubkey ) :
  oOO00oo = green ( self . signature_eid . print_address ( ) , False )
  if ( pubkey == None ) :
   lprint ( "Public-key not found for signature-EID {}" . format ( oOO00oo ) )
   return ( False )
   if 41 - 41: iII111i + I11i . oO0o - ooOoO0o . OoooooooOO
   if 83 - 83: OoooooooOO * iIii1I11I1II1 . OoooooooOO / II111iiii . OoooooooOO - IiII
  i1i1Ii1iiII1I = self . source_eid . print_address ( )
  IIIII11IIi = self . target_eid . print_address ( )
  i11I1iiI1iI = lisp_hex_string ( self . nonce ) + i1i1Ii1iiII1I + IIIII11IIi
  pubkey = binascii . a2b_base64 ( pubkey )
  if 90 - 90: Oo0Ooo % i11iIiiIii + O0 % O0
  OoOoO00OoOOo = True
  try :
   o0Oo = ecdsa . VerifyingKey . from_pem ( pubkey )
  except :
   lprint ( "Invalid public-key in mapping system for sig-eid {}" . format ( self . signature_eid . print_address_no_iid ( ) ) )
   if 64 - 64: Ii1I
   OoOoO00OoOOo = False
   if 55 - 55: I11i - I11i + ooOoO0o
   if 87 - 87: OoooooooOO / OoOoOO00 . iIii1I11I1II1 / II111iiii
  if ( OoOoO00OoOOo ) :
   try :
    OoOoO00OoOOo = o0Oo . verify ( self . map_request_signature , i11I1iiI1iI )
   except :
    OoOoO00OoOOo = False
    if 27 - 27: i1IIi - iIii1I11I1II1 + O0 % Oo0Ooo / OOooOOo + i1IIi
    if 48 - 48: Oo0Ooo
    if 70 - 70: OoooooooOO * i11iIiiIii
  O0Oo = bold ( "passed" if OoOoO00OoOOo else "failed" , False )
  lprint ( "Signature verification {} for EID {}" . format ( O0Oo , oOO00oo ) )
  return ( OoOoO00OoOOo )
  if 58 - 58: I1ii11iIi11i * i11iIiiIii
  if 47 - 47: O0 . I1IiiI / ooOoO0o % i11iIiiIii
 def encode_json ( self , json_string ) :
  OOOoooO000O0 = LISP_LCAF_JSON_TYPE
  I1i = socket . htons ( LISP_AFI_LCAF )
  iII = socket . htons ( len ( json_string ) + 4 )
  IIIii1i11111 = socket . htons ( len ( json_string ) )
  IiiiIi1iiii11 = struct . pack ( "HBBBBHH" , I1i , 0 , 0 , OOOoooO000O0 , 0 , iII ,
 IIIii1i11111 )
  IiiiIi1iiii11 += json_string
  IiiiIi1iiii11 += struct . pack ( "H" , 0 )
  return ( IiiiIi1iiii11 )
  if 12 - 12: ooOoO0o % OoOoOO00
  if 1 - 1: O0 / ooOoO0o
 def encode ( self , probe_dest , probe_port ) :
  i1OOoO0OO0oO = ( LISP_MAP_REQUEST << 28 ) | self . record_count
  if 83 - 83: Ii1I / OoooooooOO * oO0o . I1IiiI . i1IIi
  O00O00Oo = lisp_telemetry_configured ( ) if ( self . rloc_probe ) else None
  if ( O00O00Oo != None ) : self . itr_rloc_count += 1
  i1OOoO0OO0oO = i1OOoO0OO0oO | ( self . itr_rloc_count << 8 )
  if 62 - 62: oO0o / Oo0Ooo
  if ( self . auth_bit ) : i1OOoO0OO0oO |= 0x08000000
  if ( self . map_data_present ) : i1OOoO0OO0oO |= 0x04000000
  if ( self . rloc_probe ) : i1OOoO0OO0oO |= 0x02000000
  if ( self . smr_bit ) : i1OOoO0OO0oO |= 0x01000000
  if ( self . pitr_bit ) : i1OOoO0OO0oO |= 0x00800000
  if ( self . smr_invoked_bit ) : i1OOoO0OO0oO |= 0x00400000
  if ( self . mobile_node ) : i1OOoO0OO0oO |= 0x00200000
  if ( self . xtr_id_present ) : i1OOoO0OO0oO |= 0x00100000
  if ( self . local_xtr ) : i1OOoO0OO0oO |= 0x00004000
  if ( self . dont_reply_bit ) : i1OOoO0OO0oO |= 0x00002000
  if 10 - 10: O0 + iII111i + i11iIiiIii % iIii1I11I1II1 * iII111i * Oo0Ooo
  IiiiIi1iiii11 = struct . pack ( "I" , socket . htonl ( i1OOoO0OO0oO ) )
  IiiiIi1iiii11 += struct . pack ( "Q" , self . nonce )
  if 55 - 55: i11iIiiIii
  if 11 - 11: ooOoO0o . I1Ii111 - iII111i . o0oOOo0O0Ooo
  if 41 - 41: oO0o / OoO0O00 - OoO0O00 + ooOoO0o * OOooOOo
  if 13 - 13: I1Ii111 * II111iiii - OoOoOO00
  if 3 - 3: OOooOOo + ooOoO0o * i11iIiiIii . iII111i / iIii1I11I1II1
  if 44 - 44: OoO0O00
  O00oO0ooooOOo = False
  oo0i1ii = self . privkey_filename
  if ( oo0i1ii != None and os . path . exists ( oo0i1ii ) ) :
   I1ii1ii = open ( oo0i1ii , "r" ) ; o0Oo = I1ii1ii . read ( ) ; I1ii1ii . close ( )
   try :
    o0Oo = ecdsa . SigningKey . from_pem ( o0Oo )
   except :
    return ( None )
    if 22 - 22: i11iIiiIii
   o0Ooo = self . sign_map_request ( o0Oo )
   O00oO0ooooOOo = True
  elif ( self . map_request_signature != None ) :
   i1i11 = binascii . b2a_base64 ( self . map_request_signature )
   o0Ooo = { "source-eid" : self . source_eid . print_address ( ) ,
 "signature-eid" : self . signature_eid . print_address ( ) ,
 "signature" : i1i11 }
   o0Ooo = json . dumps ( o0Ooo )
   O00oO0ooooOOo = True
   if 1 - 1: Ii1I - iIii1I11I1II1 * Ii1I . i11iIiiIii
  if ( O00oO0ooooOOo ) :
   IiiiIi1iiii11 += self . encode_json ( o0Ooo )
  else :
   if ( self . source_eid . instance_id != 0 ) :
    IiiiIi1iiii11 += struct . pack ( "H" , socket . htons ( LISP_AFI_LCAF ) )
    IiiiIi1iiii11 += self . source_eid . lcaf_encode_iid ( )
   else :
    IiiiIi1iiii11 += struct . pack ( "H" , socket . htons ( self . source_eid . afi ) )
    IiiiIi1iiii11 += self . source_eid . pack_address ( )
    if 96 - 96: Ii1I + iII111i - OoOoOO00 . I11i * o0oOOo0O0Ooo - Ii1I
    if 73 - 73: Oo0Ooo - I11i - ooOoO0o / I1Ii111 * IiII
    if 55 - 55: i1IIi / I1Ii111 . iII111i
    if 98 - 98: i1IIi % O0 . ooOoO0o * O0
    if 10 - 10: OOooOOo / Oo0Ooo - o0oOOo0O0Ooo / ooOoO0o % ooOoO0o / OoooooooOO
    if 26 - 26: Oo0Ooo . i1IIi / i11iIiiIii + I1Ii111 / II111iiii - I1ii11iIi11i
    if 71 - 71: iIii1I11I1II1 + O0 . IiII . iII111i % o0oOOo0O0Ooo % O0
  if ( probe_dest ) :
   if ( probe_port == 0 ) : probe_port = LISP_DATA_PORT
   oo0o00OO = probe_dest . print_address_no_iid ( ) + ":" + str ( probe_port )
   if 51 - 51: o0oOOo0O0Ooo - Ii1I - iIii1I11I1II1 * iIii1I11I1II1 * o0oOOo0O0Ooo - O0
   if ( lisp_crypto_keys_by_rloc_encap . has_key ( oo0o00OO ) ) :
    self . keys = lisp_crypto_keys_by_rloc_encap [ oo0o00OO ]
    if 27 - 27: i1IIi . I1Ii111
    if 64 - 64: ooOoO0o / i1IIi
    if 100 - 100: II111iiii
    if 16 - 16: Ii1I
    if 96 - 96: o0oOOo0O0Ooo / I1Ii111 % Ii1I - ooOoO0o
    if 35 - 35: OOooOOo
    if 90 - 90: i11iIiiIii
  for OooO0OO0 in self . itr_rlocs :
   if ( lisp_data_plane_security and self . itr_rlocs . index ( OooO0OO0 ) == 0 ) :
    if ( self . keys == None or self . keys [ 1 ] == None ) :
     iIi11III = lisp_keys ( 1 )
     self . keys = [ None , iIi11III , None , None ]
     if 47 - 47: OoO0O00 . i11iIiiIii
    iIi11III = self . keys [ 1 ]
    iIi11III . add_key_by_nonce ( self . nonce )
    IiiiIi1iiii11 += iIi11III . encode_lcaf ( OooO0OO0 )
   else :
    IiiiIi1iiii11 += struct . pack ( "H" , socket . htons ( OooO0OO0 . afi ) )
    IiiiIi1iiii11 += OooO0OO0 . pack_address ( )
    if 9 - 9: OoOoOO00 - I11i . OoooooooOO % ooOoO0o
    if 13 - 13: OoO0O00 * iIii1I11I1II1 + II111iiii - Oo0Ooo - OoOoOO00
    if 43 - 43: iII111i / I1Ii111 * I1IiiI % ooOoO0o % I1IiiI
    if 18 - 18: OoO0O00
    if 99 - 99: iII111i / oO0o . i11iIiiIii / I11i + i1IIi - I11i
    if 50 - 50: i1IIi
  if ( O00O00Oo != None ) :
   i1 = str ( time . time ( ) )
   O00O00Oo = lisp_encode_telemetry ( O00O00Oo , io = i1 )
   self . json_telemetry = O00O00Oo
   IiiiIi1iiii11 += self . encode_json ( O00O00Oo )
   if 56 - 56: OoO0O00 + I1Ii111 / Ii1I
   if 75 - 75: OoOoOO00
  oO00OO0Ooo00O = 0 if self . target_eid . is_binary ( ) == False else self . target_eid . mask_len
  if 45 - 45: OoO0O00 * II111iiii * OoOoOO00 - OOooOOo % oO0o - Oo0Ooo
  if 4 - 4: o0oOOo0O0Ooo . OoOoOO00 - iIii1I11I1II1 / IiII / I1IiiI % I1IiiI
  Iiii1I = 0
  if ( self . subscribe_bit ) :
   Iiii1I = 0x80
   self . xtr_id_present = True
   if ( self . xtr_id == None ) :
    self . xtr_id = random . randint ( 0 , ( 2 ** 128 ) - 1 )
    if 26 - 26: Oo0Ooo + OoooooooOO - OOooOOo * II111iiii / iII111i
    if 77 - 77: I11i
    if 50 - 50: o0oOOo0O0Ooo - OoOoOO00
  O0O00Oo = "BB"
  IiiiIi1iiii11 += struct . pack ( O0O00Oo , Iiii1I , oO00OO0Ooo00O )
  if 1 - 1: i1IIi / Ii1I % IiII - I11i % o0oOOo0O0Ooo
  if ( self . target_group . is_null ( ) == False ) :
   IiiiIi1iiii11 += struct . pack ( "H" , socket . htons ( LISP_AFI_LCAF ) )
   IiiiIi1iiii11 += self . target_eid . lcaf_encode_sg ( self . target_group )
  elif ( self . target_eid . instance_id != 0 or
 self . target_eid . is_geo_prefix ( ) ) :
   IiiiIi1iiii11 += struct . pack ( "H" , socket . htons ( LISP_AFI_LCAF ) )
   IiiiIi1iiii11 += self . target_eid . lcaf_encode_iid ( )
  else :
   IiiiIi1iiii11 += struct . pack ( "H" , socket . htons ( self . target_eid . afi ) )
   IiiiIi1iiii11 += self . target_eid . pack_address ( )
   if 28 - 28: ooOoO0o - IiII + iII111i . ooOoO0o % OoooooooOO
   if 17 - 17: OOooOOo / iII111i / IiII / OoO0O00 . I11i / o0oOOo0O0Ooo
   if 1 - 1: iIii1I11I1II1 + IiII % ooOoO0o + O0 / iIii1I11I1II1 % OoO0O00
   if 83 - 83: i11iIiiIii * II111iiii . i1IIi * I1Ii111
   if 48 - 48: iIii1I11I1II1
  if ( self . subscribe_bit ) : IiiiIi1iiii11 = self . encode_xtr_id ( IiiiIi1iiii11 )
  return ( IiiiIi1iiii11 )
  if 69 - 69: OoOoOO00 - OoO0O00 - iIii1I11I1II1 % Oo0Ooo - I1Ii111
  if 77 - 77: oO0o % O0 % O0 - iII111i - iII111i - I1IiiI
 def lcaf_decode_json ( self , packet ) :
  O0O00Oo = "BBBBHH"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 37 - 37: iIii1I11I1II1
  iI1i , O0OooO00O0 , OOOoooO000O0 , iiI1i111I1 , iII , IIIii1i11111 = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  if 26 - 26: OoooooooOO . i1IIi + OoO0O00
  if 42 - 42: i11iIiiIii * o0oOOo0O0Ooo % I11i % Oo0Ooo + o0oOOo0O0Ooo * i11iIiiIii
  if ( OOOoooO000O0 != LISP_LCAF_JSON_TYPE ) : return ( packet )
  if 66 - 66: Ii1I / IiII . OoooooooOO * Oo0Ooo % i11iIiiIii
  if 100 - 100: I1ii11iIi11i % II111iiii * i11iIiiIii - iII111i
  if 69 - 69: OOooOOo + iII111i / I1Ii111
  if 37 - 37: iIii1I11I1II1 * I11i / IiII * Oo0Ooo % i11iIiiIii
  iII = socket . ntohs ( iII )
  IIIii1i11111 = socket . ntohs ( IIIii1i11111 )
  packet = packet [ IiIii1i : : ]
  if ( len ( packet ) < iII ) : return ( None )
  if ( iII != IIIii1i11111 + 2 ) : return ( None )
  if 93 - 93: ooOoO0o + ooOoO0o
  if 65 - 65: OoooooooOO * I11i * oO0o % I1ii11iIi11i * II111iiii
  if 86 - 86: i11iIiiIii / I11i * iII111i - iII111i
  if 32 - 32: Oo0Ooo . O0
  o0Ooo = packet [ 0 : IIIii1i11111 ]
  packet = packet [ IIIii1i11111 : : ]
  if 48 - 48: I1ii11iIi11i % II111iiii + I11i
  if 25 - 25: IiII * o0oOOo0O0Ooo / I1IiiI . IiII % II111iiii
  if 50 - 50: OoOoOO00 * iII111i
  if 59 - 59: I1IiiI * I1IiiI / I11i
  if ( lisp_is_json_telemetry ( o0Ooo ) != None ) :
   self . json_telemetry = o0Ooo
   if 92 - 92: o0oOOo0O0Ooo
   if 8 - 8: iII111i + I1ii11iIi11i . Ii1I
   if 50 - 50: Oo0Ooo
   if 16 - 16: Ii1I - OoOoOO00 % Oo0Ooo / Ii1I . I11i + ooOoO0o
   if 78 - 78: iIii1I11I1II1 + OoO0O00 + i11iIiiIii
  O0O00Oo = "H"
  IiIii1i = struct . calcsize ( O0O00Oo )
  IiiiII = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] ) [ 0 ]
  packet = packet [ IiIii1i : : ]
  if ( IiiiII != 0 ) : return ( packet )
  if 21 - 21: Oo0Ooo + Ii1I % ooOoO0o + OoOoOO00 % I11i
  if ( self . json_telemetry != None ) : return ( packet )
  if 22 - 22: i1IIi / OoooooooOO . OoO0O00
  if 83 - 83: I1IiiI - OoooooooOO + I1ii11iIi11i . Ii1I / o0oOOo0O0Ooo + ooOoO0o
  if 90 - 90: I1IiiI - i11iIiiIii
  if 42 - 42: OOooOOo . Oo0Ooo
  try :
   o0Ooo = json . loads ( o0Ooo )
  except :
   return ( None )
   if 21 - 21: iII111i . I1IiiI / I11i
   if 97 - 97: iIii1I11I1II1 + i1IIi - o0oOOo0O0Ooo
   if 73 - 73: OoO0O00 - i11iIiiIii % I1Ii111 / Oo0Ooo - OoooooooOO % OOooOOo
   if 79 - 79: I1IiiI / o0oOOo0O0Ooo . Ii1I * I1ii11iIi11i + I11i
   if 96 - 96: OoO0O00 * II111iiii
  if ( o0Ooo . has_key ( "source-eid" ) == False ) : return ( packet )
  iiI1I1IIi = o0Ooo [ "source-eid" ]
  IiiiII = LISP_AFI_IPV4 if iiI1I1IIi . count ( "." ) == 3 else LISP_AFI_IPV6 if iiI1I1IIi . count ( ":" ) == 7 else None
  if 44 - 44: I11i
  if ( IiiiII == None ) :
   lprint ( "Bad JSON 'source-eid' value: {}" . format ( iiI1I1IIi ) )
   return ( None )
   if 3 - 3: iIii1I11I1II1 - i1IIi / iII111i + i1IIi + O0
   if 18 - 18: iIii1I11I1II1 . iII111i % OOooOOo % oO0o + iIii1I11I1II1 * OoooooooOO
  self . source_eid . afi = IiiiII
  self . source_eid . store_address ( iiI1I1IIi )
  if 78 - 78: IiII
  if ( o0Ooo . has_key ( "signature-eid" ) == False ) : return ( packet )
  iiI1I1IIi = o0Ooo [ "signature-eid" ]
  if ( iiI1I1IIi . count ( ":" ) != 7 ) :
   lprint ( "Bad JSON 'signature-eid' value: {}" . format ( iiI1I1IIi ) )
   return ( None )
   if 38 - 38: OoO0O00 * I1ii11iIi11i
   if 4 - 4: OoO0O00 . I1ii11iIi11i
  self . signature_eid . afi = LISP_AFI_IPV6
  self . signature_eid . store_address ( iiI1I1IIi )
  if 21 - 21: i11iIiiIii / OoO0O00 / I1ii11iIi11i * O0 - II111iiii * OOooOOo
  if ( o0Ooo . has_key ( "signature" ) == False ) : return ( packet )
  i1i11 = binascii . a2b_base64 ( o0Ooo [ "signature" ] )
  self . map_request_signature = i1i11
  return ( packet )
  if 27 - 27: o0oOOo0O0Ooo . OoOoOO00 * Ii1I * iII111i * O0
  if 93 - 93: IiII % I1Ii111 % II111iiii
 def decode ( self , packet , source , port ) :
  O0O00Oo = "I"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 20 - 20: OoooooooOO * I1Ii111
  i1OOoO0OO0oO = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  i1OOoO0OO0oO = i1OOoO0OO0oO [ 0 ]
  packet = packet [ IiIii1i : : ]
  if 38 - 38: iII111i . OoooooooOO
  O0O00Oo = "Q"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 28 - 28: I1Ii111 * i1IIi . I1ii11iIi11i
  o0OOO = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  packet = packet [ IiIii1i : : ]
  if 75 - 75: O0 / oO0o * ooOoO0o - OOooOOo / i1IIi
  i1OOoO0OO0oO = socket . ntohl ( i1OOoO0OO0oO )
  self . auth_bit = True if ( i1OOoO0OO0oO & 0x08000000 ) else False
  self . map_data_present = True if ( i1OOoO0OO0oO & 0x04000000 ) else False
  self . rloc_probe = True if ( i1OOoO0OO0oO & 0x02000000 ) else False
  self . smr_bit = True if ( i1OOoO0OO0oO & 0x01000000 ) else False
  self . pitr_bit = True if ( i1OOoO0OO0oO & 0x00800000 ) else False
  self . smr_invoked_bit = True if ( i1OOoO0OO0oO & 0x00400000 ) else False
  self . mobile_node = True if ( i1OOoO0OO0oO & 0x00200000 ) else False
  self . xtr_id_present = True if ( i1OOoO0OO0oO & 0x00100000 ) else False
  self . local_xtr = True if ( i1OOoO0OO0oO & 0x00004000 ) else False
  self . dont_reply_bit = True if ( i1OOoO0OO0oO & 0x00002000 ) else False
  self . itr_rloc_count = ( ( i1OOoO0OO0oO >> 8 ) & 0x1f )
  self . record_count = i1OOoO0OO0oO & 0xff
  self . nonce = o0OOO [ 0 ]
  if 61 - 61: I11i
  if 100 - 100: O0 - iIii1I11I1II1 * Oo0Ooo
  if 35 - 35: ooOoO0o
  if 57 - 57: OoO0O00 . Oo0Ooo + I1IiiI
  if ( self . xtr_id_present ) :
   if ( self . decode_xtr_id ( packet ) == False ) : return ( None )
   if 18 - 18: I1IiiI - I1ii11iIi11i * I11i / i11iIiiIii - o0oOOo0O0Ooo % o0oOOo0O0Ooo
   if 31 - 31: I11i
  IiIii1i = struct . calcsize ( "H" )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 100 - 100: i11iIiiIii * i11iIiiIii . iIii1I11I1II1 % iII111i * I1ii11iIi11i
  IiiiII = struct . unpack ( "H" , packet [ : IiIii1i ] )
  self . source_eid . afi = socket . ntohs ( IiiiII [ 0 ] )
  packet = packet [ IiIii1i : : ]
  if 17 - 17: Ii1I * IiII * i11iIiiIii / I1ii11iIi11i / i11iIiiIii
  if ( self . source_eid . afi == LISP_AFI_LCAF ) :
   IiiiiI = packet
   packet = self . source_eid . lcaf_decode_iid ( packet )
   if ( packet == None ) :
    packet = self . lcaf_decode_json ( IiiiiI )
    if ( packet == None ) : return ( None )
    if 5 - 5: iII111i * ooOoO0o + IiII . I1IiiI / I1IiiI
  elif ( self . source_eid . afi != LISP_AFI_NONE ) :
   packet = self . source_eid . unpack_address ( packet )
   if ( packet == None ) : return ( None )
   if 72 - 72: OoO0O00 / I1ii11iIi11i - OOooOOo - OoooooooOO / OoooooooOO % OoooooooOO
  self . source_eid . mask_len = self . source_eid . host_mask_len ( )
  if 85 - 85: OoO0O00 . o0oOOo0O0Ooo . I1IiiI
  Oo000o0o0 = ( os . getenv ( "LISP_NO_CRYPTO" ) != None )
  self . itr_rlocs = [ ]
  oOO0ooOoOoOo = self . itr_rloc_count + 1
  if 91 - 91: IiII - I1ii11iIi11i - I1Ii111
  while ( oOO0ooOoOoOo != 0 ) :
   IiIii1i = struct . calcsize ( "H" )
   if ( len ( packet ) < IiIii1i ) : return ( None )
   if 35 - 35: iIii1I11I1II1 . O0 + OoOoOO00 / OoO0O00 / IiII * II111iiii
   IiiiII = socket . ntohs ( struct . unpack ( "H" , packet [ : IiIii1i ] ) [ 0 ] )
   OooO0OO0 = lisp_address ( LISP_AFI_NONE , "" , 32 , 0 )
   OooO0OO0 . afi = IiiiII
   if 32 - 32: I1Ii111 - iIii1I11I1II1 / I11i * OoO0O00 * OoO0O00
   if 77 - 77: I1ii11iIi11i
   if 16 - 16: II111iiii - II111iiii * I11i / OOooOOo . IiII
   if 36 - 36: I11i / iIii1I11I1II1
   if 59 - 59: i1IIi
   if ( OooO0OO0 . afi == LISP_AFI_LCAF ) :
    oO0ooOoOooO00o00 = packet
    O0OoO0O = packet [ IiIii1i : : ]
    packet = self . lcaf_decode_json ( O0OoO0O )
    if ( packet == O0OoO0O ) : packet = oO0ooOoOooO00o00
    if 75 - 75: O0 . I11i - Ii1I / I1Ii111 / I1ii11iIi11i % I11i
    if 97 - 97: OoOoOO00 - OoO0O00
    if 64 - 64: i1IIi / OoooooooOO / I1ii11iIi11i - Oo0Ooo + oO0o
    if 6 - 6: OOooOOo % II111iiii * IiII
    if 34 - 34: I11i % iII111i - ooOoO0o - I1IiiI
    if 44 - 44: Ii1I . o0oOOo0O0Ooo . iIii1I11I1II1 + OoooooooOO - I1IiiI
   if ( OooO0OO0 . afi != LISP_AFI_LCAF ) :
    if ( len ( packet ) < OooO0OO0 . addr_length ( ) ) : return ( None )
    packet = OooO0OO0 . unpack_address ( packet [ IiIii1i : : ] )
    if ( packet == None ) : return ( None )
    if 22 - 22: I11i * I1ii11iIi11i . OoooooooOO / Oo0Ooo / Ii1I
    if ( Oo000o0o0 ) :
     self . itr_rlocs . append ( OooO0OO0 )
     oOO0ooOoOoOo -= 1
     continue
     if 54 - 54: I1Ii111 % Ii1I + ooOoO0o
     if 45 - 45: Ii1I / oO0o * I1Ii111 . Ii1I
    oo0o00OO = lisp_build_crypto_decap_lookup_key ( OooO0OO0 , port )
    if 25 - 25: I1ii11iIi11i / I1ii11iIi11i
    if 79 - 79: Oo0Ooo - OoO0O00 % Oo0Ooo . II111iiii
    if 84 - 84: ooOoO0o * OoooooooOO + O0
    if 84 - 84: i1IIi . I11i . i1IIi . Oo0Ooo
    if 21 - 21: II111iiii . O0 + Oo0Ooo - i11iIiiIii
    if ( lisp_nat_traversal and OooO0OO0 . is_private_address ( ) and source ) : OooO0OO0 = source
    if 5 - 5: iIii1I11I1II1 * i11iIiiIii + OoO0O00 + I11i * O0 % ooOoO0o
    oO0oooo0 = lisp_crypto_keys_by_rloc_decap
    if ( oO0oooo0 . has_key ( oo0o00OO ) ) : oO0oooo0 . pop ( oo0o00OO )
    if 66 - 66: i1IIi % OoooooooOO * i11iIiiIii + oO0o * O0 / OoO0O00
    if 14 - 14: I1IiiI . IiII
    if 29 - 29: OoooooooOO / IiII + OoOoOO00 - I1Ii111 + IiII . i1IIi
    if 26 - 26: i11iIiiIii - II111iiii
    if 43 - 43: I1IiiI
    if 35 - 35: ooOoO0o + OoOoOO00 * OoooooooOO - II111iiii
    lisp_write_ipc_decap_key ( oo0o00OO , None )
    if 19 - 19: i1IIi / Ii1I / OoOoOO00 . I1IiiI / Ii1I % o0oOOo0O0Ooo
   elif ( self . json_telemetry == None ) :
    if 39 - 39: ooOoO0o - OoooooooOO
    if 88 - 88: i1IIi + iIii1I11I1II1 * i11iIiiIii - OoooooooOO % o0oOOo0O0Ooo
    if 74 - 74: ooOoO0o - i11iIiiIii
    if 34 - 34: IiII + I1Ii111 + Oo0Ooo / II111iiii
    oO0ooOoOooO00o00 = packet
    I1 = lisp_keys ( 1 )
    packet = I1 . decode_lcaf ( oO0ooOoOooO00o00 , 0 )
    if 59 - 59: II111iiii - OoO0O00
    if ( packet == None ) : return ( None )
    if 31 - 31: I11i - OoOoOO00 / o0oOOo0O0Ooo * OoOoOO00 / Oo0Ooo + o0oOOo0O0Ooo
    if 46 - 46: IiII * OoO0O00 / OOooOOo + Oo0Ooo
    if 24 - 24: ooOoO0o % OOooOOo . O0 * Oo0Ooo
    if 52 - 52: O0 . I1Ii111 + iII111i / i11iIiiIii
    o0OOoOoo = [ LISP_CS_25519_CBC , LISP_CS_25519_GCM ,
 LISP_CS_25519_CHACHA ]
    if ( I1 . cipher_suite in o0OOoOoo ) :
     if ( I1 . cipher_suite == LISP_CS_25519_CBC or
 I1 . cipher_suite == LISP_CS_25519_GCM ) :
      o0Oo = lisp_keys ( 1 , do_poly = False , do_chacha = False )
      if 52 - 52: oO0o % Oo0Ooo * II111iiii
     if ( I1 . cipher_suite == LISP_CS_25519_CHACHA ) :
      o0Oo = lisp_keys ( 1 , do_poly = True , do_chacha = True )
      if 24 - 24: i11iIiiIii * i1IIi * i1IIi
    else :
     o0Oo = lisp_keys ( 1 , do_poly = False , do_curve = False ,
 do_chacha = False )
     if 27 - 27: i1IIi - oO0o + OOooOOo
    packet = o0Oo . decode_lcaf ( oO0ooOoOooO00o00 , 0 )
    if ( packet == None ) : return ( None )
    if 3 - 3: IiII % I1Ii111 . OoooooooOO
    if ( len ( packet ) < IiIii1i ) : return ( None )
    IiiiII = struct . unpack ( "H" , packet [ : IiIii1i ] ) [ 0 ]
    OooO0OO0 . afi = socket . ntohs ( IiiiII )
    if ( len ( packet ) < OooO0OO0 . addr_length ( ) ) : return ( None )
    if 19 - 19: I1Ii111 * Ii1I - oO0o
    packet = OooO0OO0 . unpack_address ( packet [ IiIii1i : : ] )
    if ( packet == None ) : return ( None )
    if 78 - 78: OoO0O00 - Ii1I / OOooOOo
    if ( Oo000o0o0 ) :
     self . itr_rlocs . append ( OooO0OO0 )
     oOO0ooOoOoOo -= 1
     continue
     if 81 - 81: OoOoOO00
     if 21 - 21: iII111i / OOooOOo % IiII
    oo0o00OO = lisp_build_crypto_decap_lookup_key ( OooO0OO0 , port )
    if 51 - 51: I11i + ooOoO0o / I1IiiI
    Ii11i = None
    if ( lisp_nat_traversal and OooO0OO0 . is_private_address ( ) and source ) : OooO0OO0 = source
    if 65 - 65: Ii1I % OoO0O00 - i11iIiiIii % Oo0Ooo
    if 19 - 19: O0
    if ( lisp_crypto_keys_by_rloc_decap . has_key ( oo0o00OO ) ) :
     iIi11III = lisp_crypto_keys_by_rloc_decap [ oo0o00OO ]
     Ii11i = iIi11III [ 1 ] if iIi11III and iIi11III [ 1 ] else None
     if 77 - 77: IiII * OoooooooOO . I1ii11iIi11i % Ii1I
     if 51 - 51: I1ii11iIi11i % OoooooooOO - OoooooooOO . I11i
    Ooo00O0ooOo = True
    if ( Ii11i ) :
     if ( Ii11i . compare_keys ( o0Oo ) ) :
      self . keys = [ None , Ii11i , None , None ]
      lprint ( "Maintain stored decap-keys for RLOC {}" . format ( red ( oo0o00OO , False ) ) )
      if 4 - 4: OOooOOo - ooOoO0o - Ii1I . I1IiiI * ooOoO0o
     else :
      Ooo00O0ooOo = False
      o0OOo = bold ( "Remote decap-rekeying" , False )
      lprint ( "{} for RLOC {}" . format ( o0OOo , red ( oo0o00OO ,
 False ) ) )
      o0Oo . copy_keypair ( Ii11i )
      o0Oo . uptime = Ii11i . uptime
      Ii11i = None
      if 39 - 39: iII111i - OoO0O00
      if 1 - 1: OoooooooOO - ooOoO0o
      if 24 - 24: II111iiii % iII111i % Ii1I % iII111i % I11i . iIii1I11I1II1
    if ( Ii11i == None ) :
     self . keys = [ None , o0Oo , None , None ]
     if ( lisp_i_am_etr == False and lisp_i_am_rtr == False ) :
      o0Oo . local_public_key = None
      lprint ( "{} for {}" . format ( bold ( "Ignoring decap-keys" ,
 False ) , red ( oo0o00OO , False ) ) )
     elif ( o0Oo . remote_public_key != None ) :
      if ( Ooo00O0ooOo ) :
       lprint ( "{} for RLOC {}" . format ( bold ( "New decap-keying" , False ) ,
       # i11iIiiIii * ooOoO0o - II111iiii
 red ( oo0o00OO , False ) ) )
       if 23 - 23: IiII
      o0Oo . compute_shared_key ( "decap" )
      o0Oo . add_key_by_rloc ( oo0o00OO , False )
      if 53 - 53: I1Ii111 % OOooOOo . Ii1I / OOooOOo * OOooOOo * O0
      if 1 - 1: iIii1I11I1II1 % I1ii11iIi11i . oO0o . IiII . o0oOOo0O0Ooo / o0oOOo0O0Ooo
      if 52 - 52: O0 * OoooooooOO . I1Ii111 . OOooOOo - iII111i % iII111i
      if 33 - 33: i11iIiiIii - o0oOOo0O0Ooo . I1IiiI - oO0o - II111iiii + O0
   self . itr_rlocs . append ( OooO0OO0 )
   oOO0ooOoOoOo -= 1
   if 54 - 54: iIii1I11I1II1 - IiII - IiII
   if 18 - 18: i11iIiiIii + iIii1I11I1II1 . i11iIiiIii
  IiIii1i = struct . calcsize ( "BBH" )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 63 - 63: iII111i - OoO0O00 * OOooOOo
  Iiii1I , oO00OO0Ooo00O , IiiiII = struct . unpack ( "BBH" , packet [ : IiIii1i ] )
  self . subscribe_bit = ( Iiii1I & 0x80 )
  self . target_eid . afi = socket . ntohs ( IiiiII )
  packet = packet [ IiIii1i : : ]
  if 89 - 89: iII111i / Oo0Ooo
  self . target_eid . mask_len = oO00OO0Ooo00O
  if ( self . target_eid . afi == LISP_AFI_LCAF ) :
   packet , OO0Ooo = self . target_eid . lcaf_decode_eid ( packet )
   if ( packet == None ) : return ( None )
   if ( OO0Ooo ) : self . target_group = OO0Ooo
  else :
   packet = self . target_eid . unpack_address ( packet )
   if ( packet == None ) : return ( None )
   packet = packet [ IiIii1i : : ]
   if 74 - 74: OOooOOo - II111iiii
  return ( packet )
  if 66 - 66: i11iIiiIii + I1Ii111 . ooOoO0o
  if 46 - 46: I1Ii111 / I1ii11iIi11i
 def print_eid_tuple ( self ) :
  return ( lisp_print_eid_tuple ( self . target_eid , self . target_group ) )
  if 41 - 41: i1IIi % Ii1I + I1Ii111 . Oo0Ooo / iIii1I11I1II1
  if 77 - 77: Oo0Ooo . OoO0O00 % O0 - OoO0O00 - Oo0Ooo
 def encode_xtr_id ( self , packet ) :
  OOO0oo = self . xtr_id >> 64
  ii1iII1 = self . xtr_id & 0xffffffffffffffff
  OOO0oo = byte_swap_64 ( OOO0oo )
  ii1iII1 = byte_swap_64 ( ii1iII1 )
  packet += struct . pack ( "QQ" , OOO0oo , ii1iII1 )
  return ( packet )
  if 95 - 95: IiII * II111iiii % o0oOOo0O0Ooo * Oo0Ooo . I11i
  if 46 - 46: II111iiii - OoO0O00 % ooOoO0o
 def decode_xtr_id ( self , packet ) :
  IiIii1i = struct . calcsize ( "QQ" )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  packet = packet [ len ( packet ) - IiIii1i : : ]
  OOO0oo , ii1iII1 = struct . unpack ( "QQ" , packet [ : IiIii1i ] )
  OOO0oo = byte_swap_64 ( OOO0oo )
  ii1iII1 = byte_swap_64 ( ii1iII1 )
  self . xtr_id = ( OOO0oo << 64 ) | ii1iII1
  return ( True )
  if 97 - 97: OoO0O00 . OoOoOO00
  if 78 - 78: I1ii11iIi11i + I1ii11iIi11i . OoOoOO00 - IiII * iIii1I11I1II1 * O0
  if 26 - 26: OoooooooOO + oO0o + OoO0O00 . O0
  if 46 - 46: OoooooooOO - Oo0Ooo * I1Ii111 * OOooOOo * I1Ii111 . oO0o
  if 96 - 96: Ii1I / IiII % o0oOOo0O0Ooo + I11i
  if 46 - 46: OoO0O00 * I1IiiI
  if 25 - 25: I1Ii111 . IiII % O0 % i1IIi
  if 53 - 53: O0 % ooOoO0o
  if 41 - 41: IiII
  if 29 - 29: ooOoO0o
  if 70 - 70: oO0o . O0 % I11i % IiII - I11i * I1ii11iIi11i
  if 22 - 22: i1IIi
  if 82 - 82: oO0o . iIii1I11I1II1 - I1ii11iIi11i
  if 55 - 55: Oo0Ooo % Ii1I . iIii1I11I1II1 * I1Ii111
  if 33 - 33: O0 - I1IiiI / I1ii11iIi11i / OoO0O00 + iII111i - oO0o
  if 27 - 27: I1Ii111 + ooOoO0o - I1Ii111 % i11iIiiIii * Oo0Ooo * o0oOOo0O0Ooo
  if 88 - 88: OOooOOo
  if 25 - 25: OoO0O00 + o0oOOo0O0Ooo . ooOoO0o - Ii1I . oO0o * Ii1I
  if 85 - 85: i1IIi
  if 94 - 94: OoooooooOO . O0 / OoooooooOO
  if 67 - 67: i11iIiiIii + OoOoOO00
  if 50 - 50: ooOoO0o . i1IIi + I1ii11iIi11i . OOooOOo
  if 97 - 97: I1IiiI
  if 63 - 63: O0 - OoOoOO00 / i11iIiiIii / OoooooooOO / ooOoO0o / II111iiii
  if 45 - 45: II111iiii . OoO0O00 + OoO0O00 * iIii1I11I1II1
  if 23 - 23: IiII * OoOoOO00 % Ii1I / Ii1I - ooOoO0o - OOooOOo
  if 86 - 86: OOooOOo . OoooooooOO * I1IiiI - Oo0Ooo / i11iIiiIii * iII111i
  if 56 - 56: I1IiiI . I11i % iII111i
  if 33 - 33: I11i / OOooOOo - OOooOOo / i11iIiiIii * OoOoOO00 + O0
  if 2 - 2: i11iIiiIii % I1IiiI
  if 90 - 90: II111iiii
  if 2 - 2: Ii1I - OoooooooOO - i11iIiiIii % Oo0Ooo / Ii1I
class lisp_map_reply ( ) :
 def __init__ ( self ) :
  self . rloc_probe = False
  self . echo_nonce_capable = False
  self . security = False
  self . record_count = 0
  self . hop_count = 0
  self . nonce = 0
  self . keys = None
  if 77 - 77: o0oOOo0O0Ooo . o0oOOo0O0Ooo * I1Ii111 + OOooOOo - i11iIiiIii
  if 45 - 45: I1IiiI . I1IiiI - Oo0Ooo * OOooOOo
 def print_map_reply ( self ) :
  oOOo0ooO0 = "{} -> flags: {}{}{}, hop-count: {}, record-count: {}, " + "nonce: 0x{}"
  if 71 - 71: i1IIi / I11i
  lprint ( oOOo0ooO0 . format ( bold ( "Map-Reply" , False ) , "R" if self . rloc_probe else "r" ,
  # O0
 "E" if self . echo_nonce_capable else "e" ,
 "S" if self . security else "s" , self . hop_count , self . record_count ,
 lisp_hex_string ( self . nonce ) ) )
  if 19 - 19: IiII / o0oOOo0O0Ooo - Ii1I . i11iIiiIii + oO0o % OoOoOO00
  if 97 - 97: OOooOOo . OOooOOo . iII111i . iII111i
 def encode ( self ) :
  i1OOoO0OO0oO = ( LISP_MAP_REPLY << 28 ) | self . record_count
  i1OOoO0OO0oO |= self . hop_count << 8
  if ( self . rloc_probe ) : i1OOoO0OO0oO |= 0x08000000
  if ( self . echo_nonce_capable ) : i1OOoO0OO0oO |= 0x04000000
  if ( self . security ) : i1OOoO0OO0oO |= 0x02000000
  if 63 - 63: O0 * IiII / Oo0Ooo . I1IiiI . I1IiiI / i11iIiiIii
  IiiiIi1iiii11 = struct . pack ( "I" , socket . htonl ( i1OOoO0OO0oO ) )
  IiiiIi1iiii11 += struct . pack ( "Q" , self . nonce )
  return ( IiiiIi1iiii11 )
  if 17 - 17: iIii1I11I1II1 / OoO0O00 - II111iiii
  if 46 - 46: iIii1I11I1II1 * oO0o / i11iIiiIii + II111iiii + I11i
 def decode ( self , packet ) :
  O0O00Oo = "I"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 30 - 30: O0 * IiII - I1Ii111 % O0 * Ii1I
  i1OOoO0OO0oO = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  i1OOoO0OO0oO = i1OOoO0OO0oO [ 0 ]
  packet = packet [ IiIii1i : : ]
  if 29 - 29: I1ii11iIi11i % I1ii11iIi11i % Ii1I + ooOoO0o % iIii1I11I1II1
  O0O00Oo = "Q"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 41 - 41: I1ii11iIi11i % I1Ii111
  o0OOO = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  packet = packet [ IiIii1i : : ]
  if 37 - 37: Oo0Ooo . I1IiiI % OoOoOO00 . OoO0O00 - Oo0Ooo / OoO0O00
  i1OOoO0OO0oO = socket . ntohl ( i1OOoO0OO0oO )
  self . rloc_probe = True if ( i1OOoO0OO0oO & 0x08000000 ) else False
  self . echo_nonce_capable = True if ( i1OOoO0OO0oO & 0x04000000 ) else False
  self . security = True if ( i1OOoO0OO0oO & 0x02000000 ) else False
  self . hop_count = ( i1OOoO0OO0oO >> 8 ) & 0xff
  self . record_count = i1OOoO0OO0oO & 0xff
  self . nonce = o0OOO [ 0 ]
  if 34 - 34: i11iIiiIii + OoO0O00 + i11iIiiIii . IiII % O0
  if ( lisp_crypto_keys_by_nonce . has_key ( self . nonce ) ) :
   self . keys = lisp_crypto_keys_by_nonce [ self . nonce ]
   self . keys [ 1 ] . delete_key_by_nonce ( self . nonce )
   if 64 - 64: o0oOOo0O0Ooo . iIii1I11I1II1
  return ( packet )
  if 86 - 86: ooOoO0o - I11i . iIii1I11I1II1 - iIii1I11I1II1
  if 61 - 61: Ii1I % Oo0Ooo + OoOoOO00
  if 60 - 60: oO0o . OoooooooOO
  if 40 - 40: I11i
  if 44 - 44: ooOoO0o
  if 35 - 35: II111iiii + iII111i / I1ii11iIi11i * I1IiiI . I11i
  if 97 - 97: I1IiiI / o0oOOo0O0Ooo
  if 13 - 13: I1ii11iIi11i
  if 72 - 72: Oo0Ooo + IiII / Ii1I * Oo0Ooo
  if 41 - 41: OOooOOo - OoOoOO00 . I1IiiI + i11iIiiIii + OoO0O00 * iII111i
  if 85 - 85: OoO0O00 + II111iiii
  if 87 - 87: OoO0O00
  if 93 - 93: OoooooooOO
  if 80 - 80: o0oOOo0O0Ooo
  if 3 - 3: i11iIiiIii / OOooOOo + oO0o
  if 10 - 10: OoO0O00 . OoO0O00 + O0
  if 13 - 13: i1IIi . I1IiiI
  if 45 - 45: ooOoO0o % I11i
  if 37 - 37: iII111i
  if 70 - 70: O0 + iIii1I11I1II1 % O0 * o0oOOo0O0Ooo - Oo0Ooo - ooOoO0o
  if 94 - 94: i1IIi + IiII / OoooooooOO - oO0o / OOooOOo / OoOoOO00
  if 55 - 55: OOooOOo
  if 5 - 5: I11i / OoOoOO00
  if 48 - 48: i1IIi - oO0o . OoooooooOO - OoO0O00 - i1IIi
  if 19 - 19: oO0o % Ii1I + I1ii11iIi11i . II111iiii * i11iIiiIii
  if 87 - 87: Ii1I / I1Ii111 % OoOoOO00 * I1ii11iIi11i - OoooooooOO / OoOoOO00
  if 24 - 24: I11i . OOooOOo * i1IIi . I1ii11iIi11i / ooOoO0o / O0
  if 62 - 62: o0oOOo0O0Ooo % II111iiii
  if 22 - 22: oO0o - o0oOOo0O0Ooo
  if 89 - 89: OOooOOo
  if 34 - 34: iII111i . OOooOOo
  if 13 - 13: OoO0O00 * OOooOOo + oO0o
class lisp_eid_record ( ) :
 def __init__ ( self ) :
  self . record_ttl = 0
  self . rloc_count = 0
  self . action = 0
  self . authoritative = False
  self . ddt_incomplete = False
  self . signature_count = 0
  self . map_version = 0
  self . eid = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . group = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . record_ttl = 0
  if 21 - 21: i11iIiiIii . Ii1I % i1IIi * Ii1I . oO0o + Ii1I
  if 92 - 92: i1IIi + OoO0O00 * I11i
 def print_prefix ( self ) :
  if ( self . group . is_null ( ) ) :
   return ( green ( self . eid . print_prefix ( ) , False ) )
   if 70 - 70: Oo0Ooo
  return ( green ( self . eid . print_sg ( self . group ) , False ) )
  if 93 - 93: iII111i . I1ii11iIi11i . Oo0Ooo . oO0o . OoooooooOO
  if 51 - 51: O0 - iII111i
 def print_ttl ( self ) :
  Oo0o0 = self . record_ttl
  if ( self . record_ttl & 0x80000000 ) :
   Oo0o0 = str ( self . record_ttl & 0x7fffffff ) + " secs"
  elif ( ( Oo0o0 % 60 ) == 0 ) :
   Oo0o0 = str ( Oo0o0 / 60 ) + " hours"
  else :
   Oo0o0 = str ( Oo0o0 ) + " mins"
   if 87 - 87: o0oOOo0O0Ooo % OoO0O00 + Oo0Ooo
  return ( Oo0o0 )
  if 93 - 93: OoooooooOO + i1IIi * iII111i + Oo0Ooo - iII111i * OoO0O00
  if 96 - 96: O0 + I1ii11iIi11i
 def store_ttl ( self ) :
  Oo0o0 = self . record_ttl * 60
  if ( self . record_ttl & 0x80000000 ) : Oo0o0 = self . record_ttl & 0x7fffffff
  return ( Oo0o0 )
  if 27 - 27: i1IIi - i1IIi - Ii1I - OOooOOo
  if 75 - 75: iII111i % O0 - I11i - I1ii11iIi11i + I1IiiI - I1IiiI
 def print_record ( self , indent , ddt ) :
  Oo00OoooO0o = ""
  I1III1ii1 = ""
  iiI111iiII = bold ( "invalid-action" , False )
  if ( ddt ) :
   if ( self . action < len ( lisp_map_referral_action_string ) ) :
    iiI111iiII = lisp_map_referral_action_string [ self . action ]
    iiI111iiII = bold ( iiI111iiII , False )
    Oo00OoooO0o = ( ", " + bold ( "ddt-incomplete" , False ) ) if self . ddt_incomplete else ""
    if 92 - 92: iII111i / OoooooooOO * OoOoOO00 + OoOoOO00 - Ii1I * o0oOOo0O0Ooo
    I1III1ii1 = ( ", sig-count: " + str ( self . signature_count ) ) if ( self . signature_count != 0 ) else ""
    if 91 - 91: OoOoOO00
    if 65 - 65: OOooOOo . II111iiii * i11iIiiIii + OOooOOo
  else :
   if ( self . action < len ( lisp_map_reply_action_string ) ) :
    iiI111iiII = lisp_map_reply_action_string [ self . action ]
    if ( self . action != LISP_NO_ACTION ) :
     iiI111iiII = bold ( iiI111iiII , False )
     if 99 - 99: I1ii11iIi11i % Oo0Ooo
     if 31 - 31: o0oOOo0O0Ooo - II111iiii * OOooOOo . OOooOOo - oO0o
     if 57 - 57: OOooOOo / i11iIiiIii / I1Ii111 - Oo0Ooo . iIii1I11I1II1
     if 84 - 84: IiII
  IiiiII = LISP_AFI_LCAF if ( self . eid . afi < 0 ) else self . eid . afi
  oOOo0ooO0 = ( "{}EID-record -> record-ttl: {}, rloc-count: {}, action: " +
 "{}, {}{}{}, map-version: {}, afi: {}, [iid]eid/ml: {}" )
  if 42 - 42: O0 . I1Ii111 / I11i
  lprint ( oOOo0ooO0 . format ( indent , self . print_ttl ( ) , self . rloc_count ,
 iiI111iiII , "auth" if ( self . authoritative is True ) else "non-auth" ,
 Oo00OoooO0o , I1III1ii1 , self . map_version , IiiiII ,
 green ( self . print_prefix ( ) , False ) ) )
  if 69 - 69: OoOoOO00 / I1Ii111 * I1IiiI
  if 76 - 76: O0 + II111iiii * OoO0O00
 def encode ( self ) :
  iI1IIi1I = self . action << 13
  if ( self . authoritative ) : iI1IIi1I |= 0x1000
  if ( self . ddt_incomplete ) : iI1IIi1I |= 0x800
  if 42 - 42: OoooooooOO / IiII * II111iiii
  if 77 - 77: II111iiii + iII111i . o0oOOo0O0Ooo / I1Ii111
  if 100 - 100: Ii1I
  if 84 - 84: I11i * ooOoO0o + i11iIiiIii + iII111i - II111iiii
  IiiiII = self . eid . afi if ( self . eid . instance_id == 0 ) else LISP_AFI_LCAF
  if ( IiiiII < 0 ) : IiiiII = LISP_AFI_LCAF
  Oo0ooO = ( self . group . is_null ( ) == False )
  if ( Oo0ooO ) : IiiiII = LISP_AFI_LCAF
  if 54 - 54: oO0o
  O0o0 = ( self . signature_count << 12 ) | self . map_version
  oO00OO0Ooo00O = 0 if self . eid . is_binary ( ) == False else self . eid . mask_len
  if 64 - 64: OoOoOO00 + iII111i * OoOoOO00 - I1IiiI * OoooooooOO
  IiiiIi1iiii11 = struct . pack ( "IBBHHH" , socket . htonl ( self . record_ttl ) ,
 self . rloc_count , oO00OO0Ooo00O , socket . htons ( iI1IIi1I ) ,
 socket . htons ( O0o0 ) , socket . htons ( IiiiII ) )
  if 27 - 27: II111iiii + i11iIiiIii
  if 32 - 32: i1IIi
  if 76 - 76: II111iiii % ooOoO0o - I1ii11iIi11i
  if 50 - 50: II111iiii / I1IiiI . Ii1I % i11iIiiIii
  if ( Oo0ooO ) :
   IiiiIi1iiii11 += self . eid . lcaf_encode_sg ( self . group )
   return ( IiiiIi1iiii11 )
   if 66 - 66: oO0o / OOooOOo / iII111i
   if 5 - 5: I1Ii111 . oO0o
   if 77 - 77: iII111i / i11iIiiIii
   if 20 - 20: O0 . I11i
   if 67 - 67: OoOoOO00 - ooOoO0o - iIii1I11I1II1
  if ( self . eid . afi == LISP_AFI_GEO_COORD and self . eid . instance_id == 0 ) :
   IiiiIi1iiii11 = IiiiIi1iiii11 [ 0 : - 2 ]
   IiiiIi1iiii11 += self . eid . address . encode_geo ( )
   return ( IiiiIi1iiii11 )
   if 31 - 31: II111iiii + o0oOOo0O0Ooo * i11iIiiIii . o0oOOo0O0Ooo
   if 73 - 73: oO0o / OOooOOo * II111iiii % OoooooooOO - i1IIi - ooOoO0o
   if 43 - 43: o0oOOo0O0Ooo + Ii1I % OoO0O00 . I1Ii111 + i1IIi
   if 85 - 85: Oo0Ooo % I1ii11iIi11i / OOooOOo
   if 65 - 65: ooOoO0o + IiII - OoOoOO00 % II111iiii - iIii1I11I1II1
  if ( IiiiII == LISP_AFI_LCAF ) :
   IiiiIi1iiii11 += self . eid . lcaf_encode_iid ( )
   return ( IiiiIi1iiii11 )
   if 39 - 39: I1IiiI + I1ii11iIi11i - i11iIiiIii
   if 43 - 43: iIii1I11I1II1
   if 73 - 73: OoOoOO00 + o0oOOo0O0Ooo
   if 58 - 58: i1IIi * I1ii11iIi11i % iII111i . OoO0O00 % IiII % I11i
   if 63 - 63: I1ii11iIi11i % ooOoO0o % I1ii11iIi11i
  IiiiIi1iiii11 += self . eid . pack_address ( )
  return ( IiiiIi1iiii11 )
  if 71 - 71: Ii1I
  if 43 - 43: o0oOOo0O0Ooo / ooOoO0o
 def decode ( self , packet ) :
  O0O00Oo = "IBBHHH"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 88 - 88: i11iIiiIii - i1IIi + Oo0Ooo - O0
  self . record_ttl , self . rloc_count , self . eid . mask_len , iI1IIi1I , self . map_version , self . eid . afi = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  if 50 - 50: I1ii11iIi11i
  if 37 - 37: oO0o % iII111i / II111iiii / OoO0O00 - IiII - ooOoO0o
  if 69 - 69: I1ii11iIi11i . OoooooooOO % I1Ii111
  self . record_ttl = socket . ntohl ( self . record_ttl )
  iI1IIi1I = socket . ntohs ( iI1IIi1I )
  self . action = ( iI1IIi1I >> 13 ) & 0x7
  self . authoritative = True if ( ( iI1IIi1I >> 12 ) & 1 ) else False
  self . ddt_incomplete = True if ( ( iI1IIi1I >> 11 ) & 1 ) else False
  self . map_version = socket . ntohs ( self . map_version )
  self . signature_count = self . map_version >> 12
  self . map_version = self . map_version & 0xfff
  self . eid . afi = socket . ntohs ( self . eid . afi )
  self . eid . instance_id = 0
  packet = packet [ IiIii1i : : ]
  if 79 - 79: I1IiiI - IiII . OoooooooOO - I1ii11iIi11i
  if 79 - 79: OOooOOo + o0oOOo0O0Ooo % iII111i . oO0o
  if 49 - 49: Ii1I + i11iIiiIii * OoOoOO00 . OoOoOO00 . I1ii11iIi11i . Oo0Ooo
  if 61 - 61: I11i / OOooOOo
  if ( self . eid . afi == LISP_AFI_LCAF ) :
   packet , OOo0oOOO0 = self . eid . lcaf_decode_eid ( packet )
   if ( OOo0oOOO0 ) : self . group = OOo0oOOO0
   self . group . instance_id = self . eid . instance_id
   return ( packet )
   if 79 - 79: OoooooooOO * OoO0O00 + OoO0O00 % Ii1I % OOooOOo * IiII
   if 11 - 11: OOooOOo - Ii1I
  packet = self . eid . unpack_address ( packet )
  return ( packet )
  if 44 - 44: oO0o + oO0o - I11i % I11i - i11iIiiIii / Oo0Ooo
  if 51 - 51: I1IiiI * I1IiiI
 def print_eid_tuple ( self ) :
  return ( lisp_print_eid_tuple ( self . eid , self . group ) )
  if 49 - 49: I1Ii111
  if 11 - 11: i1IIi
  if 65 - 65: OoO0O00 . ooOoO0o
  if 12 - 12: I1Ii111 + O0 - oO0o . IiII
  if 46 - 46: IiII . ooOoO0o / iII111i
  if 63 - 63: II111iiii - I1ii11iIi11i * II111iiii
  if 92 - 92: OoO0O00 % ooOoO0o * O0 % iIii1I11I1II1 / i1IIi / OoOoOO00
  if 67 - 67: I1Ii111 + I11i + I1Ii111 . OOooOOo % o0oOOo0O0Ooo / ooOoO0o
  if 78 - 78: I1ii11iIi11i . O0
  if 56 - 56: oO0o - i1IIi * O0 / I11i * I1IiiI . I11i
  if 54 - 54: i11iIiiIii % i1IIi + Oo0Ooo / OoOoOO00
  if 26 - 26: I11i . I1ii11iIi11i
  if 55 - 55: OoOoOO00 * I1Ii111 % OoO0O00 - OoO0O00
  if 34 - 34: O0 * OoO0O00 - oO0o - IiII * Ii1I . II111iiii
  if 28 - 28: O0 % iII111i - i1IIi
  if 49 - 49: ooOoO0o . I11i - iIii1I11I1II1
  if 41 - 41: ooOoO0o * i11iIiiIii % ooOoO0o . oO0o
  if 97 - 97: oO0o - iII111i + IiII . OoOoOO00 + iIii1I11I1II1
  if 75 - 75: ooOoO0o + ooOoO0o . I1Ii111 % iII111i / iIii1I11I1II1 * iII111i
  if 13 - 13: II111iiii * i11iIiiIii - i1IIi * OoO0O00 + i1IIi
  if 43 - 43: O0 % oO0o * I1IiiI
  if 64 - 64: II111iiii + i11iIiiIii
  if 17 - 17: O0 * I1IiiI
  if 40 - 40: iIii1I11I1II1 * iII111i % iIii1I11I1II1
  if 39 - 39: i1IIi . Ii1I - Oo0Ooo
  if 91 - 91: I1IiiI - OoooooooOO - OoooooooOO
  if 69 - 69: iII111i * i11iIiiIii / i1IIi
  if 86 - 86: I1IiiI % I11i * O0 + i1IIi % I1Ii111
  if 97 - 97: II111iiii * OoOoOO00 - I1Ii111 / i11iIiiIii / OoOoOO00
  if 25 - 25: Oo0Ooo / Oo0Ooo
  if 74 - 74: OOooOOo
LISP_UDP_PROTOCOL = 17
LISP_DEFAULT_ECM_TTL = 128
if 30 - 30: O0 . Ii1I / o0oOOo0O0Ooo + I1IiiI - O0
class lisp_ecm ( ) :
 def __init__ ( self , sport ) :
  self . security = False
  self . ddt = False
  self . to_etr = False
  self . to_ms = False
  self . length = 0
  self . ttl = LISP_DEFAULT_ECM_TTL
  self . protocol = LISP_UDP_PROTOCOL
  self . ip_checksum = 0
  self . source = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . dest = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . udp_sport = sport
  self . udp_dport = LISP_CTRL_PORT
  self . udp_checksum = 0
  self . udp_length = 0
  self . afi = LISP_AFI_NONE
  if 88 - 88: i11iIiiIii
  if 33 - 33: OoO0O00 + O0
 def print_ecm ( self ) :
  oOOo0ooO0 = ( "{} -> flags: {}{}{}{}, " + "inner IP: {} -> {}, inner UDP: {} -> {}" )
  if 20 - 20: o0oOOo0O0Ooo % I11i . ooOoO0o - i1IIi . O0
  lprint ( oOOo0ooO0 . format ( bold ( "ECM" , False ) , "S" if self . security else "s" ,
 "D" if self . ddt else "d" , "E" if self . to_etr else "e" ,
 "M" if self . to_ms else "m" ,
 green ( self . source . print_address ( ) , False ) ,
 green ( self . dest . print_address ( ) , False ) , self . udp_sport ,
 self . udp_dport ) )
  if 10 - 10: i1IIi
 def encode ( self , packet , inner_source , inner_dest ) :
  self . udp_length = len ( packet ) + 8
  self . source = inner_source
  self . dest = inner_dest
  if ( inner_dest . is_ipv4 ( ) ) :
   self . afi = LISP_AFI_IPV4
   self . length = self . udp_length + 20
   if 49 - 49: I1Ii111 - Ii1I . O0
  if ( inner_dest . is_ipv6 ( ) ) :
   self . afi = LISP_AFI_IPV6
   self . length = self . udp_length
   if 46 - 46: OOooOOo
   if 64 - 64: I1IiiI / OoOoOO00
   if 6 - 6: i11iIiiIii - iII111i * i1IIi - iII111i
   if 8 - 8: I11i / i11iIiiIii . O0 / OoO0O00 * oO0o + I1Ii111
   if 91 - 91: I1IiiI
   if 84 - 84: O0 % Ii1I
  i1OOoO0OO0oO = ( LISP_ECM << 28 )
  if ( self . security ) : i1OOoO0OO0oO |= 0x08000000
  if ( self . ddt ) : i1OOoO0OO0oO |= 0x04000000
  if ( self . to_etr ) : i1OOoO0OO0oO |= 0x02000000
  if ( self . to_ms ) : i1OOoO0OO0oO |= 0x01000000
  if 3 - 3: I1IiiI . I11i / I1ii11iIi11i
  I1i1ii = struct . pack ( "I" , socket . htonl ( i1OOoO0OO0oO ) )
  if 14 - 14: ooOoO0o
  ooooo0Oo0 = ""
  if ( self . afi == LISP_AFI_IPV4 ) :
   ooooo0Oo0 = struct . pack ( "BBHHHBBH" , 0x45 , 0 , socket . htons ( self . length ) ,
 0 , 0 , self . ttl , self . protocol , socket . htons ( self . ip_checksum ) )
   ooooo0Oo0 += self . source . pack_address ( )
   ooooo0Oo0 += self . dest . pack_address ( )
   ooooo0Oo0 = lisp_ip_checksum ( ooooo0Oo0 )
   if 24 - 24: OOooOOo . Oo0Ooo . O0 - oO0o - O0 . Ii1I
  if ( self . afi == LISP_AFI_IPV6 ) :
   ooooo0Oo0 = struct . pack ( "BBHHBB" , 0x60 , 0 , 0 , socket . htons ( self . length ) ,
 self . protocol , self . ttl )
   ooooo0Oo0 += self . source . pack_address ( )
   ooooo0Oo0 += self . dest . pack_address ( )
   if 26 - 26: iIii1I11I1II1 / i1IIi
   if 18 - 18: ooOoO0o + Ii1I
  OO0o0OO0 = socket . htons ( self . udp_sport )
  o0 = socket . htons ( self . udp_dport )
  IIi1I1 = socket . htons ( self . udp_length )
  IiiI11iIi = socket . htons ( self . udp_checksum )
  oOoO0OOO00O = struct . pack ( "HHHH" , OO0o0OO0 , o0 , IIi1I1 , IiiI11iIi )
  return ( I1i1ii + ooooo0Oo0 + oOoO0OOO00O )
  if 16 - 16: iII111i / II111iiii + I1IiiI . II111iiii - iII111i
  if 61 - 61: II111iiii . OoO0O00 - II111iiii
 def decode ( self , packet ) :
  if 75 - 75: Oo0Ooo - OoOoOO00 + oO0o % i1IIi * OOooOOo
  if 56 - 56: OoOoOO00 / OoO0O00 / I1IiiI % OoooooooOO
  if 39 - 39: I1IiiI + II111iiii * Oo0Ooo % Ii1I . o0oOOo0O0Ooo * oO0o
  if 42 - 42: Ii1I / Oo0Ooo
  O0O00Oo = "I"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 25 - 25: OoooooooOO % Ii1I * I1Ii111 * I11i + I1IiiI % I1ii11iIi11i
  i1OOoO0OO0oO = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  if 70 - 70: Ii1I + I1ii11iIi11i * I11i * i1IIi . I1Ii111
  i1OOoO0OO0oO = socket . ntohl ( i1OOoO0OO0oO [ 0 ] )
  self . security = True if ( i1OOoO0OO0oO & 0x08000000 ) else False
  self . ddt = True if ( i1OOoO0OO0oO & 0x04000000 ) else False
  self . to_etr = True if ( i1OOoO0OO0oO & 0x02000000 ) else False
  self . to_ms = True if ( i1OOoO0OO0oO & 0x01000000 ) else False
  packet = packet [ IiIii1i : : ]
  if 76 - 76: OoooooooOO * OoOoOO00 . OoooooooOO
  if 46 - 46: ooOoO0o * o0oOOo0O0Ooo % II111iiii / I1Ii111
  if 29 - 29: OoO0O00 - i11iIiiIii % Oo0Ooo % o0oOOo0O0Ooo
  if 30 - 30: oO0o - Ii1I % Ii1I
  if ( len ( packet ) < 1 ) : return ( None )
  Iii11111I1iii = struct . unpack ( "B" , packet [ 0 : 1 ] ) [ 0 ]
  Iii11111I1iii = Iii11111I1iii >> 4
  if 8 - 8: IiII
  if ( Iii11111I1iii == 4 ) :
   IiIii1i = struct . calcsize ( "HHIBBH" )
   if ( len ( packet ) < IiIii1i ) : return ( None )
   if 68 - 68: IiII . OoooooooOO - i11iIiiIii + i11iIiiIii
   oOo0oo , IIi1I1 , oOo0oo , oO0Oo0O , IiI1i1i1 , IiiI11iIi = struct . unpack ( "HHIBBH" , packet [ : IiIii1i ] )
   self . length = socket . ntohs ( IIi1I1 )
   self . ttl = oO0Oo0O
   self . protocol = IiI1i1i1
   self . ip_checksum = socket . ntohs ( IiiI11iIi )
   self . source . afi = self . dest . afi = LISP_AFI_IPV4
   if 12 - 12: Oo0Ooo * Ii1I / OoO0O00 % oO0o / I11i * ooOoO0o
   if 64 - 64: I1IiiI % I1Ii111 + OoooooooOO
   if 11 - 11: I1Ii111
   if 87 - 87: i11iIiiIii * I1ii11iIi11i + OOooOOo - ooOoO0o
   IiI1i1i1 = struct . pack ( "H" , 0 )
   IIiIII1I1i = struct . calcsize ( "HHIBB" )
   I1iiI1IiI1iii = struct . calcsize ( "H" )
   packet = packet [ : IIiIII1I1i ] + IiI1i1i1 + packet [ IIiIII1I1i + I1iiI1IiI1iii : ]
   if 28 - 28: iII111i - i1IIi - OOooOOo
   packet = packet [ IiIii1i : : ]
   packet = self . source . unpack_address ( packet )
   if ( packet == None ) : return ( None )
   packet = self . dest . unpack_address ( packet )
   if ( packet == None ) : return ( None )
   if 54 - 54: i11iIiiIii
   if 57 - 57: I11i / IiII * i1IIi + II111iiii . o0oOOo0O0Ooo
  if ( Iii11111I1iii == 6 ) :
   IiIii1i = struct . calcsize ( "IHBB" )
   if ( len ( packet ) < IiIii1i ) : return ( None )
   if 11 - 11: II111iiii
   oOo0oo , IIi1I1 , IiI1i1i1 , oO0Oo0O = struct . unpack ( "IHBB" , packet [ : IiIii1i ] )
   self . length = socket . ntohs ( IIi1I1 )
   self . protocol = IiI1i1i1
   self . ttl = oO0Oo0O
   self . source . afi = self . dest . afi = LISP_AFI_IPV6
   if 66 - 66: Ii1I - I1IiiI . OoooooooOO * I1Ii111
   packet = packet [ IiIii1i : : ]
   packet = self . source . unpack_address ( packet )
   if ( packet == None ) : return ( None )
   packet = self . dest . unpack_address ( packet )
   if ( packet == None ) : return ( None )
   if 16 - 16: IiII * OoO0O00 * i11iIiiIii - ooOoO0o
   if 88 - 88: iIii1I11I1II1 / Ii1I * IiII / I1Ii111
  self . source . mask_len = self . source . host_mask_len ( )
  self . dest . mask_len = self . dest . host_mask_len ( )
  if 31 - 31: O0 . I1IiiI
  IiIii1i = struct . calcsize ( "HHHH" )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 8 - 8: OoOoOO00
  OO0o0OO0 , o0 , IIi1I1 , IiiI11iIi = struct . unpack ( "HHHH" , packet [ : IiIii1i ] )
  self . udp_sport = socket . ntohs ( OO0o0OO0 )
  self . udp_dport = socket . ntohs ( o0 )
  self . udp_length = socket . ntohs ( IIi1I1 )
  self . udp_checksum = socket . ntohs ( IiiI11iIi )
  packet = packet [ IiIii1i : : ]
  return ( packet )
  if 99 - 99: iII111i
  if 93 - 93: I1Ii111
  if 39 - 39: Ii1I
  if 10 - 10: OoOoOO00 . iIii1I11I1II1 / I1ii11iIi11i % iII111i / i11iIiiIii
  if 14 - 14: i11iIiiIii % o0oOOo0O0Ooo * O0 % iIii1I11I1II1 . IiII - II111iiii
  if 14 - 14: Ii1I % ooOoO0o - OoOoOO00
  if 52 - 52: OoO0O00 / i1IIi - Ii1I
  if 8 - 8: oO0o + ooOoO0o . I1ii11iIi11i . i1IIi / I1IiiI . IiII
  if 8 - 8: i1IIi * O0
  if 60 - 60: Oo0Ooo - II111iiii + I1IiiI
  if 17 - 17: OoOoOO00 % I1IiiI
  if 8 - 8: Oo0Ooo
  if 49 - 49: OoOoOO00 * I11i - o0oOOo0O0Ooo / OoO0O00 * oO0o
  if 51 - 51: ooOoO0o - iIii1I11I1II1 . I11i * OoOoOO00 + I1Ii111 * i1IIi
  if 37 - 37: IiII * oO0o / OoooooooOO . OoO0O00
  if 77 - 77: II111iiii + OoOoOO00 * OOooOOo
  if 9 - 9: II111iiii - i11iIiiIii * o0oOOo0O0Ooo % OoO0O00 * i11iIiiIii / I11i
  if 45 - 45: i11iIiiIii * iII111i - I1ii11iIi11i + ooOoO0o % iII111i
  if 11 - 11: iIii1I11I1II1
  if 48 - 48: iIii1I11I1II1 - Oo0Ooo
  if 80 - 80: i1IIi
  if 56 - 56: II111iiii - o0oOOo0O0Ooo
  if 48 - 48: Oo0Ooo - I1ii11iIi11i - II111iiii . Ii1I . oO0o / iIii1I11I1II1
  if 38 - 38: I1Ii111 % i11iIiiIii + Ii1I * ooOoO0o / I1Ii111
  if 93 - 93: oO0o
  if 60 - 60: I1Ii111 . oO0o / Oo0Ooo * ooOoO0o + OoOoOO00 - i1IIi
  if 13 - 13: i11iIiiIii * oO0o / I11i * I1IiiI
  if 31 - 31: iIii1I11I1II1 * Ii1I % OOooOOo . II111iiii
  if 56 - 56: IiII / i11iIiiIii . o0oOOo0O0Ooo . oO0o - i11iIiiIii
  if 23 - 23: I1ii11iIi11i * i11iIiiIii % ooOoO0o
  if 47 - 47: iIii1I11I1II1 . OOooOOo / I11i % II111iiii
  if 92 - 92: I1ii11iIi11i % i11iIiiIii
  if 82 - 82: I1Ii111 * I1ii11iIi11i % Ii1I / o0oOOo0O0Ooo
  if 28 - 28: iII111i % OoO0O00 - OOooOOo - Oo0Ooo
  if 16 - 16: i11iIiiIii - i11iIiiIii . OoOoOO00 / i1IIi
  if 76 - 76: O0 * OoO0O00 / O0
  if 23 - 23: I1ii11iIi11i . iIii1I11I1II1 - i11iIiiIii / II111iiii
  if 48 - 48: oO0o - II111iiii * I1IiiI
  if 78 - 78: I1IiiI * i11iIiiIii * II111iiii
  if 19 - 19: OoooooooOO * i11iIiiIii / O0 . I1IiiI % I11i
  if 35 - 35: iIii1I11I1II1 + I1IiiI - ooOoO0o / Oo0Ooo * I1ii11iIi11i * Oo0Ooo
  if 17 - 17: OoOoOO00
  if 24 - 24: iIii1I11I1II1 / OOooOOo % OoooooooOO / O0 / oO0o
  if 93 - 93: Oo0Ooo
  if 5 - 5: iII111i
  if 61 - 61: OOooOOo * OoO0O00 - O0
  if 30 - 30: iIii1I11I1II1
  if 14 - 14: o0oOOo0O0Ooo + Ii1I
  if 91 - 91: OoooooooOO / oO0o + OoOoOO00
  if 100 - 100: i1IIi
  if 13 - 13: i1IIi . I1ii11iIi11i * o0oOOo0O0Ooo
  if 31 - 31: i11iIiiIii % OoO0O00 . i11iIiiIii % oO0o - i1IIi
  if 62 - 62: oO0o + oO0o . OoooooooOO
  if 59 - 59: iIii1I11I1II1 . Oo0Ooo * I11i
  if 29 - 29: Oo0Ooo - I1IiiI * I11i
  if 58 - 58: i1IIi * Ii1I / ooOoO0o % iIii1I11I1II1
  if 24 - 24: OoOoOO00 - o0oOOo0O0Ooo * I1IiiI . I11i / OoO0O00 * Ii1I
  if 12 - 12: OoooooooOO % oO0o
  if 92 - 92: ooOoO0o % OoO0O00 + O0 + OoOoOO00 / OoO0O00 * iIii1I11I1II1
  if 79 - 79: O0
  if 71 - 71: OoO0O00 - O0
  if 73 - 73: iIii1I11I1II1
  if 7 - 7: OoOoOO00
  if 55 - 55: oO0o . OoO0O00 + iIii1I11I1II1 + OoOoOO00 / I1ii11iIi11i - O0
  if 14 - 14: II111iiii - OoO0O00 - O0 * OoooooooOO / I1IiiI
  if 3 - 3: I11i
  if 46 - 46: I1ii11iIi11i * I1Ii111 - iIii1I11I1II1
  if 25 - 25: II111iiii / OOooOOo + Oo0Ooo - iIii1I11I1II1 - OoOoOO00
  if 97 - 97: OOooOOo . OOooOOo / I1ii11iIi11i + I1IiiI * i1IIi
  if 53 - 53: O0
  if 28 - 28: iII111i % OoO0O00 . OoO0O00 / IiII * Oo0Ooo * iII111i
  if 49 - 49: I1IiiI / I1Ii111 * iII111i + I1IiiI % oO0o % ooOoO0o
  if 27 - 27: OoO0O00 / iII111i . I1ii11iIi11i
  if 71 - 71: OoO0O00 . i11iIiiIii . iIii1I11I1II1 + I1IiiI - o0oOOo0O0Ooo
  if 34 - 34: iII111i
  if 6 - 6: OoO0O00 . OoOoOO00 + I1ii11iIi11i
  if 24 - 24: OoO0O00 . Ii1I
  if 26 - 26: O0 * I1IiiI - OOooOOo * OoooooooOO * II111iiii % OoOoOO00
  if 56 - 56: OOooOOo * i11iIiiIii % ooOoO0o * OoOoOO00 % Oo0Ooo * IiII
  if 30 - 30: i1IIi + o0oOOo0O0Ooo - OoOoOO00 . OOooOOo
  if 95 - 95: i1IIi . I11i + O0 . I11i - I11i / Oo0Ooo
  if 41 - 41: OoooooooOO . OOooOOo - Ii1I * OoO0O00 % i11iIiiIii
  if 7 - 7: Ii1I
  if 16 - 16: IiII * o0oOOo0O0Ooo % II111iiii - II111iiii + ooOoO0o
  if 55 - 55: OoO0O00 % OoOoOO00
  if 58 - 58: Ii1I
  if 17 - 17: OoO0O00 - oO0o % Oo0Ooo % oO0o * I1Ii111 / IiII
  if 88 - 88: ooOoO0o . II111iiii * O0 % IiII
  if 15 - 15: O0 % i1IIi - OOooOOo . IiII
  if 1 - 1: I1IiiI
  if 40 - 40: o0oOOo0O0Ooo % I11i % O0
  if 88 - 88: o0oOOo0O0Ooo - oO0o
  if 73 - 73: II111iiii
  if 7 - 7: O0 / OoO0O00
  if 90 - 90: iII111i % oO0o / iIii1I11I1II1
  if 52 - 52: I1IiiI / o0oOOo0O0Ooo
  if 20 - 20: I1Ii111 . I1IiiI - iIii1I11I1II1 / iII111i
  if 46 - 46: I1Ii111 . i11iIiiIii
  if 89 - 89: OoO0O00 - OOooOOo - i1IIi - OoO0O00 % iIii1I11I1II1
  if 52 - 52: o0oOOo0O0Ooo * O0 + I1ii11iIi11i
  if 83 - 83: I11i + OOooOOo - OoooooooOO
  if 7 - 7: IiII % ooOoO0o / OoooooooOO / o0oOOo0O0Ooo + OoO0O00 - OoO0O00
  if 15 - 15: i1IIi + OOooOOo / Ii1I
  if 51 - 51: OOooOOo + O0
  if 91 - 91: i11iIiiIii + o0oOOo0O0Ooo % OoO0O00 / oO0o - i1IIi
  if 82 - 82: Ii1I . OoooooooOO + OoooooooOO % OoO0O00 % I1ii11iIi11i
  if 65 - 65: Oo0Ooo . I11i
  if 7 - 7: Oo0Ooo * II111iiii
  if 11 - 11: OoOoOO00 % OoooooooOO
  if 92 - 92: OoOoOO00 - iII111i * Ii1I - i1IIi
  if 87 - 87: Ii1I * I1Ii111 + iIii1I11I1II1 * o0oOOo0O0Ooo * iIii1I11I1II1 . I11i
  if 66 - 66: Ii1I / OoO0O00 . O0 . I11i % OoooooooOO / OOooOOo
  if 49 - 49: I1IiiI * iII111i - OoO0O00 % Ii1I + Ii1I * I1Ii111
  if 94 - 94: OoOoOO00 - I11i + Ii1I + OoOoOO00 + II111iiii
  if 61 - 61: IiII + Ii1I / oO0o . OoooooooOO + iII111i
  if 29 - 29: OOooOOo
  if 69 - 69: oO0o % OoooooooOO * iII111i
  if 58 - 58: oO0o / i11iIiiIii . OoOoOO00 % O0 / iIii1I11I1II1
  if 50 - 50: I1Ii111 . I11i / O0 . I11i
  if 91 - 91: i11iIiiIii . I1ii11iIi11i + I11i
  if 67 - 67: I1ii11iIi11i * I1Ii111 * I1IiiI / I11i - IiII + oO0o
  if 11 - 11: O0 + i1IIi / o0oOOo0O0Ooo * OoO0O00
  if 64 - 64: i1IIi % IiII . ooOoO0o . iIii1I11I1II1 + OoO0O00 - iIii1I11I1II1
  if 52 - 52: II111iiii - IiII
  if 91 - 91: iIii1I11I1II1 + iII111i . I11i % i11iIiiIii - i11iIiiIii + I1IiiI
  if 75 - 75: I1ii11iIi11i / I1IiiI - iIii1I11I1II1 / OoO0O00 * OOooOOo
  if 73 - 73: OoooooooOO % IiII / I1Ii111 * I11i + i1IIi % i11iIiiIii
  if 91 - 91: i11iIiiIii
  if 6 - 6: O0 - iIii1I11I1II1 + I1Ii111 . o0oOOo0O0Ooo * i11iIiiIii
  if 53 - 53: OOooOOo / I1IiiI / oO0o * OOooOOo / i1IIi - I1Ii111
  if 71 - 71: O0 + Oo0Ooo % oO0o - o0oOOo0O0Ooo
  if 82 - 82: iIii1I11I1II1
  if 64 - 64: ooOoO0o + I1IiiI % OOooOOo + II111iiii
  if 46 - 46: I1IiiI
  if 72 - 72: iII111i
class lisp_rloc_record ( ) :
 def __init__ ( self ) :
  self . priority = 0
  self . weight = 0
  self . mpriority = 0
  self . mweight = 0
  self . local_bit = False
  self . probe_bit = False
  self . reach_bit = False
  self . rloc = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . geo = None
  self . elp = None
  self . rle = None
  self . json = None
  self . rloc_name = None
  self . keys = None
  if 100 - 100: I1IiiI
  if 55 - 55: i1IIi % IiII
 def print_rloc_name ( self , cour = False ) :
  if ( self . rloc_name == None ) : return ( "" )
  IIiiI11iI = self . rloc_name
  if ( cour ) : IIiiI11iI = lisp_print_cour ( IIiiI11iI )
  return ( 'rloc-name: {}' . format ( blue ( IIiiI11iI , cour ) ) )
  if 24 - 24: Oo0Ooo % I11i . OoOoOO00 + IiII + OoOoOO00 - IiII
  if 13 - 13: i1IIi % OoO0O00 * OOooOOo - Oo0Ooo
 def print_record ( self , indent ) :
  O0ooo0Ooo = self . print_rloc_name ( )
  if ( O0ooo0Ooo != "" ) : O0ooo0Ooo = ", " + O0ooo0Ooo
  I1i1iiIII1i1 = ""
  if ( self . geo ) :
   II1 = ""
   if ( self . geo . geo_name ) : II1 = "'{}' " . format ( self . geo . geo_name )
   I1i1iiIII1i1 = ", geo: {}{}" . format ( II1 , self . geo . print_geo ( ) )
   if 17 - 17: OOooOOo - ooOoO0o % II111iiii . I1ii11iIi11i
  OoOiIIiI = ""
  if ( self . elp ) :
   II1 = ""
   if ( self . elp . elp_name ) : II1 = "'{}' " . format ( self . elp . elp_name )
   OoOiIIiI = ", elp: {}{}" . format ( II1 , self . elp . print_elp ( True ) )
   if 19 - 19: o0oOOo0O0Ooo * I1Ii111 / I1Ii111 * II111iiii
  oOOOO0o000OoO = ""
  if ( self . rle ) :
   II1 = ""
   if ( self . rle . rle_name ) : II1 = "'{}' " . format ( self . rle . rle_name )
   oOOOO0o000OoO = ", rle: {}{}" . format ( II1 , self . rle . print_rle ( False ,
 True ) )
   if 9 - 9: ooOoO0o
  oOo0oo0o0O0O = ""
  if ( self . json ) :
   II1 = ""
   if ( self . json . json_name ) :
    II1 = "'{}' " . format ( self . json . json_name )
    if 47 - 47: i1IIi
   oOo0oo0o0O0O = ", json: {}" . format ( self . json . print_json ( False ) )
   if 2 - 2: OoooooooOO
   if 13 - 13: oO0o . o0oOOo0O0Ooo . i11iIiiIii * I1ii11iIi11i / ooOoO0o
  I1i1Ii = ""
  if ( self . rloc . is_null ( ) == False and self . keys and self . keys [ 1 ] ) :
   I1i1Ii = ", " + self . keys [ 1 ] . print_keys ( )
   if 12 - 12: IiII + ooOoO0o . i11iIiiIii - iIii1I11I1II1
   if 27 - 27: I11i + iIii1I11I1II1
  oOOo0ooO0 = ( "{}RLOC-record -> flags: {}, {}/{}/{}/{}, afi: {}, rloc: "
 + "{}{}{}{}{}{}{}" )
  lprint ( oOOo0ooO0 . format ( indent , self . print_flags ( ) , self . priority ,
 self . weight , self . mpriority , self . mweight , self . rloc . afi ,
 red ( self . rloc . print_address_no_iid ( ) , False ) , O0ooo0Ooo , I1i1iiIII1i1 ,
 OoOiIIiI , oOOOO0o000OoO , oOo0oo0o0O0O , I1i1Ii ) )
  if 71 - 71: OoOoOO00 + oO0o % OOooOOo * I1IiiI
  if 89 - 89: Ii1I % I1Ii111 / Oo0Ooo * Ii1I + OoOoOO00
 def print_flags ( self ) :
  return ( "{}{}{}" . format ( "L" if self . local_bit else "l" , "P" if self . probe_bit else "p" , "R" if self . reach_bit else "r" ) )
  if 5 - 5: Ii1I * I1IiiI + I1Ii111
  if 22 - 22: Oo0Ooo . OoO0O00
  if 55 - 55: Oo0Ooo % OoooooooOO * II111iiii % OoooooooOO
 def store_rloc_entry ( self , rloc_entry ) :
  I1II = rloc_entry . rloc if ( rloc_entry . translated_rloc . is_null ( ) ) else rloc_entry . translated_rloc
  if 43 - 43: OoO0O00
  self . rloc . copy_address ( I1II )
  if 50 - 50: II111iiii + OoooooooOO / IiII
  if ( rloc_entry . rloc_name ) :
   self . rloc_name = rloc_entry . rloc_name
   if 82 - 82: i11iIiiIii - oO0o - i1IIi
   if 78 - 78: oO0o % iII111i / i1IIi / ooOoO0o
  if ( rloc_entry . geo ) :
   self . geo = rloc_entry . geo
  else :
   II1 = rloc_entry . geo_name
   if ( II1 and lisp_geo_list . has_key ( II1 ) ) :
    self . geo = lisp_geo_list [ II1 ]
    if 44 - 44: o0oOOo0O0Ooo + Ii1I + I1IiiI % O0
    if 100 - 100: OoooooooOO
  if ( rloc_entry . elp ) :
   self . elp = rloc_entry . elp
  else :
   II1 = rloc_entry . elp_name
   if ( II1 and lisp_elp_list . has_key ( II1 ) ) :
    self . elp = lisp_elp_list [ II1 ]
    if 27 - 27: i11iIiiIii % II111iiii + I1Ii111
    if 76 - 76: OOooOOo - I1Ii111 + iIii1I11I1II1 + I1IiiI * oO0o
  if ( rloc_entry . rle ) :
   self . rle = rloc_entry . rle
  else :
   II1 = rloc_entry . rle_name
   if ( II1 and lisp_rle_list . has_key ( II1 ) ) :
    self . rle = lisp_rle_list [ II1 ]
    if 93 - 93: i11iIiiIii * i11iIiiIii - I1IiiI + iIii1I11I1II1 * i11iIiiIii
    if 14 - 14: ooOoO0o . OoooooooOO . I1IiiI - IiII + iIii1I11I1II1
  if ( rloc_entry . json ) :
   self . json = rloc_entry . json
  else :
   II1 = rloc_entry . json_name
   if ( II1 and lisp_json_list . has_key ( II1 ) ) :
    self . json = lisp_json_list [ II1 ]
    if 47 - 47: OOooOOo % i1IIi
    if 23 - 23: Ii1I * Ii1I / I11i
  self . priority = rloc_entry . priority
  self . weight = rloc_entry . weight
  self . mpriority = rloc_entry . mpriority
  self . mweight = rloc_entry . mweight
  if 11 - 11: OOooOOo
  if 58 - 58: OoO0O00 * OoooooooOO
 def encode_json ( self , lisp_json ) :
  o0Ooo = lisp_json . json_string
  i1Ii1iiI = 0
  if ( lisp_json . json_encrypted ) :
   i1Ii1iiI = ( lisp_json . json_key_id << 5 ) | 0x02
   if 23 - 23: Oo0Ooo % II111iiii
   if 96 - 96: ooOoO0o % Ii1I
  OOOoooO000O0 = LISP_LCAF_JSON_TYPE
  I1i = socket . htons ( LISP_AFI_LCAF )
  OooO0OO0o = self . rloc . addr_length ( ) + 2
  if 46 - 46: Ii1I
  iII = socket . htons ( len ( o0Ooo ) + OooO0OO0o )
  if 14 - 14: OoO0O00 * OoooooooOO
  IIIii1i11111 = socket . htons ( len ( o0Ooo ) )
  IiiiIi1iiii11 = struct . pack ( "HBBBBHH" , I1i , 0 , 0 , OOOoooO000O0 , i1Ii1iiI ,
 iII , IIIii1i11111 )
  IiiiIi1iiii11 += o0Ooo
  if 45 - 45: iIii1I11I1II1 * I1IiiI . OoOoOO00
  if 97 - 97: I11i % II111iiii % Ii1I . II111iiii . iIii1I11I1II1
  if 98 - 98: i11iIiiIii + O0 - O0 - iII111i
  if 25 - 25: oO0o / O0 + I1Ii111 % i11iIiiIii / I1IiiI
  if ( lisp_is_json_telemetry ( o0Ooo ) ) :
   IiiiIi1iiii11 += struct . pack ( "H" , socket . htons ( self . rloc . afi ) )
   IiiiIi1iiii11 += self . rloc . pack_address ( )
  else :
   IiiiIi1iiii11 += struct . pack ( "H" , 0 )
   if 62 - 62: iII111i . I11i * i1IIi + iII111i
  return ( IiiiIi1iiii11 )
  if 95 - 95: Ii1I / o0oOOo0O0Ooo % ooOoO0o - I1IiiI / OOooOOo * OOooOOo
  if 6 - 6: OoO0O00 % IiII + iIii1I11I1II1
 def encode_lcaf ( self ) :
  I1i = socket . htons ( LISP_AFI_LCAF )
  IiIoOo0ooo = ""
  if ( self . geo ) :
   IiIoOo0ooo = self . geo . encode_geo ( )
   if 26 - 26: I11i - i1IIi - Oo0Ooo * O0 * OOooOOo . OoooooooOO
   if 99 - 99: oO0o . OoO0O00 / OOooOOo
  Ii1111i = ""
  if ( self . elp ) :
   i1iiIiI = ""
   for IIii in self . elp . elp_nodes :
    IiiiII = socket . htons ( IIii . address . afi )
    O0OooO00O0 = 0
    if ( IIii . eid ) : O0OooO00O0 |= 0x4
    if ( IIii . probe ) : O0OooO00O0 |= 0x2
    if ( IIii . strict ) : O0OooO00O0 |= 0x1
    O0OooO00O0 = socket . htons ( O0OooO00O0 )
    i1iiIiI += struct . pack ( "HH" , O0OooO00O0 , IiiiII )
    i1iiIiI += IIii . address . pack_address ( )
    if 22 - 22: iIii1I11I1II1 % iIii1I11I1II1 . o0oOOo0O0Ooo
    if 46 - 46: oO0o
   I1Iiiii1i = socket . htons ( len ( i1iiIiI ) )
   Ii1111i = struct . pack ( "HBBBBH" , I1i , 0 , 0 , LISP_LCAF_ELP_TYPE ,
 0 , I1Iiiii1i )
   Ii1111i += i1iiIiI
   if 78 - 78: i1IIi % oO0o + IiII
   if 75 - 75: O0 + I1ii11iIi11i
  oo0oO0 = ""
  if ( self . rle ) :
   i1ii1i1Iii = ""
   for IiioOoo in self . rle . rle_nodes :
    IiiiII = socket . htons ( IiioOoo . address . afi )
    i1ii1i1Iii += struct . pack ( "HBBH" , 0 , 0 , IiioOoo . level , IiiiII )
    i1ii1i1Iii += IiioOoo . address . pack_address ( )
    if ( IiioOoo . rloc_name ) :
     i1ii1i1Iii += struct . pack ( "H" , socket . htons ( LISP_AFI_NAME ) )
     i1ii1i1Iii += IiioOoo . rloc_name + "\0"
     if 15 - 15: o0oOOo0O0Ooo
     if 55 - 55: i11iIiiIii / OoooooooOO - I11i
     if 89 - 89: I11i - i1IIi - i1IIi * OOooOOo - O0
   oOo0 = socket . htons ( len ( i1ii1i1Iii ) )
   oo0oO0 = struct . pack ( "HBBBBH" , I1i , 0 , 0 , LISP_LCAF_RLE_TYPE ,
 0 , oOo0 )
   oo0oO0 += i1ii1i1Iii
   if 60 - 60: OoOoOO00 + i11iIiiIii
   if 3 - 3: II111iiii
  O0OOoO0000ooO = ""
  if ( self . json ) :
   O0OOoO0000ooO = self . encode_json ( self . json )
   if 53 - 53: iIii1I11I1II1
   if 79 - 79: Ii1I - II111iiii / oO0o + Oo0Ooo . I1IiiI
  OOoO0o0 = ""
  if ( self . rloc . is_null ( ) == False and self . keys and self . keys [ 1 ] ) :
   OOoO0o0 = self . keys [ 1 ] . encode_lcaf ( self . rloc )
   if 51 - 51: OoO0O00 . OoO0O00 - iIii1I11I1II1
   if 41 - 41: OoO0O00 * i11iIiiIii / i1IIi + o0oOOo0O0Ooo . IiII
  iii111iIiiIII = ""
  if ( self . rloc_name ) :
   iii111iIiiIII += struct . pack ( "H" , socket . htons ( LISP_AFI_NAME ) )
   iii111iIiiIII += self . rloc_name + "\0"
   if 21 - 21: OOooOOo / O0
   if 46 - 46: OoooooooOO % Oo0Ooo % i1IIi / ooOoO0o - I11i
  IiiiI = len ( IiIoOo0ooo ) + len ( Ii1111i ) + len ( oo0oO0 ) + len ( OOoO0o0 ) + 2 + len ( O0OOoO0000ooO ) + self . rloc . addr_length ( ) + len ( iii111iIiiIII )
  if 57 - 57: I1Ii111 * I1ii11iIi11i / i1IIi % i11iIiiIii
  IiiiI = socket . htons ( IiiiI )
  oOOo00Oo0 = struct . pack ( "HBBBBHH" , I1i , 0 , 0 , LISP_LCAF_AFI_LIST_TYPE ,
 0 , IiiiI , socket . htons ( self . rloc . afi ) )
  oOOo00Oo0 += self . rloc . pack_address ( )
  return ( oOOo00Oo0 + iii111iIiiIII + IiIoOo0ooo + Ii1111i + oo0oO0 + OOoO0o0 + O0OOoO0000ooO )
  if 78 - 78: iIii1I11I1II1 * OoOoOO00 - I1IiiI . O0 / I1Ii111
  if 5 - 5: I1ii11iIi11i % OoOoOO00 . OoooooooOO . o0oOOo0O0Ooo + i11iIiiIii
 def encode ( self ) :
  O0OooO00O0 = 0
  if ( self . local_bit ) : O0OooO00O0 |= 0x0004
  if ( self . probe_bit ) : O0OooO00O0 |= 0x0002
  if ( self . reach_bit ) : O0OooO00O0 |= 0x0001
  if 54 - 54: ooOoO0o - O0 + iII111i
  IiiiIi1iiii11 = struct . pack ( "BBBBHH" , self . priority , self . weight ,
 self . mpriority , self . mweight , socket . htons ( O0OooO00O0 ) ,
 socket . htons ( self . rloc . afi ) )
  if 34 - 34: Ii1I - OOooOOo % iII111i
  if ( self . geo or self . elp or self . rle or self . keys or self . rloc_name or self . json ) :
   if 48 - 48: oO0o - O0
   IiiiIi1iiii11 = IiiiIi1iiii11 [ 0 : - 2 ] + self . encode_lcaf ( )
  else :
   IiiiIi1iiii11 += self . rloc . pack_address ( )
   if 17 - 17: iIii1I11I1II1 . IiII / ooOoO0o % I11i + o0oOOo0O0Ooo - iIii1I11I1II1
  return ( IiiiIi1iiii11 )
  if 95 - 95: OoOoOO00 + OOooOOo - I11i * i1IIi + i1IIi * O0
  if 60 - 60: Oo0Ooo + I11i % iIii1I11I1II1 % oO0o - I1Ii111 / o0oOOo0O0Ooo
 def decode_lcaf ( self , packet , nonce , ms_json_encrypt ) :
  O0O00Oo = "HBBBBH"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 9 - 9: IiII / oO0o % O0 * I1Ii111 - iIii1I11I1II1 % i1IIi
  IiiiII , iI1i , O0OooO00O0 , OOOoooO000O0 , iiI1i111I1 , iII = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  if 83 - 83: OoOoOO00 + OOooOOo / OoooooooOO
  if 39 - 39: OoO0O00 % iII111i . oO0o . II111iiii - i11iIiiIii
  iII = socket . ntohs ( iII )
  packet = packet [ IiIii1i : : ]
  if ( iII > len ( packet ) ) : return ( None )
  if 85 - 85: O0 - OoOoOO00
  if 17 - 17: o0oOOo0O0Ooo / i1IIi / OOooOOo
  if 91 - 91: I1ii11iIi11i / Ii1I - OoOoOO00 . I11i / oO0o
  if 16 - 16: IiII % iII111i . oO0o . I1IiiI % O0 * I11i
  if ( OOOoooO000O0 == LISP_LCAF_AFI_LIST_TYPE ) :
   while ( iII > 0 ) :
    O0O00Oo = "H"
    IiIii1i = struct . calcsize ( O0O00Oo )
    if ( iII < IiIii1i ) : return ( None )
    if 99 - 99: OoOoOO00 / OoooooooOO + iII111i * I11i * i11iIiiIii + OOooOOo
    ii11I = len ( packet )
    IiiiII = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] ) [ 0 ]
    IiiiII = socket . ntohs ( IiiiII )
    if 40 - 40: II111iiii / I11i % I1IiiI - O0
    if ( IiiiII == LISP_AFI_LCAF ) :
     packet = self . decode_lcaf ( packet , nonce , ms_json_encrypt )
     if ( packet == None ) : return ( None )
    else :
     packet = packet [ IiIii1i : : ]
     self . rloc_name = None
     if ( IiiiII == LISP_AFI_NAME ) :
      packet , IIiiI11iI = lisp_decode_dist_name ( packet )
      self . rloc_name = IIiiI11iI
     else :
      self . rloc . afi = IiiiII
      packet = self . rloc . unpack_address ( packet )
      if ( packet == None ) : return ( None )
      self . rloc . mask_len = self . rloc . host_mask_len ( )
      if 39 - 39: i11iIiiIii - OoOoOO00 % OOooOOo + ooOoO0o + i11iIiiIii
      if 59 - 59: IiII / OoOoOO00 - I1Ii111 - ooOoO0o . oO0o
      if 87 - 87: oO0o + I1IiiI * I1Ii111 * o0oOOo0O0Ooo + O0
    iII -= ii11I - len ( packet )
    if 21 - 21: I1Ii111 + OoOoOO00 + OoOoOO00 . II111iiii / I1Ii111 . I1IiiI
    if 66 - 66: I1Ii111 % oO0o . iII111i * i1IIi
  elif ( OOOoooO000O0 == LISP_LCAF_GEO_COORD_TYPE ) :
   if 81 - 81: OoooooooOO * I1IiiI / I1Ii111
   if 10 - 10: I1IiiI - II111iiii / IiII * II111iiii
   if 67 - 67: II111iiii . Ii1I % oO0o . Oo0Ooo + IiII
   if 10 - 10: OOooOOo - OoO0O00 * oO0o / iIii1I11I1II1 - OoOoOO00
   I1Ii1i111I = lisp_geo ( "" )
   packet = I1Ii1i111I . decode_geo ( packet , iII , iiI1i111I1 )
   if ( packet == None ) : return ( None )
   self . geo = I1Ii1i111I
   if 51 - 51: O0 + Ii1I * OoooooooOO . oO0o + OoooooooOO
  elif ( OOOoooO000O0 == LISP_LCAF_JSON_TYPE ) :
   O0iI1Iii = iiI1i111I1 & 0x02
   if 35 - 35: I1ii11iIi11i + O0
   if 7 - 7: OoooooooOO % iII111i % Ii1I % II111iiii / oO0o
   if 15 - 15: OoO0O00
   if 18 - 18: OoooooooOO / OOooOOo % i1IIi - i1IIi / Oo0Ooo
   O0O00Oo = "H"
   IiIii1i = struct . calcsize ( O0O00Oo )
   if ( iII < IiIii1i ) : return ( None )
   if 94 - 94: I1Ii111 + i11iIiiIii / iII111i + OoooooooOO % i1IIi
   IIIii1i11111 = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] ) [ 0 ]
   IIIii1i11111 = socket . ntohs ( IIIii1i11111 )
   if ( iII < IiIii1i + IIIii1i11111 ) : return ( None )
   if 57 - 57: iIii1I11I1II1 - i11iIiiIii / II111iiii
   packet = packet [ IiIii1i : : ]
   self . json = lisp_json ( "" , packet [ 0 : IIIii1i11111 ] , O0iI1Iii ,
 ms_json_encrypt )
   packet = packet [ IIIii1i11111 : : ]
   if 35 - 35: I1IiiI - IiII * I1Ii111 - ooOoO0o % oO0o
   if 88 - 88: IiII * OoO0O00 / IiII * I1IiiI + O0 / IiII
   if 41 - 41: OoOoOO00
   if 81 - 81: Ii1I . I1IiiI % o0oOOo0O0Ooo . OoOoOO00
   IiiiII = socket . ntohs ( struct . unpack ( "H" , packet [ : 2 ] ) [ 0 ] )
   packet = packet [ 2 : : ]
   if 94 - 94: oO0o % Oo0Ooo + OoO0O00 * oO0o - i11iIiiIii / I11i
   if ( IiiiII != 0 and lisp_is_json_telemetry ( self . json . json_string ) ) :
    self . rloc . afi = IiiiII
    packet = self . rloc . unpack_address ( packet )
    if 46 - 46: IiII - OoO0O00 * iII111i . I1Ii111 - ooOoO0o . i1IIi
    if 53 - 53: I1Ii111 * I1IiiI + Oo0Ooo + I1IiiI + OOooOOo
  elif ( OOOoooO000O0 == LISP_LCAF_ELP_TYPE ) :
   if 8 - 8: i11iIiiIii + OoOoOO00 . I1ii11iIi11i / OoooooooOO % II111iiii
   if 21 - 21: oO0o - o0oOOo0O0Ooo + ooOoO0o . I1IiiI * oO0o * Ii1I
   if 41 - 41: i1IIi % i11iIiiIii + I11i % OoooooooOO / I1ii11iIi11i
   if 8 - 8: OoooooooOO - OoO0O00 / i11iIiiIii / O0 . IiII
   O0OoO0O0O0oO = lisp_elp ( None )
   O0OoO0O0O0oO . elp_nodes = [ ]
   while ( iII > 0 ) :
    O0OooO00O0 , IiiiII = struct . unpack ( "HH" , packet [ : 4 ] )
    if 58 - 58: I1ii11iIi11i + Oo0Ooo . Oo0Ooo / iII111i . i11iIiiIii
    IiiiII = socket . ntohs ( IiiiII )
    if ( IiiiII == LISP_AFI_LCAF ) : return ( None )
    if 8 - 8: I1ii11iIi11i + O0 - oO0o % II111iiii . I1Ii111
    IIii = lisp_elp_node ( )
    O0OoO0O0O0oO . elp_nodes . append ( IIii )
    if 86 - 86: IiII
    O0OooO00O0 = socket . ntohs ( O0OooO00O0 )
    IIii . eid = ( O0OooO00O0 & 0x4 )
    IIii . probe = ( O0OooO00O0 & 0x2 )
    IIii . strict = ( O0OooO00O0 & 0x1 )
    IIii . address . afi = IiiiII
    IIii . address . mask_len = IIii . address . host_mask_len ( )
    packet = IIii . address . unpack_address ( packet [ 4 : : ] )
    iII -= IIii . address . addr_length ( ) + 4
    if 71 - 71: Ii1I - i1IIi . I1IiiI
   O0OoO0O0O0oO . select_elp_node ( )
   self . elp = O0OoO0O0O0oO
   if 15 - 15: i1IIi % II111iiii / II111iiii - I1ii11iIi11i - I11i % i1IIi
  elif ( OOOoooO000O0 == LISP_LCAF_RLE_TYPE ) :
   if 54 - 54: i1IIi . OoO0O00 + iII111i + OoO0O00 * i1IIi
   if 13 - 13: Oo0Ooo / OoO0O00 + OOooOOo
   if 90 - 90: OoO0O00 * i11iIiiIii / oO0o
   if 91 - 91: iII111i - OoOoOO00 / Oo0Ooo % II111iiii / II111iiii / o0oOOo0O0Ooo
   iI1Ii11 = lisp_rle ( None )
   iI1Ii11 . rle_nodes = [ ]
   while ( iII > 0 ) :
    oOo0oo , IIIi1i1iIIIi , oOOoOoooOo0o , IiiiII = struct . unpack ( "HBBH" , packet [ : 6 ] )
    if 59 - 59: i11iIiiIii - I11i * Oo0Ooo % o0oOOo0O0Ooo + i1IIi
    IiiiII = socket . ntohs ( IiiiII )
    if ( IiiiII == LISP_AFI_LCAF ) : return ( None )
    if 30 - 30: ooOoO0o / iII111i
    IiioOoo = lisp_rle_node ( )
    iI1Ii11 . rle_nodes . append ( IiioOoo )
    if 66 - 66: ooOoO0o / IiII * iIii1I11I1II1
    IiioOoo . level = oOOoOoooOo0o
    IiioOoo . address . afi = IiiiII
    IiioOoo . address . mask_len = IiioOoo . address . host_mask_len ( )
    packet = IiioOoo . address . unpack_address ( packet [ 6 : : ] )
    if 42 - 42: I1Ii111 - i11iIiiIii % II111iiii * ooOoO0o . O0 % I11i
    iII -= IiioOoo . address . addr_length ( ) + 6
    if ( iII >= 2 ) :
     IiiiII = struct . unpack ( "H" , packet [ : 2 ] ) [ 0 ]
     if ( socket . ntohs ( IiiiII ) == LISP_AFI_NAME ) :
      packet = packet [ 2 : : ]
      packet , IiioOoo . rloc_name = lisp_decode_dist_name ( packet )
      if 82 - 82: Oo0Ooo % O0 + I1ii11iIi11i % I1ii11iIi11i
      if ( packet == None ) : return ( None )
      iII -= len ( IiioOoo . rloc_name ) + 1 + 2
      if 74 - 74: O0 * IiII . I11i - I1Ii111 + O0 + I11i
      if 48 - 48: oO0o . o0oOOo0O0Ooo - OOooOOo
      if 29 - 29: Oo0Ooo - Ii1I - Oo0Ooo
   self . rle = iI1Ii11
   self . rle . build_forwarding_list ( )
   if 89 - 89: Oo0Ooo . OoO0O00 . I1ii11iIi11i * oO0o . O0
  elif ( OOOoooO000O0 == LISP_LCAF_SECURITY_TYPE ) :
   if 72 - 72: i11iIiiIii % I11i / I1Ii111 + I1IiiI * iII111i
   if 69 - 69: I1Ii111 + O0 . IiII . o0oOOo0O0Ooo
   if 38 - 38: IiII / i1IIi
   if 60 - 60: OoOoOO00
   if 75 - 75: II111iiii / iIii1I11I1II1 / OoooooooOO
   oO0ooOoOooO00o00 = packet
   I1 = lisp_keys ( 1 )
   packet = I1 . decode_lcaf ( oO0ooOoOooO00o00 , iII , False )
   if ( packet == None ) : return ( None )
   if 61 - 61: IiII . IiII
   if 17 - 17: OoOoOO00 % Oo0Ooo / I1Ii111 . Ii1I % OoO0O00
   if 32 - 32: I1IiiI + ooOoO0o / O0 * i11iIiiIii % Oo0Ooo + II111iiii
   if 95 - 95: iII111i / ooOoO0o + I1Ii111
   o0OOoOoo = [ LISP_CS_25519_CBC , LISP_CS_25519_CHACHA ]
   if ( I1 . cipher_suite in o0OOoOoo ) :
    if ( I1 . cipher_suite == LISP_CS_25519_CBC ) :
     o0Oo = lisp_keys ( 1 , do_poly = False , do_chacha = False )
     if 78 - 78: iIii1I11I1II1 / I1IiiI - IiII
    if ( I1 . cipher_suite == LISP_CS_25519_CHACHA ) :
     o0Oo = lisp_keys ( 1 , do_poly = True , do_chacha = True )
     if 81 - 81: I1ii11iIi11i
   else :
    o0Oo = lisp_keys ( 1 , do_poly = False , do_chacha = False )
    if 31 - 31: O0 % ooOoO0o / I1IiiI * iII111i % iIii1I11I1II1 * OoOoOO00
   packet = o0Oo . decode_lcaf ( oO0ooOoOooO00o00 , iII , False )
   if ( packet == None ) : return ( None )
   if 76 - 76: I1Ii111 - O0
   if ( len ( packet ) < 2 ) : return ( None )
   IiiiII = struct . unpack ( "H" , packet [ : 2 ] ) [ 0 ]
   self . rloc . afi = socket . ntohs ( IiiiII )
   if ( len ( packet ) < self . rloc . addr_length ( ) ) : return ( None )
   packet = self . rloc . unpack_address ( packet [ 2 : : ] )
   if ( packet == None ) : return ( None )
   self . rloc . mask_len = self . rloc . host_mask_len ( )
   if 23 - 23: O0 * Ii1I * ooOoO0o % ooOoO0o
   if 7 - 7: II111iiii + I11i
   if 99 - 99: iIii1I11I1II1 * oO0o
   if 37 - 37: ooOoO0o * iII111i * I11i
   if 11 - 11: I1IiiI
   if 48 - 48: O0 . I11i
   if ( self . rloc . is_null ( ) ) : return ( packet )
   if 9 - 9: oO0o / Oo0Ooo
   Ooooo = self . rloc_name
   if ( Ooooo ) : Ooooo = blue ( self . rloc_name , False )
   if 45 - 45: I11i
   if 90 - 90: OoO0O00 * I1IiiI - I1IiiI % OoO0O00
   if 84 - 84: I1IiiI % I1IiiI * Ii1I
   if 75 - 75: iIii1I11I1II1 - I1Ii111
   if 86 - 86: O0 + O0 / I11i - iIii1I11I1II1
   if 42 - 42: OOooOOo
   Ii11i = self . keys [ 1 ] if self . keys else None
   if ( Ii11i == None ) :
    if ( o0Oo . remote_public_key == None ) :
     O0ooo = bold ( "No remote encap-public-key supplied" , False )
     lprint ( "    {} for {}" . format ( O0ooo , Ooooo ) )
     o0Oo = None
    else :
     O0ooo = bold ( "New encap-keying with new state" , False )
     lprint ( "    {} for {}" . format ( O0ooo , Ooooo ) )
     o0Oo . compute_shared_key ( "encap" )
     if 39 - 39: O0 % Ii1I . I11i * o0oOOo0O0Ooo
     if 14 - 14: I11i . iIii1I11I1II1 + I1Ii111 % OoooooooOO
     if 9 - 9: oO0o + Ii1I / I1ii11iIi11i * iIii1I11I1II1 + o0oOOo0O0Ooo
     if 64 - 64: I11i % i11iIiiIii % I1ii11iIi11i
     if 14 - 14: I1Ii111 - OoOoOO00 - I1ii11iIi11i % I11i + OoooooooOO
     if 4 - 4: I1Ii111 - I1IiiI / iIii1I11I1II1 + I1ii11iIi11i % iIii1I11I1II1 * I1IiiI
     if 30 - 30: i11iIiiIii % OOooOOo
     if 52 - 52: I11i - oO0o . i11iIiiIii - II111iiii + Ii1I . iII111i
     if 27 - 27: I1IiiI + OoOoOO00 + iII111i
     if 70 - 70: I11i + IiII . ooOoO0o - I1ii11iIi11i
   if ( Ii11i ) :
    if ( o0Oo . remote_public_key == None ) :
     o0Oo = None
     o0OOo = bold ( "Remote encap-unkeying occurred" , False )
     lprint ( "    {} for {}" . format ( o0OOo , Ooooo ) )
    elif ( Ii11i . compare_keys ( o0Oo ) ) :
     o0Oo = Ii11i
     lprint ( "    Maintain stored encap-keys for {}" . format ( Ooooo ) )
     if 34 - 34: i1IIi % Oo0Ooo . oO0o
    else :
     if ( Ii11i . remote_public_key == None ) :
      O0ooo = "New encap-keying for existing state"
     else :
      O0ooo = "Remote encap-rekeying"
      if 36 - 36: I1ii11iIi11i / I1Ii111 - IiII + OOooOOo + I1Ii111
     lprint ( "    {} for {}" . format ( bold ( O0ooo , False ) ,
 Ooooo ) )
     Ii11i . remote_public_key = o0Oo . remote_public_key
     Ii11i . compute_shared_key ( "encap" )
     o0Oo = Ii11i
     if 62 - 62: Oo0Ooo . OoO0O00 * I1Ii111 . i11iIiiIii * O0
     if 10 - 10: Oo0Ooo / OoOoOO00 * OOooOOo - IiII + Ii1I
   self . keys = [ None , o0Oo , None , None ]
   if 62 - 62: I1IiiI . Ii1I
  else :
   if 74 - 74: Ii1I - I11i % ooOoO0o - I1IiiI - Ii1I - II111iiii
   if 81 - 81: i1IIi * I1ii11iIi11i + IiII - OoO0O00 * i1IIi
   if 6 - 6: iIii1I11I1II1 % OoOoOO00 % II111iiii % o0oOOo0O0Ooo
   if 52 - 52: Ii1I - I1IiiI * iIii1I11I1II1 % Oo0Ooo * OOooOOo
   packet = packet [ iII : : ]
   if 67 - 67: OoooooooOO * I11i * Ii1I * iIii1I11I1II1
  return ( packet )
  if 22 - 22: OoO0O00 / o0oOOo0O0Ooo
  if 35 - 35: I1Ii111 / I1Ii111 + o0oOOo0O0Ooo - oO0o
 def decode ( self , packet , nonce , ms_json_encrypt = False ) :
  O0O00Oo = "BBBBHH"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 40 - 40: OoOoOO00 - II111iiii
  self . priority , self . weight , self . mpriority , self . mweight , O0OooO00O0 , IiiiII = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  if 29 - 29: I1IiiI - O0
  if 36 - 36: I1IiiI * I1IiiI
  O0OooO00O0 = socket . ntohs ( O0OooO00O0 )
  IiiiII = socket . ntohs ( IiiiII )
  self . local_bit = True if ( O0OooO00O0 & 0x0004 ) else False
  self . probe_bit = True if ( O0OooO00O0 & 0x0002 ) else False
  self . reach_bit = True if ( O0OooO00O0 & 0x0001 ) else False
  if 79 - 79: I1Ii111 - I11i
  if ( IiiiII == LISP_AFI_LCAF ) :
   packet = packet [ IiIii1i - 2 : : ]
   packet = self . decode_lcaf ( packet , nonce , ms_json_encrypt )
  else :
   self . rloc . afi = IiiiII
   packet = packet [ IiIii1i : : ]
   packet = self . rloc . unpack_address ( packet )
   if 49 - 49: II111iiii + O0 * ooOoO0o - Oo0Ooo
  self . rloc . mask_len = self . rloc . host_mask_len ( )
  return ( packet )
  if 89 - 89: I1IiiI + I11i . oO0o . II111iiii + oO0o / Oo0Ooo
  if 32 - 32: OoO0O00 % oO0o * I1ii11iIi11i + I11i / I1Ii111
 def end_of_rlocs ( self , packet , rloc_count ) :
  for iIi1I1 in range ( rloc_count ) :
   packet = self . decode ( packet , None , False )
   if ( packet == None ) : return ( None )
   if 5 - 5: o0oOOo0O0Ooo + iII111i / OoooooooOO + Ii1I . OoOoOO00 / oO0o
  return ( packet )
  if 18 - 18: II111iiii . o0oOOo0O0Ooo
  if 75 - 75: OoooooooOO - Oo0Ooo
  if 56 - 56: II111iiii - i11iIiiIii - oO0o . o0oOOo0O0Ooo
  if 4 - 4: i1IIi
  if 91 - 91: IiII . OoO0O00 * Ii1I / o0oOOo0O0Ooo
  if 41 - 41: I1IiiI . OoO0O00 / i1IIi . Oo0Ooo . oO0o
  if 44 - 44: iII111i * I11i + i11iIiiIii + i1IIi / IiII * II111iiii
  if 58 - 58: OOooOOo
  if 72 - 72: OoO0O00 + OOooOOo - Oo0Ooo % ooOoO0o . IiII
  if 95 - 95: iII111i % OOooOOo - IiII - OoOoOO00 % o0oOOo0O0Ooo * O0
  if 16 - 16: I1Ii111 / Oo0Ooo
  if 48 - 48: Oo0Ooo / oO0o + iII111i % iII111i
  if 9 - 9: I1ii11iIi11i - o0oOOo0O0Ooo . Oo0Ooo + I1ii11iIi11i . OOooOOo
  if 30 - 30: OoooooooOO - iIii1I11I1II1 / oO0o * Ii1I / Ii1I
  if 52 - 52: OoOoOO00 - OoO0O00 + I1IiiI + IiII
  if 49 - 49: oO0o / I11i - oO0o
  if 31 - 31: OoOoOO00 + I1IiiI + I1ii11iIi11i + I11i * II111iiii % oO0o
  if 90 - 90: OOooOOo * iIii1I11I1II1 / i1IIi
  if 60 - 60: OOooOOo * I1Ii111 . oO0o
  if 47 - 47: oO0o % OOooOOo / OOooOOo % OoOoOO00 % I1Ii111 / OoOoOO00
  if 51 - 51: I1IiiI . I11i - OoOoOO00
  if 10 - 10: Oo0Ooo * OOooOOo / IiII . o0oOOo0O0Ooo
  if 97 - 97: Ii1I . Ii1I % iII111i
  if 49 - 49: Oo0Ooo % OOooOOo - OoooooooOO + IiII
  if 54 - 54: iIii1I11I1II1 - OoooooooOO / I11i / oO0o % I1IiiI + OoOoOO00
  if 26 - 26: OoO0O00 * II111iiii % OOooOOo * iII111i + iII111i
  if 25 - 25: I11i - I1ii11iIi11i
  if 100 - 100: I1Ii111 / Ii1I + OoOoOO00 . OoooooooOO
  if 83 - 83: O0
  if 35 - 35: i11iIiiIii - I11i . OoOoOO00 * II111iiii % i11iIiiIii
class lisp_map_referral ( ) :
 def __init__ ( self ) :
  self . record_count = 0
  self . nonce = 0
  if 55 - 55: o0oOOo0O0Ooo / O0 / OoooooooOO * Oo0Ooo % iII111i
  if 24 - 24: I1ii11iIi11i % OOooOOo + OoooooooOO + OoO0O00
 def print_map_referral ( self ) :
  lprint ( "{} -> record-count: {}, nonce: 0x{}" . format ( bold ( "Map-Referral" , False ) , self . record_count ,
  # OOooOOo + o0oOOo0O0Ooo + OoOoOO00 + iIii1I11I1II1 + II111iiii - O0
 lisp_hex_string ( self . nonce ) ) )
  if 22 - 22: Ii1I % O0 - oO0o / I1IiiI * OoOoOO00
  if 31 - 31: IiII + I1IiiI * I11i % OoO0O00
 def encode ( self ) :
  i1OOoO0OO0oO = ( LISP_MAP_REFERRAL << 28 ) | self . record_count
  IiiiIi1iiii11 = struct . pack ( "I" , socket . htonl ( i1OOoO0OO0oO ) )
  IiiiIi1iiii11 += struct . pack ( "Q" , self . nonce )
  return ( IiiiIi1iiii11 )
  if 77 - 77: II111iiii * OoooooooOO * ooOoO0o % OOooOOo % OOooOOo * i1IIi
  if 37 - 37: I1ii11iIi11i * iII111i . ooOoO0o - I1IiiI
 def decode ( self , packet ) :
  O0O00Oo = "I"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 95 - 95: I11i / I1Ii111 % Ii1I % o0oOOo0O0Ooo . Ii1I
  i1OOoO0OO0oO = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  i1OOoO0OO0oO = socket . ntohl ( i1OOoO0OO0oO [ 0 ] )
  self . record_count = i1OOoO0OO0oO & 0xff
  packet = packet [ IiIii1i : : ]
  if 40 - 40: iII111i . ooOoO0o % OoooooooOO % OOooOOo / OoooooooOO / Oo0Ooo
  O0O00Oo = "Q"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 93 - 93: o0oOOo0O0Ooo % iIii1I11I1II1 % oO0o / I1IiiI
  self . nonce = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] ) [ 0 ]
  packet = packet [ IiIii1i : : ]
  return ( packet )
  if 98 - 98: II111iiii + Oo0Ooo - i1IIi + iII111i + II111iiii
  if 93 - 93: O0
  if 78 - 78: I1Ii111 * i1IIi + OoooooooOO * ooOoO0o
  if 69 - 69: i1IIi
  if 83 - 83: I1ii11iIi11i . ooOoO0o + I1IiiI + O0
  if 78 - 78: O0 + Oo0Ooo
  if 14 - 14: O0
  if 67 - 67: II111iiii / O0
class lisp_ddt_entry ( ) :
 def __init__ ( self ) :
  self . eid = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . group = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . uptime = lisp_get_timestamp ( )
  self . delegation_set = [ ]
  self . source_cache = None
  self . map_referrals_sent = 0
  if 10 - 10: i1IIi / Oo0Ooo
  if 20 - 20: Oo0Ooo * I1Ii111 / I1ii11iIi11i . ooOoO0o
 def is_auth_prefix ( self ) :
  if ( len ( self . delegation_set ) != 0 ) : return ( False )
  if ( self . is_star_g ( ) ) : return ( False )
  return ( True )
  if 67 - 67: o0oOOo0O0Ooo . Oo0Ooo % I11i
  if 38 - 38: OOooOOo - OoO0O00 . ooOoO0o
 def is_ms_peer_entry ( self ) :
  if ( len ( self . delegation_set ) == 0 ) : return ( False )
  return ( self . delegation_set [ 0 ] . is_ms_peer ( ) )
  if 50 - 50: o0oOOo0O0Ooo
  if 85 - 85: II111iiii . iII111i - i1IIi
 def print_referral_type ( self ) :
  if ( len ( self . delegation_set ) == 0 ) : return ( "unknown" )
  I1I = self . delegation_set [ 0 ]
  return ( I1I . print_node_type ( ) )
  if 80 - 80: II111iiii + I1ii11iIi11i
  if 9 - 9: I11i
 def print_eid_tuple ( self ) :
  return ( lisp_print_eid_tuple ( self . eid , self . group ) )
  if 69 - 69: Oo0Ooo % I1Ii111
  if 80 - 80: I11i * oO0o % iIii1I11I1II1 / iII111i
 def add_cache ( self ) :
  if ( self . group . is_null ( ) ) :
   lisp_ddt_cache . add_cache ( self . eid , self )
  else :
   O0oo0OoOO = lisp_ddt_cache . lookup_cache ( self . group , True )
   if ( O0oo0OoOO == None ) :
    O0oo0OoOO = lisp_ddt_entry ( )
    O0oo0OoOO . eid . copy_address ( self . group )
    O0oo0OoOO . group . copy_address ( self . group )
    lisp_ddt_cache . add_cache ( self . group , O0oo0OoOO )
    if 58 - 58: II111iiii . I1IiiI . i1IIi
   if ( self . eid . is_null ( ) ) : self . eid . make_default_route ( O0oo0OoOO . group )
   O0oo0OoOO . add_source_entry ( self )
   if 60 - 60: iIii1I11I1II1 + ooOoO0o * i11iIiiIii + OoooooooOO
   if 43 - 43: I1ii11iIi11i % Oo0Ooo - i11iIiiIii / I1Ii111 * i1IIi
   if 78 - 78: o0oOOo0O0Ooo / OOooOOo / oO0o
 def add_source_entry ( self , source_ddt ) :
  if ( self . source_cache == None ) : self . source_cache = lisp_cache ( )
  self . source_cache . add_cache ( source_ddt . eid , source_ddt )
  if 9 - 9: IiII + O0 / I1IiiI
  if 92 - 92: OOooOOo / i11iIiiIii + OoooooooOO
 def lookup_source_cache ( self , source , exact ) :
  if ( self . source_cache == None ) : return ( None )
  return ( self . source_cache . lookup_cache ( source , exact ) )
  if 9 - 9: iII111i
  if 9 - 9: O0 / o0oOOo0O0Ooo / I11i - i11iIiiIii - iII111i / IiII
 def is_star_g ( self ) :
  if ( self . group . is_null ( ) ) : return ( False )
  return ( self . eid . is_exact_match ( self . group ) )
  if 46 - 46: IiII + OoooooooOO % I1IiiI
  if 51 - 51: I1IiiI * I1Ii111 . i11iIiiIii % Oo0Ooo . i1IIi - oO0o
  if 56 - 56: Oo0Ooo / II111iiii
class lisp_ddt_node ( ) :
 def __init__ ( self ) :
  self . delegate_address = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . public_key = ""
  self . map_server_peer = False
  self . map_server_child = False
  self . priority = 0
  self . weight = 0
  if 76 - 76: OoOoOO00 % OoO0O00 * O0
  if 39 - 39: ooOoO0o / iII111i
 def print_node_type ( self ) :
  if ( self . is_ddt_child ( ) ) : return ( "ddt-child" )
  if ( self . is_ms_child ( ) ) : return ( "map-server-child" )
  if ( self . is_ms_peer ( ) ) : return ( "map-server-peer" )
  if 94 - 94: oO0o + iII111i * OoOoOO00 - i1IIi / OoooooooOO
  if 59 - 59: I11i % Ii1I / OoOoOO00
 def is_ddt_child ( self ) :
  if ( self . map_server_child ) : return ( False )
  if ( self . map_server_peer ) : return ( False )
  return ( True )
  if 99 - 99: Ii1I + II111iiii / i11iIiiIii - IiII / iII111i + iII111i
  if 55 - 55: IiII + OoooooooOO * I1ii11iIi11i . IiII * I1ii11iIi11i + IiII
 def is_ms_child ( self ) :
  return ( self . map_server_child )
  if 81 - 81: iIii1I11I1II1 . ooOoO0o + OoOoOO00
  if 31 - 31: I11i / OoOoOO00 + o0oOOo0O0Ooo
 def is_ms_peer ( self ) :
  return ( self . map_server_peer )
  if 80 - 80: Oo0Ooo
  if 58 - 58: I1Ii111 + OOooOOo
  if 76 - 76: II111iiii - o0oOOo0O0Ooo % OoO0O00 + iII111i
  if 38 - 38: I1Ii111 - I11i * i1IIi + iIii1I11I1II1
  if 41 - 41: Ii1I . OoO0O00 + I1ii11iIi11i + OoOoOO00
  if 76 - 76: iII111i - iIii1I11I1II1
  if 23 - 23: I11i / OoO0O00 % OOooOOo
class lisp_ddt_map_request ( ) :
 def __init__ ( self , lisp_sockets , packet , eid , group , nonce ) :
  self . uptime = lisp_get_timestamp ( )
  self . lisp_sockets = lisp_sockets
  self . packet = packet
  self . eid = eid
  self . group = group
  self . nonce = nonce
  self . mr_source = None
  self . sport = 0
  self . itr = None
  self . retry_count = 0
  self . send_count = 0
  self . retransmit_timer = None
  self . last_request_sent_to = None
  self . from_pitr = False
  self . tried_root = False
  self . last_cached_prefix = [ None , None ]
  if 9 - 9: ooOoO0o % I1ii11iIi11i . OoooooooOO + OoO0O00 % OOooOOo * OoooooooOO
  if 21 - 21: Ii1I % O0
 def print_ddt_map_request ( self ) :
  lprint ( "Queued Map-Request from {}ITR {}->{}, nonce 0x{}" . format ( "P" if self . from_pitr else "" ,
  # oO0o
 red ( self . itr . print_address ( ) , False ) ,
 green ( self . eid . print_address ( ) , False ) , self . nonce ) )
  if 93 - 93: Ii1I + iII111i
  if 89 - 89: Oo0Ooo * II111iiii * I1Ii111 / I1IiiI + I1IiiI . o0oOOo0O0Ooo
 def queue_map_request ( self ) :
  self . retransmit_timer = threading . Timer ( LISP_DDT_MAP_REQUEST_INTERVAL ,
 lisp_retransmit_ddt_map_request , [ self ] )
  self . retransmit_timer . start ( )
  lisp_ddt_map_requestQ [ str ( self . nonce ) ] = self
  if 40 - 40: O0 - i1IIi - i11iIiiIii % IiII % II111iiii
  if 54 - 54: o0oOOo0O0Ooo + I1IiiI % ooOoO0o . Ii1I - o0oOOo0O0Ooo
 def dequeue_map_request ( self ) :
  self . retransmit_timer . cancel ( )
  if ( lisp_ddt_map_requestQ . has_key ( str ( self . nonce ) ) ) :
   lisp_ddt_map_requestQ . pop ( str ( self . nonce ) )
   if 1 - 1: I1IiiI + iIii1I11I1II1
   if 81 - 81: OoO0O00 * ooOoO0o
   if 98 - 98: OoOoOO00 % ooOoO0o * I1ii11iIi11i
 def print_eid_tuple ( self ) :
  return ( lisp_print_eid_tuple ( self . eid , self . group ) )
  if 64 - 64: OOooOOo + I11i . ooOoO0o
  if 17 - 17: OoOoOO00 . I1Ii111
  if 10 - 10: I1ii11iIi11i * I1Ii111 * Ii1I * o0oOOo0O0Ooo - o0oOOo0O0Ooo + OoOoOO00
  if 92 - 92: Ii1I / iII111i . I1ii11iIi11i % Ii1I
  if 18 - 18: OOooOOo + I1IiiI + i1IIi + o0oOOo0O0Ooo % o0oOOo0O0Ooo
  if 48 - 48: O0
  if 5 - 5: OOooOOo / i11iIiiIii . I11i % OOooOOo
  if 1 - 1: II111iiii + O0 * OoOoOO00 / IiII . O0
  if 87 - 87: IiII + I1IiiI
  if 74 - 74: OoO0O00 + OoO0O00 % iII111i / I11i / O0
  if 54 - 54: o0oOOo0O0Ooo / OoooooooOO * ooOoO0o . OoOoOO00 - I1Ii111
  if 69 - 69: oO0o - OoO0O00
  if 80 - 80: ooOoO0o + iIii1I11I1II1 . II111iiii + I1IiiI - oO0o % OoOoOO00
  if 10 - 10: iIii1I11I1II1
  if 44 - 44: OoOoOO00 * oO0o . I1ii11iIi11i + i11iIiiIii
  if 85 - 85: I11i
  if 36 - 36: ooOoO0o % OoO0O00
  if 1 - 1: OoooooooOO - OoOoOO00
  if 35 - 35: I1Ii111
  if 35 - 35: Oo0Ooo - iIii1I11I1II1 / i1IIi + OoO0O00 - OoooooooOO / i11iIiiIii
LISP_DDT_ACTION_SITE_NOT_FOUND = - 2
LISP_DDT_ACTION_NULL = - 1
LISP_DDT_ACTION_NODE_REFERRAL = 0
LISP_DDT_ACTION_MS_REFERRAL = 1
LISP_DDT_ACTION_MS_ACK = 2
LISP_DDT_ACTION_MS_NOT_REG = 3
LISP_DDT_ACTION_DELEGATION_HOLE = 4
LISP_DDT_ACTION_NOT_AUTH = 5
LISP_DDT_ACTION_MAX = LISP_DDT_ACTION_NOT_AUTH
if 79 - 79: I1IiiI * ooOoO0o * ooOoO0o
lisp_map_referral_action_string = [
 "node-referral" , "ms-referral" , "ms-ack" , "ms-not-registered" ,
 "delegation-hole" , "not-authoritative" ]
if 92 - 92: iII111i % I1ii11iIi11i
if 16 - 16: oO0o
if 52 - 52: OoooooooOO % ooOoO0o - I1Ii111 * I11i
if 24 - 24: Ii1I + IiII + OoooooooOO / oO0o / I1IiiI + IiII
if 52 - 52: ooOoO0o
if 38 - 38: OoO0O00 + I1IiiI % IiII
if 87 - 87: oO0o * Ii1I - I1Ii111 / oO0o
if 65 - 65: OoOoOO00
if 87 - 87: I11i - i11iIiiIii - OOooOOo . OoOoOO00 + IiII . OoO0O00
if 70 - 70: iIii1I11I1II1 % OoooooooOO / OoO0O00 . O0 - I11i % II111iiii
if 84 - 84: OOooOOo * i1IIi . iIii1I11I1II1 * iII111i + I1Ii111 + II111iiii
if 97 - 97: Ii1I - IiII
if 64 - 64: oO0o . ooOoO0o / ooOoO0o - II111iiii
if 81 - 81: I1ii11iIi11i
if 64 - 64: oO0o * OoO0O00 / OOooOOo + Ii1I % Oo0Ooo . IiII
if 2 - 2: I1Ii111 + I11i
if 47 - 47: i11iIiiIii + iIii1I11I1II1 % I1ii11iIi11i - oO0o % OoO0O00
if 85 - 85: oO0o * OoOoOO00 / OoOoOO00
if 85 - 85: OOooOOo / I1Ii111 . i1IIi / OoOoOO00 + iIii1I11I1II1
if 71 - 71: OoO0O00
if 96 - 96: I1ii11iIi11i / I1IiiI - I1ii11iIi11i / II111iiii - IiII
if 74 - 74: Ii1I * OoooooooOO % OOooOOo + OoooooooOO + iII111i
if 83 - 83: i1IIi
if 2 - 2: i1IIi / OOooOOo * O0
if 99 - 99: OoooooooOO . OoOoOO00 / II111iiii
if 64 - 64: iII111i / i1IIi . I1IiiI + O0
if 5 - 5: O0 . i11iIiiIii
if 71 - 71: o0oOOo0O0Ooo + iII111i + ooOoO0o
if 27 - 27: OoooooooOO . iII111i * I1Ii111 % O0 + OoooooooOO - iII111i
if 86 - 86: i1IIi
if 81 - 81: OoOoOO00
if 52 - 52: iII111i * IiII % I1IiiI * I11i
if 73 - 73: I1Ii111 * ooOoO0o
if 62 - 62: OOooOOo . I1IiiI * iIii1I11I1II1 + OoO0O00 * ooOoO0o / oO0o
if 14 - 14: iII111i / OoO0O00
if 75 - 75: IiII
if 68 - 68: IiII - i1IIi % IiII . OoO0O00 . i11iIiiIii . OoooooooOO
if 32 - 32: iII111i + OoO0O00 % IiII + I1IiiI
if 69 - 69: I1Ii111 + I11i - iIii1I11I1II1 - II111iiii . Ii1I
if 74 - 74: I1ii11iIi11i % o0oOOo0O0Ooo + O0 - i11iIiiIii - IiII % OOooOOo
if 39 - 39: OoO0O00 - o0oOOo0O0Ooo
if 71 - 71: iII111i . OoO0O00 + ooOoO0o - OOooOOo - Oo0Ooo
if 100 - 100: OoooooooOO - o0oOOo0O0Ooo + I1Ii111 . OoooooooOO % i11iIiiIii
if 64 - 64: I1Ii111 % OoooooooOO / i1IIi / OoO0O00
if 2 - 2: I11i % o0oOOo0O0Ooo . OoO0O00 . OoO0O00
if 89 - 89: ooOoO0o - oO0o + II111iiii + OoO0O00 - IiII
if 27 - 27: I1Ii111 - o0oOOo0O0Ooo + OoO0O00
if 38 - 38: OoOoOO00 + OoO0O00 . i11iIiiIii + Ii1I % i1IIi % I1IiiI
if 93 - 93: i11iIiiIii
if 63 - 63: iIii1I11I1II1 - iIii1I11I1II1 % o0oOOo0O0Ooo
if 97 - 97: i1IIi % I11i % OoOoOO00
if 25 - 25: OoOoOO00 . iIii1I11I1II1 - iII111i % II111iiii . OoOoOO00
if 16 - 16: OOooOOo . Oo0Ooo . I1IiiI % O0 . I1ii11iIi11i + i11iIiiIii
if 100 - 100: I1ii11iIi11i - i1IIi - OoO0O00 * o0oOOo0O0Ooo + OoOoOO00
if 31 - 31: i1IIi
if 21 - 21: o0oOOo0O0Ooo / O0 % O0 . OoooooooOO / I1IiiI
if 94 - 94: ooOoO0o + OoO0O00 / ooOoO0o - ooOoO0o + Oo0Ooo + o0oOOo0O0Ooo
if 50 - 50: oO0o . Oo0Ooo
if 15 - 15: Ii1I
class lisp_info ( ) :
 def __init__ ( self ) :
  self . info_reply = False
  self . nonce = 0
  self . private_etr_rloc = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . global_etr_rloc = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . global_ms_rloc = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . ms_port = 0
  self . etr_port = 0
  self . rtr_list = [ ]
  self . hostname = lisp_hostname
  if 64 - 64: OoooooooOO
  if 25 - 25: IiII
 def print_info ( self ) :
  if ( self . info_reply ) :
   iI11iiIIii = "Info-Reply"
   I1II = ( ", ms-port: {}, etr-port: {}, global-rloc: {}, " + "ms-rloc: {}, private-rloc: {}, RTR-list: " ) . format ( self . ms_port , self . etr_port ,
   # OoooooooOO * IiII * O0 . i11iIiiIii + iIii1I11I1II1 - OoooooooOO
   # I1ii11iIi11i + OoOoOO00 % I1ii11iIi11i - Oo0Ooo
 red ( self . global_etr_rloc . print_address_no_iid ( ) , False ) ,
 red ( self . global_ms_rloc . print_address_no_iid ( ) , False ) ,
 red ( self . private_etr_rloc . print_address_no_iid ( ) , False ) )
   if ( len ( self . rtr_list ) == 0 ) : I1II += "empty, "
   for iIi in self . rtr_list :
    I1II += red ( iIi . print_address_no_iid ( ) , False ) + ", "
    if 56 - 56: I1IiiI * iIii1I11I1II1 . II111iiii % II111iiii - o0oOOo0O0Ooo
   I1II = I1II [ 0 : - 2 ]
  else :
   iI11iiIIii = "Info-Request"
   IIIi = "<none>" if self . hostname == None else self . hostname
   I1II = ", hostname: {}" . format ( blue ( IIIi , False ) )
   if 5 - 5: IiII * i11iIiiIii * OOooOOo . iII111i - Ii1I * oO0o
  lprint ( "{} -> nonce: 0x{}{}" . format ( bold ( iI11iiIIii , False ) ,
 lisp_hex_string ( self . nonce ) , I1II ) )
  if 25 - 25: O0 . I1Ii111 / IiII % I1ii11iIi11i
  if 75 - 75: iII111i % I11i - Oo0Ooo * I1ii11iIi11i - IiII
 def encode ( self ) :
  i1OOoO0OO0oO = ( LISP_NAT_INFO << 28 )
  if ( self . info_reply ) : i1OOoO0OO0oO |= ( 1 << 27 )
  if 73 - 73: Ii1I - ooOoO0o / i1IIi
  if 8 - 8: Ii1I
  if 52 - 52: IiII
  if 86 - 86: I1Ii111 / O0 + OoooooooOO % oO0o
  if 45 - 45: I1IiiI . Oo0Ooo . I11i . Ii1I
  if 81 - 81: II111iiii + OoOoOO00 % i11iIiiIii / iII111i . I1Ii111 + II111iiii
  if 48 - 48: I1IiiI . I1ii11iIi11i * OoOoOO00 % i1IIi / I1Ii111 * II111iiii
  IiiiIi1iiii11 = struct . pack ( "I" , socket . htonl ( i1OOoO0OO0oO ) )
  IiiiIi1iiii11 += struct . pack ( "Q" , self . nonce )
  IiiiIi1iiii11 += struct . pack ( "III" , 0 , 0 , 0 )
  if 62 - 62: o0oOOo0O0Ooo * I1Ii111 . iIii1I11I1II1 / i1IIi
  if 75 - 75: OoooooooOO / ooOoO0o - iII111i . OoooooooOO . OoOoOO00 % i1IIi
  if 7 - 7: OoOoOO00 . i1IIi * i11iIiiIii % i11iIiiIii
  if 54 - 54: OoO0O00 / I1IiiI . Oo0Ooo
  if ( self . info_reply == False ) :
   if ( self . hostname == None ) :
    IiiiIi1iiii11 += struct . pack ( "H" , 0 )
   else :
    IiiiIi1iiii11 += struct . pack ( "H" , socket . htons ( LISP_AFI_NAME ) )
    IiiiIi1iiii11 += self . hostname + "\0"
    if 39 - 39: OoO0O00 . ooOoO0o
   return ( IiiiIi1iiii11 )
   if 41 - 41: Oo0Ooo * I1ii11iIi11i - II111iiii - II111iiii
   if 7 - 7: oO0o
   if 41 - 41: ooOoO0o
   if 93 - 93: Ii1I + I1Ii111 + Ii1I
   if 23 - 23: I1IiiI - i1IIi / ooOoO0o
  IiiiII = socket . htons ( LISP_AFI_LCAF )
  OOOoooO000O0 = LISP_LCAF_NAT_TYPE
  iII = socket . htons ( 16 )
  I1IO0oo0oo00OO = socket . htons ( self . ms_port )
  iIiI = socket . htons ( self . etr_port )
  IiiiIi1iiii11 += struct . pack ( "HHBBHHHH" , IiiiII , 0 , OOOoooO000O0 , 0 , iII ,
 I1IO0oo0oo00OO , iIiI , socket . htons ( self . global_etr_rloc . afi ) )
  IiiiIi1iiii11 += self . global_etr_rloc . pack_address ( )
  IiiiIi1iiii11 += struct . pack ( "HH" , 0 , socket . htons ( self . private_etr_rloc . afi ) )
  IiiiIi1iiii11 += self . private_etr_rloc . pack_address ( )
  if ( len ( self . rtr_list ) == 0 ) : IiiiIi1iiii11 += struct . pack ( "H" , 0 )
  if 41 - 41: I1Ii111 + ooOoO0o / OOooOOo + I11i % Oo0Ooo
  if 91 - 91: I1IiiI % I1ii11iIi11i % oO0o / i1IIi * iIii1I11I1II1 + I11i
  if 48 - 48: ooOoO0o / I1ii11iIi11i / OoO0O00 / II111iiii * OoOoOO00
  if 73 - 73: I11i / I1IiiI - IiII - i1IIi * IiII - OOooOOo
  for iIi in self . rtr_list :
   IiiiIi1iiii11 += struct . pack ( "H" , socket . htons ( iIi . afi ) )
   IiiiIi1iiii11 += iIi . pack_address ( )
   if 39 - 39: I11i . ooOoO0o * II111iiii
  return ( IiiiIi1iiii11 )
  if 21 - 21: Ii1I
  if 92 - 92: OoO0O00 * I1ii11iIi11i + iIii1I11I1II1
 def decode ( self , packet ) :
  oO0ooOoOooO00o00 = packet
  O0O00Oo = "I"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 88 - 88: iIii1I11I1II1 + iIii1I11I1II1 * i11iIiiIii . I1ii11iIi11i % oO0o
  i1OOoO0OO0oO = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  i1OOoO0OO0oO = i1OOoO0OO0oO [ 0 ]
  packet = packet [ IiIii1i : : ]
  if 94 - 94: I1IiiI / I1ii11iIi11i / OOooOOo
  O0O00Oo = "Q"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 45 - 45: II111iiii
  o0OOO = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  if 98 - 98: i11iIiiIii + I1ii11iIi11i * OOooOOo / OoOoOO00
  i1OOoO0OO0oO = socket . ntohl ( i1OOoO0OO0oO )
  self . nonce = o0OOO [ 0 ]
  self . info_reply = i1OOoO0OO0oO & 0x08000000
  self . hostname = None
  packet = packet [ IiIii1i : : ]
  if 84 - 84: o0oOOo0O0Ooo
  if 40 - 40: OoooooooOO - oO0o / O0 * I1Ii111 . O0 + i11iIiiIii
  if 9 - 9: OOooOOo % O0 % O0 / I1ii11iIi11i . II111iiii / II111iiii
  if 78 - 78: iIii1I11I1II1 - i1IIi . I11i . o0oOOo0O0Ooo
  if 66 - 66: OOooOOo * Oo0Ooo
  O0O00Oo = "HH"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 58 - 58: OOooOOo
  if 96 - 96: IiII % OoooooooOO + O0 * II111iiii / OOooOOo . I1Ii111
  if 47 - 47: OoO0O00 - Oo0Ooo * OoO0O00 / oO0o
  if 13 - 13: ooOoO0o
  if 55 - 55: i1IIi . I11i . II111iiii + O0 + ooOoO0o - i1IIi
  o00oO , Ooo = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  if ( Ooo != 0 ) : return ( None )
  if 3 - 3: iIii1I11I1II1 / oO0o
  packet = packet [ IiIii1i : : ]
  O0O00Oo = "IBBH"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 61 - 61: I1Ii111 / O0 - iII111i
  Oo0o0 , iI111iiI1II , iiIi , oO0O = struct . unpack ( O0O00Oo ,
 packet [ : IiIii1i ] )
  if 89 - 89: OoOoOO00 + Oo0Ooo . OoOoOO00 - II111iiii
  if ( oO0O != 0 ) : return ( None )
  packet = packet [ IiIii1i : : ]
  if 85 - 85: OoooooooOO * OoooooooOO / Ii1I - II111iiii
  if 69 - 69: iII111i * I11i
  if 43 - 43: o0oOOo0O0Ooo - IiII * Ii1I . i11iIiiIii / II111iiii
  if 61 - 61: OoOoOO00 / I1IiiI . I1ii11iIi11i % OOooOOo
  if ( self . info_reply == False ) :
   O0O00Oo = "H"
   IiIii1i = struct . calcsize ( O0O00Oo )
   if ( len ( packet ) >= IiIii1i ) :
    IiiiII = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] ) [ 0 ]
    if ( socket . ntohs ( IiiiII ) == LISP_AFI_NAME ) :
     packet = packet [ IiIii1i : : ]
     packet , self . hostname = lisp_decode_dist_name ( packet )
     if 70 - 70: OOooOOo * OoOoOO00 / oO0o + Oo0Ooo / O0
     if 16 - 16: Oo0Ooo / OoooooooOO / IiII + Oo0Ooo * i11iIiiIii
   return ( oO0ooOoOooO00o00 )
   if 15 - 15: o0oOOo0O0Ooo / i11iIiiIii
   if 63 - 63: I1ii11iIi11i - Ii1I + I11i
   if 98 - 98: iII111i / IiII * I1IiiI / oO0o - iIii1I11I1II1
   if 72 - 72: O0 . OOooOOo
   if 99 - 99: i1IIi + iIii1I11I1II1 - ooOoO0o + OoO0O00 + Oo0Ooo . I1ii11iIi11i
  O0O00Oo = "HHBBHHH"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 74 - 74: i1IIi
  IiiiII , oOo0oo , OOOoooO000O0 , iI111iiI1II , iII , I1IO0oo0oo00OO , iIiI = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  if 80 - 80: ooOoO0o + I1Ii111 . I1ii11iIi11i % OoooooooOO
  if 26 - 26: OoOoOO00 . iII111i * iIii1I11I1II1 / IiII
  if ( socket . ntohs ( IiiiII ) != LISP_AFI_LCAF ) : return ( None )
  if 69 - 69: OoooooooOO / I11i + Ii1I * II111iiii
  self . ms_port = socket . ntohs ( I1IO0oo0oo00OO )
  self . etr_port = socket . ntohs ( iIiI )
  packet = packet [ IiIii1i : : ]
  if 35 - 35: i11iIiiIii + oO0o
  if 85 - 85: OoOoOO00 . O0 % OoooooooOO % oO0o
  if 43 - 43: I1IiiI - I11i . I1IiiI / i11iIiiIii % IiII * i11iIiiIii
  if 12 - 12: II111iiii - iIii1I11I1II1
  O0O00Oo = "H"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 43 - 43: i11iIiiIii % OoO0O00
  if 100 - 100: i1IIi
  if 4 - 4: i11iIiiIii - OOooOOo * IiII % OoooooooOO - OoOoOO00
  if 81 - 81: Ii1I * ooOoO0o . oO0o . IiII
  IiiiII = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] ) [ 0 ]
  packet = packet [ IiIii1i : : ]
  if ( IiiiII != 0 ) :
   self . global_etr_rloc . afi = socket . ntohs ( IiiiII )
   packet = self . global_etr_rloc . unpack_address ( packet )
   if ( packet == None ) : return ( None )
   self . global_etr_rloc . mask_len = self . global_etr_rloc . host_mask_len ( )
   if 71 - 71: IiII + OoO0O00
   if 39 - 39: I1IiiI % IiII / II111iiii / II111iiii
   if 95 - 95: II111iiii + i11iIiiIii + o0oOOo0O0Ooo
   if 30 - 30: O0 - O0 % iIii1I11I1II1 + iII111i * OoooooooOO
   if 1 - 1: O0
   if 36 - 36: oO0o . iII111i
  if ( len ( packet ) < IiIii1i ) : return ( oO0ooOoOooO00o00 )
  if 62 - 62: I11i + iIii1I11I1II1 % I11i * OOooOOo + iIii1I11I1II1 % Ii1I
  IiiiII = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] ) [ 0 ]
  packet = packet [ IiIii1i : : ]
  if ( IiiiII != 0 ) :
   self . global_ms_rloc . afi = socket . ntohs ( IiiiII )
   packet = self . global_ms_rloc . unpack_address ( packet )
   if ( packet == None ) : return ( oO0ooOoOooO00o00 )
   self . global_ms_rloc . mask_len = self . global_ms_rloc . host_mask_len ( )
   if 56 - 56: o0oOOo0O0Ooo
   if 55 - 55: oO0o - I1Ii111 / ooOoO0o % I1IiiI * OoooooooOO * I1IiiI
   if 88 - 88: Ii1I + O0
   if 92 - 92: I1IiiI % iII111i % I11i + OoooooooOO - i11iIiiIii
   if 9 - 9: i11iIiiIii - II111iiii / ooOoO0o
  if ( len ( packet ) < IiIii1i ) : return ( oO0ooOoOooO00o00 )
  if 81 - 81: i11iIiiIii % OoOoOO00 % OoO0O00 * Ii1I
  IiiiII = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] ) [ 0 ]
  packet = packet [ IiIii1i : : ]
  if ( IiiiII != 0 ) :
   self . private_etr_rloc . afi = socket . ntohs ( IiiiII )
   packet = self . private_etr_rloc . unpack_address ( packet )
   if ( packet == None ) : return ( oO0ooOoOooO00o00 )
   self . private_etr_rloc . mask_len = self . private_etr_rloc . host_mask_len ( )
   if 85 - 85: OoooooooOO * ooOoO0o
   if 23 - 23: OOooOOo / I11i / OoooooooOO - Ii1I / OoO0O00 - OoO0O00
   if 60 - 60: OOooOOo . ooOoO0o % i1IIi % Ii1I % ooOoO0o + OoO0O00
   if 26 - 26: O0 % o0oOOo0O0Ooo + iII111i * I1ii11iIi11i * I1Ii111
   if 4 - 4: OOooOOo * OoooooooOO * i1IIi % I1ii11iIi11i % Oo0Ooo
   if 1 - 1: OoO0O00 / iIii1I11I1II1 % I1ii11iIi11i - o0oOOo0O0Ooo
  while ( len ( packet ) >= IiIii1i ) :
   IiiiII = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] ) [ 0 ]
   packet = packet [ IiIii1i : : ]
   if ( IiiiII == 0 ) : continue
   iIi = lisp_address ( socket . ntohs ( IiiiII ) , "" , 0 , 0 )
   packet = iIi . unpack_address ( packet )
   if ( packet == None ) : return ( oO0ooOoOooO00o00 )
   iIi . mask_len = iIi . host_mask_len ( )
   self . rtr_list . append ( iIi )
   if 62 - 62: I1Ii111 % II111iiii
  return ( oO0ooOoOooO00o00 )
  if 91 - 91: I11i % Ii1I - IiII + iIii1I11I1II1 * iIii1I11I1II1
  if 91 - 91: i11iIiiIii + Ii1I
  if 85 - 85: I11i % IiII
class lisp_nat_info ( ) :
 def __init__ ( self , addr_str , hostname , port ) :
  self . address = addr_str
  self . hostname = hostname
  self . port = port
  self . uptime = lisp_get_timestamp ( )
  if 68 - 68: Oo0Ooo . I1Ii111 - o0oOOo0O0Ooo * iIii1I11I1II1 - II111iiii % i1IIi
  if 58 - 58: I11i / i11iIiiIii * i11iIiiIii
 def timed_out ( self ) :
  Ooo0o0oo0 = time . time ( ) - self . uptime
  return ( Ooo0o0oo0 >= ( LISP_INFO_INTERVAL * 2 ) )
  if 24 - 24: ooOoO0o - I1Ii111 * II111iiii - II111iiii
  if 47 - 47: IiII - iIii1I11I1II1 / OoOoOO00 * iII111i - iIii1I11I1II1 % oO0o
  if 93 - 93: Ii1I / iII111i
class lisp_info_source ( ) :
 def __init__ ( self , hostname , addr_str , port ) :
  self . address = lisp_address ( LISP_AFI_IPV4 , addr_str , 32 , 0 )
  self . port = port
  self . uptime = lisp_get_timestamp ( )
  self . nonce = None
  self . hostname = hostname
  self . no_timeout = False
  if 100 - 100: Oo0Ooo
  if 94 - 94: I1ii11iIi11i / i1IIi * I1IiiI - I11i - I1ii11iIi11i
 def cache_address_for_info_source ( self ) :
  o0Oo = self . address . print_address_no_iid ( ) + self . hostname
  lisp_info_sources_by_address [ o0Oo ] = self
  if 6 - 6: I1ii11iIi11i % o0oOOo0O0Ooo + o0oOOo0O0Ooo / OOooOOo / I1IiiI
  if 67 - 67: OoOoOO00 . iII111i / OOooOOo * ooOoO0o + i1IIi
 def cache_nonce_for_info_source ( self , nonce ) :
  self . nonce = nonce
  lisp_info_sources_by_nonce [ nonce ] = self
  if 100 - 100: OOooOOo . ooOoO0o + I1Ii111 . oO0o
  if 20 - 20: i11iIiiIii - i1IIi - iIii1I11I1II1 - OoooooooOO
  if 72 - 72: I1Ii111 . OoO0O00
  if 59 - 59: I1IiiI * I11i % i1IIi
  if 77 - 77: OOooOOo * OoooooooOO + I1IiiI + I1IiiI % oO0o . OoooooooOO
  if 60 - 60: iIii1I11I1II1
  if 13 - 13: II111iiii + Ii1I
  if 33 - 33: i1IIi
  if 36 - 36: ooOoO0o % ooOoO0o . i11iIiiIii
  if 42 - 42: OoO0O00 . I1Ii111 / Ii1I
  if 57 - 57: iIii1I11I1II1 % I1ii11iIi11i . OOooOOo / oO0o . OoOoOO00
def lisp_concat_auth_data ( alg_id , auth1 , auth2 , auth3 , auth4 ) :
 if 74 - 74: I1IiiI * OoO0O00 + OoooooooOO * ooOoO0o . oO0o
 if ( lisp_is_x86 ( ) ) :
  if ( auth1 != "" ) : auth1 = byte_swap_64 ( auth1 )
  if ( auth2 != "" ) : auth2 = byte_swap_64 ( auth2 )
  if ( auth3 != "" ) :
   if ( alg_id == LISP_SHA_1_96_ALG_ID ) : auth3 = socket . ntohl ( auth3 )
   else : auth3 = byte_swap_64 ( auth3 )
   if 66 - 66: II111iiii + OOooOOo + i11iIiiIii / II111iiii
  if ( auth4 != "" ) : auth4 = byte_swap_64 ( auth4 )
  if 37 - 37: I1IiiI + OoO0O00 . OoO0O00 % OoOoOO00 + o0oOOo0O0Ooo
  if 81 - 81: i1IIi % iIii1I11I1II1
 if ( alg_id == LISP_SHA_1_96_ALG_ID ) :
  auth1 = lisp_hex_string ( auth1 )
  auth1 = auth1 . zfill ( 16 )
  auth2 = lisp_hex_string ( auth2 )
  auth2 = auth2 . zfill ( 16 )
  auth3 = lisp_hex_string ( auth3 )
  auth3 = auth3 . zfill ( 8 )
  Iiii = auth1 + auth2 + auth3
  if 41 - 41: oO0o - iII111i / o0oOOo0O0Ooo . iII111i % Oo0Ooo + OOooOOo
 if ( alg_id == LISP_SHA_256_128_ALG_ID ) :
  auth1 = lisp_hex_string ( auth1 )
  auth1 = auth1 . zfill ( 16 )
  auth2 = lisp_hex_string ( auth2 )
  auth2 = auth2 . zfill ( 16 )
  auth3 = lisp_hex_string ( auth3 )
  auth3 = auth3 . zfill ( 16 )
  auth4 = lisp_hex_string ( auth4 )
  auth4 = auth4 . zfill ( 16 )
  Iiii = auth1 + auth2 + auth3 + auth4
  if 82 - 82: ooOoO0o
 return ( Iiii )
 if 89 - 89: OOooOOo / I1ii11iIi11i . I1IiiI + i11iIiiIii
 if 11 - 11: oO0o . i11iIiiIii * ooOoO0o % OoooooooOO % O0
 if 59 - 59: i11iIiiIii / OoO0O00
 if 48 - 48: iIii1I11I1II1
 if 19 - 19: oO0o
 if 69 - 69: I1ii11iIi11i % iII111i - OoooooooOO % Ii1I * oO0o
 if 12 - 12: OoOoOO00 / I1Ii111 . O0 . IiII - OOooOOo - OoO0O00
 if 28 - 28: II111iiii . OoOoOO00 - o0oOOo0O0Ooo
 if 89 - 89: I1Ii111 * OoooooooOO . OOooOOo . I11i % i11iIiiIii
 if 8 - 8: I1ii11iIi11i + II111iiii . OoO0O00 + I1IiiI - II111iiii % OoO0O00
def lisp_open_listen_socket ( local_addr , port ) :
 if ( port . isdigit ( ) ) :
  if ( local_addr . find ( "." ) != - 1 ) :
   ooO0ooO00o = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
   if 47 - 47: II111iiii + I1Ii111 + II111iiii
  if ( local_addr . find ( ":" ) != - 1 ) :
   if ( lisp_is_raspbian ( ) ) : return ( None )
   ooO0ooO00o = socket . socket ( socket . AF_INET6 , socket . SOCK_DGRAM )
   if 45 - 45: II111iiii % OoOoOO00 / O0 % iIii1I11I1II1 + oO0o
  ooO0ooO00o . bind ( ( local_addr , int ( port ) ) )
 else :
  II1 = port
  if ( os . path . exists ( II1 ) ) :
   os . system ( "rm " + II1 )
   time . sleep ( 1 )
   if 51 - 51: o0oOOo0O0Ooo * o0oOOo0O0Ooo . Ii1I
  ooO0ooO00o = socket . socket ( socket . AF_UNIX , socket . SOCK_DGRAM )
  ooO0ooO00o . bind ( II1 )
  if 14 - 14: OoO0O00 . I11i % II111iiii % i11iIiiIii + OoooooooOO
 return ( ooO0ooO00o )
 if 50 - 50: i11iIiiIii * I11i + i11iIiiIii - i1IIi
 if 69 - 69: I1IiiI + IiII + oO0o * I1ii11iIi11i . iIii1I11I1II1 / OoooooooOO
 if 77 - 77: Oo0Ooo - ooOoO0o
 if 68 - 68: Ii1I * O0
 if 61 - 61: II111iiii - OoO0O00 . iIii1I11I1II1 * o0oOOo0O0Ooo . OoO0O00 % IiII
 if 11 - 11: oO0o + I11i
 if 6 - 6: i1IIi . o0oOOo0O0Ooo + OoO0O00 + OOooOOo + oO0o
def lisp_open_send_socket ( internal_name , afi ) :
 if ( internal_name == "" ) :
  if ( afi == LISP_AFI_IPV4 ) :
   ooO0ooO00o = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
   if 30 - 30: O0
  if ( afi == LISP_AFI_IPV6 ) :
   if ( lisp_is_raspbian ( ) ) : return ( None )
   ooO0ooO00o = socket . socket ( socket . AF_INET6 , socket . SOCK_DGRAM )
   if 98 - 98: I1Ii111
 else :
  if ( os . path . exists ( internal_name ) ) : os . system ( "rm " + internal_name )
  ooO0ooO00o = socket . socket ( socket . AF_UNIX , socket . SOCK_DGRAM )
  ooO0ooO00o . bind ( internal_name )
  if 58 - 58: OOooOOo
 return ( ooO0ooO00o )
 if 6 - 6: I1ii11iIi11i
 if 37 - 37: i11iIiiIii . II111iiii + OOooOOo + i1IIi * OOooOOo
 if 18 - 18: ooOoO0o
 if 18 - 18: I1Ii111 + OoOoOO00 % OOooOOo - IiII - i1IIi + I1ii11iIi11i
 if 33 - 33: I11i * Ii1I / Oo0Ooo + oO0o % OOooOOo % OoooooooOO
 if 29 - 29: Ii1I . II111iiii / I1Ii111
 if 79 - 79: IiII . OoOoOO00 / oO0o % OoO0O00 / Ii1I + I11i
def lisp_close_socket ( sock , internal_name ) :
 sock . close ( )
 if ( os . path . exists ( internal_name ) ) : os . system ( "rm " + internal_name )
 return
 if 78 - 78: o0oOOo0O0Ooo + I1Ii111 % i11iIiiIii % I1IiiI - Ii1I
 if 81 - 81: i11iIiiIii - II111iiii + I11i
 if 52 - 52: II111iiii
 if 62 - 62: iII111i / OoO0O00 + i11iIiiIii / Oo0Ooo
 if 26 - 26: I1ii11iIi11i - OoO0O00
 if 19 - 19: iIii1I11I1II1 / I1ii11iIi11i + O0
 if 12 - 12: I11i . OOooOOo + o0oOOo0O0Ooo . OoO0O00 + o0oOOo0O0Ooo
 if 56 - 56: i1IIi / i1IIi . OoO0O00 % i1IIi - OoOoOO00 % OOooOOo
def lisp_is_running ( node ) :
 return ( True if ( os . path . exists ( node ) ) else False )
 if 66 - 66: i11iIiiIii * IiII % IiII . I1IiiI / ooOoO0o
 if 50 - 50: IiII . iII111i / o0oOOo0O0Ooo % OoOoOO00 * IiII % I11i
 if 15 - 15: Ii1I
 if 29 - 29: I11i / I1IiiI / OoooooooOO . OoOoOO00 / I11i . I1Ii111
 if 69 - 69: O0 * OoOoOO00 + o0oOOo0O0Ooo + I1IiiI % iII111i . OoooooooOO
 if 45 - 45: I1Ii111 + oO0o - o0oOOo0O0Ooo - OoOoOO00 + I1IiiI / II111iiii
 if 46 - 46: II111iiii . iIii1I11I1II1
 if 62 - 62: I1ii11iIi11i % i1IIi % I1Ii111 * ooOoO0o % OOooOOo + I1IiiI
 if 100 - 100: II111iiii - o0oOOo0O0Ooo * OoooooooOO . ooOoO0o / II111iiii / oO0o
def lisp_packet_ipc ( packet , source , sport ) :
 return ( ( "packet@" + str ( len ( packet ) ) + "@" + source + "@" + str ( sport ) + "@" + packet ) )
 if 43 - 43: iIii1I11I1II1 + ooOoO0o * iII111i + iIii1I11I1II1 . I1Ii111
 if 87 - 87: I1Ii111
 if 47 - 47: II111iiii + I1IiiI . Oo0Ooo / iIii1I11I1II1
 if 14 - 14: i1IIi / OoO0O00 / iII111i % I1Ii111
 if 72 - 72: OoO0O00 . II111iiii - IiII + IiII + iIii1I11I1II1 % oO0o
 if 21 - 21: iII111i + OoOoOO00 - i11iIiiIii % O0 + OOooOOo
 if 30 - 30: o0oOOo0O0Ooo - Oo0Ooo + iII111i / O0
 if 94 - 94: IiII
 if 69 - 69: I1Ii111 . I1Ii111
def lisp_control_packet_ipc ( packet , source , dest , dport ) :
 return ( "control-packet@" + dest + "@" + str ( dport ) + "@" + packet )
 if 53 - 53: i11iIiiIii + iII111i * Oo0Ooo - I1Ii111
 if 61 - 61: o0oOOo0O0Ooo / OOooOOo . II111iiii - I1IiiI * i11iIiiIii
 if 8 - 8: iII111i % o0oOOo0O0Ooo
 if 87 - 87: Ii1I % I11i / I1Ii111
 if 21 - 21: OoO0O00 + Ii1I / I1Ii111
 if 75 - 75: I1Ii111 . Ii1I % iIii1I11I1II1 / OoOoOO00
 if 38 - 38: i1IIi
def lisp_data_packet_ipc ( packet , source ) :
 return ( "data-packet@" + str ( len ( packet ) ) + "@" + source + "@@" + packet )
 if 1 - 1: I1ii11iIi11i + OoO0O00 % I11i . OOooOOo + i1IIi / oO0o
 if 35 - 35: ooOoO0o % OoOoOO00 % OoO0O00 + OOooOOo / IiII * OoOoOO00
 if 65 - 65: I1IiiI . Oo0Ooo + i1IIi - Ii1I * i1IIi
 if 64 - 64: I1IiiI / OoO0O00 * I1IiiI * II111iiii . Ii1I
 if 98 - 98: I1Ii111 + o0oOOo0O0Ooo
 if 73 - 73: I1ii11iIi11i / I1Ii111 + i11iIiiIii + OoO0O00 . ooOoO0o
 if 54 - 54: I1ii11iIi11i + IiII - oO0o + Oo0Ooo / IiII % Oo0Ooo
 if 2 - 2: OOooOOo / I11i * I11i + I11i / O0 - OOooOOo
 if 29 - 29: OoOoOO00 + i11iIiiIii % OoO0O00 - OoooooooOO
def lisp_command_ipc ( packet , source ) :
 return ( "command@" + str ( len ( packet ) ) + "@" + source + "@@" + packet )
 if 68 - 68: iII111i / OOooOOo
 if 28 - 28: II111iiii
 if 49 - 49: I1ii11iIi11i
 if 33 - 33: iIii1I11I1II1
 if 72 - 72: I1ii11iIi11i * i11iIiiIii
 if 12 - 12: O0 - iIii1I11I1II1 % Oo0Ooo / O0 - IiII
 if 55 - 55: OOooOOo . Oo0Ooo * OoOoOO00 / OoooooooOO * i11iIiiIii + oO0o
 if 45 - 45: Ii1I
 if 8 - 8: oO0o + OOooOOo
def lisp_api_ipc ( source , data ) :
 return ( "api@" + str ( len ( data ) ) + "@" + source + "@@" + data )
 if 37 - 37: IiII - OoOoOO00 + oO0o - Oo0Ooo + IiII
 if 33 - 33: Oo0Ooo % oO0o - I1IiiI + Oo0Ooo
 if 90 - 90: I1ii11iIi11i * I1Ii111 - iIii1I11I1II1 % IiII * I1Ii111 . I1Ii111
 if 90 - 90: o0oOOo0O0Ooo - O0 % O0 - oO0o . OoooooooOO
 if 30 - 30: I11i + O0 / Ii1I / OoOoOO00 - oO0o + II111iiii
 if 21 - 21: iIii1I11I1II1 % OoooooooOO * OOooOOo % i1IIi
 if 73 - 73: OoooooooOO
 if 100 - 100: I11i / i1IIi / i1IIi % Ii1I - II111iiii . OoooooooOO
 if 72 - 72: Oo0Ooo * OoooooooOO % I1IiiI + I11i - II111iiii
def lisp_ipc ( packet , send_socket , node ) :
 if 82 - 82: iIii1I11I1II1 / i1IIi * I1IiiI . i11iIiiIii
 if 56 - 56: Ii1I * I1IiiI / ooOoO0o * II111iiii
 if 51 - 51: i1IIi . oO0o % OOooOOo
 if 90 - 90: OoooooooOO + iII111i / iIii1I11I1II1
 if ( lisp_is_running ( node ) == False ) :
  lprint ( "Suppress sending IPC to {}" . format ( node ) )
  return
  if 12 - 12: OoooooooOO
  if 9 - 9: O0 / O0 / I1IiiI - oO0o . ooOoO0o
 IiII1iiI = 1500 if ( packet . find ( "control-packet" ) == - 1 ) else 9000
 if 68 - 68: OoooooooOO . OoooooooOO % I1ii11iIi11i + i1IIi % OoooooooOO + Ii1I
 oO0ooOoO = 0
 oOOoO0O = len ( packet )
 O0000oO = 0
 I1iiI1ii1i = .001
 while ( oOOoO0O > 0 ) :
  O0IIiIi = min ( oOOoO0O , IiII1iiI )
  O0OO0O = packet [ oO0ooOoO : O0IIiIi + oO0ooOoO ]
  if 86 - 86: iII111i / i1IIi % Oo0Ooo
  try :
   send_socket . sendto ( O0OO0O , node )
   lprint ( "Send IPC {}-out-of-{} byte to {} succeeded" . format ( len ( O0OO0O ) , len ( packet ) , node ) )
   if 84 - 84: o0oOOo0O0Ooo * OOooOOo . I11i * Ii1I
   O0000oO = 0
   I1iiI1ii1i = .001
   if 32 - 32: ooOoO0o % ooOoO0o * I1ii11iIi11i % Ii1I + Oo0Ooo . OoOoOO00
  except socket . error , iIIi1iI1I1IIi :
   if ( O0000oO == 12 ) :
    lprint ( "Giving up on {}, consider it down" . format ( node ) )
    break
    if 2 - 2: I1Ii111 / ooOoO0o * oO0o + IiII
    if 14 - 14: OoOoOO00 / iIii1I11I1II1 . o0oOOo0O0Ooo % i11iIiiIii . OoOoOO00
   lprint ( "Send IPC {}-out-of-{} byte to {} failed: {}" . format ( len ( O0OO0O ) , len ( packet ) , node , iIIi1iI1I1IIi ) )
   if 92 - 92: OoO0O00 . i1IIi
   if 22 - 22: Ii1I . I1IiiI
   O0000oO += 1
   time . sleep ( I1iiI1ii1i )
   if 54 - 54: OOooOOo / I1ii11iIi11i % oO0o
   lprint ( "Retrying after {} ms ..." . format ( I1iiI1ii1i * 1000 ) )
   I1iiI1ii1i *= 2
   continue
   if 66 - 66: I11i + iII111i
   if 50 - 50: IiII
  oO0ooOoO += O0IIiIi
  oOOoO0O -= O0IIiIi
  if 33 - 33: OOooOOo % I1IiiI - I1IiiI / IiII
 return
 if 22 - 22: ooOoO0o * ooOoO0o % o0oOOo0O0Ooo * Ii1I . OoO0O00
 if 55 - 55: OoOoOO00 - I1ii11iIi11i + iIii1I11I1II1 - i11iIiiIii / i1IIi / II111iiii
 if 37 - 37: Ii1I + o0oOOo0O0Ooo
 if 74 - 74: Oo0Ooo / O0 + i1IIi . I1IiiI + OoO0O00 / Oo0Ooo
 if 13 - 13: o0oOOo0O0Ooo / Ii1I . II111iiii
 if 8 - 8: I11i - I11i % IiII
 if 8 - 8: I1IiiI . IiII * O0 * o0oOOo0O0Ooo
def lisp_format_packet ( packet ) :
 packet = binascii . hexlify ( packet )
 oO0ooOoO = 0
 Ooo00O0ooOo = ""
 oOOoO0O = len ( packet ) * 2
 while ( oO0ooOoO < oOOoO0O ) :
  Ooo00O0ooOo += packet [ oO0ooOoO : oO0ooOoO + 8 ] + " "
  oO0ooOoO += 8
  oOOoO0O -= 4
  if 17 - 17: I1IiiI . oO0o + Oo0Ooo + I11i / o0oOOo0O0Ooo
 return ( Ooo00O0ooOo )
 if 25 - 25: iII111i / iII111i % OoOoOO00 / ooOoO0o
 if 81 - 81: OOooOOo * oO0o
 if 32 - 32: Oo0Ooo * OoO0O00 + ooOoO0o . O0 * oO0o * iIii1I11I1II1
 if 50 - 50: i1IIi
 if 53 - 53: II111iiii + O0 . ooOoO0o * IiII + i1IIi
 if 80 - 80: Ii1I + O0
 if 59 - 59: i11iIiiIii - OoooooooOO % I11i . OoO0O00 - Oo0Ooo * o0oOOo0O0Ooo
def lisp_send ( lisp_sockets , dest , port , packet ) :
 ii11iiIii1 = lisp_sockets [ 0 ] if dest . is_ipv4 ( ) else lisp_sockets [ 1 ]
 if 97 - 97: OOooOOo . OoOoOO00 / I11i - IiII - iIii1I11I1II1
 if 82 - 82: II111iiii + OoO0O00 % iIii1I11I1II1 / O0
 if 75 - 75: OOooOOo * OoO0O00 + OoooooooOO + i11iIiiIii . OoO0O00
 if 94 - 94: I11i * ooOoO0o . I1IiiI / Ii1I - I1IiiI % OoooooooOO
 if 32 - 32: OoO0O00
 if 22 - 22: II111iiii . I11i
 if 61 - 61: OOooOOo % O0 . I1ii11iIi11i . iIii1I11I1II1 * I11i
 if 29 - 29: ooOoO0o + i1IIi % IiII * Ii1I
 if 94 - 94: OOooOOo / IiII
 if 18 - 18: IiII - I11i / Ii1I % IiII * i1IIi
 if 22 - 22: OoOoOO00 - Oo0Ooo
 if 41 - 41: iIii1I11I1II1 * I1Ii111 / OoO0O00
 ii1i1II11II1i = dest . print_address_no_iid ( )
 if ( ii1i1II11II1i . find ( "::ffff:" ) != - 1 and ii1i1II11II1i . count ( "." ) == 3 ) :
  if ( lisp_i_am_rtr ) : ii11iiIii1 = lisp_sockets [ 0 ]
  if ( ii11iiIii1 == None ) :
   ii11iiIii1 = lisp_sockets [ 0 ]
   ii1i1II11II1i = ii1i1II11II1i . split ( "::ffff:" ) [ - 1 ]
   if 33 - 33: I11i + O0
   if 9 - 9: I11i . iII111i * ooOoO0o * ooOoO0o
   if 68 - 68: O0 - i11iIiiIii % iIii1I11I1II1 % ooOoO0o
 lprint ( "{} {} bytes {} {}, packet: {}" . format ( bold ( "Send" , False ) ,
 len ( packet ) , bold ( "to " + ii1i1II11II1i , False ) , port ,
 lisp_format_packet ( packet ) ) )
 if 12 - 12: II111iiii + I11i
 if 9 - 9: I1ii11iIi11i
 if 51 - 51: I1ii11iIi11i
 if 37 - 37: I1IiiI % I1Ii111
 IIIII1i111I = ( LISP_RLOC_PROBE_TTL == 128 )
 if ( IIIII1i111I ) :
  OoO0OOo = struct . unpack ( "B" , packet [ 0 ] ) [ 0 ]
  IIIII1i111I = ( OoO0OOo in [ 0x12 , 0x28 ] )
  if ( IIIII1i111I ) : lisp_set_ttl ( ii11iiIii1 , LISP_RLOC_PROBE_TTL )
  if 94 - 94: Ii1I
  if 73 - 73: ooOoO0o . OoO0O00 % I1ii11iIi11i - oO0o
 try : ii11iiIii1 . sendto ( packet , ( ii1i1II11II1i , port ) )
 except socket . error , iIIi1iI1I1IIi :
  lprint ( "socket.sendto() failed: {}" . format ( iIIi1iI1I1IIi ) )
  if 67 - 67: o0oOOo0O0Ooo . I11i + i1IIi
  if 100 - 100: Oo0Ooo - I1IiiI . OOooOOo % iIii1I11I1II1 . I11i
  if 83 - 83: OoOoOO00 * iII111i
  if 75 - 75: i11iIiiIii . o0oOOo0O0Ooo / oO0o . OoO0O00 % Ii1I % Ii1I
  if 94 - 94: iII111i . Ii1I
 if ( IIIII1i111I ) : lisp_set_ttl ( ii11iiIii1 , 64 )
 return
 if 71 - 71: o0oOOo0O0Ooo * II111iiii / OOooOOo . OoO0O00
 if 73 - 73: I1Ii111 * OoO0O00 / OoOoOO00 . II111iiii
 if 87 - 87: OoO0O00 + Oo0Ooo + O0 % OoooooooOO - iIii1I11I1II1
 if 100 - 100: Oo0Ooo + IiII
 if 81 - 81: iIii1I11I1II1 + iIii1I11I1II1
 if 19 - 19: ooOoO0o + i1IIi / Oo0Ooo * II111iiii * I1Ii111 / ooOoO0o
 if 23 - 23: I1Ii111
 if 76 - 76: Ii1I + Ii1I / i1IIi % o0oOOo0O0Ooo . iIii1I11I1II1 . OoOoOO00
def lisp_receive_segments ( lisp_socket , packet , source , total_length ) :
 if 75 - 75: I11i . Ii1I / I1ii11iIi11i
 if 99 - 99: Ii1I
 if 85 - 85: I1Ii111 + I1Ii111 + OoOoOO00 / ooOoO0o / o0oOOo0O0Ooo . Oo0Ooo
 if 41 - 41: i1IIi % Ii1I . i1IIi * OoooooooOO % Ii1I
 if 21 - 21: iII111i
 O0IIiIi = total_length - len ( packet )
 if ( O0IIiIi == 0 ) : return ( [ True , packet ] )
 if 72 - 72: I11i % o0oOOo0O0Ooo . iIii1I11I1II1 - I1Ii111 / i11iIiiIii
 lprint ( "Received {}-out-of-{} byte segment from {}" . format ( len ( packet ) ,
 total_length , source ) )
 if 75 - 75: OoooooooOO
 if 24 - 24: oO0o % iII111i - II111iiii / Ii1I + O0
 if 37 - 37: I1Ii111 - i1IIi / iIii1I11I1II1
 if 53 - 53: Ii1I - iIii1I11I1II1 % I1ii11iIi11i * i11iIiiIii + ooOoO0o
 if 63 - 63: Oo0Ooo * I1IiiI
 oOOoO0O = O0IIiIi
 while ( oOOoO0O > 0 ) :
  try : O0OO0O = lisp_socket . recvfrom ( 9000 )
  except : return ( [ False , None ] )
  if 84 - 84: Oo0Ooo
  O0OO0O = O0OO0O [ 0 ]
  if 67 - 67: oO0o / II111iiii . I11i / oO0o
  if 46 - 46: oO0o * Oo0Ooo - I11i / iIii1I11I1II1
  if 100 - 100: i11iIiiIii % oO0o
  if 62 - 62: OOooOOo * i1IIi - OOooOOo / i11iIiiIii
  if 17 - 17: I1ii11iIi11i + ooOoO0o % Ii1I % OOooOOo
  if ( O0OO0O . find ( "packet@" ) == 0 ) :
   oOOO0OO0OO = O0OO0O . split ( "@" )
   lprint ( "Received new message ({}-out-of-{}) while receiving " + "fragments, old message discarded" , len ( O0OO0O ) ,
   # I1ii11iIi11i % i1IIi - Oo0Ooo - IiII - o0oOOo0O0Ooo . OoooooooOO
 oOOO0OO0OO [ 1 ] if len ( oOOO0OO0OO ) > 2 else "?" )
   return ( [ False , O0OO0O ] )
   if 15 - 15: iIii1I11I1II1 / Ii1I + i1IIi
   if 68 - 68: ooOoO0o - i1IIi
  oOOoO0O -= len ( O0OO0O )
  packet += O0OO0O
  if 61 - 61: II111iiii * I1ii11iIi11i / I11i / OoO0O00
  lprint ( "Received {}-out-of-{} byte segment from {}" . format ( len ( O0OO0O ) , total_length , source ) )
  if 44 - 44: O0 + OoOoOO00 . iIii1I11I1II1 . IiII
  if 2 - 2: iII111i
 return ( [ True , packet ] )
 if 47 - 47: i1IIi % I11i
 if 17 - 17: OoOoOO00 - iII111i % I11i / o0oOOo0O0Ooo / II111iiii
 if 22 - 22: Oo0Ooo + I1ii11iIi11i % i11iIiiIii . OoO0O00 - I11i % I11i
 if 21 - 21: I1IiiI . OoO0O00 * IiII % OoooooooOO - Oo0Ooo + Oo0Ooo
 if 94 - 94: ooOoO0o
 if 80 - 80: i11iIiiIii - O0 / I1Ii111 + OOooOOo % Oo0Ooo
 if 95 - 95: II111iiii
 if 76 - 76: OoO0O00 % iII111i * OoOoOO00 / ooOoO0o / i1IIi
def lisp_bit_stuff ( payload ) :
 lprint ( "Bit-stuffing, found {} segments" . format ( len ( payload ) ) )
 IiiiIi1iiii11 = ""
 for O0OO0O in payload : IiiiIi1iiii11 += O0OO0O + "\x40"
 return ( IiiiIi1iiii11 [ : - 1 ] )
 if 45 - 45: Ii1I . I11i * I1Ii111 . i11iIiiIii
 if 34 - 34: O0 * o0oOOo0O0Ooo / IiII
 if 75 - 75: I1Ii111 - i1IIi - OoO0O00
 if 25 - 25: iII111i . o0oOOo0O0Ooo
 if 62 - 62: I11i + i1IIi . I1ii11iIi11i - I1ii11iIi11i
 if 68 - 68: ooOoO0o % OoooooooOO
 if 94 - 94: Oo0Ooo * o0oOOo0O0Ooo
 if 60 - 60: iII111i . OOooOOo
 if 39 - 39: O0 - i11iIiiIii - I1IiiI / Oo0Ooo - i11iIiiIii
 if 30 - 30: OoO0O00 / OoOoOO00 + I1ii11iIi11i % IiII - OoO0O00
 if 19 - 19: I1IiiI
 if 99 - 99: OOooOOo - OOooOOo
 if 98 - 98: o0oOOo0O0Ooo + O0 * oO0o - i11iIiiIii
 if 83 - 83: o0oOOo0O0Ooo
 if 23 - 23: o0oOOo0O0Ooo . I11i
 if 67 - 67: iII111i
 if 52 - 52: IiII . OoooooooOO
 if 34 - 34: o0oOOo0O0Ooo / IiII . OoooooooOO . Oo0Ooo / ooOoO0o + O0
 if 38 - 38: I11i
 if 66 - 66: II111iiii
def lisp_receive ( lisp_socket , internal ) :
 while ( True ) :
  if 57 - 57: OoO0O00 / Oo0Ooo % I1IiiI * I1ii11iIi11i
  if 68 - 68: iII111i - o0oOOo0O0Ooo - OoO0O00 . O0 - i11iIiiIii
  if 2 - 2: I1ii11iIi11i * i1IIi
  if 17 - 17: I1ii11iIi11i * Ii1I % Oo0Ooo * I1Ii111 + OoO0O00 . OoooooooOO
  try : o0o = lisp_socket . recvfrom ( 9000 )
  except : return ( [ "" , "" , "" , "" ] )
  if 36 - 36: IiII . iII111i * O0 . i1IIi * O0 * I1Ii111
  if 50 - 50: OoooooooOO + o0oOOo0O0Ooo + iIii1I11I1II1 + OOooOOo
  if 90 - 90: Ii1I * I11i % I1Ii111 - I1ii11iIi11i * I1Ii111 % OoO0O00
  if 50 - 50: iIii1I11I1II1
  if 56 - 56: oO0o
  if 55 - 55: iIii1I11I1II1 % oO0o % OOooOOo / I1Ii111 * OoooooooOO / Oo0Ooo
  if ( internal == False ) :
   IiiiIi1iiii11 = o0o [ 0 ]
   iI1Iii1i1 = lisp_convert_6to4 ( o0o [ 1 ] [ 0 ] )
   Oo0o = o0o [ 1 ] [ 1 ]
   if 88 - 88: I11i + OoO0O00 . iIii1I11I1II1 . II111iiii
   if ( Oo0o == LISP_DATA_PORT ) :
    O0000000 = lisp_data_plane_logging
    OO0OOo = lisp_format_packet ( IiiiIi1iiii11 [ 0 : 60 ] ) + " ..."
   else :
    O0000000 = True
    OO0OOo = lisp_format_packet ( IiiiIi1iiii11 )
    if 15 - 15: i1IIi
    if 43 - 43: II111iiii + OOooOOo . i11iIiiIii - II111iiii
   if ( O0000000 ) :
    lprint ( "{} {} bytes {} {}, packet: {}" . format ( bold ( "Receive" ,
 False ) , len ( IiiiIi1iiii11 ) , bold ( "from " + iI1Iii1i1 , False ) , Oo0o ,
 OO0OOo ) )
    if 80 - 80: o0oOOo0O0Ooo . oO0o . I1Ii111
   return ( [ "packet" , iI1Iii1i1 , Oo0o , IiiiIi1iiii11 ] )
   if 26 - 26: i1IIi - I1IiiI + IiII / OoO0O00 . I1ii11iIi11i
   if 82 - 82: I1Ii111 % iII111i . OoOoOO00 % OoO0O00 + I1ii11iIi11i
   if 69 - 69: I1IiiI * OoOoOO00 - ooOoO0o . O0
   if 15 - 15: oO0o . IiII + I1Ii111 - OoooooooOO
   if 85 - 85: II111iiii - Oo0Ooo + oO0o . i11iIiiIii + Oo0Ooo
   if 86 - 86: ooOoO0o . OoO0O00
  i1i1i11i11 = False
  oOO00o0 = o0o [ 0 ]
  I1II1i = False
  if 53 - 53: IiII * I1ii11iIi11i
  while ( i1i1i11i11 == False ) :
   oOO00o0 = oOO00o0 . split ( "@" )
   if 64 - 64: OOooOOo + Oo0Ooo . OoOoOO00 . OOooOOo + i11iIiiIii
   if ( len ( oOO00o0 ) < 4 ) :
    lprint ( "Possible fragment (length {}), from old message, " + "discarding" , len ( oOO00o0 [ 0 ] ) )
    if 7 - 7: ooOoO0o * I11i / iIii1I11I1II1
    I1II1i = True
    break
    if 15 - 15: OoooooooOO / iII111i
    if 40 - 40: o0oOOo0O0Ooo
   OO0Oo0o0o = oOO00o0 [ 0 ]
   try :
    Iii1 = int ( oOO00o0 [ 1 ] )
   except :
    oo0Ooo = bold ( "Internal packet reassembly error" , False )
    lprint ( "{}: {}" . format ( oo0Ooo , o0o ) )
    I1II1i = True
    break
    if 15 - 15: i11iIiiIii % iIii1I11I1II1 . II111iiii * I11i / I11i
   iI1Iii1i1 = oOO00o0 [ 2 ]
   Oo0o = oOO00o0 [ 3 ]
   if 80 - 80: Ii1I % II111iiii
   if 4 - 4: OoOoOO00 * OOooOOo / OoooooooOO % OoOoOO00 * I1ii11iIi11i * o0oOOo0O0Ooo
   if 69 - 69: O0 % iIii1I11I1II1
   if 94 - 94: O0
   if 50 - 50: I1Ii111 * o0oOOo0O0Ooo - ooOoO0o - I1ii11iIi11i % I1IiiI . ooOoO0o
   if 35 - 35: Ii1I % i1IIi + I1IiiI
   if 51 - 51: I1Ii111 / iIii1I11I1II1 + i1IIi
   if 71 - 71: iIii1I11I1II1 * ooOoO0o % iIii1I11I1II1 % I1IiiI
   if ( len ( oOO00o0 ) > 5 ) :
    IiiiIi1iiii11 = lisp_bit_stuff ( oOO00o0 [ 4 : : ] )
   else :
    IiiiIi1iiii11 = oOO00o0 [ 4 ]
    if 75 - 75: I1IiiI
    if 33 - 33: OoOoOO00
    if 53 - 53: i11iIiiIii / i1IIi . i1IIi + I11i
    if 19 - 19: ooOoO0o . OoOoOO00 + Oo0Ooo + iIii1I11I1II1 . OoOoOO00 - I1IiiI
    if 70 - 70: OOooOOo . OoOoOO00 . OOooOOo / iII111i
    if 72 - 72: OoooooooOO + Ii1I + iIii1I11I1II1
   i1i1i11i11 , IiiiIi1iiii11 = lisp_receive_segments ( lisp_socket , IiiiIi1iiii11 ,
 iI1Iii1i1 , Iii1 )
   if ( IiiiIi1iiii11 == None ) : return ( [ "" , "" , "" , "" ] )
   if 13 - 13: iII111i . I1Ii111 % ooOoO0o / i1IIi
   if 64 - 64: iII111i
   if 9 - 9: I1ii11iIi11i + Oo0Ooo * I11i / I1Ii111 / I1ii11iIi11i / oO0o
   if 48 - 48: Oo0Ooo % i1IIi / I1ii11iIi11i / oO0o + iII111i
   if 47 - 47: Ii1I
   if ( i1i1i11i11 == False ) :
    oOO00o0 = IiiiIi1iiii11
    continue
    if 75 - 75: II111iiii / OoOoOO00 - o0oOOo0O0Ooo % I1ii11iIi11i + OoO0O00
    if 7 - 7: iII111i - OoO0O00 + ooOoO0o * iII111i
   if ( Oo0o == "" ) : Oo0o = "no-port"
   if ( OO0Oo0o0o == "command" and lisp_i_am_core == False ) :
    ooo = IiiiIi1iiii11 . find ( " {" )
    iIiI1ii1I = IiiiIi1iiii11 if ooo == - 1 else IiiiIi1iiii11 [ : ooo ]
    iIiI1ii1I = ": '" + iIiI1ii1I + "'"
   else :
    iIiI1ii1I = ""
    if 5 - 5: OoooooooOO / IiII / I1ii11iIi11i / OoO0O00 * i1IIi / iIii1I11I1II1
    if 32 - 32: I1Ii111 % Oo0Ooo / OoOoOO00 + OoOoOO00 % i11iIiiIii . OoO0O00
   lprint ( "{} {} bytes {} {}, {}{}" . format ( bold ( "Receive" , False ) ,
 len ( IiiiIi1iiii11 ) , bold ( "from " + iI1Iii1i1 , False ) , Oo0o , OO0Oo0o0o ,
 iIiI1ii1I if ( OO0Oo0o0o in [ "command" , "api" ] ) else ": ... " if ( OO0Oo0o0o == "data-packet" ) else ": " + lisp_format_packet ( IiiiIi1iiii11 ) ) )
   if 42 - 42: OoO0O00 % ooOoO0o . I11i + ooOoO0o . iIii1I11I1II1 * ooOoO0o
   if 79 - 79: I1ii11iIi11i . IiII * IiII - o0oOOo0O0Ooo
   if 49 - 49: iIii1I11I1II1 % Ii1I / OoooooooOO - II111iiii . Ii1I
   if 65 - 65: OoooooooOO + I1Ii111 % ooOoO0o + II111iiii . i1IIi + OoooooooOO
   if 26 - 26: I1IiiI / II111iiii % I1ii11iIi11i * o0oOOo0O0Ooo . IiII / OoO0O00
  if ( I1II1i ) : continue
  return ( [ OO0Oo0o0o , iI1Iii1i1 , Oo0o , IiiiIi1iiii11 ] )
  if 10 - 10: i11iIiiIii / i1IIi + O0 - i11iIiiIii % I11i - i1IIi
  if 38 - 38: O0 - I1IiiI + Oo0Ooo + ooOoO0o
  if 56 - 56: I1Ii111 + oO0o / Ii1I + I1Ii111
  if 21 - 21: OOooOOo / OoOoOO00 + OoOoOO00 + OoOoOO00 - i1IIi + Ii1I
  if 43 - 43: O0 % II111iiii
  if 60 - 60: iII111i / ooOoO0o - Ii1I - OoooooooOO
  if 79 - 79: oO0o / iII111i . iIii1I11I1II1 * i11iIiiIii * i1IIi . iIii1I11I1II1
  if 31 - 31: OoooooooOO / ooOoO0o / OoooooooOO + ooOoO0o . O0 - IiII
def lisp_parse_packet ( lisp_sockets , packet , source , udp_sport , ttl = - 1 ) :
 oO0000o00OO = False
 II1IIII = time . time ( )
 if 24 - 24: I1ii11iIi11i * i11iIiiIii + OoooooooOO
 O00O0OO = lisp_control_header ( )
 if ( O00O0OO . decode ( packet ) == None ) :
  lprint ( "Could not decode control header" )
  return ( oO0000o00OO )
  if 20 - 20: OOooOOo / O0
  if 51 - 51: ooOoO0o - I1Ii111 * oO0o
  if 47 - 47: Oo0Ooo % OoO0O00 * Ii1I / OoOoOO00
  if 1 - 1: I1IiiI
  if 68 - 68: ooOoO0o
 o00o0OOO000 = source
 if ( source . find ( "lisp" ) == - 1 ) :
  OO0o0OO0 = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  OO0o0OO0 . string_to_afi ( source )
  OO0o0OO0 . store_address ( source )
  source = OO0o0OO0
  if 43 - 43: I1Ii111
  if 53 - 53: I1Ii111 + ooOoO0o - iII111i + I1ii11iIi11i * iII111i
 if ( O00O0OO . type == LISP_MAP_REQUEST ) :
  lisp_process_map_request ( lisp_sockets , packet , None , 0 , source ,
 udp_sport , False , ttl , II1IIII )
  if 95 - 95: OoO0O00 * OoOoOO00 / i1IIi / iII111i + IiII - Ii1I
 elif ( O00O0OO . type == LISP_MAP_REPLY ) :
  lisp_process_map_reply ( lisp_sockets , packet , source , ttl , II1IIII )
  if 36 - 36: II111iiii * OoO0O00 + I11i
 elif ( O00O0OO . type == LISP_MAP_REGISTER ) :
  lisp_process_map_register ( lisp_sockets , packet , source , udp_sport )
  if 39 - 39: II111iiii - OoO0O00
 elif ( O00O0OO . type == LISP_MAP_NOTIFY ) :
  if ( o00o0OOO000 == "lisp-etr" ) :
   lisp_process_multicast_map_notify ( packet , source )
  elif ( lisp_is_running ( "lisp-rtr" ) ) :
   lisp_process_multicast_map_notify ( packet , source )
  elif ( lisp_is_running ( "lisp-itr" ) ) :
   lisp_process_unicast_map_notify ( lisp_sockets , packet , source )
   if 8 - 8: I11i - OoO0O00 / II111iiii
   if 32 - 32: oO0o
 elif ( O00O0OO . type == LISP_MAP_NOTIFY_ACK ) :
  lisp_process_map_notify_ack ( packet , source )
  if 26 - 26: OoOoOO00 / i11iIiiIii - OOooOOo % oO0o % I1IiiI
 elif ( O00O0OO . type == LISP_MAP_REFERRAL ) :
  lisp_process_map_referral ( lisp_sockets , packet , source )
  if 23 - 23: i11iIiiIii / iII111i + IiII / i11iIiiIii
 elif ( O00O0OO . type == LISP_NAT_INFO and O00O0OO . is_info_reply ( ) ) :
  oOo0oo , IIIi1i1iIIIi , oO0000o00OO = lisp_process_info_reply ( source , packet , True )
  if 97 - 97: o0oOOo0O0Ooo + o0oOOo0O0Ooo / I1ii11iIi11i * OoooooooOO
 elif ( O00O0OO . type == LISP_NAT_INFO and O00O0OO . is_info_reply ( ) == False ) :
  oo0o00OO = source . print_address_no_iid ( )
  lisp_process_info_request ( lisp_sockets , packet , oo0o00OO , udp_sport ,
 None )
  if 61 - 61: I1IiiI - I11i
 elif ( O00O0OO . type == LISP_ECM ) :
  lisp_process_ecm ( lisp_sockets , packet , source , udp_sport )
  if 5 - 5: i11iIiiIii % i1IIi / IiII * i11iIiiIii . i1IIi * iII111i
 else :
  lprint ( "Invalid LISP control packet type {}" . format ( O00O0OO . type ) )
  if 71 - 71: i11iIiiIii / iIii1I11I1II1 % i1IIi + oO0o - i1IIi + II111iiii
 return ( oO0000o00OO )
 if 40 - 40: OOooOOo + ooOoO0o
 if 96 - 96: i11iIiiIii + IiII / iIii1I11I1II1
 if 49 - 49: OoOoOO00 - I1ii11iIi11i . I11i % II111iiii % iII111i
 if 6 - 6: OoooooooOO
 if 49 - 49: iII111i
 if 12 - 12: Oo0Ooo / II111iiii * OoOoOO00 * i1IIi - i1IIi / iII111i
 if 43 - 43: I1IiiI / IiII
def lisp_process_rloc_probe_request ( lisp_sockets , map_request , source , port ,
 ttl , timestamp ) :
 if 38 - 38: I1ii11iIi11i + i11iIiiIii * I1IiiI % oO0o % OoooooooOO
 IiI1i1i1 = bold ( "RLOC-probe" , False )
 if 4 - 4: OoO0O00 . I1IiiI - O0 % iII111i . OOooOOo
 if ( lisp_i_am_etr ) :
  lprint ( "Received {} Map-Request, send RLOC-probe Map-Reply" . format ( IiI1i1i1 ) )
  lisp_etr_process_map_request ( lisp_sockets , map_request , source , port ,
 ttl , timestamp )
  return
  if 69 - 69: OoooooooOO
  if 19 - 19: O0 + iIii1I11I1II1 / OoOoOO00 / oO0o + II111iiii - OOooOOo
 if ( lisp_i_am_rtr ) :
  lprint ( "Received {} Map-Request, send RLOC-probe Map-Reply" . format ( IiI1i1i1 ) )
  lisp_rtr_process_map_request ( lisp_sockets , map_request , source , port ,
 ttl , timestamp )
  return
  if 70 - 70: i1IIi * o0oOOo0O0Ooo + I1Ii111 . ooOoO0o - O0 + i11iIiiIii
  if 81 - 81: iIii1I11I1II1 - OoO0O00 . i11iIiiIii
 lprint ( "Ignoring received {} Map-Request, not an ETR or RTR" . format ( IiI1i1i1 ) )
 return
 if 4 - 4: o0oOOo0O0Ooo / OoO0O00 - I11i
 if 52 - 52: II111iiii . iII111i
 if 36 - 36: I1IiiI * II111iiii
 if 68 - 68: oO0o * o0oOOo0O0Ooo + OoooooooOO - I1ii11iIi11i * i1IIi % OOooOOo
 if 39 - 39: I1Ii111 / I11i + oO0o / I1Ii111 % IiII * I1ii11iIi11i
def lisp_process_smr ( map_request ) :
 lprint ( "Received SMR-based Map-Request" )
 return
 if 66 - 66: I1ii11iIi11i * ooOoO0o . i11iIiiIii * Oo0Ooo - I11i . I1IiiI
 if 43 - 43: I11i . iII111i . IiII - oO0o
 if 60 - 60: i1IIi + iII111i * i1IIi . iII111i
 if 40 - 40: i1IIi . OoO0O00
 if 65 - 65: Oo0Ooo
def lisp_process_smr_invoked_request ( map_request ) :
 lprint ( "Received SMR-invoked Map-Request" )
 return
 if 81 - 81: OOooOOo % OoooooooOO / IiII . Oo0Ooo - ooOoO0o . I1IiiI
 if 3 - 3: O0
 if 95 - 95: i11iIiiIii
 if 100 - 100: iIii1I11I1II1 * I1IiiI * Ii1I * i1IIi . I1Ii111 * I1IiiI
 if 54 - 54: o0oOOo0O0Ooo / iII111i + IiII - o0oOOo0O0Ooo - I11i
 if 28 - 28: I1IiiI - iIii1I11I1II1 - o0oOOo0O0Ooo * IiII + OoooooooOO
 if 52 - 52: I1Ii111
def lisp_build_map_reply ( eid , group , rloc_set , nonce , action , ttl , map_request ,
 keys , enc , auth , mr_ttl = - 1 ) :
 if 86 - 86: O0 * IiII + OoOoOO00 + OoO0O00
 OOOooOO00O = map_request . rloc_probe if ( map_request != None ) else False
 oO0O00Oo = map_request . json_telemetry if ( map_request != None ) else None
 if 74 - 74: I11i * iIii1I11I1II1 - OoO0O00 / i1IIi / OoO0O00 / IiII
 if 60 - 60: oO0o % I1Ii111 % Oo0Ooo
 II1II1i1IIII = lisp_map_reply ( )
 II1II1i1IIII . rloc_probe = OOOooOO00O
 II1II1i1IIII . echo_nonce_capable = enc
 II1II1i1IIII . hop_count = 0 if ( mr_ttl == - 1 ) else mr_ttl
 II1II1i1IIII . record_count = 1
 II1II1i1IIII . nonce = nonce
 IiiiIi1iiii11 = II1II1i1IIII . encode ( )
 II1II1i1IIII . print_map_reply ( )
 if 88 - 88: iIii1I11I1II1 * OoO0O00 / IiII
 OOOo = lisp_eid_record ( )
 OOOo . rloc_count = len ( rloc_set )
 if ( oO0O00Oo != None ) : OOOo . rloc_count += 1
 OOOo . authoritative = auth
 OOOo . record_ttl = ttl
 OOOo . action = action
 OOOo . eid = eid
 OOOo . group = group
 if 7 - 7: Oo0Ooo / ooOoO0o
 IiiiIi1iiii11 += OOOo . encode ( )
 OOOo . print_record ( "  " , False )
 if 55 - 55: OoO0O00 % IiII
 OOoOOoOo000O = lisp_get_all_addresses ( ) + lisp_get_all_translated_rlocs ( )
 if 27 - 27: I1IiiI . I1Ii111 % OoOoOO00 * Oo0Ooo % OoooooooOO
 iiIiI1 = None
 for oOO0O in rloc_set :
  o000OO0oO0O = oOO0O . rloc . is_multicast_address ( )
  OOO0Oo = lisp_rloc_record ( )
  OO0 = OOOooOO00O and ( o000OO0oO0O or oO0O00Oo == None )
  oo0o00OO = oOO0O . rloc . print_address_no_iid ( )
  if ( oo0o00OO in OOoOOoOo000O or o000OO0oO0O ) :
   OOO0Oo . local_bit = True
   OOO0Oo . probe_bit = OO0
   OOO0Oo . keys = keys
   if ( oOO0O . priority == 254 and lisp_i_am_rtr ) :
    OOO0Oo . rloc_name = "RTR"
    if 6 - 6: Oo0Ooo + I1IiiI
   if ( iiIiI1 == None ) : iiIiI1 = oOO0O . rloc
   if 48 - 48: oO0o . I1ii11iIi11i
  OOO0Oo . store_rloc_entry ( oOO0O )
  OOO0Oo . reach_bit = True
  OOO0Oo . print_record ( "    " )
  IiiiIi1iiii11 += OOO0Oo . encode ( )
  if 59 - 59: IiII - Ii1I
  if 62 - 62: OOooOOo * o0oOOo0O0Ooo + IiII * o0oOOo0O0Ooo * i11iIiiIii - O0
  if 37 - 37: I1ii11iIi11i - Oo0Ooo . i11iIiiIii / i11iIiiIii + oO0o
  if 19 - 19: i1IIi / i1IIi - OoooooooOO - OOooOOo . i1IIi
  if 57 - 57: OOooOOo / I1ii11iIi11i * oO0o
 if ( oO0O00Oo != None ) :
  OOO0Oo = lisp_rloc_record ( )
  if ( iiIiI1 ) : OOO0Oo . rloc . copy_address ( iiIiI1 )
  OOO0Oo . local_bit = True
  OOO0Oo . probe_bit = True
  OOO0Oo . reach_bit = True
  oO0OOO0o0oooO = lisp_encode_telemetry ( oO0O00Oo , eo = str ( time . time ( ) ) )
  OOO0Oo . json = lisp_json ( "telemetry" , oO0OOO0o0oooO )
  OOO0Oo . print_record ( "    " )
  IiiiIi1iiii11 += OOO0Oo . encode ( )
  if 10 - 10: OoO0O00 % II111iiii
 return ( IiiiIi1iiii11 )
 if 28 - 28: II111iiii + OoOoOO00 . Ii1I - Ii1I % I1ii11iIi11i
 if 44 - 44: OOooOOo - o0oOOo0O0Ooo
 if 69 - 69: IiII + I1ii11iIi11i / o0oOOo0O0Ooo / OOooOOo
 if 31 - 31: oO0o + I1ii11iIi11i * i1IIi % I1IiiI % I1IiiI + iIii1I11I1II1
 if 62 - 62: OoooooooOO
 if 38 - 38: iII111i % iII111i * ooOoO0o / OoO0O00 + ooOoO0o
 if 52 - 52: ooOoO0o . iIii1I11I1II1 / iIii1I11I1II1 % oO0o - oO0o * II111iiii
def lisp_build_map_referral ( eid , group , ddt_entry , action , ttl , nonce ) :
 oooOOo00oOOo = lisp_map_referral ( )
 oooOOo00oOOo . record_count = 1
 oooOOo00oOOo . nonce = nonce
 IiiiIi1iiii11 = oooOOo00oOOo . encode ( )
 oooOOo00oOOo . print_map_referral ( )
 if 89 - 89: o0oOOo0O0Ooo / II111iiii . I1ii11iIi11i / OOooOOo
 OOOo = lisp_eid_record ( )
 if 92 - 92: OOooOOo % OOooOOo
 O0OOo0 = 0
 if ( ddt_entry == None ) :
  OOOo . eid = eid
  OOOo . group = group
 else :
  O0OOo0 = len ( ddt_entry . delegation_set )
  OOOo . eid = ddt_entry . eid
  OOOo . group = ddt_entry . group
  ddt_entry . map_referrals_sent += 1
  if 34 - 34: Oo0Ooo . OOooOOo % II111iiii / i1IIi - i1IIi + OoOoOO00
 OOOo . rloc_count = O0OOo0
 OOOo . authoritative = True
 if 37 - 37: ooOoO0o
 if 36 - 36: OoooooooOO % OoooooooOO . o0oOOo0O0Ooo * OoOoOO00 + Oo0Ooo . O0
 if 33 - 33: ooOoO0o . I1Ii111 + I1IiiI . Oo0Ooo
 if 11 - 11: o0oOOo0O0Ooo * i11iIiiIii
 if 9 - 9: OoooooooOO / OoooooooOO
 Oo00OoooO0o = False
 if ( action == LISP_DDT_ACTION_NULL ) :
  if ( O0OOo0 == 0 ) :
   action = LISP_DDT_ACTION_NODE_REFERRAL
  else :
   I1I = ddt_entry . delegation_set [ 0 ]
   if ( I1I . is_ddt_child ( ) ) :
    action = LISP_DDT_ACTION_NODE_REFERRAL
    if 57 - 57: OoO0O00 + i1IIi % OOooOOo * i11iIiiIii % i1IIi / o0oOOo0O0Ooo
   if ( I1I . is_ms_child ( ) ) :
    action = LISP_DDT_ACTION_MS_REFERRAL
    if 1 - 1: ooOoO0o
    if 81 - 81: iII111i . Oo0Ooo . O0 . II111iiii
    if 46 - 46: I1Ii111 % Ii1I - I1ii11iIi11i + iIii1I11I1II1 + OoooooooOO . oO0o
    if 43 - 43: i1IIi % o0oOOo0O0Ooo * I1IiiI / oO0o * IiII + I11i
    if 13 - 13: O0
    if 60 - 60: IiII
    if 14 - 14: II111iiii - i1IIi % OoOoOO00
 if ( action == LISP_DDT_ACTION_NOT_AUTH ) : Oo00OoooO0o = True
 if ( action in ( LISP_DDT_ACTION_MS_REFERRAL , LISP_DDT_ACTION_MS_ACK ) ) :
  Oo00OoooO0o = ( lisp_i_am_ms and I1I . is_ms_peer ( ) == False )
  if 29 - 29: OoooooooOO * O0 / iIii1I11I1II1
  if 29 - 29: OoO0O00 / IiII + i1IIi / OoO0O00 . Oo0Ooo
 OOOo . action = action
 OOOo . ddt_incomplete = Oo00OoooO0o
 OOOo . record_ttl = ttl
 if 52 - 52: OoOoOO00 . iIii1I11I1II1 / OoOoOO00
 IiiiIi1iiii11 += OOOo . encode ( )
 OOOo . print_record ( "  " , True )
 if 14 - 14: i1IIi
 if ( O0OOo0 == 0 ) : return ( IiiiIi1iiii11 )
 if 63 - 63: OoOoOO00 . i11iIiiIii / IiII
 for I1I in ddt_entry . delegation_set :
  OOO0Oo = lisp_rloc_record ( )
  OOO0Oo . rloc = I1I . delegate_address
  OOO0Oo . priority = I1I . priority
  OOO0Oo . weight = I1I . weight
  OOO0Oo . mpriority = 255
  OOO0Oo . mweight = 0
  OOO0Oo . reach_bit = True
  IiiiIi1iiii11 += OOO0Oo . encode ( )
  OOO0Oo . print_record ( "    " )
  if 36 - 36: OOooOOo * OoOoOO00 + i11iIiiIii + O0 + O0
 return ( IiiiIi1iiii11 )
 if 18 - 18: Oo0Ooo . I1ii11iIi11i * ooOoO0o % Ii1I + I1ii11iIi11i
 if 23 - 23: oO0o / o0oOOo0O0Ooo + I11i % IiII * OoO0O00
 if 48 - 48: OoO0O00
 if 30 - 30: iIii1I11I1II1
 if 53 - 53: II111iiii
 if 40 - 40: Ii1I % oO0o
 if 69 - 69: iIii1I11I1II1 - O0 . I1Ii111 % I1IiiI / o0oOOo0O0Ooo
def lisp_etr_process_map_request ( lisp_sockets , map_request , source , sport ,
 ttl , etr_in_ts ) :
 if 78 - 78: oO0o
 if ( map_request . target_group . is_null ( ) ) :
  ii1iii = lisp_db_for_lookups . lookup_cache ( map_request . target_eid , False )
 else :
  ii1iii = lisp_db_for_lookups . lookup_cache ( map_request . target_group , False )
  if ( ii1iii ) : ii1iii = ii1iii . lookup_source_cache ( map_request . target_eid , False )
  if 71 - 71: OoOoOO00 / i11iIiiIii * iII111i
 Ii1i1 = map_request . print_prefix ( )
 if 90 - 90: Ii1I
 if ( ii1iii == None ) :
  lprint ( "Database-mapping entry not found for requested EID {}" . format ( green ( Ii1i1 , False ) ) )
  if 27 - 27: oO0o + Ii1I . i11iIiiIii
  return
  if 97 - 97: iII111i . I1IiiI
  if 71 - 71: OOooOOo - IiII % oO0o * I1ii11iIi11i
 iIIiIIiII111 = ii1iii . print_eid_tuple ( )
 if 24 - 24: O0 . Oo0Ooo + O0 % Ii1I + OoooooooOO
 lprint ( "Found database-mapping EID-prefix {} for requested EID {}" . format ( green ( iIIiIIiII111 , False ) , green ( Ii1i1 , False ) ) )
 if 72 - 72: I1ii11iIi11i
 if 100 - 100: i11iIiiIii - iII111i - I11i
 if 5 - 5: oO0o % IiII * iII111i
 if 98 - 98: iII111i / OOooOOo + IiII
 if 100 - 100: II111iiii . i11iIiiIii / oO0o - OOooOOo + OoOoOO00 % I1ii11iIi11i
 o00O00oOO00 = map_request . itr_rlocs [ 0 ]
 if ( o00O00oOO00 . is_private_address ( ) and lisp_nat_traversal ) :
  o00O00oOO00 = source
  if 3 - 3: i1IIi * I1ii11iIi11i * II111iiii . I1ii11iIi11i
  if 82 - 82: OoOoOO00
 o0OOO = map_request . nonce
 i11 = lisp_nonce_echoing
 iIi11III = map_request . keys
 if 53 - 53: OOooOOo * OoOoOO00 % iII111i
 if 86 - 86: OOooOOo . OOooOOo + IiII - I1ii11iIi11i . OoO0O00
 if 66 - 66: I1IiiI * OoOoOO00 . I1IiiI / Oo0Ooo - Ii1I
 if 69 - 69: iIii1I11I1II1 % iII111i + ooOoO0o * i1IIi + iII111i * I1Ii111
 if 67 - 67: Ii1I % Oo0Ooo - Oo0Ooo . I11i + IiII
 oOooo0o = map_request . json_telemetry
 if ( oOooo0o != None ) :
  map_request . json_telemetry = lisp_encode_telemetry ( oOooo0o , ei = etr_in_ts )
  if 45 - 45: oO0o + ooOoO0o + OOooOOo * OOooOOo * o0oOOo0O0Ooo / Oo0Ooo
  if 61 - 61: OoooooooOO % i11iIiiIii . i1IIi . OOooOOo
 ii1iii . map_replies_sent += 1
 if 90 - 90: iIii1I11I1II1 - iIii1I11I1II1 % O0
 IiiiIi1iiii11 = lisp_build_map_reply ( ii1iii . eid , ii1iii . group , ii1iii . rloc_set , o0OOO ,
 LISP_NO_ACTION , 1440 , map_request , iIi11III , i11 , True , ttl )
 if 43 - 43: Oo0Ooo / i1IIi % Ii1I . OoOoOO00
 if 22 - 22: iIii1I11I1II1 + Ii1I
 if 73 - 73: I1IiiI / OoO0O00 / OoooooooOO
 if 14 - 14: ooOoO0o % o0oOOo0O0Ooo / I1ii11iIi11i . IiII + I1ii11iIi11i
 if 30 - 30: I1ii11iIi11i + iIii1I11I1II1 . I1ii11iIi11i
 if 9 - 9: I1IiiI - Ii1I * II111iiii - I11i
 if 85 - 85: oO0o % ooOoO0o / OOooOOo
 if 50 - 50: O0 * O0 / iIii1I11I1II1
 if 31 - 31: I1IiiI / o0oOOo0O0Ooo
 if 70 - 70: I1IiiI
 if 36 - 36: ooOoO0o . oO0o . I11i - I1ii11iIi11i / OoOoOO00 * Oo0Ooo
 if 42 - 42: OoooooooOO / o0oOOo0O0Ooo . Ii1I * iII111i * I1IiiI - Oo0Ooo
 if 76 - 76: oO0o * II111iiii
 if 81 - 81: I11i
 if 2 - 2: OoOoOO00
 if 75 - 75: I1IiiI - OoooooooOO * I1Ii111
 if ( map_request . rloc_probe and len ( lisp_sockets ) == 4 ) :
  i111Iii11i1Ii = ( o00O00oOO00 . is_private_address ( ) == False )
  iIi = o00O00oOO00 . print_address_no_iid ( )
  if ( ( i111Iii11i1Ii and lisp_rtr_list . has_key ( iIi ) ) or sport == 0 ) :
   lisp_encapsulate_rloc_probe ( lisp_sockets , o00O00oOO00 , None , IiiiIi1iiii11 )
   return
   if 1 - 1: o0oOOo0O0Ooo % oO0o * I1Ii111 - i1IIi - iII111i . oO0o
   if 25 - 25: i1IIi * o0oOOo0O0Ooo / oO0o
   if 11 - 11: IiII + II111iiii
   if 37 - 37: O0
   if 98 - 98: IiII * OoooooooOO . iII111i
   if 34 - 34: OoooooooOO + I1Ii111
 lisp_send_map_reply ( lisp_sockets , IiiiIi1iiii11 , o00O00oOO00 , sport )
 return
 if 97 - 97: II111iiii + I11i + OOooOOo / i11iIiiIii - iII111i
 if 9 - 9: i1IIi - I1Ii111 + I1Ii111
 if 81 - 81: II111iiii % I11i % O0 . I1Ii111 % ooOoO0o - O0
 if 58 - 58: OoooooooOO . II111iiii . O0 % I1Ii111 / OoooooooOO
 if 64 - 64: Oo0Ooo + oO0o . OoO0O00
 if 67 - 67: I11i
 if 91 - 91: OOooOOo / OoO0O00
def lisp_rtr_process_map_request ( lisp_sockets , map_request , source , sport ,
 ttl , etr_in_ts ) :
 if 36 - 36: I1IiiI . iII111i * I1Ii111 . IiII % I1ii11iIi11i
 if 44 - 44: I11i % I1ii11iIi11i - OoooooooOO % iII111i
 if 60 - 60: IiII % oO0o
 if 11 - 11: I1Ii111 - II111iiii
 o00O00oOO00 = map_request . itr_rlocs [ 0 ]
 if ( o00O00oOO00 . is_private_address ( ) ) : o00O00oOO00 = source
 o0OOO = map_request . nonce
 if 12 - 12: i11iIiiIii
 iiI1I1IIi = map_request . target_eid
 OOo0oOOO0 = map_request . target_group
 if 9 - 9: OOooOOo * I1ii11iIi11i + iIii1I11I1II1 / OoO0O00 * OoooooooOO
 OoO0oOOooOO = [ ]
 for oooOO0 in [ lisp_myrlocs [ 0 ] , lisp_myrlocs [ 1 ] ] :
  if ( oooOO0 == None ) : continue
  I1II = lisp_rloc ( )
  I1II . rloc . copy_address ( oooOO0 )
  I1II . priority = 254
  OoO0oOOooOO . append ( I1II )
  if 60 - 60: IiII + I1IiiI
  if 61 - 61: OoO0O00
 i11 = lisp_nonce_echoing
 iIi11III = map_request . keys
 if 96 - 96: ooOoO0o - OoooooooOO * iIii1I11I1II1 . IiII - O0
 if 7 - 7: iIii1I11I1II1 . OoO0O00
 if 88 - 88: i1IIi * II111iiii / i11iIiiIii % IiII . IiII
 if 93 - 93: OoOoOO00 * i1IIi . Ii1I
 if 2 - 2: i1IIi
 oOooo0o = map_request . json_telemetry
 if ( oOooo0o != None ) :
  map_request . json_telemetry = lisp_encode_telemetry ( oOooo0o , ei = etr_in_ts )
  if 84 - 84: i1IIi / Ii1I + OoOoOO00 % Ii1I . oO0o
  if 74 - 74: OOooOOo - o0oOOo0O0Ooo - I1Ii111 - OoO0O00
 IiiiIi1iiii11 = lisp_build_map_reply ( iiI1I1IIi , OOo0oOOO0 , OoO0oOOooOO , o0OOO , LISP_NO_ACTION ,
 1440 , map_request , iIi11III , i11 , True , ttl )
 lisp_send_map_reply ( lisp_sockets , IiiiIi1iiii11 , o00O00oOO00 , sport )
 return
 if 40 - 40: o0oOOo0O0Ooo . IiII * OoOoOO00
 if 14 - 14: OOooOOo
 if 18 - 18: i11iIiiIii % iII111i
 if 70 - 70: O0 + iII111i % I11i % I1Ii111 + OoOoOO00 / ooOoO0o
 if 35 - 35: IiII + OoO0O00
 if 82 - 82: i1IIi - ooOoO0o / I11i + I11i % I1IiiI - OoooooooOO
 if 56 - 56: I1ii11iIi11i
 if 80 - 80: Oo0Ooo / OOooOOo / iII111i . o0oOOo0O0Ooo
 if 43 - 43: IiII
 if 74 - 74: OoooooooOO
def lisp_get_private_rloc_set ( target_site_eid , seid , group ) :
 OoO0oOOooOO = target_site_eid . registered_rlocs
 if 88 - 88: Ii1I * o0oOOo0O0Ooo / oO0o
 oOoo = lisp_site_eid_lookup ( seid , group , False )
 if ( oOoo == None ) : return ( OoO0oOOooOO )
 if 25 - 25: I1IiiI % ooOoO0o % i11iIiiIii * i11iIiiIii + I1ii11iIi11i
 if 92 - 92: OOooOOo - Ii1I - Ii1I + o0oOOo0O0Ooo + OoO0O00 % Ii1I
 if 24 - 24: I1Ii111 % oO0o + I1ii11iIi11i % II111iiii % I1Ii111 / I1ii11iIi11i
 if 34 - 34: OoooooooOO * i11iIiiIii
 iIi1i = None
 OOO = [ ]
 for oOO0O in OoO0oOOooOO :
  if ( oOO0O . is_rtr ( ) ) : continue
  if ( oOO0O . rloc . is_private_address ( ) ) :
   I1IIII1Iiii11 = copy . deepcopy ( oOO0O )
   OOO . append ( I1IIII1Iiii11 )
   continue
   if 15 - 15: I11i + iII111i
  iIi1i = oOO0O
  break
  if 79 - 79: i11iIiiIii * IiII % iII111i
 if ( iIi1i == None ) : return ( OoO0oOOooOO )
 iIi1i = iIi1i . rloc . print_address_no_iid ( )
 if 18 - 18: iIii1I11I1II1 - O0 . o0oOOo0O0Ooo % oO0o
 if 73 - 73: IiII + I11i % I1IiiI * iII111i . O0
 if 17 - 17: OoO0O00 * OoOoOO00 % O0 % iII111i / i1IIi
 if 100 - 100: i11iIiiIii
 ooO00Oo0o0OOo = None
 for oOO0O in oOoo . registered_rlocs :
  if ( oOO0O . is_rtr ( ) ) : continue
  if ( oOO0O . rloc . is_private_address ( ) ) : continue
  ooO00Oo0o0OOo = oOO0O
  break
  if 71 - 71: I11i * OOooOOo
 if ( ooO00Oo0o0OOo == None ) : return ( OoO0oOOooOO )
 ooO00Oo0o0OOo = ooO00Oo0o0OOo . rloc . print_address_no_iid ( )
 if 92 - 92: o0oOOo0O0Ooo
 if 31 - 31: O0 . o0oOOo0O0Ooo . O0 * OoOoOO00 - OoO0O00
 if 80 - 80: II111iiii % oO0o
 if 48 - 48: OOooOOo . II111iiii * OOooOOo - I11i / iIii1I11I1II1 / i11iIiiIii
 Iii1I1 = target_site_eid . site_id
 if ( Iii1I1 == 0 ) :
  if ( ooO00Oo0o0OOo == iIi1i ) :
   lprint ( "Return private RLOCs for sites behind {}" . format ( iIi1i ) )
   if 37 - 37: II111iiii % O0 + iIii1I11I1II1 - I1IiiI . I11i + I1ii11iIi11i
   return ( OOO )
   if 14 - 14: ooOoO0o % iIii1I11I1II1 % ooOoO0o / IiII + OOooOOo
  return ( OoO0oOOooOO )
  if 14 - 14: Oo0Ooo
  if 79 - 79: I1ii11iIi11i % I1Ii111 % I11i - iII111i * OoOoOO00
  if 48 - 48: O0 + OoOoOO00 - O0
  if 79 - 79: ooOoO0o . OoOoOO00 / OoooooooOO - II111iiii
  if 48 - 48: Oo0Ooo
  if 59 - 59: OoO0O00 % o0oOOo0O0Ooo
  if 83 - 83: iII111i % iIii1I11I1II1 / OOooOOo - OoOoOO00
 if ( Iii1I1 == oOoo . site_id ) :
  lprint ( "Return private RLOCs for sites in site-id {}" . format ( Iii1I1 ) )
  return ( OOO )
  if 98 - 98: I11i % oO0o . I1IiiI % OoOoOO00
 return ( OoO0oOOooOO )
 if 32 - 32: I1ii11iIi11i / Ii1I
 if 54 - 54: I11i - i11iIiiIii
 if 91 - 91: Ii1I - OoO0O00 - I1IiiI % OoO0O00 . o0oOOo0O0Ooo
 if 85 - 85: ooOoO0o . ooOoO0o % Oo0Ooo . OOooOOo + OOooOOo / I1IiiI
 if 69 - 69: i1IIi + II111iiii / Ii1I
 if 4 - 4: I11i * OoOoOO00 % o0oOOo0O0Ooo % ooOoO0o - I1ii11iIi11i
 if 88 - 88: iIii1I11I1II1 * iIii1I11I1II1 * I11i * OoOoOO00
 if 14 - 14: i11iIiiIii * I1IiiI % O0 % iIii1I11I1II1
 if 18 - 18: Oo0Ooo % OOooOOo + IiII
def lisp_get_partial_rloc_set ( registered_rloc_set , mr_source , multicast ) :
 I1iIii1ii = [ ]
 OoO0oOOooOO = [ ]
 if 83 - 83: II111iiii . OoOoOO00 - i11iIiiIii . OoOoOO00 . i1IIi % OoooooooOO
 if 47 - 47: II111iiii
 if 30 - 30: i1IIi . Oo0Ooo / o0oOOo0O0Ooo + IiII * OOooOOo
 if 26 - 26: Ii1I % O0 - i1IIi % iII111i * OoO0O00
 if 60 - 60: I1ii11iIi11i * iII111i / OoOoOO00 . o0oOOo0O0Ooo / iIii1I11I1II1
 if 94 - 94: OoO0O00 . ooOoO0o
 i111i1iIi1i = False
 ii1i11Ii111 = False
 for oOO0O in registered_rloc_set :
  if ( oOO0O . priority != 254 ) : continue
  ii1i11Ii111 |= True
  if ( oOO0O . rloc . is_exact_match ( mr_source ) == False ) : continue
  i111i1iIi1i = True
  break
  if 21 - 21: O0
  if 65 - 65: iIii1I11I1II1
  if 83 - 83: iIii1I11I1II1 - iII111i
  if 91 - 91: i11iIiiIii . I11i . i1IIi - Ii1I
  if 37 - 37: O0
  if 68 - 68: OoO0O00 - I1Ii111
  if 66 - 66: Oo0Ooo % II111iiii / Ii1I . iII111i . OOooOOo . OOooOOo
 if ( ii1i11Ii111 == False ) : return ( registered_rloc_set )
 if 63 - 63: I11i / I11i + IiII - i1IIi / Ii1I
 if 100 - 100: OoO0O00 * iIii1I11I1II1
 if 65 - 65: II111iiii - iII111i - OOooOOo
 if 97 - 97: OoooooooOO / I1ii11iIi11i
 if 60 - 60: OOooOOo - I11i * IiII - o0oOOo0O0Ooo / I1IiiI
 if 93 - 93: OoOoOO00 . O0 - OOooOOo
 if 90 - 90: Oo0Ooo % iII111i % Oo0Ooo * I11i / OoOoOO00
 if 49 - 49: I1ii11iIi11i * II111iiii
 if 59 - 59: OoO0O00
 if 81 - 81: i11iIiiIii
 OOOo0O00OO00O = ( os . getenv ( "LISP_RTR_BEHIND_NAT" ) != None )
 if 91 - 91: Oo0Ooo - iIii1I11I1II1 - iII111i . OoooooooOO . iII111i + Oo0Ooo
 if 20 - 20: OoO0O00 . ooOoO0o - IiII
 if 82 - 82: oO0o
 if 26 - 26: I1ii11iIi11i
 if 40 - 40: OOooOOo
 for oOO0O in registered_rloc_set :
  if ( OOOo0O00OO00O and oOO0O . rloc . is_private_address ( ) ) : continue
  if ( multicast == False and oOO0O . priority == 255 ) : continue
  if ( multicast and oOO0O . mpriority == 255 ) : continue
  if ( oOO0O . priority == 254 ) :
   I1iIii1ii . append ( oOO0O )
  else :
   OoO0oOOooOO . append ( oOO0O )
   if 90 - 90: OoOoOO00
   if 21 - 21: i1IIi % oO0o + OOooOOo / I1ii11iIi11i % i1IIi
   if 64 - 64: I1Ii111 - OoOoOO00 * OoooooooOO - I1Ii111
   if 43 - 43: I1Ii111 + I11i - Ii1I + I11i - Oo0Ooo
   if 63 - 63: IiII % I11i / OoOoOO00 % OOooOOo * iII111i * OoO0O00
   if 11 - 11: I1Ii111 * II111iiii
 if ( i111i1iIi1i ) : return ( OoO0oOOooOO )
 if 3 - 3: Oo0Ooo * OOooOOo
 if 13 - 13: I1Ii111 + i11iIiiIii / OOooOOo
 if 98 - 98: I1IiiI * Oo0Ooo
 if 9 - 9: O0 / i11iIiiIii . iIii1I11I1II1 . IiII
 if 14 - 14: OoOoOO00 . OOooOOo - Oo0Ooo + I1Ii111 % ooOoO0o
 if 95 - 95: OoO0O00 * II111iiii + i1IIi
 if 22 - 22: Ii1I / ooOoO0o % I11i + OoO0O00 . ooOoO0o
 if 61 - 61: O0 - iIii1I11I1II1 * Oo0Ooo . Ii1I + O0
 if 20 - 20: ooOoO0o / ooOoO0o - Ii1I - ooOoO0o
 if 93 - 93: O0 * OoOoOO00 * iIii1I11I1II1
 OoO0oOOooOO = [ ]
 for oOO0O in registered_rloc_set :
  if ( oOO0O . rloc . is_private_address ( ) ) : OoO0oOOooOO . append ( oOO0O )
  if 3 - 3: I1ii11iIi11i - O0
 OoO0oOOooOO += I1iIii1ii
 return ( OoO0oOOooOO )
 if 46 - 46: iII111i
 if 99 - 99: oO0o
 if 85 - 85: I1Ii111 * iIii1I11I1II1 . OoOoOO00
 if 20 - 20: I11i * O0 - OoooooooOO * OOooOOo % oO0o * iII111i
 if 70 - 70: I11i + O0 . i11iIiiIii . OOooOOo
 if 48 - 48: iIii1I11I1II1 * Ii1I - OoooooooOO / oO0o - OoO0O00 / i11iIiiIii
 if 24 - 24: I1IiiI
 if 63 - 63: I11i - iIii1I11I1II1 * Ii1I + OoooooooOO . i11iIiiIii
 if 94 - 94: OoO0O00 . oO0o . OoOoOO00 * i11iIiiIii
 if 96 - 96: i1IIi . OoO0O00 . OoO0O00 - o0oOOo0O0Ooo - Ii1I
def lisp_store_pubsub_state ( reply_eid , itr_rloc , mr_sport , nonce , ttl , xtr_id ) :
 I1IIiI = lisp_pubsub ( itr_rloc , mr_sport , nonce , ttl , xtr_id )
 I1IIiI . add ( reply_eid )
 return ( I1IIiI )
 if 30 - 30: I1Ii111 + oO0o + iIii1I11I1II1 % OoO0O00 / I1IiiI
 if 55 - 55: Ii1I
 if 14 - 14: i1IIi * I1ii11iIi11i
 if 77 - 77: ooOoO0o . II111iiii
 if 41 - 41: IiII
 if 27 - 27: IiII / IiII
 if 91 - 91: Ii1I
 if 93 - 93: OoO0O00 * OoO0O00 * I1ii11iIi11i * OoO0O00 * o0oOOo0O0Ooo
 if 84 - 84: I1Ii111 * OoO0O00 - ooOoO0o - Oo0Ooo . OoO0O00 % oO0o
 if 98 - 98: OoO0O00 . i1IIi
 if 58 - 58: i1IIi * O0 + I1ii11iIi11i . IiII
 if 11 - 11: OOooOOo + iIii1I11I1II1 - ooOoO0o * OoO0O00 * i11iIiiIii
 if 45 - 45: I1ii11iIi11i + Oo0Ooo
 if 7 - 7: Oo0Ooo + ooOoO0o - I1Ii111 * iIii1I11I1II1
 if 6 - 6: ooOoO0o % I1Ii111 % ooOoO0o . Ii1I * Oo0Ooo . IiII
def lisp_convert_reply_to_notify ( packet ) :
 if 100 - 100: i1IIi . Ii1I . o0oOOo0O0Ooo + Ii1I - i1IIi . I11i
 if 19 - 19: i11iIiiIii + I11i - IiII . iII111i * i1IIi
 if 66 - 66: ooOoO0o
 if 4 - 4: iII111i / iII111i * OOooOOo + o0oOOo0O0Ooo . I1Ii111 + II111iiii
 O000oOooO0oo = struct . unpack ( "I" , packet [ 0 : 4 ] ) [ 0 ]
 O000oOooO0oo = socket . ntohl ( O000oOooO0oo ) & 0xff
 o0OOO = packet [ 4 : 12 ]
 packet = packet [ 12 : : ]
 if 24 - 24: O0 . I1ii11iIi11i / OOooOOo % IiII * Oo0Ooo / OoO0O00
 if 67 - 67: Oo0Ooo * I11i - IiII + I1Ii111
 if 90 - 90: iII111i % II111iiii % o0oOOo0O0Ooo + o0oOOo0O0Ooo + II111iiii
 if 54 - 54: OoooooooOO . IiII - oO0o
 i1OOoO0OO0oO = ( LISP_MAP_NOTIFY << 28 ) | O000oOooO0oo
 O00O0OO = struct . pack ( "I" , socket . htonl ( i1OOoO0OO0oO ) )
 o00oOOo0Oo = struct . pack ( "I" , 0 )
 if 26 - 26: o0oOOo0O0Ooo - i1IIi / I1ii11iIi11i / OoooooooOO . i1IIi
 if 22 - 22: o0oOOo0O0Ooo * I1Ii111 * I1ii11iIi11i . OoOoOO00 . i1IIi % ooOoO0o
 if 67 - 67: I11i
 if 95 - 95: OoO0O00 % I1Ii111
 packet = O00O0OO + o0OOO + o00oOOo0Oo + packet
 return ( packet )
 if 49 - 49: II111iiii % OoOoOO00 % OOooOOo
 if 40 - 40: I1ii11iIi11i + i1IIi
 if 9 - 9: OOooOOo
 if 74 - 74: OoOoOO00 - OOooOOo % OoOoOO00
 if 82 - 82: I11i % IiII + Oo0Ooo + iIii1I11I1II1 - I11i - I1IiiI
 if 65 - 65: IiII / O0 * II111iiii + oO0o
 if 52 - 52: o0oOOo0O0Ooo - OoOoOO00 * II111iiii / OoooooooOO
 if 44 - 44: OOooOOo - oO0o + o0oOOo0O0Ooo - i1IIi % o0oOOo0O0Ooo
def lisp_notify_subscribers ( lisp_sockets , eid_record , rloc_records ,
 registered_eid , site ) :
 if 79 - 79: iII111i . iIii1I11I1II1
 for Iii1i11 in lisp_pubsub_cache :
  for I1IIiI in lisp_pubsub_cache [ Iii1i11 ] . values ( ) :
   iIIi1iI1I1IIi = I1IIiI . eid_prefix
   if ( iIIi1iI1I1IIi . is_more_specific ( registered_eid ) == False ) : continue
   if 83 - 83: IiII % iIii1I11I1II1
   OooO0OO0 = I1IIiI . itr
   Oo0o = I1IIiI . port
   IiI = red ( OooO0OO0 . print_address_no_iid ( ) , False )
   IiIIi = bold ( "subscriber" , False )
   IIiiII11i11I = "0x" + lisp_hex_string ( I1IIiI . xtr_id )
   o0OOO = "0x" + lisp_hex_string ( I1IIiI . nonce )
   if 53 - 53: II111iiii . OoooooooOO
   lprint ( "    Notify {} {}:{} xtr-id {} for {}, nonce {}" . format ( IiIIi , IiI , Oo0o , IIiiII11i11I , green ( Iii1i11 , False ) , o0OOO ) )
   if 40 - 40: OoO0O00 / II111iiii + OoOoOO00
   if 96 - 96: OoOoOO00 . I1ii11iIi11i
   if 55 - 55: I1Ii111 + I1IiiI - ooOoO0o * I1Ii111
   if 44 - 44: i1IIi - I11i * I11i - OoO0O00 % OoOoOO00 / o0oOOo0O0Ooo
   if 15 - 15: i11iIiiIii + oO0o . iIii1I11I1II1 - I11i % IiII . I1Ii111
   if 31 - 31: OoooooooOO % iII111i / OOooOOo
   oOo0OOO0 = copy . deepcopy ( eid_record )
   oOo0OOO0 . eid . copy_address ( iIIi1iI1I1IIi )
   oOo0OOO0 = oOo0OOO0 . encode ( ) + rloc_records
   lisp_build_map_notify ( lisp_sockets , oOo0OOO0 , [ Iii1i11 ] , 1 , OooO0OO0 ,
 Oo0o , I1IIiI . nonce , 0 , 0 , 0 , site , False )
   if 89 - 89: iII111i
   I1IIiI . map_notify_count += 1
   if 1 - 1: iII111i * oO0o % Ii1I . oO0o
   if 86 - 86: iII111i * ooOoO0o / iIii1I11I1II1 + Ii1I . iII111i
 return
 if 64 - 64: IiII - Oo0Ooo % iII111i % I11i
 if 42 - 42: Oo0Ooo . OoO0O00
 if 22 - 22: ooOoO0o - o0oOOo0O0Ooo + I11i / I1IiiI + OOooOOo
 if 10 - 10: oO0o / I1IiiI
 if 95 - 95: II111iiii - IiII % IiII . o0oOOo0O0Ooo
 if 19 - 19: II111iiii . ooOoO0o . I11i - OoooooooOO / I1ii11iIi11i . I1Ii111
 if 57 - 57: II111iiii . I1Ii111 . i11iIiiIii / OoOoOO00 - O0
def lisp_process_pubsub ( lisp_sockets , packet , reply_eid , itr_rloc , port , nonce ,
 ttl , xtr_id ) :
 if 56 - 56: OOooOOo / I1Ii111
 if 13 - 13: oO0o + Oo0Ooo + Oo0Ooo / OoO0O00 + i1IIi + I1IiiI
 if 56 - 56: OoOoOO00
 if 10 - 10: iIii1I11I1II1 + i1IIi * Ii1I / iIii1I11I1II1 % OoOoOO00 / O0
 I1IIiI = lisp_store_pubsub_state ( reply_eid , itr_rloc , port , nonce , ttl ,
 xtr_id )
 if 14 - 14: O0
 iiI1I1IIi = green ( reply_eid . print_prefix ( ) , False )
 OooO0OO0 = red ( itr_rloc . print_address_no_iid ( ) , False )
 o0OOOII1I11Ii = bold ( "Map-Notify" , False )
 xtr_id = "0x" + lisp_hex_string ( xtr_id )
 lprint ( "{} pubsub request for {} to ack ITR {} xtr-id: {}" . format ( o0OOOII1I11Ii ,
 iiI1I1IIi , OooO0OO0 , xtr_id ) )
 if 89 - 89: oO0o % i11iIiiIii - iIii1I11I1II1 + oO0o
 if 15 - 15: I1ii11iIi11i - I1IiiI % OOooOOo
 if 9 - 9: Ii1I / O0
 if 95 - 95: iII111i / I11i
 packet = lisp_convert_reply_to_notify ( packet )
 lisp_send_map_notify ( lisp_sockets , packet , itr_rloc , port )
 I1IIiI . map_notify_count += 1
 return
 if 86 - 86: O0 / II111iiii . Oo0Ooo / Oo0Ooo * II111iiii
 if 22 - 22: Ii1I
 if 81 - 81: iIii1I11I1II1 . ooOoO0o % I11i
 if 64 - 64: I1Ii111 . Oo0Ooo * o0oOOo0O0Ooo
 if 32 - 32: oO0o . I1Ii111 * I1Ii111
 if 32 - 32: I1Ii111 . Ii1I / i1IIi
 if 2 - 2: OOooOOo * ooOoO0o / I11i + OoO0O00
 if 96 - 96: II111iiii * OoO0O00 + I1ii11iIi11i + OoOoOO00 / II111iiii . iII111i
def lisp_ms_process_map_request ( lisp_sockets , packet , map_request , mr_source ,
 mr_sport , ecm_source ) :
 if 64 - 64: iII111i % Oo0Ooo
 if 79 - 79: IiII + iII111i / II111iiii . i1IIi + iIii1I11I1II1
 if 32 - 32: Ii1I * iII111i
 if 52 - 52: I11i
 if 100 - 100: Oo0Ooo % Oo0Ooo % I1ii11iIi11i
 if 33 - 33: I1Ii111 . I1Ii111 * i1IIi
 iiI1I1IIi = map_request . target_eid
 OOo0oOOO0 = map_request . target_group
 Ii1i1 = lisp_print_eid_tuple ( iiI1I1IIi , OOo0oOOO0 )
 o00O00oOO00 = map_request . itr_rlocs [ 0 ]
 IIiiII11i11I = map_request . xtr_id
 o0OOO = map_request . nonce
 iI1IIi1I = LISP_NO_ACTION
 I1IIiI = map_request . subscribe_bit
 if 22 - 22: I1ii11iIi11i . II111iiii + iIii1I11I1II1 / OoooooooOO . ooOoO0o
 if 13 - 13: II111iiii
 if 36 - 36: iII111i - oO0o / Oo0Ooo / O0 . OoO0O00 . i1IIi
 if 19 - 19: O0 . OoooooooOO % iIii1I11I1II1 - Ii1I . Ii1I + I1IiiI
 if 98 - 98: oO0o . Oo0Ooo
 I1I1Ii1111 = True
 iIi1iIII = ( lisp_get_eid_hash ( iiI1I1IIi ) != None )
 if ( iIi1iIII ) :
  i1i11 = map_request . map_request_signature
  if ( i1i11 == None ) :
   I1I1Ii1111 = False
   lprint ( ( "EID-crypto-hash signature verification {}, " + "no signature found" ) . format ( bold ( "failed" , False ) ) )
   if 6 - 6: I1IiiI - ooOoO0o + I1IiiI + OoO0O00 - i11iIiiIii % ooOoO0o
  else :
   I1IiI11 = map_request . signature_eid
   oo0O0O , iII1II1i1iI , I1I1Ii1111 = lisp_lookup_public_key ( I1IiI11 )
   if ( I1I1Ii1111 ) :
    I1I1Ii1111 = map_request . verify_map_request_sig ( iII1II1i1iI )
   else :
    lprint ( "Public-key lookup failed for sig-eid {}, hash-eid {}" . format ( I1IiI11 . print_address ( ) , oo0O0O . print_address ( ) ) )
    if 82 - 82: I1IiiI - OoO0O00 % o0oOOo0O0Ooo
    if 72 - 72: O0 + OoOoOO00 % OOooOOo / oO0o / IiII
   oO0 = bold ( "passed" , False ) if I1I1Ii1111 else bold ( "failed" , False )
   lprint ( "EID-crypto-hash signature verification {}" . format ( oO0 ) )
   if 30 - 30: o0oOOo0O0Ooo + IiII * o0oOOo0O0Ooo + Ii1I - I11i
   if 70 - 70: oO0o * ooOoO0o / ooOoO0o - Ii1I * Ii1I % OOooOOo
   if 91 - 91: OoO0O00 - OoO0O00 % O0
 if ( I1IIiI and I1I1Ii1111 == False ) :
  I1IIiI = False
  lprint ( "Suppress creating pubsub state due to signature failure" )
  if 67 - 67: ooOoO0o * i1IIi
  if 66 - 66: o0oOOo0O0Ooo - I1ii11iIi11i . OoOoOO00 / iII111i - Ii1I - i1IIi
  if 97 - 97: oO0o % iII111i - OOooOOo . OoooooooOO
  if 94 - 94: Oo0Ooo
  if 10 - 10: i11iIiiIii / I1ii11iIi11i . i1IIi + i1IIi * iII111i
  if 64 - 64: II111iiii % I1ii11iIi11i . OoOoOO00 . iIii1I11I1II1 / I1ii11iIi11i
  if 43 - 43: OoooooooOO * I1IiiI
  if 2 - 2: OOooOOo / oO0o + I1ii11iIi11i + i11iIiiIii % iIii1I11I1II1 . I1ii11iIi11i
  if 100 - 100: Oo0Ooo * ooOoO0o + Ii1I / iII111i * o0oOOo0O0Ooo
  if 26 - 26: I1Ii111 * OoOoOO00
  if 38 - 38: II111iiii
  if 50 - 50: OoOoOO00 . IiII - OOooOOo
  if 46 - 46: iIii1I11I1II1
  if 97 - 97: O0 * OOooOOo - o0oOOo0O0Ooo % o0oOOo0O0Ooo * II111iiii % I11i
 ooOo = o00O00oOO00 if ( o00O00oOO00 . afi == ecm_source . afi ) else ecm_source
 if 38 - 38: OoooooooOO % o0oOOo0O0Ooo % I11i . Oo0Ooo
 oOoooo = lisp_site_eid_lookup ( iiI1I1IIi , OOo0oOOO0 , False )
 if 47 - 47: o0oOOo0O0Ooo / i1IIi * IiII
 if ( oOoooo == None or oOoooo . is_star_g ( ) ) :
  iiIi11I1I1 = bold ( "Site not found" , False )
  lprint ( "{} for requested EID {}" . format ( iiIi11I1I1 ,
 green ( Ii1i1 , False ) ) )
  if 96 - 96: I1IiiI
  if 34 - 34: Ii1I * i1IIi + OoooooooOO . oO0o
  if 30 - 30: I1Ii111 % IiII / II111iiii
  if 68 - 68: oO0o / O0 / OOooOOo
  lisp_send_negative_map_reply ( lisp_sockets , iiI1I1IIi , OOo0oOOO0 , o0OOO , o00O00oOO00 ,
 mr_sport , 15 , IIiiII11i11I , I1IIiI )
  if 3 - 3: o0oOOo0O0Ooo / o0oOOo0O0Ooo
  return ( [ iiI1I1IIi , OOo0oOOO0 , LISP_DDT_ACTION_SITE_NOT_FOUND ] )
  if 17 - 17: OoO0O00 * i1IIi
  if 50 - 50: OoOoOO00 + I11i
 iIIiIIiII111 = oOoooo . print_eid_tuple ( )
 OOOO0OOo0oOoo = oOoooo . site . site_name
 if 65 - 65: I11i / I1ii11iIi11i - OOooOOo . iIii1I11I1II1 * O0 + OoooooooOO
 if 83 - 83: OoooooooOO + Oo0Ooo
 if 4 - 4: Oo0Ooo - i11iIiiIii / O0 / I11i + ooOoO0o / iII111i
 if 72 - 72: II111iiii % iII111i + OoO0O00
 if 44 - 44: OoooooooOO + OoooooooOO - Ii1I * iII111i
 if ( iIi1iIII == False and oOoooo . require_signature ) :
  i1i11 = map_request . map_request_signature
  I1IiI11 = map_request . signature_eid
  if ( i1i11 == None or I1IiI11 . is_null ( ) ) :
   lprint ( "Signature required for site {}" . format ( OOOO0OOo0oOoo ) )
   I1I1Ii1111 = False
  else :
   I1IiI11 = map_request . signature_eid
   oo0O0O , iII1II1i1iI , I1I1Ii1111 = lisp_lookup_public_key ( I1IiI11 )
   if ( I1I1Ii1111 ) :
    I1I1Ii1111 = map_request . verify_map_request_sig ( iII1II1i1iI )
   else :
    lprint ( "Public-key lookup failed for sig-eid {}, hash-eid {}" . format ( I1IiI11 . print_address ( ) , oo0O0O . print_address ( ) ) )
    if 45 - 45: oO0o . O0 - ooOoO0o / o0oOOo0O0Ooo
    if 58 - 58: Ii1I . iII111i * OoO0O00 + OoO0O00 % I1Ii111 + I1ii11iIi11i
   oO0 = bold ( "passed" , False ) if I1I1Ii1111 else bold ( "failed" , False )
   lprint ( "Required signature verification {}" . format ( oO0 ) )
   if 34 - 34: i11iIiiIii + OoOoOO00
   if 57 - 57: I1IiiI + IiII . OoOoOO00 * iIii1I11I1II1 % OoooooooOO
   if 21 - 21: I11i
   if 36 - 36: IiII + OoO0O00
   if 66 - 66: iIii1I11I1II1 / oO0o
   if 36 - 36: o0oOOo0O0Ooo % I1ii11iIi11i - Oo0Ooo % o0oOOo0O0Ooo
 if ( I1I1Ii1111 and oOoooo . registered == False ) :
  lprint ( "Site '{}' with EID-prefix {} is not registered for EID {}" . format ( OOOO0OOo0oOoo , green ( iIIiIIiII111 , False ) , green ( Ii1i1 , False ) ) )
  if 18 - 18: oO0o / i1IIi * I11i
  if 71 - 71: OoooooooOO - i11iIiiIii * i1IIi % OOooOOo - oO0o / o0oOOo0O0Ooo
  if 77 - 77: iIii1I11I1II1 / OoOoOO00
  if 59 - 59: Oo0Ooo % OOooOOo
  if 14 - 14: I11i . OoO0O00
  if 46 - 46: ooOoO0o
  if ( oOoooo . accept_more_specifics == False ) :
   iiI1I1IIi = oOoooo . eid
   OOo0oOOO0 = oOoooo . group
   if 48 - 48: i1IIi * I1IiiI / i11iIiiIii
   if 40 - 40: IiII
   if 42 - 42: O0 / II111iiii
   if 88 - 88: Oo0Ooo
   if 20 - 20: OoooooooOO * i1IIi * IiII / OoooooooOO - Oo0Ooo / i11iIiiIii
  Oo0o0 = 1
  if ( oOoooo . force_ttl != None ) :
   Oo0o0 = oOoooo . force_ttl | 0x80000000
   if 28 - 28: iIii1I11I1II1 % OOooOOo * I1IiiI
   if 28 - 28: O0 . OoOoOO00
   if 27 - 27: I1ii11iIi11i / II111iiii + O0 % I1ii11iIi11i
   if 72 - 72: I1IiiI - i1IIi
   if 11 - 11: iIii1I11I1II1 . OoO0O00 * Ii1I
  lisp_send_negative_map_reply ( lisp_sockets , iiI1I1IIi , OOo0oOOO0 , o0OOO , o00O00oOO00 ,
 mr_sport , Oo0o0 , IIiiII11i11I , I1IIiI )
  if 65 - 65: Oo0Ooo / OoooooooOO
  return ( [ iiI1I1IIi , OOo0oOOO0 , LISP_DDT_ACTION_MS_NOT_REG ] )
  if 60 - 60: II111iiii + I1IiiI % oO0o - o0oOOo0O0Ooo
  if 50 - 50: iIii1I11I1II1 - i11iIiiIii / iII111i + ooOoO0o / OOooOOo
  if 80 - 80: IiII / OoooooooOO
  if 69 - 69: OoOoOO00 + IiII
  if 18 - 18: O0 / I11i
 i1iII1Iiii1ii = False
 iIii1II11I = ""
 oo0O0oOO0ooO = False
 if ( oOoooo . force_nat_proxy_reply ) :
  iIii1II11I = ", nat-forced"
  i1iII1Iiii1ii = True
  oo0O0oOO0ooO = True
 elif ( oOoooo . force_proxy_reply ) :
  iIii1II11I = ", forced"
  oo0O0oOO0ooO = True
 elif ( oOoooo . proxy_reply_requested ) :
  iIii1II11I = ", requested"
  oo0O0oOO0ooO = True
 elif ( map_request . pitr_bit and oOoooo . pitr_proxy_reply_drop ) :
  iIii1II11I = ", drop-to-pitr"
  iI1IIi1I = LISP_DROP_ACTION
 elif ( oOoooo . proxy_reply_action != "" ) :
  iI1IIi1I = oOoooo . proxy_reply_action
  iIii1II11I = ", forced, action {}" . format ( iI1IIi1I )
  iI1IIi1I = LISP_DROP_ACTION if ( iI1IIi1I == "drop" ) else LISP_NATIVE_FORWARD_ACTION
  if 11 - 11: iIii1I11I1II1 / O0 * I1Ii111 . OoooooooOO % OoooooooOO * I1Ii111
  if 63 - 63: IiII * oO0o * iIii1I11I1II1
  if 18 - 18: II111iiii * o0oOOo0O0Ooo % i11iIiiIii . OoOoOO00
  if 40 - 40: oO0o - o0oOOo0O0Ooo * II111iiii
  if 4 - 4: O0
  if 9 - 9: Oo0Ooo . i1IIi - i1IIi + I1Ii111 * ooOoO0o . I1ii11iIi11i
  if 17 - 17: I11i * I1ii11iIi11i % I1IiiI + OoO0O00 + IiII
 OooOOOOOO = False
 oO0oOoo = None
 if ( oo0O0oOO0ooO and lisp_policies . has_key ( oOoooo . policy ) ) :
  IiI1i1i1 = lisp_policies [ oOoooo . policy ]
  if ( IiI1i1i1 . match_policy_map_request ( map_request , mr_source ) ) : oO0oOoo = IiI1i1i1
  if 68 - 68: i11iIiiIii
  if ( oO0oOoo ) :
   iI1oOoo = bold ( "matched" , False )
   lprint ( "Map-Request {} policy '{}', set-action '{}'" . format ( iI1oOoo ,
 IiI1i1i1 . policy_name , IiI1i1i1 . set_action ) )
  else :
   iI1oOoo = bold ( "no match" , False )
   lprint ( "Map-Request {} for policy '{}', implied drop" . format ( iI1oOoo ,
 IiI1i1i1 . policy_name ) )
   OooOOOOOO = True
   if 29 - 29: ooOoO0o - iII111i + IiII % Ii1I - oO0o - ooOoO0o
   if 43 - 43: oO0o
   if 22 - 22: I1Ii111 + i11iIiiIii
 if ( iIii1II11I != "" ) :
  lprint ( "Proxy-replying for EID {}, found site '{}' EID-prefix {}{}" . format ( green ( Ii1i1 , False ) , OOOO0OOo0oOoo , green ( iIIiIIiII111 , False ) ,
  # Ii1I * O0 . II111iiii
 iIii1II11I ) )
  if 39 - 39: iII111i + iIii1I11I1II1 / Ii1I . IiII
  OoO0oOOooOO = oOoooo . registered_rlocs
  Oo0o0 = 1440
  if ( i1iII1Iiii1ii ) :
   if ( oOoooo . site_id != 0 ) :
    i1IiIiii = map_request . source_eid
    OoO0oOOooOO = lisp_get_private_rloc_set ( oOoooo , i1IiIiii , OOo0oOOO0 )
    if 25 - 25: I1Ii111 % iII111i / OoO0O00 % Oo0Ooo % Ii1I
   if ( OoO0oOOooOO == oOoooo . registered_rlocs ) :
    ii11I1iiii1I = ( oOoooo . group . is_null ( ) == False )
    OOO = lisp_get_partial_rloc_set ( OoO0oOOooOO , ooOo , ii11I1iiii1I )
    if ( OOO != OoO0oOOooOO ) :
     Oo0o0 = 15
     OoO0oOOooOO = OOO
     if 30 - 30: oO0o - OoOoOO00 . I1IiiI
     if 17 - 17: OoOoOO00
     if 76 - 76: I1ii11iIi11i - ooOoO0o % OoooooooOO / Oo0Ooo % IiII / ooOoO0o
     if 57 - 57: O0
     if 23 - 23: OoO0O00 / II111iiii . I1ii11iIi11i . O0
     if 13 - 13: I1ii11iIi11i
     if 32 - 32: OOooOOo / I11i + I1Ii111 / Oo0Ooo * OoooooooOO / II111iiii
     if 8 - 8: OoO0O00
  if ( oOoooo . force_ttl != None ) :
   Oo0o0 = oOoooo . force_ttl | 0x80000000
   if 17 - 17: iIii1I11I1II1 - Oo0Ooo
   if 25 - 25: O0 + I1ii11iIi11i
   if 53 - 53: OoooooooOO . Oo0Ooo
   if 35 - 35: OOooOOo % i11iIiiIii % ooOoO0o . O0
   if 9 - 9: ooOoO0o + iII111i / i1IIi % Oo0Ooo - o0oOOo0O0Ooo / I1IiiI
   if 42 - 42: OOooOOo + oO0o % O0 * I1ii11iIi11i + i11iIiiIii
  if ( oO0oOoo ) :
   if ( oO0oOoo . set_record_ttl ) :
    Oo0o0 = oO0oOoo . set_record_ttl
    lprint ( "Policy set-record-ttl to {}" . format ( Oo0o0 ) )
    if 16 - 16: i1IIi . I11i + OoO0O00 % Ii1I * IiII + I1IiiI
   if ( oO0oOoo . set_action == "drop" ) :
    lprint ( "Policy set-action drop, send negative Map-Reply" )
    iI1IIi1I = LISP_POLICY_DENIED_ACTION
    OoO0oOOooOO = [ ]
   else :
    I1II = oO0oOoo . set_policy_map_reply ( )
    if ( I1II ) : OoO0oOOooOO = [ I1II ]
    if 96 - 96: II111iiii + O0 - II111iiii
    if 97 - 97: I1IiiI
    if 87 - 87: I11i + iIii1I11I1II1
  if ( OooOOOOOO ) :
   lprint ( "Implied drop action, send negative Map-Reply" )
   iI1IIi1I = LISP_POLICY_DENIED_ACTION
   OoO0oOOooOO = [ ]
   if 91 - 91: oO0o
   if 58 - 58: i11iIiiIii / Ii1I - OoooooooOO
  i11 = oOoooo . echo_nonce_capable
  if 25 - 25: i1IIi * ooOoO0o % OOooOOo / I1IiiI
  if 75 - 75: i11iIiiIii
  if 38 - 38: iIii1I11I1II1
  if 80 - 80: OoO0O00
  if ( I1I1Ii1111 ) :
   o0o0Oo00Oo00o = oOoooo . eid
   IIiiiIiIiiii = oOoooo . group
  else :
   o0o0Oo00Oo00o = iiI1I1IIi
   IIiiiIiIiiii = OOo0oOOO0
   iI1IIi1I = LISP_AUTH_FAILURE_ACTION
   OoO0oOOooOO = [ ]
   if 80 - 80: i1IIi - iIii1I11I1II1 + OoooooooOO + ooOoO0o / IiII - I1ii11iIi11i
   if 90 - 90: I1IiiI * ooOoO0o - I11i + O0 - I11i
   if 59 - 59: OOooOOo % II111iiii
   if 30 - 30: i1IIi / I1ii11iIi11i
   if 4 - 4: Oo0Ooo
   if 31 - 31: IiII
  if ( I1IIiI ) :
   o0o0Oo00Oo00o = iiI1I1IIi
   IIiiiIiIiiii = OOo0oOOO0
   if 86 - 86: Oo0Ooo + IiII / o0oOOo0O0Ooo % OoOoOO00
   if 49 - 49: iIii1I11I1II1 % Oo0Ooo % I11i * Ii1I - OoO0O00
   if 15 - 15: i11iIiiIii + o0oOOo0O0Ooo . Ii1I . I1IiiI
   if 8 - 8: iII111i % II111iiii + IiII
   if 5 - 5: i1IIi + II111iiii
   if 75 - 75: OOooOOo . IiII . I1IiiI + OoooooooOO
  packet = lisp_build_map_reply ( o0o0Oo00Oo00o , IIiiiIiIiiii , OoO0oOOooOO ,
 o0OOO , iI1IIi1I , Oo0o0 , map_request , None , i11 , False )
  if 35 - 35: I11i % i1IIi - I1ii11iIi11i . Oo0Ooo
  if ( I1IIiI ) :
   lisp_process_pubsub ( lisp_sockets , packet , o0o0Oo00Oo00o , o00O00oOO00 ,
 mr_sport , o0OOO , Oo0o0 , IIiiII11i11I )
  else :
   lisp_send_map_reply ( lisp_sockets , packet , o00O00oOO00 , mr_sport )
   if 69 - 69: ooOoO0o * OoO0O00 % o0oOOo0O0Ooo * o0oOOo0O0Ooo
   if 35 - 35: I1IiiI . OOooOOo * OoO0O00 . I1ii11iIi11i - I1IiiI
  return ( [ oOoooo . eid , oOoooo . group , LISP_DDT_ACTION_MS_ACK ] )
  if 5 - 5: i1IIi * II111iiii
  if 64 - 64: I1IiiI * iIii1I11I1II1 % I1Ii111
  if 22 - 22: OoooooooOO + I1Ii111 . o0oOOo0O0Ooo * Oo0Ooo
  if 61 - 61: iIii1I11I1II1
  if 95 - 95: I1ii11iIi11i + IiII * Ii1I - IiII
 O0OOo0 = len ( oOoooo . registered_rlocs )
 if ( O0OOo0 == 0 ) :
  lprint ( "Requested EID {} found site '{}' with EID-prefix {} with " + "no registered RLOCs" . format ( green ( Ii1i1 , False ) , OOOO0OOo0oOoo ,
  # o0oOOo0O0Ooo - iII111i - ooOoO0o - I11i
 green ( iIIiIIiII111 , False ) ) )
  return ( [ oOoooo . eid , oOoooo . group , LISP_DDT_ACTION_MS_ACK ] )
  if 9 - 9: I1IiiI / O0 + I11i
  if 39 - 39: OoooooooOO * I1ii11iIi11i + II111iiii . I1Ii111 / II111iiii . I1ii11iIi11i
  if 72 - 72: OoOoOO00
  if 21 - 21: oO0o
  if 58 - 58: OoOoOO00 + i11iIiiIii % OOooOOo - i1IIi
 iiI = map_request . target_eid if map_request . source_eid . is_null ( ) else map_request . source_eid
 if 35 - 35: Oo0Ooo - Oo0Ooo + I11i
 I1iI1111ii1I1 = map_request . target_eid . hash_address ( iiI )
 I1iI1111ii1I1 %= O0OOo0
 Ii111 = oOoooo . registered_rlocs [ I1iI1111ii1I1 ]
 if 71 - 71: OoOoOO00 % i11iIiiIii
 if ( Ii111 . rloc . is_null ( ) ) :
  lprint ( ( "Suppress forwarding Map-Request for EID {} at site '{}' " + "EID-prefix {}, no RLOC address" ) . format ( green ( Ii1i1 , False ) ,
  # o0oOOo0O0Ooo / I1IiiI % Oo0Ooo % I1IiiI % OOooOOo
 OOOO0OOo0oOoo , green ( iIIiIIiII111 , False ) ) )
 else :
  lprint ( ( "Forwarding Map-Request for EID {} to ETR {} at site '{}' " + "EID-prefix {}" ) . format ( green ( Ii1i1 , False ) ,
  # OoO0O00 + iIii1I11I1II1
 red ( Ii111 . rloc . print_address ( ) , False ) , OOOO0OOo0oOoo ,
 green ( iIIiIIiII111 , False ) ) )
  if 52 - 52: i1IIi . i11iIiiIii * IiII * I11i % I1IiiI
  if 67 - 67: O0 . I1Ii111 + ooOoO0o
  if 88 - 88: I1Ii111 . O0 - oO0o + i1IIi % Oo0Ooo
  if 39 - 39: I1Ii111 - I1IiiI
  lisp_send_ecm ( lisp_sockets , packet , map_request . source_eid , mr_sport ,
 map_request . target_eid , Ii111 . rloc , to_etr = True )
  if 18 - 18: i1IIi
 return ( [ oOoooo . eid , oOoooo . group , LISP_DDT_ACTION_MS_ACK ] )
 if 42 - 42: II111iiii - i1IIi . oO0o % OOooOOo % ooOoO0o - i11iIiiIii
 if 23 - 23: OOooOOo + iIii1I11I1II1 - i1IIi
 if 72 - 72: OOooOOo . I1IiiI * O0 + i11iIiiIii - iII111i
 if 79 - 79: o0oOOo0O0Ooo + I1ii11iIi11i
 if 46 - 46: I11i
 if 78 - 78: IiII / II111iiii
 if 55 - 55: Oo0Ooo
def lisp_ddt_process_map_request ( lisp_sockets , map_request , ecm_source , port ) :
 if 80 - 80: o0oOOo0O0Ooo - I1Ii111 * O0 * iIii1I11I1II1
 if 59 - 59: I1ii11iIi11i + I11i / OoO0O00
 if 36 - 36: o0oOOo0O0Ooo + ooOoO0o * I11i
 if 81 - 81: OOooOOo * I11i - I1ii11iIi11i
 iiI1I1IIi = map_request . target_eid
 OOo0oOOO0 = map_request . target_group
 Ii1i1 = lisp_print_eid_tuple ( iiI1I1IIi , OOo0oOOO0 )
 o0OOO = map_request . nonce
 iI1IIi1I = LISP_DDT_ACTION_NULL
 if 82 - 82: I1ii11iIi11i * II111iiii - OoooooooOO % iII111i * I1IiiI % OoOoOO00
 if 81 - 81: I11i + o0oOOo0O0Ooo / iII111i
 if 35 - 35: ooOoO0o % I11i * I1ii11iIi11i
 if 10 - 10: OoO0O00 + OoooooooOO + I1Ii111
 if 57 - 57: Ii1I % Ii1I * Oo0Ooo % i11iIiiIii
 IIi = None
 if ( lisp_i_am_ms ) :
  oOoooo = lisp_site_eid_lookup ( iiI1I1IIi , OOo0oOOO0 , False )
  if ( oOoooo == None ) : return
  if 39 - 39: i1IIi / o0oOOo0O0Ooo . ooOoO0o - OoO0O00
  if ( oOoooo . registered ) :
   iI1IIi1I = LISP_DDT_ACTION_MS_ACK
   Oo0o0 = 1440
  else :
   iiI1I1IIi , OOo0oOOO0 , iI1IIi1I = lisp_ms_compute_neg_prefix ( iiI1I1IIi , OOo0oOOO0 )
   iI1IIi1I = LISP_DDT_ACTION_MS_NOT_REG
   Oo0o0 = 1
   if 1 - 1: I1Ii111
 else :
  IIi = lisp_ddt_cache_lookup ( iiI1I1IIi , OOo0oOOO0 , False )
  if ( IIi == None ) :
   iI1IIi1I = LISP_DDT_ACTION_NOT_AUTH
   Oo0o0 = 0
   lprint ( "DDT delegation entry not found for EID {}" . format ( green ( Ii1i1 , False ) ) )
   if 91 - 91: I1ii11iIi11i % I1Ii111 - Ii1I . OoO0O00 - OoO0O00 * i1IIi
  elif ( IIi . is_auth_prefix ( ) ) :
   if 17 - 17: oO0o
   if 23 - 23: ooOoO0o - OoO0O00 + oO0o . OOooOOo - I1IiiI
   if 66 - 66: iII111i % iII111i
   if 59 - 59: II111iiii . i1IIi % i1IIi
   iI1IIi1I = LISP_DDT_ACTION_DELEGATION_HOLE
   Oo0o0 = 15
   I1oOO0oO0 = IIi . print_eid_tuple ( )
   lprint ( ( "DDT delegation entry not found but auth-prefix {} " + "found for EID {}" ) . format ( I1oOO0oO0 ,
   # o0oOOo0O0Ooo - OoooooooOO . O0 / ooOoO0o
 green ( Ii1i1 , False ) ) )
   if 81 - 81: iIii1I11I1II1 * OoOoOO00 / o0oOOo0O0Ooo
   if ( OOo0oOOO0 . is_null ( ) ) :
    iiI1I1IIi = lisp_ddt_compute_neg_prefix ( iiI1I1IIi , IIi ,
 lisp_ddt_cache )
   else :
    OOo0oOOO0 = lisp_ddt_compute_neg_prefix ( OOo0oOOO0 , IIi ,
 lisp_ddt_cache )
    iiI1I1IIi = lisp_ddt_compute_neg_prefix ( iiI1I1IIi , IIi ,
 IIi . source_cache )
    if 5 - 5: I1IiiI
   IIi = None
  else :
   I1oOO0oO0 = IIi . print_eid_tuple ( )
   lprint ( "DDT delegation entry {} found for EID {}" . format ( I1oOO0oO0 , green ( Ii1i1 , False ) ) )
   if 6 - 6: O0
   Oo0o0 = 1440
   if 30 - 30: I1IiiI
   if 79 - 79: i11iIiiIii . OOooOOo * I1Ii111 * o0oOOo0O0Ooo + I1Ii111
   if 26 - 26: i1IIi % OoOoOO00 / i1IIi
   if 41 - 41: oO0o % oO0o . iIii1I11I1II1 . o0oOOo0O0Ooo
   if 95 - 95: i1IIi . ooOoO0o . Oo0Ooo
   if 13 - 13: OOooOOo - Oo0Ooo % O0 . I1Ii111
 IiiiIi1iiii11 = lisp_build_map_referral ( iiI1I1IIi , OOo0oOOO0 , IIi , iI1IIi1I , Oo0o0 , o0OOO )
 o0OOO = map_request . nonce >> 32
 if ( map_request . nonce != 0 and o0OOO != 0xdfdf0e1d ) : port = LISP_CTRL_PORT
 lisp_send_map_referral ( lisp_sockets , IiiiIi1iiii11 , ecm_source , port )
 return
 if 66 - 66: I1IiiI + I11i
 if 58 - 58: I1ii11iIi11i
 if 7 - 7: oO0o - I11i
 if 59 - 59: Ii1I / o0oOOo0O0Ooo / OoO0O00 + IiII + i11iIiiIii
 if 64 - 64: o0oOOo0O0Ooo * IiII * IiII * iII111i % i11iIiiIii
 if 22 - 22: I1ii11iIi11i * II111iiii - OOooOOo % i11iIiiIii
 if 10 - 10: OOooOOo / I1ii11iIi11i
 if 21 - 21: OoO0O00 % Oo0Ooo . o0oOOo0O0Ooo + IiII
 if 48 - 48: O0 / i1IIi / iII111i
 if 11 - 11: O0 - OoO0O00 + OoOoOO00 * ooOoO0o - Ii1I
 if 82 - 82: Ii1I - O0 * ooOoO0o . ooOoO0o
 if 32 - 32: o0oOOo0O0Ooo . OoooooooOO % OOooOOo
 if 2 - 2: OoOoOO00 + I1ii11iIi11i + oO0o
def lisp_find_negative_mask_len ( eid , entry_prefix , neg_prefix ) :
 Iii1IiIII = eid . hash_address ( entry_prefix )
 O0o = eid . addr_length ( ) * 8
 oO00OO0Ooo00O = 0
 if 46 - 46: I11i + II111iiii * iII111i % ooOoO0o - I1IiiI
 if 73 - 73: I1ii11iIi11i * iIii1I11I1II1 . I1Ii111 - Ii1I
 if 11 - 11: I11i
 if 48 - 48: IiII / O0
 for oO00OO0Ooo00O in range ( O0o ) :
  i1IiI11 = 1 << ( O0o - oO00OO0Ooo00O - 1 )
  if ( Iii1IiIII & i1IiI11 ) : break
  if 1 - 1: I11i / IiII * OoO0O00 / I11i
  if 18 - 18: OoO0O00 - oO0o / I11i
 if ( oO00OO0Ooo00O > neg_prefix . mask_len ) : neg_prefix . mask_len = oO00OO0Ooo00O
 return
 if 90 - 90: IiII % I1ii11iIi11i % i1IIi
 if 63 - 63: Ii1I . I1IiiI + IiII / OoOoOO00 + ooOoO0o - iIii1I11I1II1
 if 20 - 20: i1IIi % II111iiii . IiII % iIii1I11I1II1
 if 9 - 9: o0oOOo0O0Ooo
 if 68 - 68: OOooOOo % Oo0Ooo * ooOoO0o * OoO0O00 / iII111i
 if 96 - 96: i11iIiiIii - I1IiiI % OoOoOO00 * Ii1I % OoO0O00 % O0
 if 100 - 100: oO0o . OoooooooOO
 if 58 - 58: I11i % OoooooooOO
 if 97 - 97: OOooOOo - IiII
 if 77 - 77: i1IIi / IiII - o0oOOo0O0Ooo . Oo0Ooo / o0oOOo0O0Ooo . OoooooooOO
def lisp_neg_prefix_walk ( entry , parms ) :
 iiI1I1IIi , Oooo0Ooo0OOo0 , oO00Oo0O0Ooo0 = parms
 if 37 - 37: o0oOOo0O0Ooo / I1IiiI * oO0o / II111iiii
 if ( Oooo0Ooo0OOo0 == None ) :
  if ( entry . eid . instance_id != iiI1I1IIi . instance_id ) :
   return ( [ True , parms ] )
   if 39 - 39: IiII - i1IIi - IiII - OoooooooOO - I1ii11iIi11i
  if ( entry . eid . afi != iiI1I1IIi . afi ) : return ( [ True , parms ] )
 else :
  if ( entry . eid . is_more_specific ( Oooo0Ooo0OOo0 ) == False ) :
   return ( [ True , parms ] )
   if 66 - 66: IiII + i1IIi
   if 21 - 21: IiII / i11iIiiIii / OoOoOO00
   if 75 - 75: Ii1I . i1IIi / I1IiiI * iII111i . IiII / OoOoOO00
   if 58 - 58: ooOoO0o + OOooOOo / ooOoO0o / i11iIiiIii
   if 95 - 95: ooOoO0o
   if 10 - 10: OoO0O00 % ooOoO0o * o0oOOo0O0Ooo
 lisp_find_negative_mask_len ( iiI1I1IIi , entry . eid , oO00Oo0O0Ooo0 )
 return ( [ True , parms ] )
 if 37 - 37: Ii1I . o0oOOo0O0Ooo
 if 34 - 34: ooOoO0o * IiII . Ii1I + iIii1I11I1II1
 if 1 - 1: i11iIiiIii + I11i
 if 78 - 78: Ii1I % Oo0Ooo / OoO0O00 . iIii1I11I1II1 . II111iiii
 if 67 - 67: oO0o % I1Ii111
 if 72 - 72: I1IiiI . i11iIiiIii . OoOoOO00 + I1IiiI - I1Ii111 + iII111i
 if 15 - 15: I1IiiI
 if 88 - 88: IiII / I1ii11iIi11i % I11i + i11iIiiIii * O0 . I1Ii111
def lisp_ddt_compute_neg_prefix ( eid , ddt_entry , cache ) :
 if 69 - 69: Oo0Ooo - OOooOOo / I1IiiI . i11iIiiIii * OoO0O00
 if 45 - 45: I1Ii111 + OOooOOo
 if 78 - 78: OoOoOO00 . Oo0Ooo % I11i
 if 7 - 7: I1ii11iIi11i % Ii1I . OoooooooOO - iII111i
 if ( eid . is_binary ( ) == False ) : return ( eid )
 if 18 - 18: O0 * OoooooooOO % IiII - iIii1I11I1II1 % IiII * o0oOOo0O0Ooo
 oO00Oo0O0Ooo0 = lisp_address ( eid . afi , "" , 0 , 0 )
 oO00Oo0O0Ooo0 . copy_address ( eid )
 oO00Oo0O0Ooo0 . mask_len = 0
 if 13 - 13: OoO0O00 + i11iIiiIii + O0 / ooOoO0o % iIii1I11I1II1
 OOoo = ddt_entry . print_eid_tuple ( )
 Oooo0Ooo0OOo0 = ddt_entry . eid
 if 97 - 97: I11i + II111iiii / OoooooooOO + I1ii11iIi11i * o0oOOo0O0Ooo
 if 29 - 29: I1Ii111
 if 95 - 95: OoOoOO00 * II111iiii + I1ii11iIi11i - I11i . I11i % i11iIiiIii
 if 23 - 23: OoO0O00
 if 26 - 26: I1ii11iIi11i
 eid , Oooo0Ooo0OOo0 , oO00Oo0O0Ooo0 = cache . walk_cache ( lisp_neg_prefix_walk ,
 ( eid , Oooo0Ooo0OOo0 , oO00Oo0O0Ooo0 ) )
 if 66 - 66: i11iIiiIii - i11iIiiIii / Ii1I * OOooOOo / IiII
 if 67 - 67: I1IiiI . I1Ii111 - OoOoOO00
 if 18 - 18: O0
 if 26 - 26: i1IIi - iIii1I11I1II1
 oO00Oo0O0Ooo0 . mask_address ( oO00Oo0O0Ooo0 . mask_len )
 if 8 - 8: I1Ii111
 lprint ( ( "Least specific prefix computed from ddt-cache for EID {} " + "using auth-prefix {} is {}" ) . format ( green ( eid . print_address ( ) , False ) ,
 # i1IIi . Oo0Ooo / o0oOOo0O0Ooo % I1Ii111 / OOooOOo + OoOoOO00
 OOoo , oO00Oo0O0Ooo0 . print_prefix ( ) ) )
 return ( oO00Oo0O0Ooo0 )
 if 21 - 21: Oo0Ooo / Oo0Ooo
 if 1 - 1: Oo0Ooo
 if 73 - 73: Ii1I * iIii1I11I1II1 / o0oOOo0O0Ooo - o0oOOo0O0Ooo / i1IIi
 if 64 - 64: Ii1I * I1ii11iIi11i % II111iiii
 if 31 - 31: iIii1I11I1II1 % Oo0Ooo . I1IiiI % ooOoO0o
 if 38 - 38: I1ii11iIi11i + I1Ii111 * I11i / OoO0O00 + o0oOOo0O0Ooo
 if 46 - 46: iII111i
 if 56 - 56: Oo0Ooo / II111iiii
def lisp_ms_compute_neg_prefix ( eid , group ) :
 oO00Oo0O0Ooo0 = lisp_address ( eid . afi , "" , 0 , 0 )
 oO00Oo0O0Ooo0 . copy_address ( eid )
 oO00Oo0O0Ooo0 . mask_len = 0
 O0ooO0oO = lisp_address ( group . afi , "" , 0 , 0 )
 O0ooO0oO . copy_address ( group )
 O0ooO0oO . mask_len = 0
 Oooo0Ooo0OOo0 = None
 if 75 - 75: o0oOOo0O0Ooo + I1IiiI - iII111i / IiII * IiII / O0
 if 26 - 26: I11i + I1IiiI + i1IIi % OoO0O00 * OoOoOO00
 if 28 - 28: I1ii11iIi11i - o0oOOo0O0Ooo + Oo0Ooo - Ii1I
 if 98 - 98: OoOoOO00 + O0 - I1Ii111
 if 67 - 67: I1IiiI / IiII / iII111i - I1Ii111 - o0oOOo0O0Ooo
 if ( group . is_null ( ) ) :
  IIi = lisp_ddt_cache . lookup_cache ( eid , False )
  if ( IIi == None ) :
   oO00Oo0O0Ooo0 . mask_len = oO00Oo0O0Ooo0 . host_mask_len ( )
   O0ooO0oO . mask_len = O0ooO0oO . host_mask_len ( )
   return ( [ oO00Oo0O0Ooo0 , O0ooO0oO , LISP_DDT_ACTION_NOT_AUTH ] )
   if 75 - 75: OOooOOo . ooOoO0o
  IiI1i = lisp_sites_by_eid
  if ( IIi . is_auth_prefix ( ) ) : Oooo0Ooo0OOo0 = IIi . eid
 else :
  IIi = lisp_ddt_cache . lookup_cache ( group , False )
  if ( IIi == None ) :
   oO00Oo0O0Ooo0 . mask_len = oO00Oo0O0Ooo0 . host_mask_len ( )
   O0ooO0oO . mask_len = O0ooO0oO . host_mask_len ( )
   return ( [ oO00Oo0O0Ooo0 , O0ooO0oO , LISP_DDT_ACTION_NOT_AUTH ] )
   if 11 - 11: o0oOOo0O0Ooo - iII111i - OoO0O00 % I1ii11iIi11i * Oo0Ooo
  if ( IIi . is_auth_prefix ( ) ) : Oooo0Ooo0OOo0 = IIi . group
  if 51 - 51: I1IiiI + O0
  group , Oooo0Ooo0OOo0 , O0ooO0oO = lisp_sites_by_eid . walk_cache ( lisp_neg_prefix_walk , ( group , Oooo0Ooo0OOo0 , O0ooO0oO ) )
  if 4 - 4: ooOoO0o / OoO0O00 * iIii1I11I1II1 * iIii1I11I1II1
  if 33 - 33: iII111i . iIii1I11I1II1 - Ii1I
  O0ooO0oO . mask_address ( O0ooO0oO . mask_len )
  if 85 - 85: OoOoOO00
  lprint ( ( "Least specific prefix computed from site-cache for " + "group EID {} using auth-prefix {} is {}" ) . format ( group . print_address ( ) , Oooo0Ooo0OOo0 . print_prefix ( ) if ( Oooo0Ooo0OOo0 != None ) else "'not found'" ,
  # o0oOOo0O0Ooo - oO0o + ooOoO0o / I1ii11iIi11i
  # oO0o + I11i / ooOoO0o + Ii1I
  # I11i / Ii1I . IiII / o0oOOo0O0Ooo / OoO0O00 + OoOoOO00
 O0ooO0oO . print_prefix ( ) ) )
  if 50 - 50: Ii1I
  IiI1i = IIi . source_cache
  if 84 - 84: iII111i % II111iiii
  if 31 - 31: I11i
  if 28 - 28: i11iIiiIii + IiII / I11i . Ii1I / OoO0O00
  if 100 - 100: o0oOOo0O0Ooo - I11i . o0oOOo0O0Ooo
  if 90 - 90: OoOoOO00 / II111iiii / I11i * I11i - iIii1I11I1II1
 iI1IIi1I = LISP_DDT_ACTION_DELEGATION_HOLE if ( Oooo0Ooo0OOo0 != None ) else LISP_DDT_ACTION_NOT_AUTH
 if 87 - 87: IiII
 if 92 - 92: OoO0O00 / IiII - ooOoO0o
 if 45 - 45: iII111i - I11i * ooOoO0o * OOooOOo / I1Ii111 * iII111i
 if 33 - 33: iIii1I11I1II1 % I1ii11iIi11i - OOooOOo % iIii1I11I1II1 + I11i / i11iIiiIii
 if 64 - 64: I11i * ooOoO0o / OoooooooOO
 if 38 - 38: iIii1I11I1II1 . OoO0O00 * OoOoOO00 + OoOoOO00 + ooOoO0o
 eid , Oooo0Ooo0OOo0 , oO00Oo0O0Ooo0 = IiI1i . walk_cache ( lisp_neg_prefix_walk ,
 ( eid , Oooo0Ooo0OOo0 , oO00Oo0O0Ooo0 ) )
 if 44 - 44: I1ii11iIi11i * OOooOOo % OoO0O00 . I1IiiI % Ii1I + II111iiii
 if 100 - 100: oO0o - II111iiii . o0oOOo0O0Ooo
 if 63 - 63: OoOoOO00 % IiII . iII111i
 if 44 - 44: I1IiiI
 oO00Oo0O0Ooo0 . mask_address ( oO00Oo0O0Ooo0 . mask_len )
 if 25 - 25: oO0o
 lprint ( ( "Least specific prefix computed from site-cache for EID {} " + "using auth-prefix {} is {}" ) . format ( green ( eid . print_address ( ) , False ) ,
 # I1IiiI - OoO0O00 / iIii1I11I1II1 * iII111i + OoOoOO00 + IiII
 # OOooOOo
 Oooo0Ooo0OOo0 . print_prefix ( ) if ( Oooo0Ooo0OOo0 != None ) else "'not found'" , oO00Oo0O0Ooo0 . print_prefix ( ) ) )
 if 69 - 69: OOooOOo . I11i . I11i
 if 4 - 4: O0 + I11i / OoOoOO00 * iIii1I11I1II1 . Ii1I
 return ( [ oO00Oo0O0Ooo0 , O0ooO0oO , iI1IIi1I ] )
 if 68 - 68: Oo0Ooo % ooOoO0o + i11iIiiIii / oO0o / II111iiii
 if 63 - 63: OoO0O00 % i1IIi - OoooooooOO / ooOoO0o
 if 75 - 75: OOooOOo + IiII + ooOoO0o / I1IiiI . iIii1I11I1II1 / Oo0Ooo
 if 81 - 81: I1Ii111 % II111iiii - Oo0Ooo / I1IiiI + i11iIiiIii . I11i
 if 67 - 67: ooOoO0o . I1Ii111 . Oo0Ooo . Ii1I + iIii1I11I1II1 / OoooooooOO
 if 93 - 93: ooOoO0o * OoO0O00 - I1Ii111 / I1ii11iIi11i
 if 60 - 60: OoO0O00 / oO0o . I1IiiI + OoOoOO00 + I1ii11iIi11i % Ii1I
 if 70 - 70: i1IIi * II111iiii * I1IiiI
def lisp_ms_send_map_referral ( lisp_sockets , map_request , ecm_source , port ,
 action , eid_prefix , group_prefix ) :
 if 7 - 7: OoooooooOO + II111iiii % o0oOOo0O0Ooo * O0 . OoO0O00 * OoooooooOO
 iiI1I1IIi = map_request . target_eid
 OOo0oOOO0 = map_request . target_group
 o0OOO = map_request . nonce
 if 20 - 20: Oo0Ooo % OOooOOo
 if ( action == LISP_DDT_ACTION_MS_ACK ) : Oo0o0 = 1440
 if 8 - 8: OOooOOo
 if 92 - 92: iII111i / OOooOOo . IiII / I11i + o0oOOo0O0Ooo
 if 99 - 99: II111iiii
 if 70 - 70: O0 % I1ii11iIi11i
 oooOOo00oOOo = lisp_map_referral ( )
 oooOOo00oOOo . record_count = 1
 oooOOo00oOOo . nonce = o0OOO
 IiiiIi1iiii11 = oooOOo00oOOo . encode ( )
 oooOOo00oOOo . print_map_referral ( )
 if 28 - 28: IiII - i1IIi - I1Ii111 % Ii1I - IiII
 Oo00OoooO0o = False
 if 73 - 73: iIii1I11I1II1 . iIii1I11I1II1 + oO0o % i11iIiiIii . IiII
 if 33 - 33: IiII - OOooOOo / i11iIiiIii * iIii1I11I1II1
 if 2 - 2: i11iIiiIii % ooOoO0o
 if 56 - 56: IiII % ooOoO0o + I1IiiI % I11i - OOooOOo
 if 82 - 82: OoooooooOO . i1IIi . OoO0O00 . OoO0O00
 if 31 - 31: iIii1I11I1II1
 if ( action == LISP_DDT_ACTION_SITE_NOT_FOUND ) :
  eid_prefix , group_prefix , action = lisp_ms_compute_neg_prefix ( iiI1I1IIi ,
 OOo0oOOO0 )
  Oo0o0 = 15
  if 64 - 64: ooOoO0o
 if ( action == LISP_DDT_ACTION_MS_NOT_REG ) : Oo0o0 = 1
 if ( action == LISP_DDT_ACTION_MS_ACK ) : Oo0o0 = 1440
 if ( action == LISP_DDT_ACTION_DELEGATION_HOLE ) : Oo0o0 = 15
 if ( action == LISP_DDT_ACTION_NOT_AUTH ) : Oo0o0 = 0
 if 30 - 30: OoO0O00 + o0oOOo0O0Ooo / iIii1I11I1II1
 O0OoO0O0 = False
 O0OOo0 = 0
 IIi = lisp_ddt_cache_lookup ( iiI1I1IIi , OOo0oOOO0 , False )
 if ( IIi != None ) :
  O0OOo0 = len ( IIi . delegation_set )
  O0OoO0O0 = IIi . is_ms_peer_entry ( )
  IIi . map_referrals_sent += 1
  if 79 - 79: I11i * I1ii11iIi11i
  if 85 - 85: iIii1I11I1II1 * O0 / iII111i
  if 75 - 75: Oo0Ooo * IiII % Ii1I
  if 40 - 40: o0oOOo0O0Ooo * i11iIiiIii . ooOoO0o
  if 63 - 63: I1Ii111 / Ii1I - iIii1I11I1II1 / i11iIiiIii / IiII + I11i
 if ( action == LISP_DDT_ACTION_NOT_AUTH ) : Oo00OoooO0o = True
 if ( action in ( LISP_DDT_ACTION_MS_REFERRAL , LISP_DDT_ACTION_MS_ACK ) ) :
  Oo00OoooO0o = ( O0OoO0O0 == False )
  if 57 - 57: iIii1I11I1II1 % iIii1I11I1II1
  if 23 - 23: II111iiii . ooOoO0o % I1Ii111
  if 39 - 39: OoooooooOO
  if 10 - 10: Oo0Ooo * iII111i
  if 78 - 78: Oo0Ooo / i11iIiiIii - I1IiiI
 OOOo = lisp_eid_record ( )
 OOOo . rloc_count = O0OOo0
 OOOo . authoritative = True
 OOOo . action = action
 OOOo . ddt_incomplete = Oo00OoooO0o
 OOOo . eid = eid_prefix
 OOOo . group = group_prefix
 OOOo . record_ttl = Oo0o0
 if 51 - 51: ooOoO0o / Oo0Ooo - I1Ii111 - iII111i
 IiiiIi1iiii11 += OOOo . encode ( )
 OOOo . print_record ( "  " , True )
 if 68 - 68: I1ii11iIi11i - iIii1I11I1II1 * OoooooooOO
 if 44 - 44: OoooooooOO + I1Ii111 + OoO0O00
 if 15 - 15: iIii1I11I1II1 % i1IIi + iII111i
 if 48 - 48: o0oOOo0O0Ooo / oO0o
 if ( O0OOo0 != 0 ) :
  for I1I in IIi . delegation_set :
   OOO0Oo = lisp_rloc_record ( )
   OOO0Oo . rloc = I1I . delegate_address
   OOO0Oo . priority = I1I . priority
   OOO0Oo . weight = I1I . weight
   OOO0Oo . mpriority = 255
   OOO0Oo . mweight = 0
   OOO0Oo . reach_bit = True
   IiiiIi1iiii11 += OOO0Oo . encode ( )
   OOO0Oo . print_record ( "    " )
   if 61 - 61: I1IiiI + iII111i * Ii1I % I1Ii111 . Ii1I
   if 83 - 83: i11iIiiIii * OoOoOO00 * i11iIiiIii % II111iiii . i11iIiiIii * I11i
   if 67 - 67: i1IIi / i1IIi + IiII . oO0o
   if 70 - 70: i1IIi . I11i * o0oOOo0O0Ooo . iII111i
   if 75 - 75: oO0o * OoO0O00 * I11i + oO0o + O0 . I1Ii111
   if 8 - 8: I1ii11iIi11i / i1IIi - I1ii11iIi11i + Ii1I + OoO0O00 - I11i
   if 79 - 79: OoooooooOO - I1Ii111 * I1IiiI . I1Ii111 - iIii1I11I1II1
 if ( map_request . nonce != 0 ) : port = LISP_CTRL_PORT
 lisp_send_map_referral ( lisp_sockets , IiiiIi1iiii11 , ecm_source , port )
 return
 if 27 - 27: OoOoOO00 % OoOoOO00 % II111iiii
 if 45 - 45: iIii1I11I1II1 . o0oOOo0O0Ooo % I1IiiI
 if 10 - 10: I1IiiI / i1IIi * o0oOOo0O0Ooo + Oo0Ooo - OoOoOO00 % iII111i
 if 88 - 88: Ii1I % Ii1I
 if 29 - 29: OOooOOo % I1ii11iIi11i
 if 57 - 57: I1ii11iIi11i - OoOoOO00 + IiII
 if 58 - 58: OOooOOo % I1IiiI / oO0o . ooOoO0o . OoO0O00 / IiII
 if 72 - 72: ooOoO0o + ooOoO0o + o0oOOo0O0Ooo - o0oOOo0O0Ooo % Ii1I
def lisp_send_negative_map_reply ( sockets , eid , group , nonce , dest , port , ttl ,
 xtr_id , pubsub ) :
 if 52 - 52: I11i % i1IIi . I1ii11iIi11i
 lprint ( "Build negative Map-Reply EID-prefix {}, nonce 0x{} to ITR {}" . format ( lisp_print_eid_tuple ( eid , group ) , lisp_hex_string ( nonce ) ,
 # oO0o / I1ii11iIi11i * O0 % I11i
 red ( dest . print_address ( ) , False ) ) )
 if 34 - 34: oO0o / O0 * oO0o
 iI1IIi1I = LISP_NATIVE_FORWARD_ACTION if group . is_null ( ) else LISP_DROP_ACTION
 if 47 - 47: iIii1I11I1II1 - o0oOOo0O0Ooo % Ii1I
 if 38 - 38: ooOoO0o / IiII * I1ii11iIi11i % I1ii11iIi11i % oO0o
 if 82 - 82: I1ii11iIi11i . i11iIiiIii - I11i . iII111i / OOooOOo
 if 60 - 60: I1IiiI / I1IiiI / II111iiii
 if 59 - 59: OOooOOo . oO0o + ooOoO0o % o0oOOo0O0Ooo . i11iIiiIii
 if ( lisp_get_eid_hash ( eid ) != None ) :
  iI1IIi1I = LISP_SEND_MAP_REQUEST_ACTION
  if 27 - 27: OoOoOO00 - OoooooooOO / IiII / II111iiii * OOooOOo * ooOoO0o
  if 43 - 43: II111iiii . IiII - I1IiiI * I1ii11iIi11i + OoooooooOO
 IiiiIi1iiii11 = lisp_build_map_reply ( eid , group , [ ] , nonce , iI1IIi1I , ttl , None ,
 None , False , False )
 if 34 - 34: I1Ii111 / i1IIi
 if 95 - 95: OoOoOO00 * OOooOOo
 if 68 - 68: I1Ii111 / iIii1I11I1II1 % Ii1I
 if 77 - 77: i11iIiiIii + i11iIiiIii - I1ii11iIi11i % I1ii11iIi11i
 if ( pubsub ) :
  lisp_process_pubsub ( sockets , IiiiIi1iiii11 , eid , dest , port , nonce , ttl ,
 xtr_id )
 else :
  lisp_send_map_reply ( sockets , IiiiIi1iiii11 , dest , port )
  if 26 - 26: oO0o + OoooooooOO % o0oOOo0O0Ooo
 return
 if 96 - 96: ooOoO0o * OoOoOO00 - II111iiii
 if 40 - 40: oO0o * OOooOOo + Ii1I + I11i * Ii1I + OoooooooOO
 if 77 - 77: OOooOOo + ooOoO0o / O0
 if 16 - 16: ooOoO0o + Oo0Ooo * Oo0Ooo . I11i - IiII
 if 49 - 49: ooOoO0o . Ii1I
 if 75 - 75: OOooOOo / II111iiii - Oo0Ooo + I1Ii111
 if 42 - 42: OoooooooOO * II111iiii + Ii1I % OoO0O00 / I1Ii111
def lisp_retransmit_ddt_map_request ( mr ) :
 I1IIiiiI1I1iiIii = mr . mr_source . print_address ( )
 O0i1111ii1 = mr . print_eid_tuple ( )
 o0OOO = mr . nonce
 if 11 - 11: Ii1I - IiII
 if 20 - 20: I11i % oO0o * Oo0Ooo - I1Ii111 . Ii1I * I1ii11iIi11i
 if 59 - 59: OoOoOO00 + Oo0Ooo . I1ii11iIi11i - Ii1I
 if 48 - 48: I1Ii111 % Ii1I + I1IiiI * OoooooooOO % OoOoOO00 % i11iIiiIii
 if 13 - 13: iII111i % i1IIi
 if ( mr . last_request_sent_to ) :
  I1Ii = mr . last_request_sent_to . print_address ( )
  IiII111IiII1 = lisp_referral_cache_lookup ( mr . last_cached_prefix [ 0 ] ,
 mr . last_cached_prefix [ 1 ] , True )
  if ( IiII111IiII1 and IiII111IiII1 . referral_set . has_key ( I1Ii ) ) :
   IiII111IiII1 . referral_set [ I1Ii ] . no_responses += 1
   if 36 - 36: OoO0O00 . Oo0Ooo * I1ii11iIi11i
   if 16 - 16: IiII + OOooOOo
   if 33 - 33: ooOoO0o . i11iIiiIii + OOooOOo
   if 77 - 77: OoooooooOO * Ii1I * iIii1I11I1II1 + IiII
   if 53 - 53: IiII + I1Ii111 + oO0o
   if 31 - 31: OOooOOo + OoOoOO00 * OOooOOo + OoOoOO00 / o0oOOo0O0Ooo . iIii1I11I1II1
   if 1 - 1: I1Ii111 * i11iIiiIii % I1Ii111 - OoO0O00 + I1Ii111 / Oo0Ooo
 if ( mr . retry_count == LISP_MAX_MAP_NOTIFY_RETRIES ) :
  lprint ( "DDT Map-Request retry limit reached for EID {}, nonce 0x{}" . format ( green ( O0i1111ii1 , False ) , lisp_hex_string ( o0OOO ) ) )
  if 3 - 3: OOooOOo - i11iIiiIii / I1Ii111 . OOooOOo - OoO0O00
  mr . dequeue_map_request ( )
  return
  if 60 - 60: OoOoOO00 / i1IIi . Ii1I - OoO0O00 - OoooooooOO
  if 39 - 39: I1IiiI + i1IIi * OoO0O00 % I11i
 mr . retry_count += 1
 if 41 - 41: I1ii11iIi11i * IiII
 OO0o0OO0 = green ( I1IIiiiI1I1iiIii , False )
 o0 = green ( O0i1111ii1 , False )
 lprint ( "Retransmit DDT {} from {}ITR {} EIDs: {} -> {}, nonce 0x{}" . format ( bold ( "Map-Request" , False ) , "P" if mr . from_pitr else "" ,
 # IiII
 red ( mr . itr . print_address ( ) , False ) , OO0o0OO0 , o0 ,
 lisp_hex_string ( o0OOO ) ) )
 if 70 - 70: iIii1I11I1II1 / I1IiiI * OoOoOO00 / IiII / II111iiii + I1IiiI
 if 33 - 33: oO0o
 if 1 - 1: OoOoOO00 . i11iIiiIii % I1Ii111 + OoooooooOO - Oo0Ooo . I1ii11iIi11i
 if 46 - 46: i11iIiiIii + I11i - iIii1I11I1II1 / OoO0O00 - ooOoO0o / i1IIi
 lisp_send_ddt_map_request ( mr , False )
 if 44 - 44: o0oOOo0O0Ooo + Oo0Ooo
 if 46 - 46: OOooOOo % I1IiiI
 if 66 - 66: iIii1I11I1II1 . o0oOOo0O0Ooo - ooOoO0o
 if 27 - 27: Oo0Ooo - i1IIi * OoooooooOO - OoOoOO00 + OoOoOO00
 mr . retransmit_timer = threading . Timer ( LISP_DDT_MAP_REQUEST_INTERVAL ,
 lisp_retransmit_ddt_map_request , [ mr ] )
 mr . retransmit_timer . start ( )
 return
 if 24 - 24: i1IIi . OoOoOO00 / I1Ii111 + O0
 if 86 - 86: Ii1I * OoOoOO00 % I1ii11iIi11i + OOooOOo
 if 85 - 85: iII111i % i11iIiiIii
 if 78 - 78: i11iIiiIii / I11i / Oo0Ooo + II111iiii - I1ii11iIi11i / I1ii11iIi11i
 if 28 - 28: iIii1I11I1II1 / IiII - iIii1I11I1II1 . i1IIi - O0 * ooOoO0o
 if 41 - 41: Ii1I + IiII
 if 37 - 37: I1Ii111 / o0oOOo0O0Ooo - ooOoO0o - OoooooooOO . I1ii11iIi11i % I1Ii111
 if 53 - 53: I1IiiI % OOooOOo + Ii1I - Ii1I
def lisp_get_referral_node ( referral , source_eid , dest_eid ) :
 if 99 - 99: i1IIi * OoOoOO00 - i1IIi
 if 65 - 65: OoO0O00 / i11iIiiIii + I1ii11iIi11i + OoOoOO00
 if 82 - 82: Ii1I * OOooOOo % ooOoO0o / OoO0O00 - Oo0Ooo . I1Ii111
 if 90 - 90: I11i * i11iIiiIii % i1IIi + I1Ii111 / OoO0O00
 IIiI11 = [ ]
 for iiI111I in referral . referral_set . values ( ) :
  if ( iiI111I . updown == False ) : continue
  if ( len ( IIiI11 ) == 0 or IIiI11 [ 0 ] . priority == iiI111I . priority ) :
   IIiI11 . append ( iiI111I )
  elif ( IIiI11 [ 0 ] . priority > iiI111I . priority ) :
   IIiI11 = [ ]
   IIiI11 . append ( iiI111I )
   if 28 - 28: I11i - iII111i - OOooOOo - ooOoO0o
   if 68 - 68: I11i + Ii1I
   if 70 - 70: I11i + oO0o + o0oOOo0O0Ooo . I1Ii111 * i11iIiiIii
 Ii = len ( IIiI11 )
 if ( Ii == 0 ) : return ( None )
 if 19 - 19: oO0o
 I1iI1111ii1I1 = dest_eid . hash_address ( source_eid )
 I1iI1111ii1I1 = I1iI1111ii1I1 % Ii
 return ( IIiI11 [ I1iI1111ii1I1 ] )
 if 45 - 45: iIii1I11I1II1
 if 11 - 11: OoO0O00 / I1Ii111 . OoOoOO00
 if 95 - 95: I1ii11iIi11i / Ii1I % ooOoO0o . OoooooooOO % OoOoOO00 . OoOoOO00
 if 1 - 1: I1ii11iIi11i % o0oOOo0O0Ooo % i11iIiiIii - OOooOOo - ooOoO0o - OoO0O00
 if 94 - 94: OoO0O00 . Oo0Ooo / OoO0O00 + I1Ii111
 if 48 - 48: I1ii11iIi11i * i1IIi + I1Ii111
 if 80 - 80: I1IiiI % I11i
def lisp_send_ddt_map_request ( mr , send_to_root ) :
 OOOooo0 = mr . lisp_sockets
 o0OOO = mr . nonce
 OooO0OO0 = mr . itr
 OOoOooOoOo = mr . mr_source
 Ii1i1 = mr . print_eid_tuple ( )
 if 36 - 36: o0oOOo0O0Ooo . I1Ii111 . i11iIiiIii
 if 29 - 29: I11i % I1IiiI * i1IIi
 if 41 - 41: OOooOOo
 if 43 - 43: I1IiiI . Oo0Ooo + i1IIi + I11i / OoO0O00
 if 66 - 66: i11iIiiIii
 if ( mr . send_count == 8 ) :
  lprint ( "Giving up on map-request-queue entry {}, nonce 0x{}" . format ( green ( Ii1i1 , False ) , lisp_hex_string ( o0OOO ) ) )
  if 83 - 83: I1Ii111 / iIii1I11I1II1 - oO0o
  mr . dequeue_map_request ( )
  return
  if 3 - 3: OOooOOo - Oo0Ooo * I1IiiI - OoO0O00 / OOooOOo + IiII
  if 83 - 83: i1IIi * i1IIi - II111iiii / OoooooooOO . Ii1I + I1Ii111
  if 10 - 10: I11i
  if 24 - 24: Ii1I
  if 30 - 30: II111iiii / Ii1I - I11i - OoO0O00
  if 25 - 25: I11i % i1IIi / I11i * i11iIiiIii
 if ( send_to_root ) :
  O0O0Oooo0O = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  o0oOoO00 = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  mr . tried_root = True
  lprint ( "Jumping up to root for EID {}" . format ( green ( Ii1i1 , False ) ) )
 else :
  O0O0Oooo0O = mr . eid
  o0oOoO00 = mr . group
  if 97 - 97: iIii1I11I1II1 * i1IIi * II111iiii - OOooOOo - Oo0Ooo - iIii1I11I1II1
  if 26 - 26: ooOoO0o + Oo0Ooo
  if 24 - 24: I1IiiI
  if 43 - 43: OoO0O00
  if 51 - 51: OoooooooOO % IiII % Oo0Ooo
 IiiiiII1i = lisp_referral_cache_lookup ( O0O0Oooo0O , o0oOoO00 , False )
 if ( IiiiiII1i == None ) :
  lprint ( "No referral cache entry found" )
  lisp_send_negative_map_reply ( OOOooo0 , O0O0Oooo0O , o0oOoO00 ,
 o0OOO , OooO0OO0 , mr . sport , 15 , None , False )
  return
  if 91 - 91: I1IiiI . I1Ii111 + II111iiii . Oo0Ooo
  if 95 - 95: iII111i
 oo0oooo00OOO = IiiiiII1i . print_eid_tuple ( )
 lprint ( "Found referral cache entry {}, referral-type: {}" . format ( oo0oooo00OOO ,
 IiiiiII1i . print_referral_type ( ) ) )
 if 80 - 80: ooOoO0o / OOooOOo / Ii1I * i1IIi . I11i
 iiI111I = lisp_get_referral_node ( IiiiiII1i , OOoOooOoOo , mr . eid )
 if ( iiI111I == None ) :
  lprint ( "No reachable referral-nodes found" )
  mr . dequeue_map_request ( )
  lisp_send_negative_map_reply ( OOOooo0 , IiiiiII1i . eid ,
 IiiiiII1i . group , o0OOO , OooO0OO0 , mr . sport , 1 , None , False )
  return
  if 47 - 47: I1ii11iIi11i
  if 49 - 49: OoooooooOO . OoooooooOO - i1IIi
 lprint ( "Send DDT Map-Request to {} {} for EID {}, nonce 0x{}" . format ( iiI111I . referral_address . print_address ( ) ,
 # OoooooooOO / iII111i * OOooOOo
 IiiiiII1i . print_referral_type ( ) , green ( Ii1i1 , False ) ,
 lisp_hex_string ( o0OOO ) ) )
 if 1 - 1: OOooOOo / II111iiii / II111iiii % OoO0O00 % iIii1I11I1II1
 if 36 - 36: I1IiiI / O0
 if 20 - 20: OoooooooOO + o0oOOo0O0Ooo . IiII * O0 + i11iIiiIii
 if 67 - 67: ooOoO0o . Oo0Ooo
 iI = ( IiiiiII1i . referral_type == LISP_DDT_ACTION_MS_REFERRAL or
 IiiiiII1i . referral_type == LISP_DDT_ACTION_MS_ACK )
 lisp_send_ecm ( OOOooo0 , mr . packet , OOoOooOoOo , mr . sport , mr . eid ,
 iiI111I . referral_address , to_ms = iI , ddt = True )
 if 55 - 55: II111iiii - I1Ii111 * OoO0O00 % OoOoOO00
 if 16 - 16: OOooOOo / OoooooooOO
 if 62 - 62: I11i * OoO0O00 / OoooooooOO
 if 25 - 25: OoO0O00
 mr . last_request_sent_to = iiI111I . referral_address
 mr . last_sent = lisp_get_timestamp ( )
 mr . send_count += 1
 iiI111I . map_requests_sent += 1
 return
 if 45 - 45: II111iiii + I1IiiI * o0oOOo0O0Ooo - oO0o . Oo0Ooo / ooOoO0o
 if 65 - 65: OOooOOo / II111iiii * oO0o
 if 20 - 20: OoO0O00
 if 35 - 35: IiII . IiII % II111iiii + ooOoO0o % OOooOOo . i1IIi
 if 65 - 65: i1IIi - OoooooooOO / I1Ii111 + i1IIi % OoOoOO00 . i11iIiiIii
 if 25 - 25: i1IIi
 if 69 - 69: OOooOOo / Ii1I
 if 67 - 67: i11iIiiIii . II111iiii + OoooooooOO % o0oOOo0O0Ooo + IiII * i1IIi
def lisp_mr_process_map_request ( lisp_sockets , packet , map_request , ecm_source ,
 sport , mr_source ) :
 if 53 - 53: oO0o * OoooooooOO + II111iiii . IiII * I1ii11iIi11i
 iiI1I1IIi = map_request . target_eid
 OOo0oOOO0 = map_request . target_group
 O0i1111ii1 = map_request . print_eid_tuple ( )
 I1IIiiiI1I1iiIii = mr_source . print_address ( )
 o0OOO = map_request . nonce
 if 55 - 55: OoOoOO00
 OO0o0OO0 = green ( I1IIiiiI1I1iiIii , False )
 o0 = green ( O0i1111ii1 , False )
 lprint ( "Received Map-Request from {}ITR {} EIDs: {} -> {}, nonce 0x{}" . format ( "P" if map_request . pitr_bit else "" ,
 # I1IiiI . iII111i
 red ( ecm_source . print_address ( ) , False ) , OO0o0OO0 , o0 ,
 lisp_hex_string ( o0OOO ) ) )
 if 3 - 3: o0oOOo0O0Ooo + i1IIi * Oo0Ooo
 if 6 - 6: OoO0O00 * OoooooooOO * iIii1I11I1II1
 if 87 - 87: iIii1I11I1II1 - ooOoO0o * iIii1I11I1II1
 if 79 - 79: ooOoO0o . oO0o + Ii1I * ooOoO0o + O0 . II111iiii
 I1III11iIIIi = lisp_ddt_map_request ( lisp_sockets , packet , iiI1I1IIi , OOo0oOOO0 , o0OOO )
 I1III11iIIIi . packet = packet
 I1III11iIIIi . itr = ecm_source
 I1III11iIIIi . mr_source = mr_source
 I1III11iIIIi . sport = sport
 I1III11iIIIi . from_pitr = map_request . pitr_bit
 I1III11iIIIi . queue_map_request ( )
 if 96 - 96: Oo0Ooo + i1IIi * Ii1I - I1ii11iIi11i
 lisp_send_ddt_map_request ( I1III11iIIIi , False )
 return
 if 81 - 81: i11iIiiIii . OoOoOO00 * o0oOOo0O0Ooo / O0 * OoooooooOO / i11iIiiIii
 if 62 - 62: i11iIiiIii * iII111i . Oo0Ooo % Oo0Ooo
 if 4 - 4: OoooooooOO
 if 66 - 66: iII111i / IiII
 if 45 - 45: o0oOOo0O0Ooo - i1IIi / o0oOOo0O0Ooo + IiII
 if 94 - 94: Ii1I
 if 21 - 21: OoOoOO00
def lisp_process_map_request ( lisp_sockets , packet , ecm_source , ecm_port ,
 mr_source , mr_port , ddt_request , ttl , timestamp ) :
 if 68 - 68: i11iIiiIii / OOooOOo / I1ii11iIi11i % IiII * IiII + II111iiii
 oO0ooOoOooO00o00 = packet
 OoOOoO = lisp_map_request ( )
 packet = OoOOoO . decode ( packet , mr_source , mr_port )
 if ( packet == None ) :
  lprint ( "Could not decode Map-Request packet" )
  return
  if 63 - 63: ooOoO0o / i1IIi % I1ii11iIi11i + OoOoOO00 - Oo0Ooo
  if 98 - 98: II111iiii - o0oOOo0O0Ooo * Oo0Ooo - i11iIiiIii
 OoOOoO . print_map_request ( )
 if 75 - 75: oO0o * OoooooooOO . iIii1I11I1II1 + O0 - i1IIi
 if 37 - 37: II111iiii - iIii1I11I1II1 / OOooOOo % I1ii11iIi11i
 if 27 - 27: O0
 if 41 - 41: oO0o
 if ( OoOOoO . rloc_probe ) :
  lisp_process_rloc_probe_request ( lisp_sockets , OoOOoO , mr_source ,
 mr_port , ttl , timestamp )
  return
  if 20 - 20: OoooooooOO / OoO0O00 * iII111i * OOooOOo + ooOoO0o / I11i
  if 14 - 14: i1IIi * O0 . O0
  if 55 - 55: iIii1I11I1II1
  if 7 - 7: OoO0O00
  if 61 - 61: I1Ii111 / I1IiiI / OOooOOo . I1ii11iIi11i
 if ( OoOOoO . smr_bit ) :
  lisp_process_smr ( OoOOoO )
  if 3 - 3: IiII
  if 2 - 2: I1IiiI % Ii1I % Oo0Ooo / ooOoO0o % Oo0Ooo + OoOoOO00
  if 44 - 44: i1IIi / OoooooooOO * OoooooooOO
  if 93 - 93: OoOoOO00 % Oo0Ooo . OoO0O00 / OoooooooOO
  if 59 - 59: OoO0O00 + O0 + i11iIiiIii / OoOoOO00 + iIii1I11I1II1 / OoOoOO00
 if ( OoOOoO . smr_invoked_bit ) :
  lisp_process_smr_invoked_request ( OoOOoO )
  if 69 - 69: OoOoOO00 * Ii1I % ooOoO0o . OoOoOO00 / oO0o * I1Ii111
  if 93 - 93: OoO0O00 % IiII % ooOoO0o . I1IiiI
  if 96 - 96: II111iiii
  if 73 - 73: II111iiii
  if 81 - 81: I1IiiI + OoO0O00
 if ( lisp_i_am_etr ) :
  lisp_etr_process_map_request ( lisp_sockets , OoOOoO , mr_source ,
 mr_port , ttl , timestamp )
  if 22 - 22: OoO0O00 * OoOoOO00 * I11i * IiII . OoO0O00 . I1ii11iIi11i
  if 32 - 32: o0oOOo0O0Ooo - iII111i + i11iIiiIii / ooOoO0o . OoOoOO00 . IiII
  if 9 - 9: iIii1I11I1II1
  if 66 - 66: iIii1I11I1II1
  if 13 - 13: O0 / ooOoO0o
 if ( lisp_i_am_ms ) :
  packet = oO0ooOoOooO00o00
  iiI1I1IIi , OOo0oOOO0 , OoooOO0 = lisp_ms_process_map_request ( lisp_sockets ,
 oO0ooOoOooO00o00 , OoOOoO , mr_source , mr_port , ecm_source )
  if ( ddt_request ) :
   lisp_ms_send_map_referral ( lisp_sockets , OoOOoO , ecm_source ,
 ecm_port , OoooOO0 , iiI1I1IIi , OOo0oOOO0 )
   if 26 - 26: I1ii11iIi11i
  return
  if 67 - 67: I1Ii111 * iIii1I11I1II1 / O0 + OoO0O00 * iIii1I11I1II1 % II111iiii
  if 13 - 13: Ii1I / ooOoO0o / iII111i % II111iiii * I1IiiI * II111iiii
  if 40 - 40: Ii1I / i1IIi . iII111i
  if 65 - 65: iIii1I11I1II1 * O0 . II111iiii * o0oOOo0O0Ooo . I1ii11iIi11i * I1IiiI
  if 63 - 63: II111iiii . Oo0Ooo % iIii1I11I1II1
 if ( lisp_i_am_mr and not ddt_request ) :
  lisp_mr_process_map_request ( lisp_sockets , oO0ooOoOooO00o00 , OoOOoO ,
 ecm_source , mr_port , mr_source )
  if 85 - 85: I1IiiI + i1IIi % I1Ii111
  if 76 - 76: i11iIiiIii % i11iIiiIii
  if 33 - 33: OOooOOo . ooOoO0o / iIii1I11I1II1 * OOooOOo / oO0o
  if 75 - 75: Ii1I - OoOoOO00 . OOooOOo - o0oOOo0O0Ooo - I1ii11iIi11i
  if 69 - 69: O0 % I1ii11iIi11i
 if ( lisp_i_am_ddt or ddt_request ) :
  packet = oO0ooOoOooO00o00
  lisp_ddt_process_map_request ( lisp_sockets , OoOOoO , ecm_source ,
 ecm_port )
  if 77 - 77: iIii1I11I1II1 . OOooOOo
 return
 if 64 - 64: OoOoOO00 - i1IIi * i1IIi / iII111i * OoOoOO00 * OoO0O00
 if 61 - 61: OOooOOo
 if 51 - 51: Oo0Ooo * OOooOOo / iII111i
 if 49 - 49: ooOoO0o . i1IIi % I1Ii111 . I1IiiI . I1ii11iIi11i + OoO0O00
 if 65 - 65: I1ii11iIi11i + Ii1I / i11iIiiIii * I1Ii111 + OoooooooOO
 if 7 - 7: Oo0Ooo % o0oOOo0O0Ooo
 if 40 - 40: oO0o * IiII
 if 29 - 29: O0 - II111iiii + iII111i
def lisp_store_mr_stats ( source , nonce ) :
 I1III11iIIIi = lisp_get_map_resolver ( source , None )
 if ( I1III11iIIIi == None ) : return
 if 73 - 73: I1Ii111 - I11i + IiII - o0oOOo0O0Ooo - I11i - OOooOOo
 if 40 - 40: iIii1I11I1II1 . iII111i * I1ii11iIi11i + IiII - iIii1I11I1II1
 if 83 - 83: i1IIi
 if 9 - 9: iIii1I11I1II1 + i11iIiiIii
 I1III11iIIIi . neg_map_replies_received += 1
 I1III11iIIIi . last_reply = lisp_get_timestamp ( )
 if 70 - 70: I1IiiI - OoO0O00 % OOooOOo + ooOoO0o % II111iiii
 if 19 - 19: I11i + i1IIi / i1IIi - II111iiii + I1Ii111
 if 11 - 11: i11iIiiIii % i11iIiiIii / IiII - Oo0Ooo / O0 - I11i
 if 29 - 29: OOooOOo * iIii1I11I1II1 * ooOoO0o
 if ( ( I1III11iIIIi . neg_map_replies_received % 100 ) == 0 ) : I1III11iIIIi . total_rtt = 0
 if 80 - 80: oO0o * I1Ii111
 if 87 - 87: iII111i + OoOoOO00 % ooOoO0o - oO0o
 if 40 - 40: i1IIi / OoOoOO00 - I11i / ooOoO0o . Ii1I
 if 8 - 8: I1IiiI . IiII . OOooOOo . O0
 if ( I1III11iIIIi . last_nonce == nonce ) :
  I1III11iIIIi . total_rtt += ( time . time ( ) - I1III11iIIIi . last_used )
  I1III11iIIIi . last_nonce = 0
  if 3 - 3: Ii1I + i11iIiiIii
 if ( ( I1III11iIIIi . neg_map_replies_received % 10 ) == 0 ) : I1III11iIIIi . last_nonce = 0
 return
 if 87 - 87: ooOoO0o - iII111i % I11i
 if 88 - 88: I11i . OoooooooOO
 if 86 - 86: Ii1I - I1IiiI - iII111i % Ii1I . I1ii11iIi11i % i1IIi
 if 84 - 84: OoOoOO00
 if 99 - 99: OoO0O00 - OoOoOO00 - i1IIi / OoO0O00 * I1ii11iIi11i * iIii1I11I1II1
 if 65 - 65: iII111i - O0 / i1IIi . I1Ii111
 if 85 - 85: o0oOOo0O0Ooo % Ii1I
def lisp_process_map_reply ( lisp_sockets , packet , source , ttl , itr_in_ts ) :
 global lisp_map_cache
 if 81 - 81: oO0o / OoO0O00 * i1IIi % iIii1I11I1II1
 II1II1i1IIII = lisp_map_reply ( )
 packet = II1II1i1IIII . decode ( packet )
 if ( packet == None ) :
  lprint ( "Could not decode Map-Reply packet" )
  return
  if 23 - 23: II111iiii . II111iiii
 II1II1i1IIII . print_map_reply ( )
 if 17 - 17: i11iIiiIii / IiII * I1IiiI . Oo0Ooo / o0oOOo0O0Ooo - iIii1I11I1II1
 if 21 - 21: OOooOOo % Ii1I
 if 3 - 3: OOooOOo / ooOoO0o / I1Ii111 . I11i
 if 54 - 54: I1ii11iIi11i - I1IiiI . OoOoOO00
 iIii11ii1II1i = None
 for iIi1I1 in range ( II1II1i1IIII . record_count ) :
  OOOo = lisp_eid_record ( )
  packet = OOOo . decode ( packet )
  if ( packet == None ) :
   lprint ( "Could not decode EID-record in Map-Reply packet" )
   return
   if 90 - 90: I1Ii111 / I1ii11iIi11i . I11i * ooOoO0o % ooOoO0o
  OOOo . print_record ( "  " , False )
  if 60 - 60: I1ii11iIi11i / I11i + iII111i
  if 26 - 26: OoOoOO00
  if 63 - 63: I1Ii111 . oO0o + OoO0O00 / I1ii11iIi11i % IiII * II111iiii
  if 92 - 92: iIii1I11I1II1 . OoooooooOO . ooOoO0o / II111iiii
  if 30 - 30: i1IIi * Ii1I + Ii1I / I1Ii111
  if ( OOOo . rloc_count == 0 ) :
   lisp_store_mr_stats ( source , II1II1i1IIII . nonce )
   if 84 - 84: I1IiiI - Oo0Ooo * OoO0O00 * oO0o
   if 13 - 13: I1Ii111 * i11iIiiIii % o0oOOo0O0Ooo + oO0o - iII111i
  o000OO0oO0O = ( OOOo . group . is_null ( ) == False )
  if 32 - 32: I1Ii111 / I1ii11iIi11i - Ii1I % o0oOOo0O0Ooo * I1Ii111 % II111iiii
  if 33 - 33: ooOoO0o % I11i
  if 72 - 72: OoO0O00 % OoooooooOO / II111iiii * oO0o * I1Ii111
  if 98 - 98: OOooOOo * Ii1I + I1ii11iIi11i / iIii1I11I1II1 / OoOoOO00 + I1IiiI
  if 74 - 74: ooOoO0o . IiII . O0 * I1IiiI * oO0o
  if ( lisp_decent_push_configured ) :
   iI1IIi1I = OOOo . action
   if ( o000OO0oO0O and iI1IIi1I == LISP_DROP_ACTION ) :
    if ( OOOo . eid . is_local ( ) ) : continue
    if 6 - 6: O0 . Ii1I / Oo0Ooo * o0oOOo0O0Ooo
    if 1 - 1: i11iIiiIii
    if 30 - 30: I11i
    if 26 - 26: Oo0Ooo - II111iiii % ooOoO0o
    if 81 - 81: i11iIiiIii + I1ii11iIi11i * oO0o
    if 86 - 86: OoO0O00 . ooOoO0o . o0oOOo0O0Ooo
    if 70 - 70: O0 % OoooooooOO - Ii1I * Oo0Ooo
  if ( o000OO0oO0O == False and OOOo . eid . is_null ( ) ) : continue
  if 18 - 18: OOooOOo . I1IiiI + i1IIi . I1IiiI
  if 3 - 3: O0 * O0 + II111iiii + OoOoOO00 * I11i % Oo0Ooo
  if 19 - 19: oO0o % IiII % OoooooooOO % I1ii11iIi11i / OoO0O00
  if 6 - 6: O0 * I1Ii111 - II111iiii
  if 60 - 60: oO0o % oO0o
  if ( o000OO0oO0O ) :
   o0Oo0 = lisp_map_cache_lookup ( OOOo . eid , OOOo . group )
  else :
   o0Oo0 = lisp_map_cache . lookup_cache ( OOOo . eid , True )
   if 7 - 7: Ii1I
  i11i1iI1iI1i1 = ( o0Oo0 == None )
  if 98 - 98: I1IiiI - I1ii11iIi11i * I1IiiI / o0oOOo0O0Ooo % i1IIi * ooOoO0o
  if 59 - 59: I11i / OoOoOO00 % ooOoO0o . Ii1I
  if 48 - 48: OoOoOO00 % IiII % i1IIi + o0oOOo0O0Ooo
  if 33 - 33: iIii1I11I1II1 . O0
  if 54 - 54: iIii1I11I1II1
  if ( o0Oo0 == None ) :
   o0O0OoO , oOo0oo , IIIi1i1iIIIi = lisp_allow_gleaning ( OOOo . eid , OOOo . group ,
 None )
   if ( o0O0OoO ) : continue
  else :
   if ( o0Oo0 . gleaned ) : continue
   if 59 - 59: OoooooooOO * iIii1I11I1II1 * oO0o - i1IIi
   if 45 - 45: I1Ii111 + Ii1I . IiII + iIii1I11I1II1 / iII111i - OoO0O00
   if 79 - 79: OOooOOo % OoO0O00 % I1IiiI . OoO0O00 / ooOoO0o
   if 92 - 92: Oo0Ooo / iII111i + O0 * ooOoO0o * OOooOOo % Oo0Ooo
   if 97 - 97: oO0o / Ii1I
  OoO0oOOooOO = [ ]
  O0oOO = None
  for I1iII in range ( OOOo . rloc_count ) :
   OOO0Oo = lisp_rloc_record ( )
   OOO0Oo . keys = II1II1i1IIII . keys
   packet = OOO0Oo . decode ( packet , II1II1i1IIII . nonce )
   if ( packet == None ) :
    lprint ( "Could not decode RLOC-record in Map-Reply packet" )
    return
    if 67 - 67: I1Ii111 * i1IIi % iII111i
   OOO0Oo . print_record ( "    " )
   if 69 - 69: I1Ii111 . ooOoO0o + ooOoO0o * OOooOOo % I1Ii111 . OoOoOO00
   OOO00O0O000 = None
   if ( o0Oo0 ) : OOO00O0O000 = o0Oo0 . get_rloc ( OOO0Oo . rloc )
   if ( OOO00O0O000 ) :
    I1II = OOO00O0O000
   else :
    I1II = lisp_rloc ( )
    if 74 - 74: OoO0O00 + I1Ii111 / o0oOOo0O0Ooo % Ii1I
    if 19 - 19: I1IiiI % oO0o - Ii1I
    if 97 - 97: OOooOOo / ooOoO0o . Oo0Ooo - Oo0Ooo . OoOoOO00
    if 88 - 88: iIii1I11I1II1 - OoO0O00 + II111iiii
    if 100 - 100: I1Ii111 + I1IiiI + OOooOOo * iII111i
    if 35 - 35: Oo0Ooo . O0
    if 43 - 43: oO0o . O0 . OOooOOo
   Oo0o = I1II . store_rloc_from_record ( OOO0Oo , II1II1i1IIII . nonce ,
 source )
   I1II . echo_nonce_capable = II1II1i1IIII . echo_nonce_capable
   if 3 - 3: i1IIi
   if ( I1II . echo_nonce_capable ) :
    oo0o00OO = I1II . rloc . print_address_no_iid ( )
    if ( lisp_get_echo_nonce ( None , oo0o00OO ) == None ) :
     lisp_echo_nonce ( oo0o00OO )
     if 85 - 85: i11iIiiIii % i1IIi
     if 78 - 78: ooOoO0o / I1ii11iIi11i
     if 72 - 72: II111iiii / O0 - I1ii11iIi11i + oO0o + iIii1I11I1II1
     if 65 - 65: OoO0O00 * II111iiii
     if 25 - 25: I1ii11iIi11i - I1Ii111 * I1Ii111 / O0 - iIii1I11I1II1 . iII111i
     if 83 - 83: ooOoO0o * oO0o * OoO0O00 + OoO0O00
   if ( I1II . json ) :
    if ( lisp_is_json_telemetry ( I1II . json . json_string ) ) :
     oO0OOO0o0oooO = I1II . json . json_string
     oO0OOO0o0oooO = lisp_encode_telemetry ( oO0OOO0o0oooO , ii = itr_in_ts )
     I1II . json . json_string = oO0OOO0o0oooO
     if 58 - 58: I1ii11iIi11i
     if 93 - 93: i1IIi - IiII + IiII % OoooooooOO / o0oOOo0O0Ooo
     if 39 - 39: I1IiiI + Ii1I - O0
     if 25 - 25: IiII % iIii1I11I1II1 + ooOoO0o % iII111i - OoO0O00
     if 36 - 36: OoooooooOO / oO0o + IiII . I1IiiI - o0oOOo0O0Ooo % OOooOOo
     if 15 - 15: Ii1I % IiII + IiII % iII111i - O0 * OoooooooOO
     if 53 - 53: OoOoOO00 . Ii1I / Oo0Ooo
     if 62 - 62: i11iIiiIii
     if 38 - 38: I1ii11iIi11i % ooOoO0o * OoooooooOO + iIii1I11I1II1 % i1IIi / OOooOOo
     if 6 - 6: i11iIiiIii
   if ( II1II1i1IIII . rloc_probe and OOO0Oo . probe_bit ) :
    if ( I1II . rloc . afi == source . afi ) :
     lisp_process_rloc_probe_reply ( I1II , source , Oo0o ,
 II1II1i1IIII , ttl , O0oOO )
     if 8 - 8: iIii1I11I1II1 + I1ii11iIi11i . i1IIi % OoOoOO00 % OoooooooOO * Oo0Ooo
    if ( I1II . rloc . is_multicast_address ( ) ) : O0oOO = I1II
    if 53 - 53: oO0o
    if 23 - 23: I1ii11iIi11i . I1Ii111 + OOooOOo
    if 4 - 4: I1IiiI
    if 31 - 31: ooOoO0o * i1IIi . O0
    if 5 - 5: OOooOOo . I1ii11iIi11i + ooOoO0o . ooOoO0o + iII111i
   OoO0oOOooOO . append ( I1II )
   if 100 - 100: I1Ii111
   if 71 - 71: ooOoO0o * i1IIi / OoOoOO00 * i11iIiiIii - iII111i
   if 88 - 88: IiII
   if 29 - 29: iII111i . ooOoO0o
   if ( lisp_data_plane_security and I1II . rloc_recent_rekey ( ) ) :
    iIii11ii1II1i = I1II
    if 62 - 62: IiII
    if 95 - 95: ooOoO0o / i1IIi + II111iiii + OoO0O00 % OoO0O00
    if 18 - 18: ooOoO0o * I1IiiI / iII111i % iII111i
    if 9 - 9: i11iIiiIii % ooOoO0o % O0 + i1IIi / O0
    if 12 - 12: I1Ii111 - iII111i * iII111i + OoO0O00 . Ii1I % I11i
    if 28 - 28: ooOoO0o % OoO0O00 - II111iiii * IiII - I1IiiI + I1IiiI
    if 84 - 84: IiII / Ii1I
    if 39 - 39: OOooOOo - iIii1I11I1II1 + OoOoOO00 % IiII * OoooooooOO % Ii1I
    if 11 - 11: I1ii11iIi11i
    if 83 - 83: O0
    if 97 - 97: O0
  if ( II1II1i1IIII . rloc_probe == False and lisp_nat_traversal ) :
   OOO = [ ]
   I1iiI = [ ]
   for I1II in OoO0oOOooOO :
    if 55 - 55: i11iIiiIii / II111iiii / I1Ii111 * iIii1I11I1II1 / II111iiii * iIii1I11I1II1
    if 41 - 41: o0oOOo0O0Ooo . iII111i % iII111i . OOooOOo / OOooOOo
    if 98 - 98: II111iiii + ooOoO0o - iIii1I11I1II1 . I11i . iIii1I11I1II1 - iIii1I11I1II1
    if 91 - 91: ooOoO0o
    if 66 - 66: OOooOOo
    if ( I1II . rloc . is_private_address ( ) ) :
     I1II . priority = 1
     I1II . state = LISP_RLOC_UNREACH_STATE
     OOO . append ( I1II )
     I1iiI . append ( I1II . rloc . print_address_no_iid ( ) )
     continue
     if 5 - 5: i1IIi * OoOoOO00 + i1IIi % I11i
     if 79 - 79: OOooOOo % iIii1I11I1II1 / OoOoOO00
     if 9 - 9: Ii1I
     if 44 - 44: iII111i
     if 46 - 46: I11i . i11iIiiIii * OoOoOO00 + o0oOOo0O0Ooo / ooOoO0o
     if 37 - 37: OoO0O00 - Ii1I + OoO0O00
    if ( I1II . priority == 254 and lisp_i_am_rtr == False ) :
     OOO . append ( I1II )
     I1iiI . append ( I1II . rloc . print_address_no_iid ( ) )
     if 49 - 49: OoooooooOO - I1ii11iIi11i % I1ii11iIi11i / i1IIi . ooOoO0o
    if ( I1II . priority != 254 and lisp_i_am_rtr ) :
     OOO . append ( I1II )
     I1iiI . append ( I1II . rloc . print_address_no_iid ( ) )
     if 60 - 60: Oo0Ooo
     if 46 - 46: OoOoOO00 + i1IIi
     if 43 - 43: II111iiii * IiII % iIii1I11I1II1 % i11iIiiIii % I1ii11iIi11i
   if ( I1iiI != [ ] ) :
    OoO0oOOooOO = OOO
    lprint ( "NAT-traversal optimized RLOC-set: {}" . format ( I1iiI ) )
    if 81 - 81: oO0o % I1ii11iIi11i % ooOoO0o * O0 - OOooOOo
    if 17 - 17: O0 % O0 / I1ii11iIi11i . Oo0Ooo . iII111i
    if 4 - 4: OoO0O00
    if 65 - 65: Oo0Ooo % O0 / I1Ii111 * IiII - oO0o
    if 32 - 32: Ii1I * OoO0O00 + ooOoO0o
    if 41 - 41: IiII + I11i * ooOoO0o + Oo0Ooo . ooOoO0o
    if 38 - 38: iII111i * OoooooooOO - IiII
  OOO = [ ]
  for I1II in OoO0oOOooOO :
   if ( I1II . json != None ) : continue
   OOO . append ( I1II )
   if 36 - 36: I1Ii111 * II111iiii + I1ii11iIi11i - iII111i * iII111i
  if ( OOO != [ ] ) :
   I1I1 = len ( OoO0oOOooOO ) - len ( OOO )
   lprint ( "Pruning {} no-address RLOC-records for map-cache" . format ( I1I1 ) )
   if 91 - 91: O0 + I1Ii111 * II111iiii - O0 . i11iIiiIii . Oo0Ooo
   OoO0oOOooOO = OOO
   if 54 - 54: ooOoO0o * I11i / I1ii11iIi11i % ooOoO0o
   if 76 - 76: I11i . I1IiiI
   if 66 - 66: oO0o % oO0o * IiII
   if 39 - 39: i1IIi * Ii1I + OoOoOO00 / oO0o
   if 6 - 6: I1ii11iIi11i / II111iiii / OoOoOO00 . i11iIiiIii - iII111i
   if 43 - 43: i11iIiiIii * i11iIiiIii * I1Ii111
   if 80 - 80: oO0o . I1IiiI * II111iiii + o0oOOo0O0Ooo / o0oOOo0O0Ooo % OoooooooOO
   if 31 - 31: o0oOOo0O0Ooo - OoO0O00 % I1IiiI
  if ( II1II1i1IIII . rloc_probe and o0Oo0 != None ) : OoO0oOOooOO = o0Oo0 . rloc_set
  if 23 - 23: OOooOOo
  if 97 - 97: Oo0Ooo / OoooooooOO . OoooooooOO
  if 47 - 47: OoO0O00
  if 52 - 52: I1IiiI * iIii1I11I1II1 % oO0o * IiII % oO0o
  if 9 - 9: I11i
  o0ooo0oOO0o = i11i1iI1iI1i1
  if ( o0Oo0 and OoO0oOOooOO != o0Oo0 . rloc_set ) :
   o0Oo0 . delete_rlocs_from_rloc_probe_list ( )
   o0ooo0oOO0o = True
   if 78 - 78: iIii1I11I1II1 % I1ii11iIi11i % IiII
   if 59 - 59: iII111i - I1ii11iIi11i / OoooooooOO
   if 37 - 37: Oo0Ooo - OoO0O00 . i11iIiiIii + I1IiiI . iIii1I11I1II1 % OoOoOO00
   if 61 - 61: oO0o . o0oOOo0O0Ooo
   if 82 - 82: Oo0Ooo * OoooooooOO / ooOoO0o / I1IiiI
  o0o00 = o0Oo0 . uptime if ( o0Oo0 ) else None
  if ( o0Oo0 == None ) :
   o0Oo0 = lisp_mapping ( OOOo . eid , OOOo . group , OoO0oOOooOO )
   o0Oo0 . mapping_source = source
   if 28 - 28: iIii1I11I1II1 - o0oOOo0O0Ooo . iIii1I11I1II1 / I11i / I1Ii111 % iIii1I11I1II1
   if 45 - 45: OoO0O00 + ooOoO0o / iIii1I11I1II1 % i11iIiiIii
   if 16 - 16: i1IIi / oO0o - OOooOOo / Ii1I + I1IiiI
   if 62 - 62: i11iIiiIii . Ii1I . iII111i / I1Ii111 * OoO0O00
   if 31 - 31: OoOoOO00
   if 16 - 16: OoooooooOO
   if ( lisp_i_am_rtr and OOOo . group . is_null ( ) == False ) :
    o0Oo0 . map_cache_ttl = LISP_MCAST_TTL
   else :
    o0Oo0 . map_cache_ttl = OOOo . store_ttl ( )
    if 32 - 32: ooOoO0o - o0oOOo0O0Ooo / ooOoO0o + o0oOOo0O0Ooo + iII111i
   o0Oo0 . action = OOOo . action
   o0Oo0 . add_cache ( o0ooo0oOO0o )
   if 78 - 78: OoooooooOO . I1ii11iIi11i * oO0o . o0oOOo0O0Ooo * OoOoOO00 / oO0o
   if 47 - 47: OOooOOo
  iI1I11II = "Add"
  if ( o0o00 ) :
   o0Oo0 . uptime = o0o00
   o0Oo0 . refresh_time = lisp_get_timestamp ( )
   iI1I11II = "Replace"
   if 99 - 99: O0 - OoO0O00
   if 95 - 95: Ii1I . IiII * o0oOOo0O0Ooo
  lprint ( "{} {} map-cache with {} RLOCs" . format ( iI1I11II ,
 green ( o0Oo0 . print_eid_tuple ( ) , False ) , len ( OoO0oOOooOO ) ) )
  if 91 - 91: I1Ii111
  if 49 - 49: I11i
  if 17 - 17: Oo0Ooo % o0oOOo0O0Ooo
  if 3 - 3: OoO0O00 . oO0o . oO0o . Ii1I
  if 100 - 100: i11iIiiIii / i1IIi . I1ii11iIi11i
  if ( lisp_ipc_dp_socket and iIii11ii1II1i != None ) :
   lisp_write_ipc_keys ( iIii11ii1II1i )
   if 1 - 1: IiII * I1Ii111 / I1ii11iIi11i * i11iIiiIii
   if 82 - 82: o0oOOo0O0Ooo * OoO0O00 / o0oOOo0O0Ooo % OoOoOO00 * iIii1I11I1II1 % O0
   if 10 - 10: ooOoO0o
   if 69 - 69: I11i + I1IiiI / oO0o
   if 89 - 89: i1IIi % OoOoOO00 . I1ii11iIi11i
   if 85 - 85: I1Ii111 - oO0o
   if 34 - 34: iIii1I11I1II1 / IiII + OoOoOO00 - IiII / ooOoO0o + OoOoOO00
  if ( i11i1iI1iI1i1 ) :
   oO0oo000O = bold ( "RLOC-probe" , False )
   for I1II in o0Oo0 . best_rloc_set :
    oo0o00OO = red ( I1II . rloc . print_address_no_iid ( ) , False )
    lprint ( "Trigger {} to {}" . format ( oO0oo000O , oo0o00OO ) )
    lisp_send_map_request ( lisp_sockets , 0 , o0Oo0 . eid , o0Oo0 . group , I1II )
    if 14 - 14: ooOoO0o - OoooooooOO / iIii1I11I1II1
    if 98 - 98: i1IIi
    if 81 - 81: OoOoOO00 * i11iIiiIii + I1IiiI
 return
 if 2 - 2: I11i - IiII + I1IiiI % OoO0O00 + iIii1I11I1II1 + oO0o
 if 49 - 49: I1IiiI * I1Ii111 . I1IiiI - II111iiii
 if 57 - 57: oO0o + O0 - OoOoOO00
 if 14 - 14: II111iiii + i11iIiiIii + Ii1I / o0oOOo0O0Ooo . OoO0O00
 if 93 - 93: o0oOOo0O0Ooo + i1IIi
 if 24 - 24: i1IIi
 if 54 - 54: iIii1I11I1II1 - IiII + o0oOOo0O0Ooo + I1ii11iIi11i + IiII
 if 99 - 99: Oo0Ooo
def lisp_compute_auth ( packet , map_register , password ) :
 if ( map_register . alg_id == LISP_NONE_ALG_ID ) : return ( packet )
 if 38 - 38: I1ii11iIi11i - I1IiiI
 packet = map_register . zero_auth ( packet )
 I1iI1111ii1I1 = lisp_hash_me ( packet , map_register . alg_id , password , False )
 if 50 - 50: iII111i % OoO0O00 - oO0o + Oo0Ooo . O0 . iII111i
 if 42 - 42: iII111i + I1ii11iIi11i
 if 44 - 44: I1ii11iIi11i % IiII
 if 1 - 1: Oo0Ooo + IiII - I1Ii111 / I1Ii111
 map_register . auth_data = I1iI1111ii1I1
 packet = map_register . encode_auth ( packet )
 return ( packet )
 if 25 - 25: OoOoOO00
 if 52 - 52: OOooOOo + IiII
 if 73 - 73: OoooooooOO - I1Ii111 % iII111i / OOooOOo . o0oOOo0O0Ooo - IiII
 if 69 - 69: Ii1I . iIii1I11I1II1 / Oo0Ooo * Oo0Ooo % IiII
 if 5 - 5: OOooOOo - I1Ii111 + IiII
 if 82 - 82: OOooOOo
 if 26 - 26: ooOoO0o + OoooooooOO + ooOoO0o * I1Ii111
def lisp_hash_me ( packet , alg_id , password , do_hex ) :
 if ( alg_id == LISP_NONE_ALG_ID ) : return ( True )
 if 26 - 26: I1IiiI - OOooOOo
 if ( alg_id == LISP_SHA_1_96_ALG_ID ) :
  I1iiiII1i1 = hashlib . sha1
  if 2 - 2: IiII % iII111i / o0oOOo0O0Ooo * I11i
 if ( alg_id == LISP_SHA_256_128_ALG_ID ) :
  I1iiiII1i1 = hashlib . sha256
  if 35 - 35: OoOoOO00 * I1Ii111 / II111iiii / O0
  if 35 - 35: ooOoO0o * I11i
 if ( do_hex ) :
  I1iI1111ii1I1 = hmac . new ( password , packet , I1iiiII1i1 ) . hexdigest ( )
 else :
  I1iI1111ii1I1 = hmac . new ( password , packet , I1iiiII1i1 ) . digest ( )
  if 85 - 85: i1IIi
 return ( I1iI1111ii1I1 )
 if 81 - 81: I1Ii111
 if 28 - 28: i1IIi * ooOoO0o
 if 14 - 14: II111iiii + II111iiii - I11i / I11i . OoOoOO00 + OoO0O00
 if 92 - 92: II111iiii - II111iiii % IiII
 if 48 - 48: oO0o / II111iiii + oO0o
 if 16 - 16: o0oOOo0O0Ooo % II111iiii - i11iIiiIii - IiII + O0 - i11iIiiIii
 if 58 - 58: OoooooooOO / I1ii11iIi11i - Oo0Ooo / II111iiii
 if 13 - 13: o0oOOo0O0Ooo + OoOoOO00 * ooOoO0o % IiII
def lisp_verify_auth ( packet , alg_id , auth_data , password ) :
 if ( alg_id == LISP_NONE_ALG_ID ) : return ( True )
 if 18 - 18: I1IiiI . I1ii11iIi11i + Oo0Ooo - iII111i
 I1iI1111ii1I1 = lisp_hash_me ( packet , alg_id , password , True )
 o00Oo = ( I1iI1111ii1I1 == auth_data )
 if 15 - 15: I1Ii111 / I11i / i11iIiiIii + OoO0O00 % OOooOOo
 if 8 - 8: oO0o - I1IiiI / I11i + II111iiii - I1IiiI
 if 3 - 3: I11i * o0oOOo0O0Ooo . O0
 if 11 - 11: Oo0Ooo
 if ( o00Oo == False ) :
  lprint ( "Hashed value: {} does not match packet value: {}" . format ( I1iI1111ii1I1 , auth_data ) )
  if 64 - 64: OOooOOo
  if 8 - 8: ooOoO0o % o0oOOo0O0Ooo
 return ( o00Oo )
 if 22 - 22: O0 * IiII . OoO0O00
 if 63 - 63: oO0o % Oo0Ooo * OoO0O00 / II111iiii / Ii1I - ooOoO0o
 if 14 - 14: ooOoO0o . o0oOOo0O0Ooo + II111iiii
 if 50 - 50: Ii1I - i1IIi * oO0o
 if 52 - 52: I11i / oO0o - oO0o
 if 84 - 84: iIii1I11I1II1 - o0oOOo0O0Ooo
 if 37 - 37: iII111i * o0oOOo0O0Ooo
def lisp_retransmit_map_notify ( map_notify ) :
 Ii1II1I11i1I = map_notify . etr
 Oo0o = map_notify . etr_port
 if 23 - 23: ooOoO0o + OoooooooOO * iII111i . I11i
 if 2 - 2: iIii1I11I1II1 * I1ii11iIi11i - OoooooooOO
 if 93 - 93: iII111i % ooOoO0o * Oo0Ooo
 if 34 - 34: O0 * oO0o
 if 58 - 58: OOooOOo . iII111i - Oo0Ooo / iII111i . I11i
 if ( map_notify . retry_count == LISP_MAX_MAP_NOTIFY_RETRIES ) :
  lprint ( "Map-Notify with nonce 0x{} retry limit reached for ETR {}" . format ( map_notify . nonce_key , red ( Ii1II1I11i1I . print_address ( ) , False ) ) )
  if 86 - 86: iIii1I11I1II1 - iII111i % Ii1I
  if 18 - 18: oO0o / IiII - OOooOOo % Ii1I
  o0Oo = map_notify . nonce_key
  if ( lisp_map_notify_queue . has_key ( o0Oo ) ) :
   map_notify . retransmit_timer . cancel ( )
   lprint ( "Dequeue Map-Notify from retransmit queue, key is: {}" . format ( o0Oo ) )
   if 88 - 88: i11iIiiIii
   try :
    lisp_map_notify_queue . pop ( o0Oo )
   except :
    lprint ( "Key not found in Map-Notify queue" )
    if 13 - 13: I1IiiI
    if 52 - 52: Ii1I * oO0o / I1Ii111 . IiII
  return
  if 84 - 84: OoooooooOO - oO0o - I1Ii111
  if 69 - 69: OoOoOO00 * Ii1I % OoooooooOO % OOooOOo * OoOoOO00
 OOOooo0 = map_notify . lisp_sockets
 map_notify . retry_count += 1
 if 20 - 20: IiII
 lprint ( "Retransmit {} with nonce 0x{} to xTR {}, retry {}" . format ( bold ( "Map-Notify" , False ) , map_notify . nonce_key ,
 # II111iiii
 red ( Ii1II1I11i1I . print_address ( ) , False ) , map_notify . retry_count ) )
 if 80 - 80: OOooOOo . OoO0O00 + O0 / IiII
 lisp_send_map_notify ( OOOooo0 , map_notify . packet , Ii1II1I11i1I , Oo0o )
 if ( map_notify . site ) : map_notify . site . map_notifies_sent += 1
 if 30 - 30: Ii1I / I11i . II111iiii + ooOoO0o
 if 58 - 58: Oo0Ooo % OOooOOo - i11iIiiIii - I1Ii111 - Ii1I % OoO0O00
 if 67 - 67: I1Ii111 + OoO0O00 - oO0o / OOooOOo . OoooooooOO * O0
 if 91 - 91: O0 * OoOoOO00 - OoOoOO00 * II111iiii - iII111i
 map_notify . retransmit_timer = threading . Timer ( LISP_MAP_NOTIFY_INTERVAL ,
 lisp_retransmit_map_notify , [ map_notify ] )
 map_notify . retransmit_timer . start ( )
 return
 if 38 - 38: oO0o * I11i % OOooOOo
 if 80 - 80: O0 % II111iiii / O0 . Oo0Ooo * OoOoOO00 + OOooOOo
 if 47 - 47: Ii1I - Oo0Ooo * OoOoOO00
 if 20 - 20: oO0o
 if 48 - 48: I1IiiI % OoO0O00
 if 33 - 33: Ii1I
 if 73 - 73: Ii1I . IiII
def lisp_send_merged_map_notify ( lisp_sockets , parent , map_register ,
 eid_record ) :
 if 43 - 43: I11i . IiII - iII111i * I1IiiI * iII111i
 if 90 - 90: i11iIiiIii * i1IIi
 if 88 - 88: i11iIiiIii - OoOoOO00
 if 53 - 53: iIii1I11I1II1 % I1Ii111 / Oo0Ooo % Oo0Ooo
 eid_record . rloc_count = len ( parent . registered_rlocs )
 iIiIi1IiiiI1 = eid_record . encode ( )
 eid_record . print_record ( "Merged Map-Notify " , False )
 if 64 - 64: OoO0O00 + I1ii11iIi11i / OoO0O00 * I1Ii111 . Oo0Ooo
 if 5 - 5: iII111i - iIii1I11I1II1 * IiII
 if 52 - 52: OOooOOo
 if 50 - 50: OoOoOO00 % o0oOOo0O0Ooo - II111iiii - i1IIi
 for iI11IiI1 in parent . registered_rlocs :
  OOO0Oo = lisp_rloc_record ( )
  OOO0Oo . store_rloc_entry ( iI11IiI1 )
  iIiIi1IiiiI1 += OOO0Oo . encode ( )
  OOO0Oo . print_record ( "  " )
  del ( OOO0Oo )
  if 24 - 24: I1ii11iIi11i * IiII + iII111i / Oo0Ooo - ooOoO0o . IiII
  if 81 - 81: OoooooooOO + OOooOOo
  if 7 - 7: I11i + ooOoO0o
  if 28 - 28: OoooooooOO * iII111i / oO0o / iII111i
  if 80 - 80: OoO0O00 - I1IiiI + OOooOOo - iII111i / i1IIi
 for iI11IiI1 in parent . registered_rlocs :
  Ii1II1I11i1I = iI11IiI1 . rloc
  Ii1ii1 = lisp_map_notify ( lisp_sockets )
  Ii1ii1 . record_count = 1
  o00oO = map_register . key_id
  Ii1ii1 . key_id = o00oO
  Ii1ii1 . alg_id = map_register . alg_id
  Ii1ii1 . auth_len = map_register . auth_len
  Ii1ii1 . nonce = map_register . nonce
  Ii1ii1 . nonce_key = lisp_hex_string ( Ii1ii1 . nonce )
  Ii1ii1 . etr . copy_address ( Ii1II1I11i1I )
  Ii1ii1 . etr_port = map_register . sport
  Ii1ii1 . site = parent . site
  IiiiIi1iiii11 = Ii1ii1 . encode ( iIiIi1IiiiI1 , parent . site . auth_key [ o00oO ] )
  Ii1ii1 . print_notify ( )
  if 83 - 83: iIii1I11I1II1
  if 73 - 73: I1ii11iIi11i + II111iiii . i11iIiiIii + I1IiiI + I1ii11iIi11i
  if 6 - 6: O0 % Ii1I . oO0o
  if 91 - 91: O0 - oO0o * O0
  o0Oo = Ii1ii1 . nonce_key
  if ( lisp_map_notify_queue . has_key ( o0Oo ) ) :
   oOoO0O0O0O0 = lisp_map_notify_queue [ o0Oo ]
   oOoO0O0O0O0 . retransmit_timer . cancel ( )
   del ( oOoO0O0O0O0 )
   if 84 - 84: IiII . OoO0O00
  lisp_map_notify_queue [ o0Oo ] = Ii1ii1
  if 73 - 73: OoOoOO00
  if 47 - 47: oO0o
  if 17 - 17: IiII
  if 47 - 47: I11i . I1IiiI % ooOoO0o . i11iIiiIii
  lprint ( "Send merged Map-Notify to ETR {}" . format ( red ( Ii1II1I11i1I . print_address ( ) , False ) ) )
  if 63 - 63: I1ii11iIi11i % I11i % OoooooooOO
  lisp_send ( lisp_sockets , Ii1II1I11i1I , LISP_CTRL_PORT , IiiiIi1iiii11 )
  if 100 - 100: O0
  parent . site . map_notifies_sent += 1
  if 9 - 9: Ii1I
  if 87 - 87: I1IiiI
  if 56 - 56: OOooOOo % oO0o - OoOoOO00
  if 27 - 27: I1ii11iIi11i - IiII * OoooooooOO * I1ii11iIi11i + i11iIiiIii . IiII
  Ii1ii1 . retransmit_timer = threading . Timer ( LISP_MAP_NOTIFY_INTERVAL ,
 lisp_retransmit_map_notify , [ Ii1ii1 ] )
  Ii1ii1 . retransmit_timer . start ( )
  if 81 - 81: oO0o / iIii1I11I1II1
 return
 if 15 - 15: Ii1I + I1IiiI . OOooOOo / OoooooooOO + I11i - I11i
 if 27 - 27: Ii1I / o0oOOo0O0Ooo . iIii1I11I1II1 . I1IiiI - OoO0O00
 if 28 - 28: ooOoO0o
 if 88 - 88: oO0o
 if 77 - 77: ooOoO0o + I1Ii111 . OoOoOO00
 if 2 - 2: i1IIi - IiII + iIii1I11I1II1 % i1IIi * II111iiii
 if 26 - 26: I11i
def lisp_build_map_notify ( lisp_sockets , eid_records , eid_list , record_count ,
 source , port , nonce , key_id , alg_id , auth_len , site , map_register_ack ) :
 if 57 - 57: I1ii11iIi11i + I1Ii111 + i11iIiiIii . i1IIi / i11iIiiIii
 o0Oo = lisp_hex_string ( nonce ) + source . print_address ( )
 if 43 - 43: Ii1I % I11i
 if 5 - 5: OoooooooOO % i11iIiiIii * o0oOOo0O0Ooo * OoooooooOO - o0oOOo0O0Ooo % I11i
 if 58 - 58: i11iIiiIii % Ii1I + Oo0Ooo - OoOoOO00 - i11iIiiIii / O0
 if 36 - 36: OOooOOo
 if 42 - 42: OOooOOo * ooOoO0o * i11iIiiIii + OoooooooOO . iIii1I11I1II1
 if 95 - 95: i1IIi * O0 / II111iiii * OoOoOO00 * I1IiiI
 lisp_remove_eid_from_map_notify_queue ( eid_list )
 if ( lisp_map_notify_queue . has_key ( o0Oo ) ) :
  Ii1ii1 = lisp_map_notify_queue [ o0Oo ]
  OO0o0OO0 = red ( source . print_address_no_iid ( ) , False )
  lprint ( "Map-Notify with nonce 0x{} pending for xTR {}" . format ( lisp_hex_string ( Ii1ii1 . nonce ) , OO0o0OO0 ) )
  if 38 - 38: OOooOOo - OoOoOO00 / OoO0O00 / o0oOOo0O0Ooo - i11iIiiIii
  return
  if 4 - 4: I1IiiI * o0oOOo0O0Ooo - I11i - OoooooooOO . OoooooooOO
  if 79 - 79: oO0o - iII111i
 Ii1ii1 = lisp_map_notify ( lisp_sockets )
 Ii1ii1 . record_count = record_count
 key_id = key_id
 Ii1ii1 . key_id = key_id
 Ii1ii1 . alg_id = alg_id
 Ii1ii1 . auth_len = auth_len
 Ii1ii1 . nonce = nonce
 Ii1ii1 . nonce_key = lisp_hex_string ( nonce )
 Ii1ii1 . etr . copy_address ( source )
 Ii1ii1 . etr_port = port
 Ii1ii1 . site = site
 Ii1ii1 . eid_list = eid_list
 if 34 - 34: OoooooooOO + Ii1I - iII111i + OoooooooOO / I1IiiI
 if 39 - 39: o0oOOo0O0Ooo . i1IIi * OoO0O00 / II111iiii / I1ii11iIi11i * OOooOOo
 if 39 - 39: O0 . OOooOOo
 if 95 - 95: I11i
 if ( map_register_ack == False ) :
  o0Oo = Ii1ii1 . nonce_key
  lisp_map_notify_queue [ o0Oo ] = Ii1ii1
  if 58 - 58: I1ii11iIi11i / i11iIiiIii + iII111i + I11i / oO0o
  if 8 - 8: I1ii11iIi11i
 if ( map_register_ack ) :
  lprint ( "Send Map-Notify to ack Map-Register" )
 else :
  lprint ( "Send Map-Notify for RLOC-set change" )
  if 100 - 100: OoooooooOO / I11i - Ii1I
  if 11 - 11: OoO0O00
  if 20 - 20: Oo0Ooo
  if 34 - 34: I1Ii111 % i11iIiiIii / oO0o - i1IIi . o0oOOo0O0Ooo / oO0o
  if 68 - 68: I1Ii111 % Ii1I * Oo0Ooo - O0 . IiII
 IiiiIi1iiii11 = Ii1ii1 . encode ( eid_records , site . auth_key [ key_id ] )
 Ii1ii1 . print_notify ( )
 if 1 - 1: I1ii11iIi11i
 if ( map_register_ack == False ) :
  OOOo = lisp_eid_record ( )
  OOOo . decode ( eid_records )
  OOOo . print_record ( "  " , False )
  if 18 - 18: i11iIiiIii % OoO0O00 % OOooOOo . OOooOOo * Ii1I / II111iiii
  if 81 - 81: iII111i % IiII / I11i
  if 50 - 50: IiII + i1IIi % I1Ii111
  if 72 - 72: I1Ii111
  if 6 - 6: II111iiii - i1IIi
 lisp_send_map_notify ( lisp_sockets , IiiiIi1iiii11 , Ii1ii1 . etr , port )
 site . map_notifies_sent += 1
 if 78 - 78: OoOoOO00 - Oo0Ooo * II111iiii % iIii1I11I1II1 . i11iIiiIii % iII111i
 if ( map_register_ack ) : return
 if 85 - 85: I1ii11iIi11i + OOooOOo % i1IIi
 if 13 - 13: OOooOOo + i11iIiiIii / OOooOOo . O0 . OoO0O00 - Ii1I
 if 31 - 31: OoOoOO00 * o0oOOo0O0Ooo / O0 . iII111i / i11iIiiIii
 if 22 - 22: I1IiiI . OoooooooOO * I1ii11iIi11i + i11iIiiIii - O0 + i11iIiiIii
 if 98 - 98: OOooOOo + I1IiiI / IiII / OoooooooOO / OOooOOo
 if 8 - 8: OoooooooOO * OOooOOo * iII111i - iII111i
 Ii1ii1 . retransmit_timer = threading . Timer ( LISP_MAP_NOTIFY_INTERVAL ,
 lisp_retransmit_map_notify , [ Ii1ii1 ] )
 Ii1ii1 . retransmit_timer . start ( )
 return
 if 32 - 32: I1Ii111
 if 28 - 28: I11i . i11iIiiIii % iIii1I11I1II1 + OoOoOO00
 if 4 - 4: OOooOOo + I1ii11iIi11i - iII111i + OOooOOo / IiII
 if 23 - 23: iIii1I11I1II1 + OoooooooOO + ooOoO0o . iII111i . Oo0Ooo - iIii1I11I1II1
 if 25 - 25: O0 + I1IiiI % OOooOOo / Oo0Ooo . IiII / I1Ii111
 if 84 - 84: ooOoO0o . O0 + I1IiiI * OoO0O00 - I1IiiI
 if 24 - 24: Ii1I
 if 23 - 23: Oo0Ooo * i1IIi / I1IiiI . I11i - I1ii11iIi11i . iIii1I11I1II1
def lisp_send_map_notify_ack ( lisp_sockets , eid_records , map_notify , ms ) :
 map_notify . map_notify_ack = True
 if 15 - 15: O0 + o0oOOo0O0Ooo / oO0o
 if 27 - 27: Ii1I * II111iiii / oO0o
 if 99 - 99: I11i + ooOoO0o % I11i + O0 - Ii1I - I1Ii111
 if 3 - 3: Oo0Ooo . I1IiiI
 IiiiIi1iiii11 = map_notify . encode ( eid_records , ms . password )
 map_notify . print_notify ( )
 if 61 - 61: OoO0O00 - I1ii11iIi11i . Ii1I * i11iIiiIii
 if 97 - 97: ooOoO0o
 if 58 - 58: iII111i
 if 47 - 47: II111iiii % Oo0Ooo . iIii1I11I1II1 . oO0o
 Ii1II1I11i1I = ms . map_server
 lprint ( "Send Map-Notify-Ack to {}" . format (
 red ( Ii1II1I11i1I . print_address ( ) , False ) ) )
 lisp_send ( lisp_sockets , Ii1II1I11i1I , LISP_CTRL_PORT , IiiiIi1iiii11 )
 return
 if 52 - 52: I11i * I1IiiI % I11i - iII111i - Ii1I - OoooooooOO
 if 15 - 15: iII111i
 if 95 - 95: i11iIiiIii . Ii1I / II111iiii + II111iiii + Ii1I / I11i
 if 72 - 72: I1Ii111 . I1Ii111 * O0 + I1ii11iIi11i / Oo0Ooo
 if 96 - 96: oO0o . ooOoO0o * Oo0Ooo % ooOoO0o + I1Ii111 + iIii1I11I1II1
 if 45 - 45: II111iiii
 if 42 - 42: ooOoO0o
 if 62 - 62: II111iiii * o0oOOo0O0Ooo . OoO0O00 / II111iiii
def lisp_send_multicast_map_notify ( lisp_sockets , site_eid , eid_list , xtr ) :
 if 5 - 5: OoO0O00 + O0 . OoooooooOO + I1IiiI + i1IIi * OOooOOo
 Ii1ii1 = lisp_map_notify ( lisp_sockets )
 Ii1ii1 . record_count = 1
 Ii1ii1 . nonce = lisp_get_control_nonce ( )
 Ii1ii1 . nonce_key = lisp_hex_string ( Ii1ii1 . nonce )
 Ii1ii1 . etr . copy_address ( xtr )
 Ii1ii1 . etr_port = LISP_CTRL_PORT
 Ii1ii1 . eid_list = eid_list
 o0Oo = Ii1ii1 . nonce_key
 if 19 - 19: OoooooooOO + i11iIiiIii / II111iiii - Oo0Ooo . OOooOOo
 if 10 - 10: oO0o * Oo0Ooo
 if 55 - 55: OoO0O00 - i1IIi - I11i * oO0o
 if 91 - 91: I1Ii111
 if 77 - 77: I1ii11iIi11i . ooOoO0o - iIii1I11I1II1 + Ii1I % II111iiii * II111iiii
 if 41 - 41: II111iiii + Oo0Ooo - IiII / I1Ii111 - OOooOOo . oO0o
 lisp_remove_eid_from_map_notify_queue ( Ii1ii1 . eid_list )
 if ( lisp_map_notify_queue . has_key ( o0Oo ) ) :
  Ii1ii1 = lisp_map_notify_queue [ o0Oo ]
  lprint ( "Map-Notify with nonce 0x{} pending for ITR {}" . format ( Ii1ii1 . nonce , red ( xtr . print_address_no_iid ( ) , False ) ) )
  if 100 - 100: ooOoO0o / I1ii11iIi11i * OoOoOO00 . I1ii11iIi11i . o0oOOo0O0Ooo * iIii1I11I1II1
  return
  if 15 - 15: iII111i + o0oOOo0O0Ooo / IiII
  if 33 - 33: OoooooooOO . IiII * o0oOOo0O0Ooo
  if 41 - 41: Ii1I . iII111i . o0oOOo0O0Ooo % OoooooooOO % IiII
  if 81 - 81: IiII * i11iIiiIii + i1IIi + OOooOOo . i1IIi
  if 6 - 6: i11iIiiIii - oO0o % OoO0O00 + iIii1I11I1II1
 lisp_map_notify_queue [ o0Oo ] = Ii1ii1
 if 69 - 69: IiII
 if 13 - 13: i11iIiiIii
 if 49 - 49: OoOoOO00
 if 61 - 61: I1Ii111 / I1Ii111 / iII111i / ooOoO0o - I1IiiI . o0oOOo0O0Ooo
 ooo0O0OO = site_eid . rtrs_in_rloc_set ( )
 if ( ooo0O0OO ) :
  if ( site_eid . is_rtr_in_rloc_set ( xtr ) ) : ooo0O0OO = False
  if 61 - 61: OoooooooOO + I11i + I11i / i1IIi
  if 97 - 97: i11iIiiIii + oO0o % OOooOOo . OoO0O00 . OOooOOo % ooOoO0o
  if 93 - 93: I1IiiI % i11iIiiIii
  if 45 - 45: OoooooooOO * o0oOOo0O0Ooo - OOooOOo + O0
  if 64 - 64: iII111i * I1ii11iIi11i - OoOoOO00
 OOOo = lisp_eid_record ( )
 OOOo . record_ttl = 1440
 OOOo . eid . copy_address ( site_eid . eid )
 OOOo . group . copy_address ( site_eid . group )
 OOOo . rloc_count = 0
 for oOO0O in site_eid . registered_rlocs :
  if ( ooo0O0OO ^ oOO0O . is_rtr ( ) ) : continue
  OOOo . rloc_count += 1
  if 1 - 1: i1IIi / OoO0O00 % i1IIi % i11iIiiIii / i1IIi
 IiiiIi1iiii11 = OOOo . encode ( )
 if 8 - 8: O0 / OOooOOo + iII111i % iIii1I11I1II1 % iIii1I11I1II1 . ooOoO0o
 if 47 - 47: OoO0O00 / o0oOOo0O0Ooo / Ii1I * I1IiiI % ooOoO0o / I1Ii111
 if 80 - 80: I1Ii111 / O0 * O0
 if 40 - 40: OoO0O00 - oO0o / o0oOOo0O0Ooo . oO0o
 Ii1ii1 . print_notify ( )
 OOOo . print_record ( "  " , False )
 if 89 - 89: i11iIiiIii - II111iiii
 if 67 - 67: IiII % I1Ii111 + i11iIiiIii
 if 53 - 53: OOooOOo
 if 95 - 95: oO0o - OOooOOo % I1Ii111 / OoooooooOO % OoooooooOO - O0
 for oOO0O in site_eid . registered_rlocs :
  if ( ooo0O0OO ^ oOO0O . is_rtr ( ) ) : continue
  OOO0Oo = lisp_rloc_record ( )
  OOO0Oo . store_rloc_entry ( oOO0O )
  IiiiIi1iiii11 += OOO0Oo . encode ( )
  OOO0Oo . print_record ( "    " )
  if 21 - 21: I1Ii111 . i1IIi - iII111i % I1ii11iIi11i . OOooOOo
  if 52 - 52: Ii1I * I1ii11iIi11i
  if 21 - 21: I1IiiI . i11iIiiIii - o0oOOo0O0Ooo * II111iiii % iIii1I11I1II1
  if 9 - 9: I1ii11iIi11i + I11i
  if 20 - 20: iII111i + i1IIi / oO0o % OoooooooOO * OoOoOO00
 IiiiIi1iiii11 = Ii1ii1 . encode ( IiiiIi1iiii11 , "" )
 if ( IiiiIi1iiii11 == None ) : return
 if 70 - 70: Oo0Ooo - OOooOOo * OOooOOo / o0oOOo0O0Ooo
 if 4 - 4: OoOoOO00 / OoO0O00
 if 66 - 66: I1Ii111 / OoOoOO00
 if 53 - 53: OoOoOO00 . i11iIiiIii - OoooooooOO
 lisp_send_map_notify ( lisp_sockets , IiiiIi1iiii11 , xtr , LISP_CTRL_PORT )
 if 92 - 92: O0 - i11iIiiIii + OoO0O00 - OoooooooOO - o0oOOo0O0Ooo
 if 25 - 25: oO0o / oO0o / Ii1I / O0
 if 56 - 56: ooOoO0o
 if 19 - 19: O0 * I1IiiI + I1ii11iIi11i
 Ii1ii1 . retransmit_timer = threading . Timer ( LISP_MAP_NOTIFY_INTERVAL ,
 lisp_retransmit_map_notify , [ Ii1ii1 ] )
 Ii1ii1 . retransmit_timer . start ( )
 return
 if 25 - 25: I11i - ooOoO0o / OoO0O00 / iII111i - OoO0O00
 if 86 - 86: OoO0O00
 if 89 - 89: OoooooooOO % iII111i * I1ii11iIi11i + I1ii11iIi11i . Oo0Ooo
 if 4 - 4: I11i
 if 8 - 8: IiII
 if 1 - 1: ooOoO0o . IiII
 if 4 - 4: iIii1I11I1II1 % I1IiiI - OoooooooOO / iII111i
def lisp_queue_multicast_map_notify ( lisp_sockets , rle_list ) :
 Oo00oO0 = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
 if 3 - 3: oO0o % I1IiiI - O0
 for Oo0ooO in rle_list :
  IiIIiIII1I1i = lisp_site_eid_lookup ( Oo0ooO [ 0 ] , Oo0ooO [ 1 ] , True )
  if ( IiIIiIII1I1i == None ) : continue
  if 25 - 25: OoO0O00 % IiII . i1IIi / OoOoOO00 + OoOoOO00
  if 53 - 53: II111iiii % i1IIi + ooOoO0o . I1Ii111
  if 52 - 52: I1IiiI + I1Ii111 * oO0o / i11iIiiIii * iIii1I11I1II1
  if 27 - 27: Oo0Ooo
  if 85 - 85: iIii1I11I1II1 . o0oOOo0O0Ooo + oO0o
  if 79 - 79: O0 - iIii1I11I1II1 + i1IIi . I11i
  if 21 - 21: II111iiii
  I1iiiII1Ii1i1 = IiIIiIII1I1i . registered_rlocs
  if ( len ( I1iiiII1Ii1i1 ) == 0 ) :
   iII1iI1IIiii = { }
   for iIiIi1I in IiIIiIII1I1i . individual_registrations . values ( ) :
    for oOO0O in iIiIi1I . registered_rlocs :
     if ( oOO0O . is_rtr ( ) == False ) : continue
     iII1iI1IIiii [ oOO0O . rloc . print_address ( ) ] = oOO0O
     if 45 - 45: o0oOOo0O0Ooo + iIii1I11I1II1 / O0
     if 2 - 2: I11i + I1IiiI . IiII . OoOoOO00 * oO0o - ooOoO0o
   I1iiiII1Ii1i1 = iII1iI1IIiii . values ( )
   if 29 - 29: OoO0O00
   if 78 - 78: iII111i * ooOoO0o + O0 % ooOoO0o + OoO0O00
   if 41 - 41: II111iiii . oO0o + O0 % i1IIi . Ii1I
   if 90 - 90: ooOoO0o * I1IiiI / II111iiii % Oo0Ooo % OoooooooOO
   if 78 - 78: OoooooooOO . IiII
   if 55 - 55: I11i / I1ii11iIi11i * O0 + IiII % I11i
  OOooOo00Ooo = [ ]
  o00O0o0O0O0o = False
  if ( IiIIiIII1I1i . eid . address == 0 and IiIIiIII1I1i . eid . mask_len == 0 ) :
   o0ooOO0OOO00O0 = [ ]
   II11Ii1i1iiII = [ ]
   if ( len ( I1iiiII1Ii1i1 ) != 0 and I1iiiII1Ii1i1 [ 0 ] . rle != None ) :
    II11Ii1i1iiII = I1iiiII1Ii1i1 [ 0 ] . rle . rle_nodes
    if 38 - 38: I1ii11iIi11i + i1IIi % iIii1I11I1II1
   for IiioOoo in II11Ii1i1iiII :
    OOooOo00Ooo . append ( IiioOoo . address )
    o0ooOO0OOO00O0 . append ( IiioOoo . address . print_address_no_iid ( ) )
    if 96 - 96: OoOoOO00 - OoOoOO00
   lprint ( "Notify existing RLE-nodes {}" . format ( o0ooOO0OOO00O0 ) )
  else :
   if 59 - 59: OoOoOO00 / iII111i * i11iIiiIii
   if 61 - 61: I1Ii111 % oO0o - OOooOOo
   if 91 - 91: o0oOOo0O0Ooo * Oo0Ooo
   if 59 - 59: iIii1I11I1II1 / Oo0Ooo % II111iiii
   if 55 - 55: ooOoO0o - IiII + o0oOOo0O0Ooo
   for oOO0O in I1iiiII1Ii1i1 :
    if ( oOO0O . is_rtr ( ) ) : OOooOo00Ooo . append ( oOO0O . rloc )
    if 48 - 48: O0 - iIii1I11I1II1 * OOooOOo
    if 33 - 33: I11i
    if 63 - 63: Ii1I % II111iiii / OoOoOO00 + Oo0Ooo
    if 28 - 28: OoO0O00 + I1IiiI . oO0o + II111iiii - O0
    if 32 - 32: oO0o
   o00O0o0O0O0o = ( len ( OOooOo00Ooo ) != 0 )
   if ( o00O0o0O0O0o == False ) :
    oOoooo = lisp_site_eid_lookup ( Oo0ooO [ 0 ] , Oo00oO0 , False )
    if ( oOoooo == None ) : continue
    if 62 - 62: i11iIiiIii + OoooooooOO + IiII - OoO0O00 / oO0o * iIii1I11I1II1
    for oOO0O in oOoooo . registered_rlocs :
     if ( oOO0O . rloc . is_null ( ) ) : continue
     OOooOo00Ooo . append ( oOO0O . rloc )
     if 91 - 91: o0oOOo0O0Ooo - i11iIiiIii + Oo0Ooo % iIii1I11I1II1
     if 58 - 58: iII111i / ooOoO0o - I1Ii111 + I1Ii111 * ooOoO0o
     if 48 - 48: iII111i % O0 % Ii1I * OoO0O00 . OoO0O00
     if 74 - 74: OoO0O00 * i1IIi + I1ii11iIi11i / o0oOOo0O0Ooo / i1IIi
     if 94 - 94: Ii1I
     if 13 - 13: OoO0O00 - II111iiii . iII111i + OoOoOO00 / i11iIiiIii
   if ( len ( OOooOo00Ooo ) == 0 ) :
    lprint ( "No ITRs or RTRs found for {}, Map-Notify suppressed" . format ( green ( IiIIiIII1I1i . print_eid_tuple ( ) , False ) ) )
    if 32 - 32: ooOoO0o / II111iiii / I1ii11iIi11i
    continue
    if 34 - 34: iIii1I11I1II1
    if 47 - 47: OOooOOo * iII111i
    if 71 - 71: IiII - OoooooooOO * i11iIiiIii . OoooooooOO % i1IIi . Oo0Ooo
    if 3 - 3: OoO0O00 + i11iIiiIii + oO0o * IiII
    if 19 - 19: iII111i / II111iiii . I1Ii111 * I1IiiI - OOooOOo
    if 70 - 70: OoO0O00
  for iI11IiI1 in OOooOo00Ooo :
   lprint ( "Build Map-Notify to {}TR {} for {}" . format ( "R" if o00O0o0O0O0o else "x" , red ( iI11IiI1 . print_address_no_iid ( ) , False ) ,
   # OOooOOo * OoO0O00 / I1Ii111
 green ( IiIIiIII1I1i . print_eid_tuple ( ) , False ) ) )
   if 96 - 96: iII111i * iII111i / iII111i + I1IiiI
   i1I1i = [ IiIIiIII1I1i . print_eid_tuple ( ) ]
   lisp_send_multicast_map_notify ( lisp_sockets , IiIIiIII1I1i , i1I1i , iI11IiI1 )
   time . sleep ( .001 )
   if 87 - 87: IiII * I1Ii111 * O0 % O0 + i1IIi
   if 54 - 54: OOooOOo
 return
 if 88 - 88: OoooooooOO / iII111i + i1IIi
 if 64 - 64: IiII % I11i / iIii1I11I1II1
 if 66 - 66: Ii1I
 if 55 - 55: OOooOOo + I1IiiI + IiII . Ii1I * oO0o
 if 71 - 71: IiII - iII111i % I1IiiI * iII111i
 if 27 - 27: ooOoO0o - OoO0O00
 if 83 - 83: iII111i * OoOoOO00 - O0 * Ii1I
 if 79 - 79: I11i / iII111i % Ii1I / OoOoOO00 % O0 / IiII
def lisp_find_sig_in_rloc_set ( packet , rloc_count ) :
 for iIi1I1 in range ( rloc_count ) :
  OOO0Oo = lisp_rloc_record ( )
  packet = OOO0Oo . decode ( packet , None )
  i1ii11ii1iiI = OOO0Oo . json
  if ( i1ii11ii1iiI == None ) : continue
  if 67 - 67: oO0o . I1IiiI % i1IIi - OoO0O00
  try :
   i1ii11ii1iiI = json . loads ( i1ii11ii1iiI . json_string )
  except :
   lprint ( "Found corrupted JSON signature" )
   continue
   if 33 - 33: I1IiiI / I1IiiI / I1ii11iIi11i * IiII / Ii1I
   if 55 - 55: i11iIiiIii / OoooooooOO - Ii1I * Oo0Ooo . I1Ii111
  if ( i1ii11ii1iiI . has_key ( "signature" ) == False ) : continue
  return ( OOO0Oo )
  if 96 - 96: IiII / OoooooooOO + i11iIiiIii . Ii1I
 return ( None )
 if 64 - 64: OoooooooOO / IiII - IiII . Ii1I % Oo0Ooo
 if 35 - 35: iII111i * I1IiiI * Oo0Ooo + I1Ii111 + i1IIi - ooOoO0o
 if 23 - 23: II111iiii - O0
 if 58 - 58: o0oOOo0O0Ooo * OoO0O00 + OoO0O00
 if 93 - 93: IiII - I1ii11iIi11i % I11i + i1IIi % OoO0O00
 if 20 - 20: oO0o . Oo0Ooo + IiII - II111iiii % Ii1I
 if 64 - 64: Ii1I % OoO0O00 + OOooOOo % OoOoOO00 + IiII
 if 92 - 92: iII111i * Oo0Ooo - OoOoOO00
 if 33 - 33: i11iIiiIii - OoOoOO00 . OOooOOo * II111iiii . Ii1I
 if 59 - 59: OoOoOO00
 if 29 - 29: iII111i - II111iiii * OoooooooOO * OoooooooOO
 if 15 - 15: IiII / OOooOOo / iIii1I11I1II1 / OoOoOO00
 if 91 - 91: i11iIiiIii % O0 . Oo0Ooo / I1Ii111
 if 62 - 62: Oo0Ooo . II111iiii % OoO0O00 . Ii1I * OOooOOo + II111iiii
 if 7 - 7: OOooOOo
 if 22 - 22: Oo0Ooo + ooOoO0o
 if 71 - 71: OOooOOo . Ii1I * i11iIiiIii . I11i
 if 9 - 9: O0 / I1ii11iIi11i . iII111i . O0 + IiII % I11i
 if 27 - 27: i11iIiiIii - I1ii11iIi11i / O0 - i1IIi + I1IiiI * iII111i
def lisp_get_eid_hash ( eid ) :
 iI1iIIIIiiii = None
 for IiI1Iiii in lisp_eid_hashes :
  if 7 - 7: OoOoOO00 + OoO0O00 * I1IiiI
  if 63 - 63: I1ii11iIi11i + iII111i * i1IIi
  if 63 - 63: I1ii11iIi11i / II111iiii % oO0o + ooOoO0o . Ii1I % I11i
  if 59 - 59: I1Ii111 % o0oOOo0O0Ooo - I1IiiI * i1IIi
  IiIIi11i111 = IiI1Iiii . instance_id
  if ( IiIIi11i111 == - 1 ) : IiI1Iiii . instance_id = eid . instance_id
  if 5 - 5: I1IiiI
  ii1i = eid . is_more_specific ( IiI1Iiii )
  IiI1Iiii . instance_id = IiIIi11i111
  if ( ii1i ) :
   iI1iIIIIiiii = 128 - IiI1Iiii . mask_len
   break
   if 79 - 79: OoooooooOO . OoOoOO00 * OoO0O00 + I11i / iII111i - Ii1I
   if 9 - 9: I1IiiI - IiII . iIii1I11I1II1
 if ( iI1iIIIIiiii == None ) : return ( None )
 if 99 - 99: iII111i / o0oOOo0O0Ooo
 ii1i1II11II1i = eid . address
 IIiiI1 = ""
 for iIi1I1 in range ( 0 , iI1iIIIIiiii / 16 ) :
  o0o00O0oOooO0 = ii1i1II11II1i & 0xffff
  o0o00O0oOooO0 = hex ( o0o00O0oOooO0 ) [ 2 : - 1 ]
  IIiiI1 = o0o00O0oOooO0 . zfill ( 4 ) + ":" + IIiiI1
  ii1i1II11II1i >>= 16
  if 92 - 92: iII111i * i11iIiiIii * o0oOOo0O0Ooo * OoO0O00
 if ( iI1iIIIIiiii % 16 != 0 ) :
  o0o00O0oOooO0 = ii1i1II11II1i & 0xff
  o0o00O0oOooO0 = hex ( o0o00O0oOooO0 ) [ 2 : - 1 ]
  IIiiI1 = o0o00O0oOooO0 . zfill ( 2 ) + ":" + IIiiI1
  if 70 - 70: Ii1I
 return ( IIiiI1 [ 0 : - 1 ] )
 if 51 - 51: i1IIi % Oo0Ooo
 if 32 - 32: OoOoOO00 + iIii1I11I1II1 . OoO0O00 . I1ii11iIi11i . IiII
 if 97 - 97: ooOoO0o * ooOoO0o * iIii1I11I1II1 * I1Ii111 + iII111i + OoOoOO00
 if 8 - 8: Oo0Ooo . oO0o + II111iiii
 if 100 - 100: OoOoOO00 . IiII / OoO0O00 * OoooooooOO - OoOoOO00
 if 98 - 98: OoO0O00 / I1ii11iIi11i + I1ii11iIi11i
 if 70 - 70: i1IIi % Oo0Ooo % I1Ii111 + I11i . ooOoO0o
 if 66 - 66: i11iIiiIii % I11i / Oo0Ooo * oO0o
 if 7 - 7: O0 - Ii1I - oO0o
 if 95 - 95: i1IIi - OOooOOo / OoOoOO00 + I1ii11iIi11i + O0
 if 10 - 10: ooOoO0o - OOooOOo + i1IIi * Ii1I
def lisp_lookup_public_key ( eid ) :
 IiIIi11i111 = eid . instance_id
 if 78 - 78: iIii1I11I1II1
 if 76 - 76: ooOoO0o - i11iIiiIii * I11i / I1IiiI - OOooOOo
 if 41 - 41: iII111i
 if 91 - 91: I1Ii111
 if 54 - 54: o0oOOo0O0Ooo . i1IIi / iII111i
 ii1III1 = lisp_get_eid_hash ( eid )
 if ( ii1III1 == None ) : return ( [ None , None , False ] )
 if 93 - 93: I1Ii111 . II111iiii
 ii1III1 = "hash-" + ii1III1
 oo0O0O = lisp_address ( LISP_AFI_NAME , ii1III1 , len ( ii1III1 ) , IiIIi11i111 )
 OOo0oOOO0 = lisp_address ( LISP_AFI_NONE , "" , 0 , IiIIi11i111 )
 if 71 - 71: iII111i . II111iiii + i11iIiiIii
 if 41 - 41: oO0o . o0oOOo0O0Ooo . I11i
 if 53 - 53: I11i
 if 64 - 64: OoO0O00 + I11i / I1IiiI . II111iiii
 oOoooo = lisp_site_eid_lookup ( oo0O0O , OOo0oOOO0 , True )
 if ( oOoooo == None ) : return ( [ oo0O0O , None , False ] )
 if 79 - 79: I1Ii111 + IiII / OoooooooOO
 if 53 - 53: Ii1I
 if 85 - 85: OoO0O00 + II111iiii / OoO0O00 . II111iiii * OoOoOO00 * I1IiiI
 if 19 - 19: iII111i / Ii1I + iIii1I11I1II1 * O0 - Oo0Ooo
 iII1II1i1iI = None
 for I1II in oOoooo . registered_rlocs :
  iiIiIiIiII = I1II . json
  if ( iiIiIiIiII == None ) : continue
  try :
   iiIiIiIiII = json . loads ( iiIiIiIiII . json_string )
  except :
   lprint ( "Registered RLOC JSON format is invalid for {}" . format ( ii1III1 ) )
   if 89 - 89: o0oOOo0O0Ooo / i11iIiiIii
   return ( [ oo0O0O , None , False ] )
   if 42 - 42: II111iiii + i1IIi
  if ( iiIiIiIiII . has_key ( "public-key" ) == False ) : continue
  iII1II1i1iI = iiIiIiIiII [ "public-key" ]
  break
  if 67 - 67: OoOoOO00
 return ( [ oo0O0O , iII1II1i1iI , True ] )
 if 5 - 5: Oo0Ooo / OoooooooOO / Ii1I * I1Ii111
 if 37 - 37: Ii1I * o0oOOo0O0Ooo
 if 39 - 39: OoooooooOO
 if 37 - 37: OoO0O00 . iII111i
 if 32 - 32: II111iiii
 if 11 - 11: i11iIiiIii - OOooOOo . i1IIi + OOooOOo - O0
 if 17 - 17: i1IIi % o0oOOo0O0Ooo % ooOoO0o / I11i
 if 68 - 68: OoOoOO00
def lisp_verify_cga_sig ( eid , rloc_record ) :
 if 14 - 14: iIii1I11I1II1 + oO0o / ooOoO0o
 if 20 - 20: I1ii11iIi11i . II111iiii % I1Ii111 + I1Ii111 / OoooooooOO . Ii1I
 if 98 - 98: OoooooooOO - i11iIiiIii - iII111i + Ii1I - I1IiiI
 if 75 - 75: OOooOOo
 if 25 - 25: iII111i / I1ii11iIi11i - ooOoO0o
 i1i11 = json . loads ( rloc_record . json . json_string )
 if 53 - 53: IiII / OoooooooOO / ooOoO0o + Oo0Ooo - OOooOOo - iIii1I11I1II1
 if ( lisp_get_eid_hash ( eid ) ) :
  I1IiI11 = eid
 elif ( i1i11 . has_key ( "signature-eid" ) ) :
  O0iIII = i1i11 [ "signature-eid" ]
  I1IiI11 = lisp_address ( LISP_AFI_IPV6 , O0iIII , 0 , 0 )
 else :
  lprint ( "  No signature-eid found in RLOC-record" )
  return ( False )
  if 53 - 53: I11i . OoooooooOO * I1Ii111
  if 100 - 100: O0
  if 99 - 99: OoO0O00 * I1Ii111 % I11i / OoOoOO00
  if 95 - 95: II111iiii . ooOoO0o + O0
  if 58 - 58: iII111i + iIii1I11I1II1 % oO0o % OoooooooOO
 oo0O0O , iII1II1i1iI , O0OOo0oO0OO0 = lisp_lookup_public_key ( I1IiI11 )
 if ( oo0O0O == None ) :
  Ii1i1 = green ( I1IiI11 . print_address ( ) , False )
  lprint ( "  Could not parse hash in EID {}" . format ( Ii1i1 ) )
  return ( False )
  if 64 - 64: II111iiii - oO0o / iIii1I11I1II1 . Ii1I
  if 23 - 23: o0oOOo0O0Ooo + I1IiiI
 ooOoOO0o = "found" if O0OOo0oO0OO0 else bold ( "not found" , False )
 Ii1i1 = green ( oo0O0O . print_address ( ) , False )
 lprint ( "  Lookup for crypto-hashed EID {} {}" . format ( Ii1i1 , ooOoOO0o ) )
 if ( O0OOo0oO0OO0 == False ) : return ( False )
 if 60 - 60: I1ii11iIi11i * i11iIiiIii + oO0o
 if ( iII1II1i1iI == None ) :
  lprint ( "  RLOC-record with public-key not found" )
  return ( False )
  if 59 - 59: I11i
  if 61 - 61: IiII * I1Ii111 * OoO0O00 / oO0o - OoooooooOO
 iI11i11ii11 = iII1II1i1iI [ 0 : 8 ] + "..." + iII1II1i1iI [ - 8 : : ]
 lprint ( "  RLOC-record with public-key '{}' found" . format ( iI11i11ii11 ) )
 if 48 - 48: II111iiii
 if 79 - 79: II111iiii % II111iiii
 if 85 - 85: OoooooooOO / o0oOOo0O0Ooo * I11i + iII111i
 if 99 - 99: i11iIiiIii / oO0o . i11iIiiIii
 if 46 - 46: I1ii11iIi11i
 II1I1IIi1111I = i1i11 [ "signature" ]
 if 3 - 3: iII111i / i11iIiiIii % OOooOOo + Ii1I . Oo0Ooo
 try :
  i1i11 = binascii . a2b_base64 ( II1I1IIi1111I )
 except :
  lprint ( "  Incorrect padding in signature string" )
  return ( False )
  if 16 - 16: oO0o / Ii1I % i11iIiiIii % I1IiiI * I1ii11iIi11i
  if 4 - 4: iIii1I11I1II1 + Ii1I % I1Ii111 . OoOoOO00 % OoooooooOO + II111iiii
 i111Ii = len ( i1i11 )
 if ( i111Ii & 1 ) :
  lprint ( "  Signature length is odd, length {}" . format ( i111Ii ) )
  return ( False )
  if 14 - 14: oO0o . OOooOOo * OOooOOo . OoO0O00
  if 27 - 27: OOooOOo - iII111i - IiII
  if 14 - 14: i11iIiiIii . I1ii11iIi11i % OoOoOO00 * Ii1I / OoO0O00
  if 56 - 56: o0oOOo0O0Ooo / I1IiiI + I11i + I1IiiI
  if 34 - 34: Oo0Ooo / i11iIiiIii - ooOoO0o
 i11I1iiI1iI = I1IiI11 . print_address ( )
 if 77 - 77: OoOoOO00 * OoooooooOO
 if 41 - 41: iIii1I11I1II1 - O0 . II111iiii + I1IiiI - II111iiii / oO0o
 if 35 - 35: ooOoO0o - OoOoOO00 / iIii1I11I1II1 / OOooOOo
 if 38 - 38: i1IIi % OoooooooOO
 iII1II1i1iI = binascii . a2b_base64 ( iII1II1i1iI )
 try :
  o0Oo = ecdsa . VerifyingKey . from_pem ( iII1II1i1iI )
 except :
  IiiiIi = bold ( "Bad public-key" , False )
  lprint ( "  {}, not in PEM format" . format ( IiiiIi ) )
  return ( False )
  if 54 - 54: OOooOOo * I1ii11iIi11i + OoooooooOO
  if 58 - 58: i1IIi - OoooooooOO * OOooOOo . ooOoO0o + O0 + o0oOOo0O0Ooo
  if 87 - 87: OOooOOo + I1Ii111 + O0 / oO0o / i11iIiiIii
  if 60 - 60: O0 . II111iiii
  if 69 - 69: II111iiii / ooOoO0o - OoOoOO00 / OOooOOo
  if 52 - 52: OoO0O00 % I11i + o0oOOo0O0Ooo % OoOoOO00
  if 46 - 46: o0oOOo0O0Ooo % O0
  if 30 - 30: oO0o
  if 64 - 64: O0
  if 70 - 70: oO0o % I1IiiI . iIii1I11I1II1 - Oo0Ooo + OoOoOO00 % O0
  if 91 - 91: I1Ii111 - oO0o * ooOoO0o - I1ii11iIi11i + IiII + O0
 try :
  OoOoO00OoOOo = o0Oo . verify ( i1i11 , i11I1iiI1iI , hashfunc = hashlib . sha256 )
 except :
  lprint ( "  Signature library failed for signature data '{}'" . format ( i11I1iiI1iI ) )
  if 18 - 18: OoOoOO00 / IiII / o0oOOo0O0Ooo . OOooOOo
  lprint ( "  Signature used '{}'" . format ( II1I1IIi1111I ) )
  return ( False )
  if 35 - 35: I11i . ooOoO0o % I11i / iII111i / O0 % I11i
 return ( OoOoO00OoOOo )
 if 29 - 29: I1Ii111 + Ii1I
 if 100 - 100: Ii1I + I1Ii111 / iIii1I11I1II1 / i1IIi % OoOoOO00
 if 6 - 6: oO0o + ooOoO0o
 if 13 - 13: Oo0Ooo . IiII % iII111i + i1IIi / OOooOOo
 if 1 - 1: I11i * i1IIi * Oo0Ooo % O0
 if 41 - 41: OOooOOo % OoOoOO00
 if 82 - 82: I11i . IiII
 if 27 - 27: I1Ii111 % O0 * OoooooooOO . Oo0Ooo
 if 51 - 51: I11i
 if 80 - 80: Oo0Ooo + oO0o
def lisp_remove_eid_from_map_notify_queue ( eid_list ) :
 if 76 - 76: I1IiiI * OoooooooOO - i11iIiiIii / I11i / Oo0Ooo
 if 82 - 82: IiII % ooOoO0o
 if 100 - 100: Oo0Ooo . oO0o - iII111i + OoooooooOO
 if 27 - 27: Oo0Ooo . I1Ii111 - i1IIi * I1IiiI
 if 96 - 96: I1ii11iIi11i - Ii1I . I1ii11iIi11i
 Oo0Oo00O000 = [ ]
 for o0oOo0oo0 in eid_list :
  for iiI1IiII1iI in lisp_map_notify_queue :
   Ii1ii1 = lisp_map_notify_queue [ iiI1IiII1iI ]
   if ( o0oOo0oo0 not in Ii1ii1 . eid_list ) : continue
   if 54 - 54: IiII - I11i % OoooooooOO
   Oo0Oo00O000 . append ( iiI1IiII1iI )
   iiI1I = Ii1ii1 . retransmit_timer
   if ( iiI1I ) : iiI1I . cancel ( )
   if 87 - 87: OoOoOO00 * I11i * Ii1I / O0 + OOooOOo
   lprint ( "Remove from Map-Notify queue nonce 0x{} for EID {}" . format ( Ii1ii1 . nonce_key , green ( o0oOo0oo0 , False ) ) )
   if 81 - 81: iIii1I11I1II1 * iII111i . iIii1I11I1II1 - i1IIi % OOooOOo - I1Ii111
   if 77 - 77: iIii1I11I1II1 % II111iiii
   if 33 - 33: II111iiii
   if 60 - 60: iIii1I11I1II1 / OOooOOo
   if 78 - 78: i11iIiiIii
   if 20 - 20: OoooooooOO * OoooooooOO - OOooOOo
   if 34 - 34: I1ii11iIi11i * i1IIi % OoooooooOO / I1IiiI
 for iiI1IiII1iI in Oo0Oo00O000 : lisp_map_notify_queue . pop ( iiI1IiII1iI )
 return
 if 39 - 39: OoO0O00 + IiII - II111iiii % I11i
 if 80 - 80: o0oOOo0O0Ooo * ooOoO0o
 if 87 - 87: I1Ii111 + O0 / I1ii11iIi11i / OoOoOO00 . Oo0Ooo - IiII
 if 24 - 24: OoOoOO00
 if 19 - 19: ooOoO0o
 if 43 - 43: O0 . I1Ii111 % OoooooooOO / I1IiiI . o0oOOo0O0Ooo - OoOoOO00
 if 46 - 46: I11i - OoooooooOO % o0oOOo0O0Ooo
 if 7 - 7: OoooooooOO - I1Ii111 * IiII
def lisp_decrypt_map_register ( packet ) :
 if 20 - 20: o0oOOo0O0Ooo . OoooooooOO * I1IiiI . Oo0Ooo * OoOoOO00
 if 3 - 3: I1Ii111 % i11iIiiIii % O0 % II111iiii
 if 8 - 8: OoooooooOO * ooOoO0o
 if 26 - 26: i11iIiiIii + oO0o - i1IIi
 if 71 - 71: I1IiiI % I1Ii111 / oO0o % oO0o / iIii1I11I1II1 + I1Ii111
 O00O0OO = socket . ntohl ( struct . unpack ( "I" , packet [ 0 : 4 ] ) [ 0 ] )
 O00oOO0OO00 = ( O00O0OO >> 13 ) & 0x1
 if ( O00oOO0OO00 == 0 ) : return ( packet )
 if 61 - 61: I1ii11iIi11i % I1IiiI % OoOoOO00
 oo0Oo00oOO = ( O00O0OO >> 14 ) & 0x7
 if 88 - 88: OoO0O00
 if 82 - 82: OOooOOo / I11i / OoooooooOO % oO0o
 if 27 - 27: oO0o + IiII
 if 5 - 5: iIii1I11I1II1 + OoOoOO00 * I1Ii111 * i11iIiiIii
 try :
  II11iI11i1 = lisp_ms_encryption_keys [ oo0Oo00oOO ]
  II11iI11i1 = II11iI11i1 . zfill ( 32 )
  OO000OOOo0Oo = "0" * 8
 except :
  lprint ( "Cannot decrypt Map-Register with key-id {}" . format ( oo0Oo00oOO ) )
  return ( None )
  if 37 - 37: I1IiiI / OoO0O00 . OoO0O00 + i11iIiiIii - oO0o
  if 57 - 57: I1IiiI . OoO0O00
 o0 = bold ( "Decrypt" , False )
 lprint ( "{} Map-Register with key-id {}" . format ( o0 , oo0Oo00oOO ) )
 if 49 - 49: II111iiii + iII111i
 if 85 - 85: I11i / i11iIiiIii
 if 33 - 33: iIii1I11I1II1 % O0 + II111iiii * OOooOOo . Ii1I * iII111i
 if 48 - 48: I11i * iIii1I11I1II1 / oO0o
 i1o0 = chacha . ChaCha ( II11iI11i1 , OO000OOOo0Oo , 20 ) . decrypt ( packet [ 4 : : ] )
 return ( packet [ 0 : 4 ] + i1o0 )
 if 34 - 34: i1IIi + oO0o * Oo0Ooo * I1Ii111 % OoooooooOO % ooOoO0o
 if 17 - 17: I1ii11iIi11i + o0oOOo0O0Ooo / OoO0O00 . Oo0Ooo - o0oOOo0O0Ooo / oO0o
 if 87 - 87: ooOoO0o
 if 74 - 74: i11iIiiIii . i11iIiiIii . iIii1I11I1II1
 if 100 - 100: i11iIiiIii - oO0o + iIii1I11I1II1 * OoOoOO00 % OOooOOo % i11iIiiIii
 if 26 - 26: O0
 if 97 - 97: OOooOOo + I11i % I1Ii111 % i11iIiiIii / I1ii11iIi11i
def lisp_process_map_register ( lisp_sockets , packet , source , sport ) :
 global lisp_registered_count
 if 21 - 21: O0 + iIii1I11I1II1 / i11iIiiIii . OOooOOo * i1IIi
 if 3 - 3: i1IIi % o0oOOo0O0Ooo + OoOoOO00
 if 32 - 32: OoO0O00 . Oo0Ooo * iIii1I11I1II1
 if 12 - 12: O0 + I1ii11iIi11i + I11i . I1Ii111
 if 48 - 48: Ii1I . iIii1I11I1II1 - iIii1I11I1II1 * I11i . OoooooooOO
 if 73 - 73: Ii1I / II111iiii - iIii1I11I1II1 . ooOoO0o * II111iiii . OOooOOo
 packet = lisp_decrypt_map_register ( packet )
 if ( packet == None ) : return
 if 50 - 50: iIii1I11I1II1 + OoOoOO00 % O0 + OoO0O00 . i11iIiiIii / oO0o
 IiiI1iI1i1 = lisp_map_register ( )
 oO0ooOoOooO00o00 , packet = IiiI1iI1i1 . decode ( packet )
 if ( packet == None ) :
  lprint ( "Could not decode Map-Register packet" )
  return
  if 24 - 24: OOooOOo . I1Ii111
 IiiI1iI1i1 . sport = sport
 if 59 - 59: Ii1I - I1ii11iIi11i % Ii1I . iII111i
 IiiI1iI1i1 . print_map_register ( )
 if 78 - 78: I1ii11iIi11i
 if 69 - 69: iII111i
 if 87 - 87: ooOoO0o % OOooOOo - iII111i
 if 65 - 65: IiII + I1IiiI % I1Ii111 - oO0o
 o00o = True
 if ( IiiI1iI1i1 . auth_len == LISP_SHA1_160_AUTH_DATA_LEN ) :
  o00o = True
  if 43 - 43: o0oOOo0O0Ooo + oO0o % iII111i * IiII
 if ( IiiI1iI1i1 . alg_id == LISP_SHA_256_128_ALG_ID ) :
  o00o = False
  if 55 - 55: O0 . I1ii11iIi11i % OOooOOo % iII111i + I11i / OoOoOO00
  if 50 - 50: OoOoOO00 - i11iIiiIii - OOooOOo . iIii1I11I1II1
  if 97 - 97: oO0o % OOooOOo . OoooooooOO * Ii1I
  if 100 - 100: I1ii11iIi11i / Ii1I % Oo0Ooo
  if 83 - 83: O0 . I1Ii111 % I1ii11iIi11i
 OO0O0O00Oo = [ ]
 if 9 - 9: i11iIiiIii - i11iIiiIii / OOooOOo - ooOoO0o % OoOoOO00 + Ii1I
 if 3 - 3: iII111i / I1ii11iIi11i / I1IiiI - Oo0Ooo
 if 71 - 71: i11iIiiIii + Oo0Ooo % i11iIiiIii - i11iIiiIii
 if 84 - 84: oO0o
 ooo000O0O = None
 iI111iIII1I = packet
 OOooOo0o0oOoo = [ ]
 O000oOooO0oo = IiiI1iI1i1 . record_count
 for iIi1I1 in range ( O000oOooO0oo ) :
  OOOo = lisp_eid_record ( )
  OOO0Oo = lisp_rloc_record ( )
  packet = OOOo . decode ( packet )
  if ( packet == None ) :
   lprint ( "Could not decode EID-record in Map-Register packet" )
   return
   if 14 - 14: II111iiii + OOooOOo * Ii1I * I1IiiI + OOooOOo . OOooOOo
  OOOo . print_record ( "  " , False )
  if 5 - 5: oO0o + OoooooooOO
  if 88 - 88: oO0o + OOooOOo
  if 14 - 14: I11i / i1IIi
  if 56 - 56: OoooooooOO
  oOoooo = lisp_site_eid_lookup ( OOOo . eid , OOOo . group ,
 False )
  if 59 - 59: I1ii11iIi11i + OoO0O00
  i11iiii11iIii = oOoooo . print_eid_tuple ( ) if oOoooo else None
  if 11 - 11: o0oOOo0O0Ooo
  if 77 - 77: o0oOOo0O0Ooo / iIii1I11I1II1 * iIii1I11I1II1 / o0oOOo0O0Ooo * iII111i
  if 26 - 26: Ii1I
  if 1 - 1: OoOoOO00 . o0oOOo0O0Ooo + Oo0Ooo % Oo0Ooo * I1ii11iIi11i
  if 50 - 50: IiII / i1IIi . I1ii11iIi11i
  if 75 - 75: I11i * oO0o + OoooooooOO . iII111i + OoO0O00
  if 44 - 44: II111iiii
  if ( oOoooo and oOoooo . accept_more_specifics == False ) :
   if ( oOoooo . eid_record_matches ( OOOo ) == False ) :
    O0Ii1IiiiI = oOoooo . parent_for_more_specifics
    if ( O0Ii1IiiiI ) : oOoooo = O0Ii1IiiiI
    if 32 - 32: I1Ii111 % oO0o * iII111i * OOooOOo
    if 45 - 45: oO0o / O0
    if 5 - 5: OoO0O00 / O0
    if 64 - 64: I11i / i1IIi
    if 68 - 68: Ii1I / oO0o - iII111i
    if 52 - 52: I11i / OoO0O00 - Ii1I
    if 11 - 11: OoooooooOO - i11iIiiIii - I1ii11iIi11i / o0oOOo0O0Ooo - Ii1I
    if 16 - 16: ooOoO0o + O0
  Ii1I111IiI11I = ( oOoooo and oOoooo . accept_more_specifics )
  if ( Ii1I111IiI11I ) :
   Oo0 = lisp_site_eid ( oOoooo . site )
   Oo0 . dynamic = True
   Oo0 . eid . copy_address ( OOOo . eid )
   Oo0 . group . copy_address ( OOOo . group )
   Oo0 . parent_for_more_specifics = oOoooo
   Oo0 . add_cache ( )
   Oo0 . inherit_from_ams_parent ( )
   oOoooo . more_specific_registrations . append ( Oo0 )
   oOoooo = Oo0
  else :
   oOoooo = lisp_site_eid_lookup ( OOOo . eid , OOOo . group ,
 True )
   if 85 - 85: I1ii11iIi11i . I1IiiI - I11i
   if 92 - 92: II111iiii / OOooOOo + I1ii11iIi11i * OoooooooOO
  Ii1i1 = OOOo . print_eid_tuple ( )
  if 89 - 89: ooOoO0o / ooOoO0o
  if ( oOoooo == None ) :
   iiIi11I1I1 = bold ( "Site not found" , False )
   lprint ( "  {} for EID {}{}" . format ( iiIi11I1I1 , green ( Ii1i1 , False ) ,
 ", matched non-ams {}" . format ( green ( i11iiii11iIii , False ) if i11iiii11iIii else "" ) ) )
   if 61 - 61: iIii1I11I1II1
   if 26 - 26: i11iIiiIii + OoO0O00 - i1IIi / OOooOOo
   if 71 - 71: OOooOOo . i1IIi
   if 48 - 48: ooOoO0o - Ii1I - I11i
   if 70 - 70: O0 * I11i . i1IIi - ooOoO0o
   packet = OOO0Oo . end_of_rlocs ( packet , OOOo . rloc_count )
   if ( packet == None ) :
    lprint ( "  Could not decode RLOC-record in Map-Register packet" )
    return
    if 93 - 93: OoooooooOO / o0oOOo0O0Ooo
   continue
   if 61 - 61: II111iiii / i1IIi . I1ii11iIi11i % iIii1I11I1II1
   if 66 - 66: iIii1I11I1II1 % OoOoOO00 + i1IIi * i11iIiiIii * OoooooooOO
  ooo000O0O = oOoooo . site
  if 36 - 36: iII111i - OoO0O00 + I1IiiI + Ii1I . OoooooooOO
  if ( Ii1I111IiI11I ) :
   iIIi1iI1I1IIi = oOoooo . parent_for_more_specifics . print_eid_tuple ( )
   lprint ( "  Found ams {} for site '{}' for registering prefix {}" . format ( green ( iIIi1iI1I1IIi , False ) , ooo000O0O . site_name , green ( Ii1i1 , False ) ) )
   if 75 - 75: oO0o * Oo0Ooo * O0
  else :
   iIIi1iI1I1IIi = green ( oOoooo . print_eid_tuple ( ) , False )
   lprint ( "  Found {} for site '{}' for registering prefix {}" . format ( iIIi1iI1I1IIi , ooo000O0O . site_name , green ( Ii1i1 , False ) ) )
   if 22 - 22: ooOoO0o / OoooooooOO . II111iiii / Ii1I * OoO0O00 . i1IIi
   if 62 - 62: oO0o % Ii1I - Ii1I
   if 16 - 16: OoO0O00 - O0 - OOooOOo - I11i % OoOoOO00
   if 7 - 7: I1Ii111 / OoOoOO00 . II111iiii
   if 9 - 9: I11i . I11i . OoooooooOO
   if 42 - 42: iII111i / oO0o / iII111i * OoO0O00
  if ( ooo000O0O . shutdown ) :
   lprint ( ( "  Rejecting registration for site '{}', configured in " +
 "admin-shutdown state" ) . format ( ooo000O0O . site_name ) )
   packet = OOO0Oo . end_of_rlocs ( packet , OOOo . rloc_count )
   continue
   if 25 - 25: OoOoOO00 - II111iiii + II111iiii . Ii1I * II111iiii
   if 12 - 12: IiII / Ii1I
   if 54 - 54: Oo0Ooo + Ii1I % OoooooooOO * OOooOOo / OoOoOO00
   if 39 - 39: I1IiiI % i11iIiiIii % Ii1I
   if 59 - 59: ooOoO0o % OoO0O00 / I1IiiI - II111iiii + OoooooooOO * i11iIiiIii
   if 58 - 58: IiII / Oo0Ooo + o0oOOo0O0Ooo
   if 71 - 71: Ii1I - IiII
   if 2 - 2: OoOoOO00 % IiII % OoO0O00 . i1IIi / I1Ii111 - iIii1I11I1II1
  o00oO = IiiI1iI1i1 . key_id
  if ( ooo000O0O . auth_key . has_key ( o00oO ) ) :
   oO0oOOoo0OO0 = ooo000O0O . auth_key [ o00oO ]
  else :
   oO0oOOoo0OO0 = ""
   if 25 - 25: iII111i / iII111i
   if 7 - 7: II111iiii * Ii1I * OoO0O00 / o0oOOo0O0Ooo
  O0Oo0O000 = lisp_verify_auth ( oO0ooOoOooO00o00 , IiiI1iI1i1 . alg_id ,
 IiiI1iI1i1 . auth_data , oO0oOOoo0OO0 )
  iIiIII1 = "dynamic " if oOoooo . dynamic else ""
  if 9 - 9: IiII . I11i . I1Ii111 / i1IIi * OoOoOO00 - O0
  O0Oo = bold ( "passed" if O0Oo0O000 else "failed" , False )
  o00oO = "key-id {}" . format ( o00oO ) if o00oO == IiiI1iI1i1 . key_id else "bad key-id {}" . format ( IiiI1iI1i1 . key_id )
  if 3 - 3: O0 / iIii1I11I1II1 % IiII + I11i
  lprint ( "  Authentication {} for {}EID-prefix {}, {}" . format ( O0Oo , iIiIII1 , green ( Ii1i1 , False ) , o00oO ) )
  if 43 - 43: Oo0Ooo % I11i
  if 53 - 53: OoOoOO00 % OoooooooOO * o0oOOo0O0Ooo % OoooooooOO
  if 47 - 47: iIii1I11I1II1 - OOooOOo + I1ii11iIi11i * ooOoO0o + Oo0Ooo + OoO0O00
  if 64 - 64: OoOoOO00 - OoOoOO00 . OoooooooOO + ooOoO0o
  if 100 - 100: ooOoO0o . OoooooooOO % i1IIi % OoO0O00
  if 26 - 26: OoOoOO00 * IiII
  Oo000O = True
  o00OoOO = ( lisp_get_eid_hash ( OOOo . eid ) != None )
  if ( o00OoOO or oOoooo . require_signature ) :
   Ooo00oooOoO = "Required " if oOoooo . require_signature else ""
   Ii1i1 = green ( Ii1i1 , False )
   I1II = lisp_find_sig_in_rloc_set ( packet , OOOo . rloc_count )
   if ( I1II == None ) :
    Oo000O = False
    lprint ( ( "  {}EID-crypto-hash signature verification {} " + "for EID-prefix {}, no signature found" ) . format ( Ooo00oooOoO ,
    # ooOoO0o * OOooOOo / I11i % I11i / OoooooooOO . I1Ii111
 bold ( "failed" , False ) , Ii1i1 ) )
   else :
    Oo000O = lisp_verify_cga_sig ( OOOo . eid , I1II )
    O0Oo = bold ( "passed" if Oo000O else "failed" , False )
    lprint ( ( "  {}EID-crypto-hash signature verification {} " + "for EID-prefix {}" ) . format ( Ooo00oooOoO , O0Oo , Ii1i1 ) )
    if 70 - 70: I1ii11iIi11i % I1ii11iIi11i / oO0o
    if 85 - 85: OoOoOO00 % I11i / Oo0Ooo + I11i - Oo0Ooo
    if 20 - 20: IiII
    if 81 - 81: Oo0Ooo / I1Ii111
  if ( O0Oo0O000 == False or Oo000O == False ) :
   packet = OOO0Oo . end_of_rlocs ( packet , OOOo . rloc_count )
   if ( packet == None ) :
    lprint ( "  Could not decode RLOC-record in Map-Register packet" )
    return
    if 20 - 20: o0oOOo0O0Ooo + ooOoO0o % i1IIi
   continue
   if 51 - 51: iII111i - ooOoO0o
   if 32 - 32: IiII - i11iIiiIii
   if 41 - 41: Ii1I % Ii1I * oO0o - I11i + iIii1I11I1II1 . ooOoO0o
   if 30 - 30: Ii1I * iII111i . II111iiii / i1IIi
   if 77 - 77: oO0o . IiII + I1ii11iIi11i . i1IIi
   if 49 - 49: I1Ii111 . OoooooooOO / o0oOOo0O0Ooo - iII111i - iII111i - i11iIiiIii
  if ( IiiI1iI1i1 . merge_register_requested ) :
   O0Ii1IiiiI = oOoooo
   O0Ii1IiiiI . inconsistent_registration = False
   if 37 - 37: OOooOOo
   if 79 - 79: I1Ii111 - OoO0O00 + ooOoO0o + oO0o . i11iIiiIii + i1IIi
   if 32 - 32: IiII . ooOoO0o / OoO0O00 / iII111i . iIii1I11I1II1 % IiII
   if 28 - 28: I1Ii111 + OoooooooOO + IiII . ooOoO0o . I1IiiI / oO0o
   if 66 - 66: Ii1I - I11i + Oo0Ooo . ooOoO0o
   if ( oOoooo . group . is_null ( ) ) :
    if ( O0Ii1IiiiI . site_id != IiiI1iI1i1 . site_id ) :
     O0Ii1IiiiI . site_id = IiiI1iI1i1 . site_id
     O0Ii1IiiiI . registered = False
     O0Ii1IiiiI . individual_registrations = { }
     O0Ii1IiiiI . registered_rlocs = [ ]
     lisp_registered_count -= 1
     if 89 - 89: IiII . II111iiii / OoO0O00 + I1ii11iIi11i * i11iIiiIii
     if 85 - 85: o0oOOo0O0Ooo - Oo0Ooo / I1Ii111
     if 100 - 100: OoO0O00 * iIii1I11I1II1 - IiII . i1IIi % i11iIiiIii % Oo0Ooo
   o0Oo = IiiI1iI1i1 . xtr_id
   if ( oOoooo . individual_registrations . has_key ( o0Oo ) ) :
    oOoooo = oOoooo . individual_registrations [ o0Oo ]
   else :
    oOoooo = lisp_site_eid ( ooo000O0O )
    oOoooo . eid . copy_address ( O0Ii1IiiiI . eid )
    oOoooo . group . copy_address ( O0Ii1IiiiI . group )
    oOoooo . encrypt_json = O0Ii1IiiiI . encrypt_json
    O0Ii1IiiiI . individual_registrations [ o0Oo ] = oOoooo
    if 22 - 22: ooOoO0o - OOooOOo
  else :
   oOoooo . inconsistent_registration = oOoooo . merge_register_requested
   if 90 - 90: i11iIiiIii . i11iIiiIii - iIii1I11I1II1
   if 20 - 20: ooOoO0o - i11iIiiIii
   if 23 - 23: OoO0O00 + I1IiiI / I1ii11iIi11i * I1ii11iIi11i % ooOoO0o
  oOoooo . map_registers_received += 1
  if 83 - 83: I1IiiI * i11iIiiIii - I1ii11iIi11i + I11i
  if 33 - 33: OoO0O00 . OoooooooOO % iII111i / oO0o * Ii1I + ooOoO0o
  if 29 - 29: oO0o
  if 21 - 21: i11iIiiIii . o0oOOo0O0Ooo
  if 78 - 78: Oo0Ooo
  IiiiIi = ( oOoooo . is_rloc_in_rloc_set ( source ) == False )
  if ( OOOo . record_ttl == 0 and IiiiIi ) :
   lprint ( "  Ignore deregistration request from {}" . format ( red ( source . print_address_no_iid ( ) , False ) ) )
   if 77 - 77: oO0o % Oo0Ooo % O0
   continue
   if 51 - 51: IiII % IiII + OOooOOo . II111iiii / I1ii11iIi11i
   if 4 - 4: o0oOOo0O0Ooo % I1IiiI * o0oOOo0O0Ooo * OoOoOO00 - Ii1I
   if 61 - 61: OoooooooOO - OoOoOO00 . O0 / ooOoO0o . Ii1I
   if 41 - 41: Oo0Ooo / OoOoOO00 % I1Ii111 - O0
   if 19 - 19: I1IiiI % I1Ii111 - O0 . iIii1I11I1II1 . I11i % O0
   if 88 - 88: ooOoO0o
  oo00ooo0o0 = oOoooo . registered_rlocs
  oOoooo . registered_rlocs = [ ]
  if 29 - 29: IiII / OOooOOo
  if 39 - 39: O0 + II111iiii
  if 94 - 94: OOooOOo % I1ii11iIi11i % O0 + iII111i
  if 62 - 62: iIii1I11I1II1 . OoOoOO00 / iIii1I11I1II1 + IiII
  I1ii1Iii1I1ii1 = packet
  for I1iII in range ( OOOo . rloc_count ) :
   OOO0Oo = lisp_rloc_record ( )
   packet = OOO0Oo . decode ( packet , None , oOoooo . encrypt_json )
   if ( packet == None ) :
    lprint ( "  Could not decode RLOC-record in Map-Register packet" )
    return
    if 64 - 64: O0
   OOO0Oo . print_record ( "    " )
   if 71 - 71: iIii1I11I1II1 % OoOoOO00
   if 83 - 83: ooOoO0o + I1Ii111 - OoooooooOO
   if 55 - 55: OoooooooOO * O0 - II111iiii / IiII
   if 18 - 18: II111iiii % O0 - o0oOOo0O0Ooo * ooOoO0o
   if ( len ( ooo000O0O . allowed_rlocs ) > 0 ) :
    oo0o00OO = OOO0Oo . rloc . print_address ( )
    if ( ooo000O0O . allowed_rlocs . has_key ( oo0o00OO ) == False ) :
     lprint ( ( "  Reject registration, RLOC {} not " + "configured in allowed RLOC-set" ) . format ( red ( oo0o00OO , False ) ) )
     if 74 - 74: I11i . oO0o + I11i * o0oOOo0O0Ooo / O0
     if 55 - 55: OoO0O00 / i11iIiiIii / o0oOOo0O0Ooo
     oOoooo . registered = False
     packet = OOO0Oo . end_of_rlocs ( packet ,
 OOOo . rloc_count - I1iII - 1 )
     break
     if 19 - 19: ooOoO0o * iII111i
     if 38 - 38: ooOoO0o
     if 35 - 35: o0oOOo0O0Ooo * IiII * Oo0Ooo
     if 34 - 34: I11i - OoooooooOO % i1IIi + I1IiiI
     if 14 - 14: I1IiiI . o0oOOo0O0Ooo / I1Ii111
     if 67 - 67: OoooooooOO . oO0o * OoOoOO00 - OoooooooOO
   I1II = lisp_rloc ( )
   I1II . store_rloc_from_record ( OOO0Oo , None , source )
   if 32 - 32: oO0o
   if 72 - 72: I1IiiI
   if 34 - 34: ooOoO0o % II111iiii / ooOoO0o
   if 87 - 87: Oo0Ooo
   if 7 - 7: iIii1I11I1II1
   if 85 - 85: iIii1I11I1II1 . O0
   if ( source . is_exact_match ( I1II . rloc ) ) :
    I1II . map_notify_requested = IiiI1iI1i1 . map_notify_requested
    if 43 - 43: II111iiii / OoOoOO00 + OOooOOo % Oo0Ooo * OOooOOo
    if 62 - 62: ooOoO0o * OOooOOo . I11i + Oo0Ooo - I1Ii111
    if 48 - 48: I1Ii111 * Oo0Ooo % OoO0O00 % Ii1I
    if 8 - 8: OoO0O00 . OoO0O00
    if 29 - 29: I11i + OoooooooOO % o0oOOo0O0Ooo - I1Ii111
   oOoooo . registered_rlocs . append ( I1II )
   if 45 - 45: II111iiii - OOooOOo / oO0o % O0 . iII111i . iII111i
   if 82 - 82: iIii1I11I1II1 % Oo0Ooo * i1IIi - I1Ii111 - I1ii11iIi11i / iII111i
  i1II11I11III = ( oOoooo . do_rloc_sets_match ( oo00ooo0o0 ) == False )
  if 12 - 12: I1ii11iIi11i % Ii1I * OoOoOO00 . iIii1I11I1II1 * I1Ii111 - OoOoOO00
  if 33 - 33: OoO0O00 * I1IiiI / i1IIi
  if 88 - 88: Ii1I / ooOoO0o - I11i % OoO0O00 * iII111i
  if 47 - 47: i11iIiiIii + Oo0Ooo % oO0o % O0
  if 98 - 98: oO0o - O0 / iII111i % oO0o % I1IiiI / i1IIi
  if 61 - 61: ooOoO0o + II111iiii
  if ( IiiI1iI1i1 . map_register_refresh and i1II11I11III and
 oOoooo . registered ) :
   lprint ( "  Reject registration, refreshes cannot change RLOC-set" )
   oOoooo . registered_rlocs = oo00ooo0o0
   continue
   if 54 - 54: OoOoOO00 * o0oOOo0O0Ooo . OoO0O00
   if 53 - 53: oO0o % OoO0O00 / OoO0O00 / I11i * Oo0Ooo
   if 13 - 13: i1IIi % iIii1I11I1II1 - iII111i - I1IiiI - IiII + iIii1I11I1II1
   if 22 - 22: IiII - OOooOOo + I1ii11iIi11i
   if 64 - 64: OoOoOO00
   if 79 - 79: IiII
  if ( oOoooo . registered == False ) :
   oOoooo . first_registered = lisp_get_timestamp ( )
   lisp_registered_count += 1
   if 65 - 65: Oo0Ooo - i11iIiiIii * OoOoOO00 . I1Ii111 . iIii1I11I1II1
  oOoooo . last_registered = lisp_get_timestamp ( )
  oOoooo . registered = ( OOOo . record_ttl != 0 )
  oOoooo . last_registerer = source
  if 48 - 48: iIii1I11I1II1 - oO0o / OoO0O00 + O0 . Ii1I + I1Ii111
  if 17 - 17: OoOoOO00 . Oo0Ooo - I1Ii111 / I1Ii111 + I11i % i1IIi
  if 31 - 31: OoooooooOO . O0 / OoO0O00 . I1Ii111
  if 41 - 41: OoooooooOO + iII111i . OOooOOo
  oOoooo . auth_sha1_or_sha2 = o00o
  oOoooo . proxy_reply_requested = IiiI1iI1i1 . proxy_reply_requested
  oOoooo . lisp_sec_present = IiiI1iI1i1 . lisp_sec_present
  oOoooo . map_notify_requested = IiiI1iI1i1 . map_notify_requested
  oOoooo . mobile_node_requested = IiiI1iI1i1 . mobile_node
  oOoooo . merge_register_requested = IiiI1iI1i1 . merge_register_requested
  if 73 - 73: oO0o + i1IIi + i11iIiiIii / I1ii11iIi11i
  oOoooo . use_register_ttl_requested = IiiI1iI1i1 . use_ttl_for_timeout
  if ( oOoooo . use_register_ttl_requested ) :
   oOoooo . register_ttl = OOOo . store_ttl ( )
  else :
   oOoooo . register_ttl = LISP_SITE_TIMEOUT_CHECK_INTERVAL * 3
   if 100 - 100: I1IiiI % ooOoO0o % OoooooooOO / i11iIiiIii + i11iIiiIii % IiII
  oOoooo . xtr_id_present = IiiI1iI1i1 . xtr_id_present
  if ( oOoooo . xtr_id_present ) :
   oOoooo . xtr_id = IiiI1iI1i1 . xtr_id
   oOoooo . site_id = IiiI1iI1i1 . site_id
   if 39 - 39: Ii1I % o0oOOo0O0Ooo + OOooOOo / iIii1I11I1II1
   if 40 - 40: iIii1I11I1II1 / iII111i % OOooOOo % i11iIiiIii
   if 57 - 57: II111iiii % OoO0O00 * i1IIi
   if 19 - 19: ooOoO0o . iIii1I11I1II1 + I1ii11iIi11i + I1ii11iIi11i / o0oOOo0O0Ooo . Oo0Ooo
   if 9 - 9: II111iiii % OoooooooOO
  if ( IiiI1iI1i1 . merge_register_requested ) :
   if ( O0Ii1IiiiI . merge_in_site_eid ( oOoooo ) ) :
    OO0O0O00Oo . append ( [ OOOo . eid , OOOo . group ] )
    if 4 - 4: i1IIi * i11iIiiIii % OoooooooOO + OoOoOO00 . oO0o
   if ( IiiI1iI1i1 . map_notify_requested ) :
    lisp_send_merged_map_notify ( lisp_sockets , O0Ii1IiiiI , IiiI1iI1i1 ,
 OOOo )
    if 95 - 95: I1ii11iIi11i * OoOoOO00 % o0oOOo0O0Ooo / O0 + ooOoO0o % OOooOOo
    if 48 - 48: i1IIi + IiII - iIii1I11I1II1 . i11iIiiIii % OOooOOo + I1ii11iIi11i
    if 95 - 95: ooOoO0o + OoOoOO00 . II111iiii + Ii1I
  if ( i1II11I11III == False ) : continue
  if ( len ( OO0O0O00Oo ) != 0 ) : continue
  if 81 - 81: OoooooooOO / OOooOOo / Oo0Ooo
  OOooOo0o0oOoo . append ( oOoooo . print_eid_tuple ( ) )
  if 26 - 26: iII111i
  if 93 - 93: Oo0Ooo + I1IiiI % OoOoOO00 / OOooOOo / I1ii11iIi11i
  if 6 - 6: IiII
  if 68 - 68: Oo0Ooo
  if 83 - 83: OOooOOo / iIii1I11I1II1 . OoO0O00 - oO0o % Oo0Ooo
  if 30 - 30: Ii1I . OoOoOO00 / oO0o . OoO0O00
  if 93 - 93: i11iIiiIii
  IiIi1Iii1Ii = copy . deepcopy ( OOOo )
  OOOo = OOOo . encode ( )
  OOOo += I1ii1Iii1I1ii1
  i1I1i = [ oOoooo . print_eid_tuple ( ) ]
  lprint ( "    Changed RLOC-set, Map-Notifying old RLOC-set" )
  if 77 - 77: O0 * I1Ii111 - Oo0Ooo / IiII / OoOoOO00 % O0
  for I1II in oo00ooo0o0 :
   if ( I1II . map_notify_requested == False ) : continue
   if ( I1II . rloc . is_exact_match ( source ) ) : continue
   lisp_build_map_notify ( lisp_sockets , OOOo , i1I1i , 1 , I1II . rloc ,
 LISP_CTRL_PORT , IiiI1iI1i1 . nonce , IiiI1iI1i1 . key_id ,
 IiiI1iI1i1 . alg_id , IiiI1iI1i1 . auth_len , ooo000O0O , False )
   if 12 - 12: iIii1I11I1II1 - I11i + OoooooooOO % O0 * I1ii11iIi11i
   if 95 - 95: iII111i . I1IiiI . O0 - Ii1I + OoOoOO00
   if 93 - 93: OoO0O00
   if 68 - 68: OOooOOo
   if 87 - 87: IiII * IiII - OoO0O00 / I1ii11iIi11i + OOooOOo / i11iIiiIii
  lisp_notify_subscribers ( lisp_sockets , IiIi1Iii1Ii , I1ii1Iii1I1ii1 ,
 oOoooo . eid , ooo000O0O )
  if 21 - 21: o0oOOo0O0Ooo / oO0o + oO0o + Oo0Ooo / o0oOOo0O0Ooo
  if 39 - 39: i11iIiiIii - OoO0O00 - i11iIiiIii / OoooooooOO
  if 15 - 15: i1IIi . iII111i + IiII / I1ii11iIi11i - i1IIi / iII111i
  if 27 - 27: OoOoOO00 / OoooooooOO + i1IIi % iIii1I11I1II1 / OoO0O00
  if 73 - 73: I1ii11iIi11i / OoOoOO00 / IiII + oO0o
 if ( len ( OO0O0O00Oo ) != 0 ) :
  lisp_queue_multicast_map_notify ( lisp_sockets , OO0O0O00Oo )
  if 73 - 73: I11i * o0oOOo0O0Ooo * I1IiiI . OoooooooOO % I1Ii111
  if 9 - 9: oO0o % I1Ii111 . O0 + I1ii11iIi11i - Ii1I - I1ii11iIi11i
  if 57 - 57: i11iIiiIii
  if 21 - 21: iIii1I11I1II1 / I1IiiI / iII111i
  if 19 - 19: Oo0Ooo / iIii1I11I1II1 / I11i
  if 71 - 71: iIii1I11I1II1 * I1IiiI
 if ( IiiI1iI1i1 . merge_register_requested ) : return
 if 35 - 35: O0
 if 10 - 10: Ii1I - I1Ii111 / Oo0Ooo + O0
 if 67 - 67: Ii1I % i11iIiiIii . Oo0Ooo
 if 78 - 78: I1IiiI - iIii1I11I1II1
 if 20 - 20: i11iIiiIii % I1IiiI % OoOoOO00
 if ( IiiI1iI1i1 . map_notify_requested and ooo000O0O != None ) :
  lisp_build_map_notify ( lisp_sockets , iI111iIII1I , OOooOo0o0oOoo ,
 IiiI1iI1i1 . record_count , source , sport , IiiI1iI1i1 . nonce ,
 IiiI1iI1i1 . key_id , IiiI1iI1i1 . alg_id , IiiI1iI1i1 . auth_len ,
 ooo000O0O , True )
  if 85 - 85: I11i + OoOoOO00 * O0 * O0
 return
 if 92 - 92: i11iIiiIii
 if 16 - 16: I11i . ooOoO0o - Oo0Ooo / OoO0O00 . i1IIi
 if 59 - 59: ooOoO0o - ooOoO0o % I11i + OoO0O00
 if 88 - 88: Ii1I - ooOoO0o . Oo0Ooo
 if 83 - 83: I11i + Oo0Ooo . I1ii11iIi11i * I1ii11iIi11i
 if 80 - 80: i1IIi * I11i - OOooOOo / II111iiii * iIii1I11I1II1
 if 42 - 42: OoOoOO00 . I11i % II111iiii
 if 19 - 19: OoooooooOO
def lisp_process_unicast_map_notify ( lisp_sockets , packet , source ) :
 Ii1ii1 = lisp_map_notify ( "" )
 packet = Ii1ii1 . decode ( packet )
 if ( packet == None ) :
  lprint ( "Could not decode Map-Notify packet" )
  return
  if 31 - 31: I11i . OoOoOO00 - O0 * iII111i % I1Ii111 - II111iiii
  if 21 - 21: OOooOOo . Oo0Ooo - i1IIi
 Ii1ii1 . print_notify ( )
 if ( Ii1ii1 . record_count == 0 ) : return
 if 56 - 56: I11i
 ii = Ii1ii1 . eid_records
 if 74 - 74: I1IiiI * OoO0O00
 for iIi1I1 in range ( Ii1ii1 . record_count ) :
  OOOo = lisp_eid_record ( )
  ii = OOOo . decode ( ii )
  if ( packet == None ) : return
  OOOo . print_record ( "  " , False )
  Ii1i1 = OOOo . print_eid_tuple ( )
  if 21 - 21: i1IIi / ooOoO0o % ooOoO0o - IiII * Oo0Ooo
  if 93 - 93: OoO0O00 + O0
  if 36 - 36: i1IIi * oO0o
  if 51 - 51: iIii1I11I1II1 / o0oOOo0O0Ooo % OOooOOo * Oo0Ooo . I1ii11iIi11i - oO0o
  if 91 - 91: OOooOOo % OoooooooOO
  o0Oo0 = lisp_map_cache_lookup ( OOOo . eid , OOOo . eid )
  if ( o0Oo0 == None ) :
   iIIi1iI1I1IIi = green ( Ii1i1 , False )
   lprint ( "Ignoring Map-Notify EID {}, no subscribe-request entry" . format ( iIIi1iI1I1IIi ) )
   if 52 - 52: OOooOOo + OoO0O00
   continue
   if 96 - 96: OOooOOo % O0 - Oo0Ooo % oO0o / I1IiiI . i1IIi
   if 42 - 42: i1IIi
   if 52 - 52: OoO0O00 % iII111i % O0
   if 11 - 11: i1IIi / i11iIiiIii + Ii1I % Oo0Ooo % O0
   if 50 - 50: oO0o . I1Ii111
   if 38 - 38: iIii1I11I1II1 . Ii1I
   if 82 - 82: OOooOOo * Ii1I + I1ii11iIi11i . OoO0O00
  if ( o0Oo0 . action != LISP_SEND_PUBSUB_ACTION ) :
   if ( o0Oo0 . subscribed_eid == None ) :
    iIIi1iI1I1IIi = green ( Ii1i1 , False )
    lprint ( "Ignoring Map-Notify for non-subscribed EID {}" . format ( iIIi1iI1I1IIi ) )
    if 15 - 15: O0
    continue
    if 44 - 44: Ii1I . Oo0Ooo . I1Ii111 + oO0o
    if 32 - 32: OOooOOo - II111iiii + IiII * iIii1I11I1II1 - Oo0Ooo
    if 25 - 25: ooOoO0o
    if 33 - 33: Oo0Ooo
    if 11 - 11: I11i
    if 55 - 55: i11iIiiIii * OoOoOO00 - OoOoOO00 * OoO0O00 / iII111i
    if 64 - 64: iIii1I11I1II1 . Ii1I * Oo0Ooo - OoO0O00
    if 74 - 74: I1IiiI / o0oOOo0O0Ooo
  ooOOO00oO00Oo = [ ]
  if ( o0Oo0 . action == LISP_SEND_PUBSUB_ACTION ) :
   o0Oo0 = lisp_mapping ( OOOo . eid , OOOo . group , [ ] )
   o0Oo0 . add_cache ( )
   OoO00Oo = copy . deepcopy ( OOOo . eid )
   Ii1iIIiIi1IiI = copy . deepcopy ( OOOo . group )
  else :
   OoO00Oo = o0Oo0 . subscribed_eid
   Ii1iIIiIi1IiI = o0Oo0 . subscribed_group
   ooOOO00oO00Oo = o0Oo0 . rloc_set
   o0Oo0 . delete_rlocs_from_rloc_probe_list ( )
   o0Oo0 . rloc_set = [ ]
   if 60 - 60: oO0o * I1Ii111
   if 81 - 81: oO0o - OOooOOo - oO0o
   if 54 - 54: oO0o % I11i
   if 71 - 71: oO0o / I1ii11iIi11i . Ii1I % II111iiii
   if 22 - 22: iIii1I11I1II1 - OoooooooOO
  o0Oo0 . mapping_source = None if source == "lisp-itr" else source
  o0Oo0 . map_cache_ttl = OOOo . store_ttl ( )
  o0Oo0 . subscribed_eid = OoO00Oo
  o0Oo0 . subscribed_group = Ii1iIIiIi1IiI
  if 8 - 8: ooOoO0o % i11iIiiIii
  if 41 - 41: I1Ii111 . ooOoO0o - i11iIiiIii + Ii1I . OOooOOo . OoOoOO00
  if 70 - 70: i1IIi % OoOoOO00 / iII111i + i11iIiiIii % ooOoO0o + IiII
  if 58 - 58: OOooOOo / i11iIiiIii . Oo0Ooo % iII111i
  if 92 - 92: OoOoOO00 / ooOoO0o % iII111i / iIii1I11I1II1
  if ( len ( ooOOO00oO00Oo ) != 0 and OOOo . rloc_count == 0 ) :
   o0Oo0 . build_best_rloc_set ( )
   lisp_write_ipc_map_cache ( True , o0Oo0 )
   lprint ( "Update {} map-cache entry with no RLOC-set" . format ( green ( Ii1i1 , False ) ) )
   if 73 - 73: O0 % i11iIiiIii
   continue
   if 16 - 16: O0
   if 15 - 15: i1IIi % i11iIiiIii
   if 18 - 18: Ii1I . OoO0O00 . iII111i * oO0o + O0
   if 35 - 35: OoOoOO00 . oO0o / II111iiii
   if 97 - 97: Ii1I + I1Ii111 / II111iiii
   if 14 - 14: iII111i / IiII / oO0o
   if 55 - 55: OoO0O00 % O0
  Ooo00O0ooOo = ooooo = 0
  for I1iII in range ( OOOo . rloc_count ) :
   OOO0Oo = lisp_rloc_record ( )
   ii = OOO0Oo . decode ( ii , None )
   OOO0Oo . print_record ( "    " )
   if 5 - 5: OOooOOo . OOooOOo % I11i
   if 81 - 81: Oo0Ooo
   if 75 - 75: I1Ii111 * iIii1I11I1II1
   if 49 - 49: ooOoO0o * I11i / OOooOOo
   ooOoOO0o = False
   for I1I111iIiI in ooOOO00oO00Oo :
    if ( I1I111iIiI . rloc . is_exact_match ( OOO0Oo . rloc ) ) :
     ooOoOO0o = True
     break
     if 94 - 94: Ii1I . I1Ii111 * I11i . ooOoO0o . oO0o
     if 54 - 54: Oo0Ooo
   if ( ooOoOO0o ) :
    I1II = copy . deepcopy ( I1I111iIiI )
    ooooo += 1
   else :
    I1II = lisp_rloc ( )
    Ooo00O0ooOo += 1
    if 2 - 2: OoooooooOO / o0oOOo0O0Ooo / Oo0Ooo
    if 100 - 100: O0 . i11iIiiIii % I1Ii111 % OoooooooOO
    if 88 - 88: IiII - OOooOOo * Ii1I * iII111i . OoO0O00 % IiII
    if 24 - 24: OOooOOo / oO0o * OOooOOo
    if 35 - 35: OoooooooOO + I1ii11iIi11i + Oo0Ooo - i11iIiiIii / o0oOOo0O0Ooo . II111iiii
   I1II . store_rloc_from_record ( OOO0Oo , None , o0Oo0 . mapping_source )
   o0Oo0 . rloc_set . append ( I1II )
   if 63 - 63: O0
   if 64 - 64: i11iIiiIii / oO0o . oO0o - Oo0Ooo
  lprint ( "Update {} map-cache entry with {}/{} new/replaced RLOCs" . format ( green ( Ii1i1 , False ) , Ooo00O0ooOo , ooooo ) )
  if 48 - 48: i1IIi + I1ii11iIi11i + I1Ii111 - iII111i
  if 3 - 3: i1IIi + OoooooooOO * ooOoO0o + I1Ii111 % OOooOOo / IiII
  if 70 - 70: oO0o + i1IIi % o0oOOo0O0Ooo - I11i
  if 74 - 74: i11iIiiIii
  if 93 - 93: I1Ii111 % OOooOOo * I1IiiI % iII111i / iIii1I11I1II1 + OoO0O00
  o0Oo0 . build_best_rloc_set ( )
  lisp_write_ipc_map_cache ( True , o0Oo0 )
  if 6 - 6: I11i
  if 70 - 70: ooOoO0o + OoooooooOO % OoOoOO00 % oO0o / Ii1I . I11i
  if 63 - 63: I1ii11iIi11i - ooOoO0o . OOooOOo / O0 . iIii1I11I1II1 - Ii1I
  if 6 - 6: Ii1I
  if 60 - 60: iII111i + I1IiiI
  if 36 - 36: i1IIi . O0 . OoO0O00 % OOooOOo * I11i / Ii1I
 ii1i = lisp_get_map_server ( source )
 if ( ii1i == None ) :
  lprint ( "Cannot find Map-Server for Map-Notify source address {}" . format ( source . print_address_no_iid ( ) ) )
  if 16 - 16: Oo0Ooo
  return
  if 44 - 44: iIii1I11I1II1 - II111iiii . IiII . i1IIi
 lisp_send_map_notify_ack ( lisp_sockets , ii , Ii1ii1 , ii1i )
 if 37 - 37: OoooooooOO + Oo0Ooo - Oo0Ooo + I1ii11iIi11i . I1Ii111 / I1IiiI
 if 60 - 60: I1IiiI % Ii1I / I1Ii111 + Ii1I
 if 43 - 43: I1ii11iIi11i + I11i
 if 83 - 83: II111iiii + o0oOOo0O0Ooo - I1Ii111
 if 100 - 100: IiII - OoOoOO00 / I11i
 if 33 - 33: I1Ii111 * OoOoOO00 . I1ii11iIi11i % I1Ii111
 if 87 - 87: Oo0Ooo
 if 65 - 65: ooOoO0o . I1IiiI
 if 51 - 51: IiII
 if 43 - 43: oO0o - I11i . i11iIiiIii
def lisp_process_multicast_map_notify ( packet , source ) :
 Ii1ii1 = lisp_map_notify ( "" )
 packet = Ii1ii1 . decode ( packet )
 if ( packet == None ) :
  lprint ( "Could not decode Map-Notify packet" )
  return
  if 78 - 78: i11iIiiIii + Oo0Ooo * Ii1I - o0oOOo0O0Ooo % i11iIiiIii
  if 30 - 30: I1IiiI % oO0o * OoooooooOO
 Ii1ii1 . print_notify ( )
 if ( Ii1ii1 . record_count == 0 ) : return
 if 64 - 64: I1IiiI
 ii = Ii1ii1 . eid_records
 if 11 - 11: I1ii11iIi11i % iII111i / II111iiii % ooOoO0o % IiII
 for iIi1I1 in range ( Ii1ii1 . record_count ) :
  OOOo = lisp_eid_record ( )
  ii = OOOo . decode ( ii )
  if ( packet == None ) : return
  OOOo . print_record ( "  " , False )
  if 14 - 14: ooOoO0o / IiII . o0oOOo0O0Ooo
  if 27 - 27: I1IiiI - OOooOOo . II111iiii * I1ii11iIi11i % ooOoO0o / I1IiiI
  if 90 - 90: o0oOOo0O0Ooo / I1ii11iIi11i - oO0o - Ii1I - I1IiiI + I1Ii111
  if 93 - 93: I1IiiI - I11i . I1IiiI - iIii1I11I1II1
  o0Oo0 = lisp_map_cache_lookup ( OOOo . eid , OOOo . group )
  if ( o0Oo0 == None ) :
   IiO0ooOoO , oOo0oo , IIIi1i1iIIIi = lisp_allow_gleaning ( OOOo . eid , OOOo . group ,
 None )
   if ( IiO0ooOoO == False ) : continue
   if 3 - 3: I1Ii111 % OOooOOo . ooOoO0o / I1IiiI
   o0Oo0 = lisp_mapping ( OOOo . eid , OOOo . group , [ ] )
   o0Oo0 . add_cache ( )
   if 76 - 76: OOooOOo . ooOoO0o * iII111i . Oo0Ooo
   if 50 - 50: I1Ii111 / Oo0Ooo * OoooooooOO % II111iiii . i11iIiiIii
   if 51 - 51: o0oOOo0O0Ooo . o0oOOo0O0Ooo
   if 93 - 93: i11iIiiIii / OoO0O00 + I1IiiI
   if 4 - 4: ooOoO0o . i11iIiiIii . i1IIi
   if 37 - 37: i11iIiiIii + OoO0O00 * Ii1I
   if 100 - 100: IiII . I1Ii111 + II111iiii + i1IIi
  if ( o0Oo0 . gleaned ) :
   lprint ( "Ignore Map-Notify for gleaned {}" . format ( green ( o0Oo0 . print_eid_tuple ( ) , False ) ) )
   if 37 - 37: iII111i
   continue
   if 27 - 27: iII111i / Ii1I / iII111i + OoooooooOO - O0 + OoO0O00
   if 62 - 62: iIii1I11I1II1
  o0Oo0 . mapping_source = None if source == "lisp-etr" else source
  o0Oo0 . map_cache_ttl = OOOo . store_ttl ( )
  if 60 - 60: Oo0Ooo % IiII % OoO0O00 - i11iIiiIii
  if 53 - 53: i11iIiiIii + OoooooooOO
  if 23 - 23: i11iIiiIii - IiII - I1ii11iIi11i + I1ii11iIi11i % I1IiiI
  if 79 - 79: II111iiii / OoooooooOO
  if 35 - 35: i1IIi + IiII + II111iiii % OOooOOo
  if ( len ( o0Oo0 . rloc_set ) != 0 and OOOo . rloc_count == 0 ) :
   o0Oo0 . rloc_set = [ ]
   o0Oo0 . build_best_rloc_set ( )
   lisp_write_ipc_map_cache ( True , o0Oo0 )
   lprint ( "Update {} map-cache entry with no RLOC-set" . format ( green ( o0Oo0 . print_eid_tuple ( ) , False ) ) )
   if 25 - 25: I11i + i11iIiiIii + O0 - Ii1I
   continue
   if 69 - 69: I11i . OoOoOO00 / OOooOOo / i1IIi . II111iiii
   if 17 - 17: I1Ii111
  iiIIIi1I1I1 = o0Oo0 . rtrs_in_rloc_set ( )
  if 73 - 73: OoooooooOO * O0
  if 51 - 51: IiII
  if 31 - 31: I11i - iIii1I11I1II1 * Ii1I + Ii1I
  if 10 - 10: OoOoOO00 - i11iIiiIii % iIii1I11I1II1 / ooOoO0o * i11iIiiIii - Ii1I
  if 64 - 64: II111iiii . i11iIiiIii . iII111i . OOooOOo
  for I1iII in range ( OOOo . rloc_count ) :
   OOO0Oo = lisp_rloc_record ( )
   ii = OOO0Oo . decode ( ii , None )
   OOO0Oo . print_record ( "    " )
   if ( OOOo . group . is_null ( ) ) : continue
   if ( OOO0Oo . rle == None ) : continue
   if 95 - 95: O0 - OoOoOO00
   if 68 - 68: ooOoO0o . I1Ii111
   if 84 - 84: OoooooooOO + oO0o % i1IIi + o0oOOo0O0Ooo * i1IIi
   if 51 - 51: oO0o . OoooooooOO + OOooOOo * I1ii11iIi11i - ooOoO0o
   if 41 - 41: Oo0Ooo
   Iiiiii1 = o0Oo0 . rloc_set [ 0 ] . stats if len ( o0Oo0 . rloc_set ) != 0 else None
   if 66 - 66: oO0o % i1IIi % OoooooooOO
   if 58 - 58: OOooOOo
   if 89 - 89: iIii1I11I1II1 - i1IIi
   if 26 - 26: OOooOOo - iII111i * I1ii11iIi11i / iII111i
   I1II = lisp_rloc ( )
   I1II . store_rloc_from_record ( OOO0Oo , None , o0Oo0 . mapping_source )
   if ( Iiiiii1 != None ) : I1II . stats = copy . deepcopy ( Iiiiii1 )
   if 9 - 9: I1Ii111 / II111iiii * I1Ii111 / I11i - OoO0O00
   if ( iiIIIi1I1I1 and I1II . is_rtr ( ) == False ) : continue
   if 36 - 36: IiII . OoOoOO00 . Ii1I
   o0Oo0 . rloc_set = [ I1II ]
   o0Oo0 . build_best_rloc_set ( )
   lisp_write_ipc_map_cache ( True , o0Oo0 )
   if 31 - 31: iIii1I11I1II1
   lprint ( "Update {} map-cache entry with RLE {}" . format ( green ( o0Oo0 . print_eid_tuple ( ) , False ) ,
   # I1ii11iIi11i + I1Ii111 - I1IiiI % I1IiiI * OOooOOo / Oo0Ooo
 I1II . rle . print_rle ( False , True ) ) )
   if 31 - 31: II111iiii
   if 32 - 32: o0oOOo0O0Ooo % o0oOOo0O0Ooo
 return
 if 67 - 67: IiII + oO0o * IiII
 if 26 - 26: I1ii11iIi11i + i1IIi . i1IIi - oO0o + I1IiiI * o0oOOo0O0Ooo
 if 62 - 62: ooOoO0o + ooOoO0o % I11i
 if 100 - 100: II111iiii . OoooooooOO
 if 32 - 32: I11i % OOooOOo * O0 / iIii1I11I1II1 / i1IIi
 if 87 - 87: OoO0O00 . I1ii11iIi11i * I1IiiI
 if 83 - 83: OOooOOo
 if 86 - 86: I1Ii111 / oO0o
def lisp_process_map_notify ( lisp_sockets , orig_packet , source ) :
 Ii1ii1 = lisp_map_notify ( "" )
 IiiiIi1iiii11 = Ii1ii1 . decode ( orig_packet )
 if ( IiiiIi1iiii11 == None ) :
  lprint ( "Could not decode Map-Notify packet" )
  return
  if 67 - 67: OoOoOO00 + Oo0Ooo / i11iIiiIii . I1IiiI
  if 53 - 53: Oo0Ooo + IiII * ooOoO0o % OoooooooOO * oO0o . iII111i
 Ii1ii1 . print_notify ( )
 if 78 - 78: O0 . Ii1I - I1ii11iIi11i
 if 69 - 69: O0 % O0 . oO0o * OoooooooOO
 if 13 - 13: i1IIi % oO0o . OoooooooOO + I1ii11iIi11i - OOooOOo
 if 99 - 99: OoooooooOO % OOooOOo / I11i
 if 77 - 77: II111iiii - IiII % OOooOOo
 OO0o0OO0 = source . print_address ( )
 if ( Ii1ii1 . alg_id != 0 or Ii1ii1 . auth_len != 0 ) :
  ii1i = None
  for o0Oo in lisp_map_servers_list :
   if ( o0Oo . find ( OO0o0OO0 ) == - 1 ) : continue
   ii1i = lisp_map_servers_list [ o0Oo ]
   if 22 - 22: OoooooooOO / oO0o
  if ( ii1i == None ) :
   lprint ( ( "  Could not find Map-Server {} to authenticate " + "Map-Notify" ) . format ( OO0o0OO0 ) )
   if 78 - 78: oO0o * I11i . i1IIi % i1IIi + i1IIi / OOooOOo
   return
   if 66 - 66: OoooooooOO % o0oOOo0O0Ooo / I11i * I1Ii111
   if 12 - 12: I1Ii111
  ii1i . map_notifies_received += 1
  if 17 - 17: I1Ii111 % oO0o + O0
  O0Oo0O000 = lisp_verify_auth ( IiiiIi1iiii11 , Ii1ii1 . alg_id ,
 Ii1ii1 . auth_data , ii1i . password )
  if 15 - 15: o0oOOo0O0Ooo - OoooooooOO % ooOoO0o % oO0o / i11iIiiIii / Oo0Ooo
  lprint ( "  Authentication {} for Map-Notify" . format ( "succeeded" if O0Oo0O000 else "failed" ) )
  if 59 - 59: iII111i + O0 - I1ii11iIi11i * I1ii11iIi11i + iIii1I11I1II1
  if ( O0Oo0O000 == False ) : return
 else :
  ii1i = lisp_ms ( OO0o0OO0 , None , "" , 0 , "" , False , False , False , False , 0 , 0 , 0 ,
 None )
  if 41 - 41: iIii1I11I1II1 . O0 - ooOoO0o / OoOoOO00 % iIii1I11I1II1 + IiII
  if 23 - 23: OoOoOO00 + ooOoO0o . i11iIiiIii
  if 39 - 39: OoOoOO00 - I1ii11iIi11i / I1Ii111
  if 48 - 48: IiII - oO0o + I11i % o0oOOo0O0Ooo
  if 81 - 81: Oo0Ooo . I1Ii111 * iIii1I11I1II1
  if 60 - 60: OoooooooOO
 ii = Ii1ii1 . eid_records
 if ( Ii1ii1 . record_count == 0 ) :
  lisp_send_map_notify_ack ( lisp_sockets , ii , Ii1ii1 , ii1i )
  return
  if 41 - 41: iIii1I11I1II1 + O0 % o0oOOo0O0Ooo - IiII . I11i * O0
  if 39 - 39: i11iIiiIii . Ii1I
  if 68 - 68: OOooOOo * ooOoO0o . I1IiiI - iII111i
  if 81 - 81: I11i % Oo0Ooo / iII111i
  if 44 - 44: Oo0Ooo
  if 90 - 90: Oo0Ooo . ooOoO0o / IiII * I1Ii111 . ooOoO0o + II111iiii
  if 43 - 43: iIii1I11I1II1 % OOooOOo + OoOoOO00 + I1ii11iIi11i - Oo0Ooo / Ii1I
  if 94 - 94: Ii1I / Oo0Ooo % II111iiii % Oo0Ooo * oO0o
 OOOo = lisp_eid_record ( )
 IiiiIi1iiii11 = OOOo . decode ( ii )
 if ( IiiiIi1iiii11 == None ) : return
 if 54 - 54: O0 / ooOoO0o * I1Ii111
 OOOo . print_record ( "  " , False )
 if 5 - 5: Ii1I / OoOoOO00 - O0 * OoO0O00
 for I1iII in range ( OOOo . rloc_count ) :
  OOO0Oo = lisp_rloc_record ( )
  IiiiIi1iiii11 = OOO0Oo . decode ( IiiiIi1iiii11 , None )
  if ( IiiiIi1iiii11 == None ) :
   lprint ( "  Could not decode RLOC-record in Map-Notify packet" )
   return
   if 13 - 13: IiII + Oo0Ooo - I1Ii111
  OOO0Oo . print_record ( "    " )
  if 10 - 10: OOooOOo % OoooooooOO / I1IiiI . II111iiii % iII111i
  if 47 - 47: o0oOOo0O0Ooo . i11iIiiIii * i1IIi % I11i - ooOoO0o * oO0o
  if 95 - 95: oO0o / Ii1I + OoO0O00
  if 57 - 57: iIii1I11I1II1 + I1Ii111 % oO0o - Ii1I . I1IiiI
  if 39 - 39: OoO0O00 + II111iiii
 if ( OOOo . group . is_null ( ) == False ) :
  if 98 - 98: O0 - I1Ii111 % oO0o - iII111i + Ii1I * i1IIi
  if 76 - 76: o0oOOo0O0Ooo
  if 55 - 55: OOooOOo + I1ii11iIi11i * Oo0Ooo
  if 11 - 11: i1IIi - OoooooooOO * OoOoOO00 / oO0o - OoooooooOO - I1IiiI
  if 22 - 22: i11iIiiIii . Ii1I . Oo0Ooo * Oo0Ooo - iII111i / I1ii11iIi11i
  lprint ( "Send {} Map-Notify IPC message to ITR process" . format ( green ( OOOo . print_eid_tuple ( ) , False ) ) )
  if 49 - 49: iII111i + I11i . Oo0Ooo
  if 23 - 23: I1IiiI . Ii1I + ooOoO0o . OoooooooOO
  oOOO0oo0 = lisp_control_packet_ipc ( orig_packet , OO0o0OO0 , "lisp-itr" , 0 )
  lisp_ipc ( oOOO0oo0 , lisp_sockets [ 2 ] , "lisp-core-pkt" )
  if 57 - 57: OOooOOo / OoOoOO00 / i11iIiiIii - I11i - I11i . Ii1I
  if 53 - 53: ooOoO0o . iII111i + Ii1I * I1Ii111
  if 49 - 49: II111iiii . I1ii11iIi11i * OoOoOO00 - OOooOOo
  if 48 - 48: OoO0O00 . iIii1I11I1II1 - OoooooooOO + I1Ii111 / i11iIiiIii . Oo0Ooo
  if 61 - 61: II111iiii + OOooOOo . o0oOOo0O0Ooo . iIii1I11I1II1
 lisp_send_map_notify_ack ( lisp_sockets , ii , Ii1ii1 , ii1i )
 return
 if 63 - 63: I11i + i11iIiiIii . o0oOOo0O0Ooo . i1IIi + OoOoOO00
 if 1 - 1: i11iIiiIii
 if 1 - 1: iIii1I11I1II1
 if 73 - 73: iII111i + IiII
 if 95 - 95: O0
 if 75 - 75: ooOoO0o
 if 8 - 8: O0 - OoooooooOO + I1ii11iIi11i / Oo0Ooo . oO0o + I1Ii111
 if 85 - 85: ooOoO0o
def lisp_process_map_notify_ack ( packet , source ) :
 Ii1ii1 = lisp_map_notify ( "" )
 packet = Ii1ii1 . decode ( packet )
 if ( packet == None ) :
  lprint ( "Could not decode Map-Notify-Ack packet" )
  return
  if 29 - 29: iII111i . Ii1I
  if 43 - 43: I11i - I1ii11iIi11i + iIii1I11I1II1 / I1ii11iIi11i * oO0o / iIii1I11I1II1
 Ii1ii1 . print_notify ( )
 if 45 - 45: IiII
 if 49 - 49: I1IiiI . Ii1I * I1IiiI - OoooooooOO . I11i / I1Ii111
 if 9 - 9: iIii1I11I1II1 * Ii1I / O0 - OOooOOo
 if 95 - 95: i11iIiiIii * II111iiii * OOooOOo * iIii1I11I1II1
 if 22 - 22: iIii1I11I1II1 / I1IiiI + OoOoOO00 - OOooOOo . i11iIiiIii / i11iIiiIii
 if ( Ii1ii1 . record_count < 1 ) :
  lprint ( "No EID-prefix found, cannot authenticate Map-Notify-Ack" )
  return
  if 10 - 10: iIii1I11I1II1 % i1IIi
  if 78 - 78: I11i + II111iiii % o0oOOo0O0Ooo
 OOOo = lisp_eid_record ( )
 if 17 - 17: i11iIiiIii + oO0o * iII111i . II111iiii
 if ( OOOo . decode ( Ii1ii1 . eid_records ) == None ) :
  lprint ( "Could not decode EID-record, cannot authenticate " +
 "Map-Notify-Ack" )
  return
  if 44 - 44: I1ii11iIi11i
 OOOo . print_record ( "  " , False )
 if 39 - 39: iII111i + Oo0Ooo / oO0o
 Ii1i1 = OOOo . print_eid_tuple ( )
 if 95 - 95: I1Ii111 * oO0o / ooOoO0o . Ii1I . OoOoOO00
 if 99 - 99: I1IiiI * II111iiii
 if 84 - 84: II111iiii - I1IiiI
 if 41 - 41: iIii1I11I1II1 % I1Ii111 % OoOoOO00
 if ( Ii1ii1 . alg_id != LISP_NONE_ALG_ID and Ii1ii1 . auth_len != 0 ) :
  oOoooo = lisp_sites_by_eid . lookup_cache ( OOOo . eid , True )
  if ( oOoooo == None ) :
   iiIi11I1I1 = bold ( "Site not found" , False )
   lprint ( ( "{} for EID {}, cannot authenticate Map-Notify-Ack" ) . format ( iiIi11I1I1 , green ( Ii1i1 , False ) ) )
   if 35 - 35: I11i + i1IIi
   return
   if 85 - 85: Ii1I * Ii1I . OoOoOO00 / Oo0Ooo
  ooo000O0O = oOoooo . site
  if 97 - 97: oO0o % iIii1I11I1II1
  if 87 - 87: II111iiii % I1IiiI + oO0o - I11i / I11i
  if 16 - 16: I1IiiI
  if 39 - 39: ooOoO0o * II111iiii
  ooo000O0O . map_notify_acks_received += 1
  if 90 - 90: OoooooooOO * ooOoO0o
  o00oO = Ii1ii1 . key_id
  if ( ooo000O0O . auth_key . has_key ( o00oO ) ) :
   oO0oOOoo0OO0 = ooo000O0O . auth_key [ o00oO ]
  else :
   oO0oOOoo0OO0 = ""
   if 14 - 14: I1IiiI % i1IIi
   if 35 - 35: ooOoO0o % o0oOOo0O0Ooo % ooOoO0o
  O0Oo0O000 = lisp_verify_auth ( packet , Ii1ii1 . alg_id ,
 Ii1ii1 . auth_data , oO0oOOoo0OO0 )
  if 77 - 77: OOooOOo % I1Ii111 / i11iIiiIii . i1IIi % OOooOOo
  o00oO = "key-id {}" . format ( o00oO ) if o00oO == Ii1ii1 . key_id else "bad key-id {}" . format ( Ii1ii1 . key_id )
  if 55 - 55: i1IIi
  if 64 - 64: oO0o . OOooOOo * i11iIiiIii + I1Ii111
  lprint ( "  Authentication {} for Map-Notify-Ack, {}" . format ( "succeeded" if O0Oo0O000 else "failed" , o00oO ) )
  if 88 - 88: O0
  if ( O0Oo0O000 == False ) : return
  if 75 - 75: iII111i - Oo0Ooo / OoooooooOO - O0
  if 36 - 36: OoO0O00 % Ii1I . Oo0Ooo
  if 90 - 90: i11iIiiIii - iII111i * oO0o
  if 79 - 79: IiII
  if 38 - 38: I1Ii111
 if ( Ii1ii1 . retransmit_timer ) : Ii1ii1 . retransmit_timer . cancel ( )
 if 56 - 56: i11iIiiIii
 Ii111 = source . print_address ( )
 o0Oo = Ii1ii1 . nonce_key
 if 58 - 58: i11iIiiIii / OoOoOO00
 if ( lisp_map_notify_queue . has_key ( o0Oo ) ) :
  Ii1ii1 = lisp_map_notify_queue . pop ( o0Oo )
  if ( Ii1ii1 . retransmit_timer ) : Ii1ii1 . retransmit_timer . cancel ( )
  lprint ( "Dequeue Map-Notify from retransmit queue, key is: {}" . format ( o0Oo ) )
  if 23 - 23: I1IiiI % iIii1I11I1II1 - oO0o - iII111i - o0oOOo0O0Ooo
 else :
  lprint ( "Map-Notify with nonce 0x{} queue entry not found for {}" . format ( Ii1ii1 . nonce_key , red ( Ii111 , False ) ) )
  if 39 - 39: Oo0Ooo . OoO0O00
  if 74 - 74: I1IiiI . O0 . IiII + IiII - IiII
 return
 if 100 - 100: ooOoO0o / OoooooooOO
 if 73 - 73: i11iIiiIii - Oo0Ooo
 if 100 - 100: iIii1I11I1II1 + I1Ii111
 if 51 - 51: o0oOOo0O0Ooo * I11i
 if 42 - 42: OOooOOo % I11i
 if 84 - 84: Oo0Ooo * OoOoOO00 / Ii1I / IiII / o0oOOo0O0Ooo . I1ii11iIi11i
 if 81 - 81: I1IiiI
 if 82 - 82: I1Ii111 - OoooooooOO - Ii1I
def lisp_map_referral_loop ( mr , eid , group , action , s ) :
 if ( action not in ( LISP_DDT_ACTION_NODE_REFERRAL ,
 LISP_DDT_ACTION_MS_REFERRAL ) ) : return ( False )
 if 34 - 34: OOooOOo . iIii1I11I1II1 / I1IiiI . Oo0Ooo - iIii1I11I1II1
 if ( mr . last_cached_prefix [ 0 ] == None ) : return ( False )
 if 83 - 83: iII111i - I1ii11iIi11i + iII111i
 if 4 - 4: o0oOOo0O0Ooo % iIii1I11I1II1 + I11i
 if 60 - 60: I1ii11iIi11i / I1Ii111 % i11iIiiIii % oO0o % I1IiiI . Oo0Ooo
 if 20 - 20: IiII - OOooOOo + OoOoOO00
 I1II1i = False
 if ( group . is_null ( ) == False ) :
  I1II1i = mr . last_cached_prefix [ 1 ] . is_more_specific ( group )
  if 83 - 83: OoooooooOO / I1IiiI + iII111i - iIii1I11I1II1 % ooOoO0o
 if ( I1II1i == False ) :
  I1II1i = mr . last_cached_prefix [ 0 ] . is_more_specific ( eid )
  if 74 - 74: OoO0O00
  if 13 - 13: I1ii11iIi11i / OoO0O00
 if ( I1II1i ) :
  iIIiIIiII111 = lisp_print_eid_tuple ( eid , group )
  OooOooOOo = lisp_print_eid_tuple ( mr . last_cached_prefix [ 0 ] ,
 mr . last_cached_prefix [ 1 ] )
  if 94 - 94: IiII * i1IIi
  lprint ( ( "Map-Referral prefix {} from {} is not more-specific " + "than cached prefix {}" ) . format ( green ( iIIiIIiII111 , False ) , s ,
  # OOooOOo % O0 . iII111i + Ii1I - I1IiiI * OoooooooOO
 OooOooOOo ) )
  if 91 - 91: II111iiii + OOooOOo
 return ( I1II1i )
 if 21 - 21: O0
 if 16 - 16: I1Ii111 - o0oOOo0O0Ooo + OoOoOO00 % II111iiii
 if 67 - 67: I1IiiI / OoO0O00 + iIii1I11I1II1
 if 70 - 70: I1Ii111 * Oo0Ooo . oO0o
 if 11 - 11: I11i . IiII / I1IiiI + II111iiii * iII111i + i1IIi
 if 10 - 10: Oo0Ooo . o0oOOo0O0Ooo - i11iIiiIii / iII111i + i11iIiiIii . I11i
 if 66 - 66: i1IIi
def lisp_process_map_referral ( lisp_sockets , packet , source ) :
 if 98 - 98: Oo0Ooo / iIii1I11I1II1
 oooOOo00oOOo = lisp_map_referral ( )
 packet = oooOOo00oOOo . decode ( packet )
 if ( packet == None ) :
  lprint ( "Could not decode Map-Referral packet" )
  return
  if 33 - 33: O0 - iII111i
 oooOOo00oOOo . print_map_referral ( )
 if 40 - 40: iII111i * I11i
 OO0o0OO0 = source . print_address ( )
 o0OOO = oooOOo00oOOo . nonce
 if 25 - 25: O0 * o0oOOo0O0Ooo % ooOoO0o % I1IiiI
 if 87 - 87: OoOoOO00
 if 30 - 30: IiII % OoOoOO00 + I1Ii111
 if 13 - 13: iII111i * Ii1I % o0oOOo0O0Ooo * i1IIi . IiII % i1IIi
 for iIi1I1 in range ( oooOOo00oOOo . record_count ) :
  OOOo = lisp_eid_record ( )
  packet = OOOo . decode ( packet )
  if ( packet == None ) :
   lprint ( "Could not decode EID-record in Map-Referral packet" )
   return
   if 79 - 79: OoooooooOO % I11i / o0oOOo0O0Ooo + IiII + O0 + iII111i
  OOOo . print_record ( "  " , True )
  if 87 - 87: I11i
  if 39 - 39: I1ii11iIi11i * i11iIiiIii % I1Ii111
  if 72 - 72: OoO0O00 * Oo0Ooo - IiII
  if 74 - 74: Ii1I
  o0Oo = str ( o0OOO )
  if ( o0Oo not in lisp_ddt_map_requestQ ) :
   lprint ( ( "Map-Referral nonce 0x{} from {} not found in " + "Map-Request queue, EID-record ignored" ) . format ( lisp_hex_string ( o0OOO ) , OO0o0OO0 ) )
   if 26 - 26: I11i . O0
   if 68 - 68: Ii1I
   continue
   if 26 - 26: o0oOOo0O0Ooo - I1ii11iIi11i / O0 % i11iIiiIii
  I1III11iIIIi = lisp_ddt_map_requestQ [ o0Oo ]
  if ( I1III11iIIIi == None ) :
   lprint ( ( "No Map-Request queue entry found for Map-Referral " +
 "nonce 0x{} from {}, EID-record ignored" ) . format ( lisp_hex_string ( o0OOO ) , OO0o0OO0 ) )
   if 7 - 7: I1Ii111 . Oo0Ooo + IiII / iIii1I11I1II1
   continue
   if 22 - 22: iIii1I11I1II1 - O0 . iII111i - IiII - ooOoO0o
   if 54 - 54: OoO0O00 . iII111i . OoOoOO00 * OoO0O00 + o0oOOo0O0Ooo . ooOoO0o
   if 44 - 44: I11i * iIii1I11I1II1 . I1ii11iIi11i
   if 9 - 9: o0oOOo0O0Ooo
   if 23 - 23: ooOoO0o * OoO0O00 + O0 % I1Ii111
   if 21 - 21: Ii1I * OoOoOO00
  if ( lisp_map_referral_loop ( I1III11iIIIi , OOOo . eid , OOOo . group ,
 OOOo . action , OO0o0OO0 ) ) :
   I1III11iIIIi . dequeue_map_request ( )
   continue
   if 29 - 29: iIii1I11I1II1 / ooOoO0o
   if 75 - 75: OoooooooOO + I1IiiI % OoOoOO00 / O0 - IiII
  I1III11iIIIi . last_cached_prefix [ 0 ] = OOOo . eid
  I1III11iIIIi . last_cached_prefix [ 1 ] = OOOo . group
  if 88 - 88: OoO0O00 % Ii1I
  if 12 - 12: OoooooooOO . O0
  if 33 - 33: OoooooooOO / I11i . II111iiii * i1IIi
  if 34 - 34: i11iIiiIii / OoOoOO00
  iI1I11II = False
  IiiiiII1i = lisp_referral_cache_lookup ( OOOo . eid , OOOo . group ,
 True )
  if ( IiiiiII1i == None ) :
   iI1I11II = True
   IiiiiII1i = lisp_referral ( )
   IiiiiII1i . eid = OOOo . eid
   IiiiiII1i . group = OOOo . group
   if ( OOOo . ddt_incomplete == False ) : IiiiiII1i . add_cache ( )
  elif ( IiiiiII1i . referral_source . not_set ( ) ) :
   lprint ( "Do not replace static referral entry {}" . format ( green ( IiiiiII1i . print_eid_tuple ( ) , False ) ) )
   if 100 - 100: o0oOOo0O0Ooo - I1IiiI / I11i
   I1III11iIIIi . dequeue_map_request ( )
   continue
   if 43 - 43: o0oOOo0O0Ooo % iIii1I11I1II1
   if 85 - 85: oO0o + OoooooooOO - IiII % o0oOOo0O0Ooo * ooOoO0o * II111iiii
  iI1IIi1I = OOOo . action
  IiiiiII1i . referral_source = source
  IiiiiII1i . referral_type = iI1IIi1I
  Oo0o0 = OOOo . store_ttl ( )
  IiiiiII1i . referral_ttl = Oo0o0
  IiiiiII1i . expires = lisp_set_timestamp ( Oo0o0 )
  if 4 - 4: Ii1I . i1IIi + Oo0Ooo % I11i . OoO0O00
  if 70 - 70: OOooOOo * OoOoOO00 / OoOoOO00 / OoOoOO00
  if 23 - 23: I1IiiI
  if 24 - 24: I1Ii111 * i1IIi % O0 * Ii1I + iII111i
  III1I11111I11 = IiiiiII1i . is_referral_negative ( )
  if ( IiiiiII1i . referral_set . has_key ( OO0o0OO0 ) ) :
   iiI111I = IiiiiII1i . referral_set [ OO0o0OO0 ]
   if 24 - 24: OOooOOo + I1IiiI + IiII . OOooOOo * I1ii11iIi11i / I1Ii111
   if ( iiI111I . updown == False and III1I11111I11 == False ) :
    iiI111I . updown = True
    lprint ( "Change up/down status for referral-node {} to up" . format ( OO0o0OO0 ) )
    if 75 - 75: ooOoO0o - i11iIiiIii . I1Ii111 % I11i . I1IiiI
   elif ( iiI111I . updown == True and III1I11111I11 == True ) :
    iiI111I . updown = False
    lprint ( ( "Change up/down status for referral-node {} " + "to down, received negative referral" ) . format ( OO0o0OO0 ) )
    if 76 - 76: iIii1I11I1II1 % IiII
    if 20 - 20: ooOoO0o . O0 . Oo0Ooo . OoO0O00 / Oo0Ooo
    if 85 - 85: o0oOOo0O0Ooo / I11i - OoOoOO00 - o0oOOo0O0Ooo
    if 99 - 99: I11i - I11i + Oo0Ooo
    if 71 - 71: IiII . I1Ii111 . oO0o
    if 30 - 30: IiII
    if 6 - 6: I1Ii111 % oO0o % I1ii11iIi11i
    if 36 - 36: IiII
  OooOOOOO00 = { }
  for o0Oo in IiiiiII1i . referral_set : OooOOOOO00 [ o0Oo ] = None
  if 58 - 58: i1IIi . I1Ii111
  if 94 - 94: ooOoO0o - IiII
  if 92 - 92: Ii1I . i11iIiiIii
  if 45 - 45: ooOoO0o * I1IiiI / iII111i
  for iIi1I1 in range ( OOOo . rloc_count ) :
   OOO0Oo = lisp_rloc_record ( )
   packet = OOO0Oo . decode ( packet , None )
   if ( packet == None ) :
    lprint ( "Could not decode RLOC-record in Map-Referral packet" )
    return
    if 29 - 29: i1IIi + Ii1I * OoO0O00
   OOO0Oo . print_record ( "    " )
   if 69 - 69: Ii1I - OOooOOo * I11i . I1IiiI + o0oOOo0O0Ooo / OoO0O00
   if 45 - 45: OOooOOo
   if 57 - 57: iIii1I11I1II1 + IiII - I1IiiI
   if 64 - 64: II111iiii . IiII / I1IiiI
   oo0o00OO = OOO0Oo . rloc . print_address ( )
   if ( IiiiiII1i . referral_set . has_key ( oo0o00OO ) == False ) :
    iiI111I = lisp_referral_node ( )
    iiI111I . referral_address . copy_address ( OOO0Oo . rloc )
    IiiiiII1i . referral_set [ oo0o00OO ] = iiI111I
    if ( OO0o0OO0 == oo0o00OO and III1I11111I11 ) : iiI111I . updown = False
   else :
    iiI111I = IiiiiII1i . referral_set [ oo0o00OO ]
    if ( OooOOOOO00 . has_key ( oo0o00OO ) ) : OooOOOOO00 . pop ( oo0o00OO )
    if 20 - 20: OoooooooOO - I1ii11iIi11i * I1ii11iIi11i * I1ii11iIi11i
   iiI111I . priority = OOO0Oo . priority
   iiI111I . weight = OOO0Oo . weight
   if 87 - 87: OoooooooOO * ooOoO0o
   if 6 - 6: I1Ii111 / ooOoO0o / OoooooooOO . iIii1I11I1II1
   if 68 - 68: OoO0O00
   if 26 - 26: I11i % i1IIi / iIii1I11I1II1 % IiII . iII111i + I1ii11iIi11i
   if 49 - 49: O0 . IiII + I1Ii111 - I11i % II111iiii
  for o0Oo in OooOOOOO00 : IiiiiII1i . referral_set . pop ( o0Oo )
  if 15 - 15: O0 - OoOoOO00 % II111iiii + O0 % O0 + OoOoOO00
  Ii1i1 = IiiiiII1i . print_eid_tuple ( )
  if 34 - 34: I1Ii111
  if ( iI1I11II ) :
   if ( OOOo . ddt_incomplete ) :
    lprint ( "Suppress add {} to referral-cache" . format ( green ( Ii1i1 , False ) ) )
    if 69 - 69: iIii1I11I1II1 . OOooOOo % I11i
   else :
    lprint ( "Add {}, referral-count {} to referral-cache" . format ( green ( Ii1i1 , False ) , OOOo . rloc_count ) )
    if 28 - 28: I1Ii111 . ooOoO0o % I1IiiI
    if 62 - 62: II111iiii + ooOoO0o + I1IiiI
  else :
   lprint ( "Replace {}, referral-count: {} in referral-cache" . format ( green ( Ii1i1 , False ) , OOOo . rloc_count ) )
   if 70 - 70: o0oOOo0O0Ooo + Ii1I . OoO0O00 * Ii1I + OOooOOo + ooOoO0o
   if 13 - 13: I1ii11iIi11i
   if 97 - 97: oO0o - Oo0Ooo . i11iIiiIii % ooOoO0o * i11iIiiIii - OoooooooOO
   if 44 - 44: I11i % OoooooooOO / iII111i - i11iIiiIii * i1IIi * o0oOOo0O0Ooo
   if 51 - 51: Ii1I + IiII / I1ii11iIi11i + O0 % Ii1I
   if 55 - 55: iII111i % o0oOOo0O0Ooo - oO0o % OoooooooOO
  if ( iI1IIi1I == LISP_DDT_ACTION_DELEGATION_HOLE ) :
   lisp_send_negative_map_reply ( I1III11iIIIi . lisp_sockets , IiiiiII1i . eid ,
 IiiiiII1i . group , I1III11iIIIi . nonce , I1III11iIIIi . itr , I1III11iIIIi . sport , 15 , None , False )
   I1III11iIIIi . dequeue_map_request ( )
   if 18 - 18: OoooooooOO - I1ii11iIi11i
   if 94 - 94: OOooOOo . Oo0Ooo + Ii1I * o0oOOo0O0Ooo
  if ( iI1IIi1I == LISP_DDT_ACTION_NOT_AUTH ) :
   if ( I1III11iIIIi . tried_root ) :
    lisp_send_negative_map_reply ( I1III11iIIIi . lisp_sockets , IiiiiII1i . eid ,
 IiiiiII1i . group , I1III11iIIIi . nonce , I1III11iIIIi . itr , I1III11iIIIi . sport , 0 , None , False )
    I1III11iIIIi . dequeue_map_request ( )
   else :
    lisp_send_ddt_map_request ( I1III11iIIIi , True )
    if 79 - 79: OOooOOo + Oo0Ooo
    if 33 - 33: iIii1I11I1II1
    if 75 - 75: I1Ii111 / iIii1I11I1II1 . OoooooooOO
  if ( iI1IIi1I == LISP_DDT_ACTION_MS_NOT_REG ) :
   if ( IiiiiII1i . referral_set . has_key ( OO0o0OO0 ) ) :
    iiI111I = IiiiiII1i . referral_set [ OO0o0OO0 ]
    iiI111I . updown = False
    if 98 - 98: iIii1I11I1II1 / I1IiiI + i1IIi
   if ( len ( IiiiiII1i . referral_set ) == 0 ) :
    I1III11iIIIi . dequeue_map_request ( )
   else :
    lisp_send_ddt_map_request ( I1III11iIIIi , False )
    if 80 - 80: II111iiii . Oo0Ooo * oO0o % II111iiii / I1ii11iIi11i
    if 66 - 66: iII111i / OoO0O00 / i11iIiiIii
    if 99 - 99: OOooOOo
  if ( iI1IIi1I in ( LISP_DDT_ACTION_NODE_REFERRAL ,
 LISP_DDT_ACTION_MS_REFERRAL ) ) :
   if ( I1III11iIIIi . eid . is_exact_match ( OOOo . eid ) ) :
    if ( not I1III11iIIIi . tried_root ) :
     lisp_send_ddt_map_request ( I1III11iIIIi , True )
    else :
     lisp_send_negative_map_reply ( I1III11iIIIi . lisp_sockets ,
 IiiiiII1i . eid , IiiiiII1i . group , I1III11iIIIi . nonce , I1III11iIIIi . itr ,
 I1III11iIIIi . sport , 15 , None , False )
     I1III11iIIIi . dequeue_map_request ( )
     if 51 - 51: i11iIiiIii . o0oOOo0O0Ooo / iII111i
   else :
    lisp_send_ddt_map_request ( I1III11iIIIi , False )
    if 53 - 53: oO0o / i1IIi - Oo0Ooo - i1IIi + IiII
    if 79 - 79: oO0o % o0oOOo0O0Ooo / o0oOOo0O0Ooo % iII111i
    if 56 - 56: Oo0Ooo % I1ii11iIi11i
  if ( iI1IIi1I == LISP_DDT_ACTION_MS_ACK ) : I1III11iIIIi . dequeue_map_request ( )
  if 53 - 53: OoO0O00 . I11i - ooOoO0o
 return
 if 11 - 11: I11i + i11iIiiIii / oO0o % oO0o * o0oOOo0O0Ooo / OoOoOO00
 if 74 - 74: oO0o . I1Ii111 . II111iiii
 if 92 - 92: I1Ii111 % OoooooooOO * I1Ii111
 if 78 - 78: Oo0Ooo . I11i . oO0o + O0 / O0
 if 41 - 41: iII111i * OoO0O00 - OoO0O00
 if 72 - 72: o0oOOo0O0Ooo + oO0o . I1ii11iIi11i + OoO0O00 / I1Ii111
 if 58 - 58: Oo0Ooo / II111iiii % OoooooooOO % II111iiii
 if 39 - 39: i1IIi
def lisp_process_ecm ( lisp_sockets , packet , source , ecm_port ) :
 I1i1ii = lisp_ecm ( 0 )
 packet = I1i1ii . decode ( packet )
 if ( packet == None ) :
  lprint ( "Could not decode ECM packet" )
  return
  if 16 - 16: OoOoOO00 % iIii1I11I1II1 + Ii1I - o0oOOo0O0Ooo . Oo0Ooo + i1IIi
  if 59 - 59: i1IIi
 I1i1ii . print_ecm ( )
 if 37 - 37: OoO0O00 / I1ii11iIi11i / OoOoOO00
 O00O0OO = lisp_control_header ( )
 if ( O00O0OO . decode ( packet ) == None ) :
  lprint ( "Could not decode control header" )
  return
  if 15 - 15: I1IiiI % iIii1I11I1II1 . I1Ii111
  if 71 - 71: I11i - Ii1I + i11iIiiIii % I1ii11iIi11i - OoO0O00 - OOooOOo
 oo0000oooO = O00O0OO . type
 del ( O00O0OO )
 if 47 - 47: OoOoOO00 % II111iiii
 if ( oo0000oooO != LISP_MAP_REQUEST ) :
  lprint ( "Received ECM without Map-Request inside" )
  return
  if 84 - 84: ooOoO0o / oO0o * I11i + I11i + oO0o - OoOoOO00
  if 15 - 15: OoO0O00
  if 88 - 88: Ii1I % i1IIi / I1Ii111
  if 2 - 2: Ii1I . IiII % OoOoOO00
  if 42 - 42: OoOoOO00 * OoO0O00 * IiII - IiII % Oo0Ooo . IiII
 I1O0o = I1i1ii . udp_sport
 II1IIII = time . time ( )
 lisp_process_map_request ( lisp_sockets , packet , source , ecm_port ,
 I1i1ii . source , I1O0o , I1i1ii . ddt , - 1 , II1IIII )
 return
 if 35 - 35: i11iIiiIii
 if 62 - 62: O0 - o0oOOo0O0Ooo + I1Ii111 * I1ii11iIi11i / OOooOOo
 if 87 - 87: Oo0Ooo / OoooooooOO + O0 / o0oOOo0O0Ooo % II111iiii - O0
 if 63 - 63: OOooOOo - OoO0O00 * i1IIi - I1ii11iIi11i . I1IiiI
 if 59 - 59: i11iIiiIii . OOooOOo % Oo0Ooo + O0
 if 84 - 84: I1Ii111 / O0 - IiII . I11i / o0oOOo0O0Ooo
 if 12 - 12: i11iIiiIii / Ii1I + i1IIi
 if 54 - 54: I1IiiI
 if 55 - 55: I1ii11iIi11i % IiII % o0oOOo0O0Ooo + i1IIi * OoooooooOO % II111iiii
 if 37 - 37: Oo0Ooo
def lisp_send_map_register ( lisp_sockets , packet , map_register , ms ) :
 if 33 - 33: OoooooooOO - O0 . O0 - o0oOOo0O0Ooo % o0oOOo0O0Ooo % OoO0O00
 if 27 - 27: ooOoO0o . i11iIiiIii / o0oOOo0O0Ooo * OoO0O00 * OoOoOO00 * oO0o
 if 19 - 19: O0 * II111iiii * OoOoOO00
 if 53 - 53: Oo0Ooo
 if 16 - 16: Ii1I
 if 73 - 73: i11iIiiIii + I1IiiI - IiII - IiII + IiII . Ii1I
 if 78 - 78: OoO0O00 + oO0o
 Ii1II1I11i1I = ms . map_server
 if ( lisp_decent_push_configured and Ii1II1I11i1I . is_multicast_address ( ) and
 ( ms . map_registers_multicast_sent == 1 or ms . map_registers_sent == 1 ) ) :
  Ii1II1I11i1I = copy . deepcopy ( Ii1II1I11i1I )
  Ii1II1I11i1I . address = 0x7f000001
  OOoo0 = bold ( "Bootstrap" , False )
  i11ii = ms . map_server . print_address_no_iid ( )
  lprint ( "{} mapping system for peer-group {}" . format ( OOoo0 , i11ii ) )
  if 86 - 86: ooOoO0o . ooOoO0o + oO0o
  if 84 - 84: OOooOOo - OoOoOO00 + i1IIi * I1ii11iIi11i % I1ii11iIi11i * I1Ii111
  if 31 - 31: IiII + iII111i
  if 5 - 5: O0 * Ii1I
  if 78 - 78: iII111i * iIii1I11I1II1 . OoO0O00 . OoOoOO00 % I1Ii111
  if 77 - 77: OOooOOo / OoooooooOO
 packet = lisp_compute_auth ( packet , map_register , ms . password )
 if 11 - 11: iIii1I11I1II1 - Ii1I - OoOoOO00 . oO0o / I1ii11iIi11i
 if 79 - 79: i11iIiiIii % o0oOOo0O0Ooo * II111iiii . i1IIi * Ii1I - i11iIiiIii
 if 31 - 31: IiII / o0oOOo0O0Ooo
 if 27 - 27: Oo0Ooo
 if 32 - 32: Oo0Ooo * i11iIiiIii % I1IiiI - i11iIiiIii - I1Ii111 % I1ii11iIi11i
 if 35 - 35: o0oOOo0O0Ooo % iII111i / O0 * I1IiiI . o0oOOo0O0Ooo / OOooOOo
 if ( ms . ekey != None ) :
  II11iI11i1 = ms . ekey . zfill ( 32 )
  OO000OOOo0Oo = "0" * 8
  o0OoOo0o0O00 = chacha . ChaCha ( II11iI11i1 , OO000OOOo0Oo , 20 ) . encrypt ( packet [ 4 : : ] )
  packet = packet [ 0 : 4 ] + o0OoOo0o0O00
  iIIi1iI1I1IIi = bold ( "Encrypt" , False )
  lprint ( "{} Map-Register with key-id {}" . format ( iIIi1iI1I1IIi , ms . ekey_id ) )
  if 81 - 81: I1ii11iIi11i - i11iIiiIii
  if 49 - 49: iII111i * I11i - II111iiii . o0oOOo0O0Ooo
 O0O0oo = ""
 if ( lisp_decent_pull_xtr_configured ( ) ) :
  O0O0oo = ", decent-index {}" . format ( bold ( ms . dns_name , False ) )
  if 43 - 43: I1ii11iIi11i
  if 60 - 60: i11iIiiIii + IiII
 lprint ( "Send Map-Register to map-server {}{}{}" . format ( Ii1II1I11i1I . print_address ( ) , ", ms-name '{}'" . format ( ms . ms_name ) , O0O0oo ) )
 if 41 - 41: I1Ii111 * o0oOOo0O0Ooo + Oo0Ooo
 lisp_send ( lisp_sockets , Ii1II1I11i1I , LISP_CTRL_PORT , packet )
 return
 if 86 - 86: Ii1I / oO0o
 if 40 - 40: OoO0O00 % oO0o + Oo0Ooo
 if 60 - 60: II111iiii / Ii1I
 if 14 - 14: iII111i - Oo0Ooo / o0oOOo0O0Ooo * oO0o / Oo0Ooo - I1IiiI
 if 89 - 89: i1IIi / I1Ii111 + Ii1I - i1IIi
 if 66 - 66: OoooooooOO
 if 68 - 68: iII111i + I1Ii111
 if 90 - 90: o0oOOo0O0Ooo
def lisp_send_ipc_to_core ( lisp_socket , packet , dest , port ) :
 iI1Iii1i1 = lisp_socket . getsockname ( )
 dest = dest . print_address_no_iid ( )
 if 48 - 48: iII111i + Ii1I
 lprint ( "Send IPC {} bytes to {} {}, control-packet: {}" . format ( len ( packet ) , dest , port , lisp_format_packet ( packet ) ) )
 if 45 - 45: oO0o / iIii1I11I1II1 % O0 % IiII % I1ii11iIi11i
 if 89 - 89: OOooOOo - I1Ii111 - iII111i
 packet = lisp_control_packet_ipc ( packet , iI1Iii1i1 , dest , port )
 lisp_ipc ( packet , lisp_socket , "lisp-core-pkt" )
 return
 if 67 - 67: oO0o
 if 76 - 76: I1IiiI % I1IiiI - IiII / OoOoOO00 / I1ii11iIi11i
 if 42 - 42: I1IiiI + I1ii11iIi11i + Oo0Ooo * i1IIi - II111iiii
 if 15 - 15: o0oOOo0O0Ooo
 if 60 - 60: I1ii11iIi11i / I1Ii111
 if 13 - 13: I1Ii111
 if 52 - 52: II111iiii / OoO0O00 . Ii1I
 if 68 - 68: iII111i
def lisp_send_map_reply ( lisp_sockets , packet , dest , port ) :
 lprint ( "Send Map-Reply to {}" . format ( dest . print_address_no_iid ( ) ) )
 lisp_send_ipc_to_core ( lisp_sockets [ 2 ] , packet , dest , port )
 return
 if 67 - 67: I1IiiI * I1IiiI
 if 100 - 100: iII111i * iII111i . Oo0Ooo
 if 10 - 10: Oo0Ooo % ooOoO0o * Oo0Ooo
 if 48 - 48: ooOoO0o + II111iiii
 if 73 - 73: II111iiii
 if 63 - 63: i11iIiiIii . Oo0Ooo . OOooOOo - II111iiii
 if 35 - 35: II111iiii + IiII
 if 66 - 66: o0oOOo0O0Ooo % IiII
def lisp_send_map_referral ( lisp_sockets , packet , dest , port ) :
 lprint ( "Send Map-Referral to {}" . format ( dest . print_address ( ) ) )
 lisp_send_ipc_to_core ( lisp_sockets [ 2 ] , packet , dest , port )
 return
 if 39 - 39: IiII
 if 18 - 18: iII111i % o0oOOo0O0Ooo - i1IIi
 if 53 - 53: o0oOOo0O0Ooo + IiII - ooOoO0o % i11iIiiIii - i11iIiiIii - I1Ii111
 if 79 - 79: II111iiii + i11iIiiIii . OOooOOo . I11i / iIii1I11I1II1
 if 62 - 62: O0
 if 52 - 52: OoooooooOO . oO0o
 if 38 - 38: ooOoO0o . i1IIi / iII111i + I1IiiI - II111iiii
 if 21 - 21: i11iIiiIii + II111iiii - i1IIi / OoooooooOO * OOooOOo % Oo0Ooo
def lisp_send_map_notify ( lisp_sockets , packet , dest , port ) :
 lprint ( "Send Map-Notify to xTR {}" . format ( dest . print_address ( ) ) )
 lisp_send_ipc_to_core ( lisp_sockets [ 2 ] , packet , dest , port )
 return
 if 59 - 59: Ii1I
 if 77 - 77: I1ii11iIi11i * Ii1I * O0 * I1IiiI % OoO0O00 - iIii1I11I1II1
 if 6 - 6: i11iIiiIii . I11i - OoooooooOO
 if 26 - 26: I1IiiI
 if 26 - 26: IiII . Ii1I / IiII - OoO0O00 % OoO0O00
 if 72 - 72: OoooooooOO * II111iiii + OoO0O00 % iIii1I11I1II1 . I1ii11iIi11i % OoooooooOO
 if 19 - 19: OoOoOO00 + I1Ii111
def lisp_send_ecm ( lisp_sockets , packet , inner_source , inner_sport , inner_dest ,
 outer_dest , to_etr = False , to_ms = False , ddt = False ) :
 if 19 - 19: I1ii11iIi11i / I1Ii111 + OoooooooOO - O0
 if ( inner_source == None or inner_source . is_null ( ) ) :
  inner_source = inner_dest
  if 49 - 49: I1ii11iIi11i / OoOoOO00 - I1IiiI + iII111i . OOooOOo % oO0o
  if 34 - 34: OoO0O00 - I1IiiI + OoOoOO00
  if 22 - 22: iIii1I11I1II1 . i1IIi . OOooOOo % Oo0Ooo - i1IIi
  if 78 - 78: I1IiiI / i1IIi % II111iiii % I1IiiI % Ii1I
  if 29 - 29: i1IIi % o0oOOo0O0Ooo + OOooOOo / Oo0Ooo
  if 38 - 38: IiII . I1Ii111
 if ( lisp_nat_traversal ) :
  oo0O = lisp_get_any_translated_port ( )
  if ( oo0O != None ) : inner_sport = oo0O
  if 69 - 69: ooOoO0o + OoOoOO00 + II111iiii % I1Ii111 + Ii1I . ooOoO0o
 I1i1ii = lisp_ecm ( inner_sport )
 if 73 - 73: I11i % I11i . ooOoO0o + OoOoOO00
 I1i1ii . to_etr = to_etr if lisp_is_running ( "lisp-etr" ) else False
 I1i1ii . to_ms = to_ms if lisp_is_running ( "lisp-ms" ) else False
 I1i1ii . ddt = ddt
 Iioooo = I1i1ii . encode ( packet , inner_source , inner_dest )
 if ( Iioooo == None ) :
  lprint ( "Could not encode ECM message" )
  return
  if 14 - 14: iIii1I11I1II1 * iII111i . i1IIi - OoooooooOO
 I1i1ii . print_ecm ( )
 if 56 - 56: ooOoO0o . OoO0O00 * iIii1I11I1II1 / I11i % II111iiii . i1IIi
 packet = Iioooo + packet
 if 48 - 48: I1IiiI . Oo0Ooo * o0oOOo0O0Ooo
 oo0o00OO = outer_dest . print_address_no_iid ( )
 lprint ( "Send Encapsulated-Control-Message to {}" . format ( oo0o00OO ) )
 Ii1II1I11i1I = lisp_convert_4to6 ( oo0o00OO )
 lisp_send ( lisp_sockets , Ii1II1I11i1I , LISP_CTRL_PORT , packet )
 return
 if 45 - 45: Ii1I % OOooOOo * Ii1I - iIii1I11I1II1
 if 18 - 18: I1Ii111 / Oo0Ooo % Ii1I + OoO0O00
 if 69 - 69: iII111i % I1ii11iIi11i
 if 19 - 19: IiII
 if 35 - 35: OoOoOO00
 if 18 - 18: II111iiii . OoOoOO00 + I1ii11iIi11i * oO0o + OoooooooOO
 if 39 - 39: I1IiiI * ooOoO0o / i11iIiiIii - oO0o - oO0o + O0
LISP_AFI_GEO_COORD = - 3
LISP_AFI_IID_RANGE = - 2
LISP_AFI_ULTIMATE_ROOT = - 1
LISP_AFI_NONE = 0
LISP_AFI_IPV4 = 1
LISP_AFI_IPV6 = 2
LISP_AFI_MAC = 6
LISP_AFI_E164 = 8
LISP_AFI_NAME = 17
LISP_AFI_LCAF = 16387
if 73 - 73: OOooOOo
LISP_RLOC_UNKNOWN_STATE = 0
LISP_RLOC_UP_STATE = 1
LISP_RLOC_DOWN_STATE = 2
LISP_RLOC_UNREACH_STATE = 3
LISP_RLOC_NO_ECHOED_NONCE_STATE = 4
LISP_RLOC_ADMIN_DOWN_STATE = 5
if 44 - 44: I1ii11iIi11i * i1IIi - iIii1I11I1II1 - oO0o - oO0o * II111iiii
LISP_AUTH_NONE = 0
LISP_AUTH_MD5 = 1
LISP_AUTH_SHA1 = 2
LISP_AUTH_SHA2 = 3
if 98 - 98: Oo0Ooo + ooOoO0o / OOooOOo . iIii1I11I1II1 . I1IiiI . OoOoOO00
if 92 - 92: i1IIi + OoOoOO00 * i1IIi / IiII
if 4 - 4: oO0o % OoO0O00 + IiII + o0oOOo0O0Ooo
if 82 - 82: O0 / I1Ii111 + OOooOOo . IiII + Ii1I
if 31 - 31: i1IIi * OoO0O00 - Ii1I + I11i
if 8 - 8: O0 + i1IIi . O0
if 67 - 67: I1IiiI
LISP_IPV4_HOST_MASK_LEN = 32
LISP_IPV6_HOST_MASK_LEN = 128
LISP_MAC_HOST_MASK_LEN = 48
LISP_E164_HOST_MASK_LEN = 60
if 42 - 42: ooOoO0o - o0oOOo0O0Ooo % oO0o - ooOoO0o
if 87 - 87: OoooooooOO / O0
if 57 - 57: iIii1I11I1II1 / IiII + OoO0O00 * oO0o + Ii1I
if 76 - 76: i11iIiiIii . OOooOOo / I11i * oO0o % iIii1I11I1II1 . ooOoO0o
if 75 - 75: O0 + I1IiiI
if 67 - 67: OoOoOO00 % OoooooooOO / OoO0O00 - OoO0O00 / O0
def byte_swap_64 ( address ) :
 o0o00O0oOooO0 = ( ( address & 0x00000000000000ff ) << 56 ) | ( ( address & 0x000000000000ff00 ) << 40 ) | ( ( address & 0x0000000000ff0000 ) << 24 ) | ( ( address & 0x00000000ff000000 ) << 8 ) | ( ( address & 0x000000ff00000000 ) >> 8 ) | ( ( address & 0x0000ff0000000000 ) >> 24 ) | ( ( address & 0x00ff000000000000 ) >> 40 ) | ( ( address & 0xff00000000000000 ) >> 56 )
 if 19 - 19: iIii1I11I1II1 / OOooOOo % I11i % I1IiiI / I1ii11iIi11i
 if 73 - 73: II111iiii
 if 26 - 26: II111iiii . iIii1I11I1II1 - I1Ii111 % OOooOOo
 if 83 - 83: OOooOOo + OoooooooOO % I1Ii111 % IiII + i11iIiiIii
 if 10 - 10: OoooooooOO . Ii1I % I1Ii111 + IiII
 if 78 - 78: OoOoOO00 - oO0o . I1ii11iIi11i * i11iIiiIii
 if 44 - 44: iIii1I11I1II1 * iII111i
 if 32 - 32: OoOoOO00
 return ( o0o00O0oOooO0 )
 if 65 - 65: iIii1I11I1II1 + iII111i
 if 90 - 90: i11iIiiIii - Oo0Ooo
 if 31 - 31: OoOoOO00 + OoOoOO00 + OoooooooOO % O0
 if 14 - 14: i1IIi / OoooooooOO . I1IiiI * I1Ii111 + OoO0O00
 if 45 - 45: OoooooooOO * I1Ii111
 if 7 - 7: O0
 if 42 - 42: o0oOOo0O0Ooo / Ii1I
 if 31 - 31: OOooOOo
 if 20 - 20: i11iIiiIii * oO0o * ooOoO0o
 if 65 - 65: I1ii11iIi11i / Oo0Ooo / I1IiiI + IiII
 if 71 - 71: OoO0O00 . I1Ii111 + OoooooooOO
 if 9 - 9: OoooooooOO / iIii1I11I1II1 % I1IiiI . I1IiiI / I11i - iII111i
 if 60 - 60: I11i - OoO0O00 - OoOoOO00 * ooOoO0o - i1IIi
 if 18 - 18: ooOoO0o + i11iIiiIii + O0 + OOooOOo / Ii1I
 if 65 - 65: I1IiiI . ooOoO0o
class lisp_cache_entries ( ) :
 def __init__ ( self ) :
  self . entries = { }
  self . entries_sorted = [ ]
  if 51 - 51: I1Ii111
  if 89 - 89: Oo0Ooo
  if 15 - 15: OOooOOo * II111iiii - OOooOOo * iIii1I11I1II1
class lisp_cache ( ) :
 def __init__ ( self ) :
  self . cache = { }
  self . cache_sorted = [ ]
  self . cache_count = 0
  if 95 - 95: I1Ii111 / OoooooooOO * I11i * OoooooooOO
  if 88 - 88: I1IiiI / Oo0Ooo / oO0o + oO0o % OOooOOo + Oo0Ooo
 def cache_size ( self ) :
  return ( self . cache_count )
  if 63 - 63: o0oOOo0O0Ooo + i11iIiiIii % OOooOOo % iIii1I11I1II1 / I1ii11iIi11i - iII111i
  if 72 - 72: iII111i % oO0o . IiII + I1ii11iIi11i . IiII . II111iiii
 def build_key ( self , prefix ) :
  if ( prefix . afi == LISP_AFI_ULTIMATE_ROOT ) :
   iiIi = 0
  elif ( prefix . afi == LISP_AFI_IID_RANGE ) :
   iiIi = prefix . mask_len
  else :
   iiIi = prefix . mask_len + 48
   if 10 - 10: I11i . ooOoO0o + I11i * Ii1I
   if 55 - 55: OOooOOo / iII111i + OoooooooOO - OoooooooOO
  IiIIi11i111 = lisp_hex_string ( prefix . instance_id ) . zfill ( 8 )
  IiiiII = lisp_hex_string ( prefix . afi ) . zfill ( 4 )
  if 51 - 51: O0 % Ii1I % Oo0Ooo - O0
  if ( prefix . afi > 0 ) :
   if ( prefix . is_binary ( ) ) :
    oOOoO0O = prefix . addr_length ( ) * 2
    o0o00O0oOooO0 = lisp_hex_string ( prefix . address ) . zfill ( oOOoO0O )
   else :
    o0o00O0oOooO0 = prefix . address
    if 94 - 94: OoooooooOO - ooOoO0o % I1ii11iIi11i + I1Ii111
  elif ( prefix . afi == LISP_AFI_GEO_COORD ) :
   IiiiII = "8003"
   o0o00O0oOooO0 = prefix . address . print_geo ( )
  else :
   IiiiII = ""
   o0o00O0oOooO0 = ""
   if 51 - 51: I1ii11iIi11i . iII111i / i1IIi * ooOoO0o % I11i
   if 82 - 82: O0 % OoOoOO00 . iII111i . i1IIi . iII111i - Oo0Ooo
  o0Oo = IiIIi11i111 + IiiiII + o0o00O0oOooO0
  return ( [ iiIi , o0Oo ] )
  if 58 - 58: O0 * OOooOOo
  if 60 - 60: ooOoO0o
 def add_cache ( self , prefix , entry ) :
  if ( prefix . is_binary ( ) ) : prefix . zero_host_bits ( )
  iiIi , o0Oo = self . build_key ( prefix )
  if ( self . cache . has_key ( iiIi ) == False ) :
   self . cache [ iiIi ] = lisp_cache_entries ( )
   self . cache_sorted = self . sort_in_entry ( self . cache_sorted , iiIi )
   if 47 - 47: i11iIiiIii
  if ( self . cache [ iiIi ] . entries . has_key ( o0Oo ) == False ) :
   self . cache_count += 1
   if 21 - 21: i1IIi - oO0o - Oo0Ooo
  self . cache [ iiIi ] . entries [ o0Oo ] = entry
  if 11 - 11: i1IIi
  if 77 - 77: I11i + i1IIi * OoOoOO00 % OoooooooOO
 def lookup_cache ( self , prefix , exact ) :
  o00ooOoo0000o , o0Oo = self . build_key ( prefix )
  if ( exact ) :
   if ( self . cache . has_key ( o00ooOoo0000o ) == False ) : return ( None )
   if ( self . cache [ o00ooOoo0000o ] . entries . has_key ( o0Oo ) == False ) : return ( None )
   return ( self . cache [ o00ooOoo0000o ] . entries [ o0Oo ] )
   if 31 - 31: Oo0Ooo % OoooooooOO + OoooooooOO * o0oOOo0O0Ooo . I1IiiI
   if 68 - 68: iII111i - iIii1I11I1II1 - OoO0O00 - iII111i . O0 - i11iIiiIii
  ooOoOO0o = None
  for iiIi in self . cache_sorted :
   if ( o00ooOoo0000o < iiIi ) : return ( ooOoOO0o )
   for i1ii1i1Ii11 in self . cache [ iiIi ] . entries . values ( ) :
    if ( prefix . is_more_specific ( i1ii1i1Ii11 . eid ) ) :
     if ( ooOoOO0o == None or
 i1ii1i1Ii11 . eid . is_more_specific ( ooOoOO0o . eid ) ) : ooOoOO0o = i1ii1i1Ii11
     if 1 - 1: i1IIi * iIii1I11I1II1
     if 29 - 29: I11i
     if 12 - 12: oO0o % i1IIi - oO0o / ooOoO0o * II111iiii % ooOoO0o
  return ( ooOoOO0o )
  if 6 - 6: IiII / OoO0O00
  if 83 - 83: IiII - iIii1I11I1II1 * ooOoO0o - oO0o
 def delete_cache ( self , prefix ) :
  iiIi , o0Oo = self . build_key ( prefix )
  if ( self . cache . has_key ( iiIi ) == False ) : return
  if ( self . cache [ iiIi ] . entries . has_key ( o0Oo ) == False ) : return
  self . cache [ iiIi ] . entries . pop ( o0Oo )
  self . cache_count -= 1
  if 77 - 77: Ii1I
  if 9 - 9: OOooOOo / OoooooooOO + iII111i
 def walk_cache ( self , function , parms ) :
  for iiIi in self . cache_sorted :
   for i1ii1i1Ii11 in self . cache [ iiIi ] . entries . values ( ) :
    O00OO , parms = function ( i1ii1i1Ii11 , parms )
    if ( O00OO == False ) : return ( parms )
    if 14 - 14: i11iIiiIii / I1IiiI * II111iiii % i11iIiiIii
    if 48 - 48: IiII / II111iiii + iIii1I11I1II1 % Ii1I * I1IiiI / iII111i
  return ( parms )
  if 24 - 24: Ii1I . Ii1I + II111iiii
  if 44 - 44: OoOoOO00 / OoooooooOO % O0 * Ii1I * IiII
 def sort_in_entry ( self , table , value ) :
  if ( table == [ ] ) : return ( [ value ] )
  if 84 - 84: o0oOOo0O0Ooo * IiII * OOooOOo * iII111i
  oO0Oo0O = table
  while ( True ) :
   if ( len ( oO0Oo0O ) == 1 ) :
    if ( value == oO0Oo0O [ 0 ] ) : return ( table )
    ooo = table . index ( oO0Oo0O [ 0 ] )
    if ( value < oO0Oo0O [ 0 ] ) :
     return ( table [ 0 : ooo ] + [ value ] + table [ ooo : : ] )
     if 56 - 56: iII111i * II111iiii . OoooooooOO . I11i
    if ( value > oO0Oo0O [ 0 ] ) :
     return ( table [ 0 : ooo + 1 ] + [ value ] + table [ ooo + 1 : : ] )
     if 25 - 25: ooOoO0o % o0oOOo0O0Ooo - i11iIiiIii
     if 79 - 79: iII111i - I1IiiI % O0 / Oo0Ooo + OoOoOO00 . Oo0Ooo
   ooo = len ( oO0Oo0O ) / 2
   oO0Oo0O = oO0Oo0O [ 0 : ooo ] if ( value < oO0Oo0O [ ooo ] ) else oO0Oo0O [ ooo : : ]
   if 59 - 59: I1ii11iIi11i * OoOoOO00 / Ii1I
   if 80 - 80: IiII - ooOoO0o / OoOoOO00 / I11i * O0 + oO0o
  return ( [ ] )
  if 77 - 77: ooOoO0o + I1ii11iIi11i * o0oOOo0O0Ooo / i1IIi * I11i
  if 70 - 70: oO0o / iII111i * i1IIi / II111iiii / OoOoOO00 + oO0o
 def print_cache ( self ) :
  lprint ( "Printing contents of {}: " . format ( self ) )
  if ( self . cache_size ( ) == 0 ) :
   lprint ( "  Cache is empty" )
   return
   if 30 - 30: i1IIi - iII111i - i11iIiiIii . OoOoOO00 . o0oOOo0O0Ooo
  for iiIi in self . cache_sorted :
   for o0Oo in self . cache [ iiIi ] . entries :
    i1ii1i1Ii11 = self . cache [ iiIi ] . entries [ o0Oo ]
    lprint ( "  Mask-length: {}, key: {}, entry: {}" . format ( iiIi , o0Oo ,
 i1ii1i1Ii11 ) )
    if 74 - 74: i11iIiiIii / II111iiii
    if 62 - 62: O0
    if 63 - 63: Oo0Ooo + Oo0Ooo
    if 48 - 48: Oo0Ooo * I1ii11iIi11i % II111iiii
    if 42 - 42: I1Ii111 - ooOoO0o % o0oOOo0O0Ooo * I1IiiI . o0oOOo0O0Ooo
    if 84 - 84: iIii1I11I1II1
    if 39 - 39: Ii1I . II111iiii / I1IiiI
    if 44 - 44: Ii1I / Ii1I / OoO0O00 % ooOoO0o / I11i . I1ii11iIi11i
lisp_referral_cache = lisp_cache ( )
lisp_ddt_cache = lisp_cache ( )
lisp_sites_by_eid = lisp_cache ( )
lisp_map_cache = lisp_cache ( )
lisp_db_for_lookups = lisp_cache ( )
if 41 - 41: I1ii11iIi11i * ooOoO0o * I11i + O0 * O0 - O0
if 81 - 81: I1Ii111 % OoO0O00 / O0
if 55 - 55: i1IIi - I1Ii111 + I11i
if 93 - 93: I1IiiI % IiII . OoOoOO00 + iII111i
if 81 - 81: ooOoO0o / I1Ii111 + OOooOOo / Oo0Ooo / OoOoOO00
if 34 - 34: ooOoO0o * iIii1I11I1II1 % i11iIiiIii * OOooOOo - OOooOOo
if 63 - 63: Oo0Ooo / oO0o + iII111i % OoooooooOO * I11i
def lisp_map_cache_lookup ( source , dest ) :
 if 34 - 34: I1IiiI + I1Ii111 % ooOoO0o
 o000OO0oO0O = dest . is_multicast_address ( )
 if 24 - 24: Ii1I % II111iiii - i11iIiiIii
 if 52 - 52: OoO0O00
 if 76 - 76: ooOoO0o - iII111i % ooOoO0o / oO0o . OOooOOo
 if 50 - 50: IiII . i11iIiiIii % I11i
 o0Oo0 = lisp_map_cache . lookup_cache ( dest , False )
 if ( o0Oo0 == None ) :
  Ii1i1 = source . print_sg ( dest ) if o000OO0oO0O else dest . print_address ( )
  Ii1i1 = green ( Ii1i1 , False )
  dprint ( "Lookup for EID {} not found in map-cache" . format ( Ii1i1 ) )
  return ( None )
  if 22 - 22: i1IIi - II111iiii - OoOoOO00 . iII111i
  if 43 - 43: I1Ii111 * OOooOOo - IiII . i11iIiiIii
  if 34 - 34: iII111i . OoOoOO00
  if 49 - 49: I1ii11iIi11i % oO0o - I1Ii111 . I1ii11iIi11i % II111iiii
  if 20 - 20: I1ii11iIi11i . iIii1I11I1II1 - Ii1I % OoO0O00
 if ( o000OO0oO0O == False ) :
  ii11I1iiii1I = green ( o0Oo0 . eid . print_prefix ( ) , False )
  dprint ( "Lookup for EID {} found map-cache entry {}" . format ( green ( dest . print_address ( ) , False ) , ii11I1iiii1I ) )
  if 27 - 27: iIii1I11I1II1 / I1Ii111 - I11i . OoO0O00 + ooOoO0o
  return ( o0Oo0 )
  if 89 - 89: I1IiiI % I11i - OOooOOo
  if 71 - 71: OOooOOo % Oo0Ooo - o0oOOo0O0Ooo / I1Ii111 - O0 - oO0o
  if 10 - 10: I1IiiI
  if 17 - 17: i11iIiiIii % o0oOOo0O0Ooo . ooOoO0o
  if 34 - 34: OoooooooOO / iII111i / O0
 o0Oo0 = o0Oo0 . lookup_source_cache ( source , False )
 if ( o0Oo0 == None ) :
  Ii1i1 = source . print_sg ( dest )
  dprint ( "Lookup for EID {} not found in map-cache" . format ( Ii1i1 ) )
  return ( None )
  if 75 - 75: I11i % OOooOOo - OoO0O00 * I11i * IiII
  if 11 - 11: I1ii11iIi11i . O0 - iII111i * IiII . i1IIi . iII111i
  if 82 - 82: i1IIi * I11i * Ii1I - IiII . i11iIiiIii
  if 40 - 40: OOooOOo - OoooooooOO
  if 36 - 36: i1IIi % OoOoOO00 - i1IIi
 ii11I1iiii1I = green ( o0Oo0 . print_eid_tuple ( ) , False )
 dprint ( "Lookup for EID {} found map-cache entry {}" . format ( green ( source . print_sg ( dest ) , False ) , ii11I1iiii1I ) )
 if 5 - 5: I1IiiI . I1IiiI % II111iiii - I1Ii111
 return ( o0Oo0 )
 if 97 - 97: I11i . ooOoO0o
 if 87 - 87: oO0o / iIii1I11I1II1 - I11i + OoooooooOO
 if 79 - 79: I1ii11iIi11i * IiII . I1ii11iIi11i
 if 65 - 65: iII111i - Ii1I - II111iiii * O0 + I1ii11iIi11i . iIii1I11I1II1
 if 76 - 76: OoO0O00 * ooOoO0o
 if 32 - 32: O0 . oO0o * o0oOOo0O0Ooo . Ii1I + IiII
 if 98 - 98: iII111i . II111iiii % O0
def lisp_referral_cache_lookup ( eid , group , exact ) :
 if ( group and group . is_null ( ) ) :
  IiII111IiII1 = lisp_referral_cache . lookup_cache ( eid , exact )
  return ( IiII111IiII1 )
  if 43 - 43: OOooOOo % I1Ii111 . IiII % OoO0O00 + I1Ii111 % OoooooooOO
  if 17 - 17: OoooooooOO - i1IIi * I11i
  if 33 - 33: i1IIi . Oo0Ooo + I11i
  if 97 - 97: OOooOOo / IiII / ooOoO0o / OoooooooOO
  if 78 - 78: I1Ii111 + I1Ii111
 if ( eid == None or eid . is_null ( ) ) : return ( None )
 if 43 - 43: I1Ii111 * o0oOOo0O0Ooo + i1IIi
 if 19 - 19: Ii1I
 if 51 - 51: oO0o
 if 57 - 57: i11iIiiIii - Oo0Ooo + I1Ii111 * OoO0O00
 if 35 - 35: o0oOOo0O0Ooo % II111iiii + O0
 if 70 - 70: I1ii11iIi11i . II111iiii
 IiII111IiII1 = lisp_referral_cache . lookup_cache ( group , exact )
 if ( IiII111IiII1 == None ) : return ( None )
 if 54 - 54: OOooOOo
 OOoOoOO = IiII111IiII1 . lookup_source_cache ( eid , exact )
 if ( OOoOoOO ) : return ( OOoOoOO )
 if 40 - 40: II111iiii - I1ii11iIi11i
 if ( exact ) : IiII111IiII1 = None
 return ( IiII111IiII1 )
 if 48 - 48: I1Ii111 / I1ii11iIi11i % OOooOOo
 if 8 - 8: O0 . IiII - ooOoO0o * OoOoOO00 / OoO0O00 - O0
 if 41 - 41: OOooOOo % I11i + I1Ii111 / ooOoO0o
 if 34 - 34: iII111i - ooOoO0o + iIii1I11I1II1 + i1IIi . Ii1I
 if 34 - 34: I1IiiI + i1IIi . II111iiii . O0
 if 86 - 86: oO0o . OoOoOO00 - I11i . OOooOOo % OoO0O00
 if 79 - 79: iII111i / Ii1I % i11iIiiIii . I1IiiI % OoO0O00 / i11iIiiIii
def lisp_ddt_cache_lookup ( eid , group , exact ) :
 if ( group . is_null ( ) ) :
  O0oo0OoOO = lisp_ddt_cache . lookup_cache ( eid , exact )
  return ( O0oo0OoOO )
  if 100 - 100: OOooOOo + Oo0Ooo . iIii1I11I1II1 . ooOoO0o * Oo0Ooo
  if 16 - 16: Oo0Ooo % OoOoOO00 + I1Ii111 % I1Ii111
  if 12 - 12: I1Ii111 . Ii1I / iIii1I11I1II1 + i1IIi
  if 9 - 9: iIii1I11I1II1
  if 75 - 75: I11i . II111iiii * I1IiiI * IiII
 if ( eid . is_null ( ) ) : return ( None )
 if 36 - 36: OOooOOo / I1ii11iIi11i / oO0o / ooOoO0o / I11i
 if 7 - 7: OoO0O00 - I11i - o0oOOo0O0Ooo / o0oOOo0O0Ooo + i11iIiiIii
 if 28 - 28: OoOoOO00 % ooOoO0o . I1IiiI + II111iiii
 if 34 - 34: iIii1I11I1II1
 if 65 - 65: II111iiii - iII111i / o0oOOo0O0Ooo
 if 35 - 35: i11iIiiIii - Oo0Ooo . I1ii11iIi11i % OoOoOO00
 O0oo0OoOO = lisp_ddt_cache . lookup_cache ( group , exact )
 if ( O0oo0OoOO == None ) : return ( None )
 if 20 - 20: OoO0O00
 o0OOOO = O0oo0OoOO . lookup_source_cache ( eid , exact )
 if ( o0OOOO ) : return ( o0OOOO )
 if 18 - 18: Oo0Ooo % ooOoO0o
 if ( exact ) : O0oo0OoOO = None
 return ( O0oo0OoOO )
 if 25 - 25: o0oOOo0O0Ooo
 if 29 - 29: I1Ii111
 if 58 - 58: i1IIi / I1ii11iIi11i
 if 5 - 5: iIii1I11I1II1 % ooOoO0o . OOooOOo . ooOoO0o
 if 65 - 65: Oo0Ooo . I1IiiI / I11i * OOooOOo
 if 17 - 17: Ii1I . IiII
 if 46 - 46: O0 . OoooooooOO . ooOoO0o
def lisp_site_eid_lookup ( eid , group , exact ) :
 if 44 - 44: IiII / II111iiii - OoooooooOO
 if ( group . is_null ( ) ) :
  oOoooo = lisp_sites_by_eid . lookup_cache ( eid , exact )
  return ( oOoooo )
  if 47 - 47: OoO0O00 - ooOoO0o
  if 22 - 22: ooOoO0o % ooOoO0o . OOooOOo - II111iiii + OoO0O00
  if 44 - 44: I11i / o0oOOo0O0Ooo - OoO0O00 . Ii1I % oO0o - o0oOOo0O0Ooo
  if 14 - 14: OOooOOo * IiII
  if 15 - 15: o0oOOo0O0Ooo + OoooooooOO - OOooOOo - o0oOOo0O0Ooo . iIii1I11I1II1 / Ii1I
 if ( eid . is_null ( ) ) : return ( None )
 if 33 - 33: OoO0O00
 if 91 - 91: I11i % I11i % iII111i
 if 19 - 19: I11i / I11i + I1IiiI * OoO0O00 - iII111i . Oo0Ooo
 if 76 - 76: iII111i % OOooOOo / OoooooooOO . I1IiiI % OoO0O00 % i1IIi
 if 95 - 95: Oo0Ooo - O0 / I1ii11iIi11i . I1IiiI / o0oOOo0O0Ooo % OoOoOO00
 if 38 - 38: OoOoOO00 % OoooooooOO . oO0o - OoooooooOO + I11i
 oOoooo = lisp_sites_by_eid . lookup_cache ( group , exact )
 if ( oOoooo == None ) : return ( None )
 if 18 - 18: OoooooooOO + ooOoO0o * OoOoOO00 - OoO0O00
 if 42 - 42: oO0o % OoOoOO00 - oO0o + I11i / i11iIiiIii
 if 74 - 74: OoO0O00 - II111iiii - ooOoO0o % i1IIi
 if 42 - 42: i11iIiiIii / O0
 if 8 - 8: I1Ii111
 if 51 - 51: i11iIiiIii
 if 1 - 1: iIii1I11I1II1 . i1IIi . i11iIiiIii % I1ii11iIi11i
 if 58 - 58: i11iIiiIii * i11iIiiIii - OoO0O00
 if 8 - 8: i11iIiiIii * OoOoOO00 . o0oOOo0O0Ooo
 if 27 - 27: I1ii11iIi11i + Ii1I % I1Ii111
 if 20 - 20: Oo0Ooo
 if 33 - 33: oO0o - OoOoOO00 - i11iIiiIii + I1Ii111 + iIii1I11I1II1
 if 2 - 2: OoooooooOO + IiII / iII111i . iIii1I11I1II1 * OoOoOO00
 if 84 - 84: OOooOOo
 if 68 - 68: I1Ii111
 if 92 - 92: oO0o * Ii1I / OoO0O00 % II111iiii
 if 54 - 54: oO0o + I11i - OoO0O00
 if 86 - 86: OoooooooOO
 i1IiIiii = oOoooo . lookup_source_cache ( eid , exact )
 if ( i1IiIiii ) : return ( i1IiIiii )
 if 51 - 51: i11iIiiIii
 if ( exact ) :
  oOoooo = None
 else :
  O0Ii1IiiiI = oOoooo . parent_for_more_specifics
  if ( O0Ii1IiiiI and O0Ii1IiiiI . accept_more_specifics ) :
   if ( group . is_more_specific ( O0Ii1IiiiI . group ) ) : oOoooo = O0Ii1IiiiI
   if 91 - 91: OOooOOo
   if 22 - 22: OoooooooOO + OoOoOO00 - Ii1I . iII111i / OoooooooOO / I1IiiI
 return ( oOoooo )
 if 73 - 73: i1IIi - Ii1I + oO0o * iIii1I11I1II1
 if 100 - 100: i11iIiiIii / iIii1I11I1II1 + Oo0Ooo + OoO0O00 - iII111i
 if 8 - 8: i11iIiiIii . O0 + o0oOOo0O0Ooo * oO0o + II111iiii
 if 61 - 61: ooOoO0o / ooOoO0o
 if 51 - 51: iIii1I11I1II1 / oO0o * I1Ii111 + i1IIi
 if 96 - 96: Oo0Ooo + oO0o - Oo0Ooo - OoOoOO00 % OOooOOo . iIii1I11I1II1
 if 93 - 93: iIii1I11I1II1 % OoooooooOO
 if 6 - 6: II111iiii / oO0o - OOooOOo . O0 - o0oOOo0O0Ooo
 if 72 - 72: iIii1I11I1II1 / OoooooooOO * ooOoO0o / ooOoO0o % O0 + IiII
 if 96 - 96: iII111i / i11iIiiIii + Oo0Ooo . I1IiiI + iII111i % OoOoOO00
 if 19 - 19: i11iIiiIii . Oo0Ooo . OoOoOO00 - I1IiiI
 if 85 - 85: I11i - OoO0O00 % iIii1I11I1II1 . iII111i + ooOoO0o . Oo0Ooo
 if 87 - 87: iII111i
 if 86 - 86: IiII - I11i
 if 99 - 99: i1IIi + I1ii11iIi11i
 if 24 - 24: ooOoO0o / OoooooooOO % I1ii11iIi11i * ooOoO0o
 if 14 - 14: I1ii11iIi11i + OoO0O00 - I1IiiI - Oo0Ooo
 if 44 - 44: II111iiii / I1ii11iIi11i
 if 39 - 39: OoooooooOO % OoO0O00
 if 83 - 83: OOooOOo % I1IiiI + O0 % OoooooooOO
 if 84 - 84: I11i - Oo0Ooo % ooOoO0o - II111iiii
 if 29 - 29: IiII
 if 4 - 4: II111iiii * o0oOOo0O0Ooo - IiII * iII111i
 if 91 - 91: I1Ii111 * iII111i * OoO0O00
 if 79 - 79: iII111i + oO0o
 if 19 - 19: I1Ii111 - OOooOOo . ooOoO0o . O0 + II111iiii . OoooooooOO
class lisp_address ( ) :
 def __init__ ( self , afi , addr_str , mask_len , iid ) :
  self . afi = afi
  self . mask_len = mask_len
  self . instance_id = iid
  self . iid_list = [ ]
  self . address = 0
  if ( addr_str != "" ) : self . store_address ( addr_str )
  if 97 - 97: O0 / OoOoOO00 / ooOoO0o
  if 11 - 11: II111iiii . i11iIiiIii - Ii1I . IiII
 def copy_address ( self , addr ) :
  if ( addr == None ) : return
  self . afi = addr . afi
  self . address = addr . address
  self . mask_len = addr . mask_len
  self . instance_id = addr . instance_id
  self . iid_list = addr . iid_list
  if 10 - 10: OOooOOo * OoooooooOO
  if 12 - 12: II111iiii - O0 . i1IIi % oO0o % OoooooooOO
 def make_default_route ( self , addr ) :
  self . afi = addr . afi
  self . instance_id = addr . instance_id
  self . mask_len = 0
  self . address = 0
  if 36 - 36: IiII * OoOoOO00 - iIii1I11I1II1 + II111iiii
  if 65 - 65: I1IiiI * I11i . I1Ii111 % I1ii11iIi11i + O0
 def make_default_multicast_route ( self , addr ) :
  self . afi = addr . afi
  self . instance_id = addr . instance_id
  if ( self . afi == LISP_AFI_IPV4 ) :
   self . address = 0xe0000000
   self . mask_len = 4
   if 91 - 91: OoooooooOO % I1Ii111 * OoO0O00 - OoOoOO00
  if ( self . afi == LISP_AFI_IPV6 ) :
   self . address = 0xff << 120
   self . mask_len = 8
   if 5 - 5: iIii1I11I1II1 * I11i - oO0o % oO0o % o0oOOo0O0Ooo . i1IIi
  if ( self . afi == LISP_AFI_MAC ) :
   self . address = 0xffffffffffff
   self . mask_len = 48
   if 95 - 95: Oo0Ooo * I1ii11iIi11i + iII111i - o0oOOo0O0Ooo - Oo0Ooo . OoO0O00
   if 62 - 62: I11i
   if 58 - 58: I11i . OoOoOO00 + iII111i . iII111i
 def not_set ( self ) :
  return ( self . afi == LISP_AFI_NONE )
  if 43 - 43: I1Ii111 + I1Ii111 % Oo0Ooo % OoO0O00 - ooOoO0o
  if 61 - 61: OoOoOO00 + Ii1I % i11iIiiIii - I1IiiI * OoO0O00 % iIii1I11I1II1
 def is_private_address ( self ) :
  if ( self . is_ipv4 ( ) == False ) : return ( False )
  o0o00O0oOooO0 = self . address
  if ( ( ( o0o00O0oOooO0 & 0xff000000 ) >> 24 ) == 10 ) : return ( True )
  if ( ( ( o0o00O0oOooO0 & 0xff000000 ) >> 24 ) == 172 ) :
   o0ooOoo = ( o0o00O0oOooO0 & 0x00ff0000 ) >> 16
   if ( o0ooOoo >= 16 and o0ooOoo <= 31 ) : return ( True )
   if 67 - 67: o0oOOo0O0Ooo + iII111i
  if ( ( ( o0o00O0oOooO0 & 0xffff0000 ) >> 16 ) == 0xc0a8 ) : return ( True )
  return ( False )
  if 45 - 45: o0oOOo0O0Ooo - II111iiii * OoO0O00
  if 75 - 75: ooOoO0o . I1Ii111 * i1IIi . I1IiiI . Ii1I
 def is_multicast_address ( self ) :
  if ( self . is_ipv4 ( ) ) : return ( self . is_ipv4_multicast ( ) )
  if ( self . is_ipv6 ( ) ) : return ( self . is_ipv6_multicast ( ) )
  if ( self . is_mac ( ) ) : return ( self . is_mac_multicast ( ) )
  return ( False )
  if 69 - 69: o0oOOo0O0Ooo % ooOoO0o * Ii1I * I1Ii111
  if 59 - 59: Ii1I + Oo0Ooo % O0 % i1IIi - iII111i
 def host_mask_len ( self ) :
  if ( self . afi == LISP_AFI_IPV4 ) : return ( LISP_IPV4_HOST_MASK_LEN )
  if ( self . afi == LISP_AFI_IPV6 ) : return ( LISP_IPV6_HOST_MASK_LEN )
  if ( self . afi == LISP_AFI_MAC ) : return ( LISP_MAC_HOST_MASK_LEN )
  if ( self . afi == LISP_AFI_E164 ) : return ( LISP_E164_HOST_MASK_LEN )
  if ( self . afi == LISP_AFI_NAME ) : return ( len ( self . address ) * 8 )
  if ( self . afi == LISP_AFI_GEO_COORD ) :
   return ( len ( self . address . print_geo ( ) ) * 8 )
   if 4 - 4: O0 - oO0o % OoO0O00 % OoooooooOO
  return ( 0 )
  if 67 - 67: I11i
  if 23 - 23: I1ii11iIi11i - OoOoOO00
 def is_iana_eid ( self ) :
  if ( self . is_ipv6 ( ) == False ) : return ( False )
  o0o00O0oOooO0 = self . address >> 96
  return ( o0o00O0oOooO0 == 0x20010005 )
  if 90 - 90: ooOoO0o - I11i / OoOoOO00
  if 12 - 12: II111iiii % I1IiiI - I1ii11iIi11i
 def addr_length ( self ) :
  if ( self . afi == LISP_AFI_IPV4 ) : return ( 4 )
  if ( self . afi == LISP_AFI_IPV6 ) : return ( 16 )
  if ( self . afi == LISP_AFI_MAC ) : return ( 6 )
  if ( self . afi == LISP_AFI_E164 ) : return ( 8 )
  if ( self . afi == LISP_AFI_LCAF ) : return ( 0 )
  if ( self . afi == LISP_AFI_NAME ) : return ( len ( self . address ) + 1 )
  if ( self . afi == LISP_AFI_IID_RANGE ) : return ( 4 )
  if ( self . afi == LISP_AFI_GEO_COORD ) :
   return ( len ( self . address . print_geo ( ) ) )
   if 24 - 24: Ii1I + I11i
  return ( 0 )
  if 5 - 5: I1Ii111 . Ii1I - ooOoO0o % OoooooooOO
  if 2 - 2: OOooOOo . IiII . iII111i / Oo0Ooo
 def afi_to_version ( self ) :
  if ( self . afi == LISP_AFI_IPV4 ) : return ( 4 )
  if ( self . afi == LISP_AFI_IPV6 ) : return ( 6 )
  return ( 0 )
  if 86 - 86: OOooOOo . o0oOOo0O0Ooo - iIii1I11I1II1
  if 12 - 12: oO0o + iII111i
 def packet_format ( self ) :
  if 16 - 16: O0 + oO0o - ooOoO0o * O0 . I1ii11iIi11i . oO0o
  if 4 - 4: I1Ii111
  if 39 - 39: OoOoOO00 - I1Ii111 / I11i + II111iiii * I1IiiI * I1IiiI
  if 9 - 9: IiII * I1IiiI * OoO0O00 - I1IiiI * I1IiiI - OoO0O00
  if 20 - 20: i1IIi + I1IiiI + i11iIiiIii + II111iiii + i1IIi
  if ( self . afi == LISP_AFI_IPV4 ) : return ( "I" )
  if ( self . afi == LISP_AFI_IPV6 ) : return ( "QQ" )
  if ( self . afi == LISP_AFI_MAC ) : return ( "HHH" )
  if ( self . afi == LISP_AFI_E164 ) : return ( "II" )
  if ( self . afi == LISP_AFI_LCAF ) : return ( "I" )
  return ( "" )
  if 18 - 18: i11iIiiIii * O0 * Oo0Ooo + iII111i + OOooOOo
  if 62 - 62: OOooOOo - oO0o + i1IIi % Ii1I . I1Ii111 . II111iiii
 def pack_address ( self ) :
  O0O00Oo = self . packet_format ( )
  IiiiIi1iiii11 = ""
  if ( self . is_ipv4 ( ) ) :
   IiiiIi1iiii11 = struct . pack ( O0O00Oo , socket . htonl ( self . address ) )
  elif ( self . is_ipv6 ( ) ) :
   ooOo0O0 = byte_swap_64 ( self . address >> 64 )
   ooo0 = byte_swap_64 ( self . address & 0xffffffffffffffff )
   IiiiIi1iiii11 = struct . pack ( O0O00Oo , ooOo0O0 , ooo0 )
  elif ( self . is_mac ( ) ) :
   o0o00O0oOooO0 = self . address
   ooOo0O0 = ( o0o00O0oOooO0 >> 32 ) & 0xffff
   ooo0 = ( o0o00O0oOooO0 >> 16 ) & 0xffff
   o0oOooo00 = o0o00O0oOooO0 & 0xffff
   IiiiIi1iiii11 = struct . pack ( O0O00Oo , ooOo0O0 , ooo0 , o0oOooo00 )
  elif ( self . is_e164 ( ) ) :
   o0o00O0oOooO0 = self . address
   ooOo0O0 = ( o0o00O0oOooO0 >> 32 ) & 0xffffffff
   ooo0 = ( o0o00O0oOooO0 & 0xffffffff )
   IiiiIi1iiii11 = struct . pack ( O0O00Oo , ooOo0O0 , ooo0 )
  elif ( self . is_dist_name ( ) ) :
   IiiiIi1iiii11 += self . address + "\0"
   if 8 - 8: IiII . I1ii11iIi11i * II111iiii - I11i
  return ( IiiiIi1iiii11 )
  if 37 - 37: I1Ii111 / i11iIiiIii . I1ii11iIi11i - OoO0O00 * ooOoO0o
  if 91 - 91: ooOoO0o % II111iiii
 def unpack_address ( self , packet ) :
  O0O00Oo = self . packet_format ( )
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 48 - 48: oO0o
  o0o00O0oOooO0 = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  if 10 - 10: Oo0Ooo - O0 * i1IIi + I11i - OoooooooOO
  if ( self . is_ipv4 ( ) ) :
   self . address = socket . ntohl ( o0o00O0oOooO0 [ 0 ] )
   if 25 - 25: I1IiiI + iIii1I11I1II1 * Oo0Ooo - iIii1I11I1II1 % IiII * oO0o
  elif ( self . is_ipv6 ( ) ) :
   if 71 - 71: iIii1I11I1II1 % I1Ii111 % IiII / IiII + iIii1I11I1II1 % i1IIi
   if 93 - 93: Oo0Ooo / I1ii11iIi11i + Oo0Ooo + OOooOOo
   if 58 - 58: oO0o
   if 9 - 9: I1Ii111 - i1IIi . ooOoO0o
   if 33 - 33: I11i
   if 37 - 37: Oo0Ooo
   if 36 - 36: IiII % I11i
   if 72 - 72: oO0o % I11i % OOooOOo * iIii1I11I1II1 - OOooOOo % O0
   if ( o0o00O0oOooO0 [ 0 ] <= 0xffff and ( o0o00O0oOooO0 [ 0 ] & 0xff ) == 0 ) :
    OOoOooO0 = ( o0o00O0oOooO0 [ 0 ] << 48 ) << 64
   else :
    OOoOooO0 = byte_swap_64 ( o0o00O0oOooO0 [ 0 ] ) << 64
    if 10 - 10: OoOoOO00 . i1IIi
   I11II1i1i = byte_swap_64 ( o0o00O0oOooO0 [ 1 ] )
   self . address = OOoOooO0 | I11II1i1i
   if 14 - 14: OoooooooOO
  elif ( self . is_mac ( ) ) :
   i1I1iii1111I = o0o00O0oOooO0 [ 0 ]
   II1Ii = o0o00O0oOooO0 [ 1 ]
   iI1i1i = o0o00O0oOooO0 [ 2 ]
   self . address = ( i1I1iii1111I << 32 ) + ( II1Ii << 16 ) + iI1i1i
   if 35 - 35: iIii1I11I1II1 / II111iiii
  elif ( self . is_e164 ( ) ) :
   self . address = ( o0o00O0oOooO0 [ 0 ] << 32 ) + o0o00O0oOooO0 [ 1 ]
   if 27 - 27: I11i / ooOoO0o . I1Ii111 + Ii1I
  elif ( self . is_dist_name ( ) ) :
   packet , self . address = lisp_decode_dist_name ( packet )
   self . mask_len = len ( self . address ) * 8
   IiIii1i = 0
   if 66 - 66: I1Ii111 + iIii1I11I1II1 / iIii1I11I1II1 - I1IiiI
  packet = packet [ IiIii1i : : ]
  return ( packet )
  if 46 - 46: I1IiiI + iIii1I11I1II1 % OoooooooOO + OoooooooOO . OoO0O00 % iIii1I11I1II1
  if 62 - 62: OoooooooOO * o0oOOo0O0Ooo
 def is_ipv4 ( self ) :
  return ( True if ( self . afi == LISP_AFI_IPV4 ) else False )
  if 59 - 59: iIii1I11I1II1
  if 18 - 18: ooOoO0o % I1IiiI / iIii1I11I1II1 + O0
 def is_ipv4_link_local ( self ) :
  if ( self . is_ipv4 ( ) == False ) : return ( False )
  return ( ( ( self . address >> 16 ) & 0xffff ) == 0xa9fe )
  if 99 - 99: i11iIiiIii - o0oOOo0O0Ooo + o0oOOo0O0Ooo . OoooooooOO * iII111i . Oo0Ooo
  if 63 - 63: I11i
 def is_ipv4_loopback ( self ) :
  if ( self . is_ipv4 ( ) == False ) : return ( False )
  return ( self . address == 0x7f000001 )
  if 60 - 60: I1IiiI / I1ii11iIi11i / I11i / Ii1I + iIii1I11I1II1
  if 85 - 85: O0 / OOooOOo . OoOoOO00 / I1ii11iIi11i
 def is_ipv4_multicast ( self ) :
  if ( self . is_ipv4 ( ) == False ) : return ( False )
  return ( ( ( self . address >> 24 ) & 0xf0 ) == 0xe0 )
  if 80 - 80: I1ii11iIi11i * iII111i % i1IIi * OOooOOo % II111iiii % i1IIi
  if 44 - 44: OoooooooOO
 def is_ipv4_string ( self , addr_str ) :
  return ( addr_str . find ( "." ) != - 1 )
  if 18 - 18: i11iIiiIii
  if 65 - 65: i1IIi . iIii1I11I1II1 % iIii1I11I1II1
 def is_ipv6 ( self ) :
  return ( True if ( self . afi == LISP_AFI_IPV6 ) else False )
  if 35 - 35: iIii1I11I1II1 - o0oOOo0O0Ooo + I1ii11iIi11i * iII111i - OOooOOo . o0oOOo0O0Ooo
  if 12 - 12: iIii1I11I1II1 % OoO0O00 * Oo0Ooo
 def is_ipv6_link_local ( self ) :
  if ( self . is_ipv6 ( ) == False ) : return ( False )
  return ( ( ( self . address >> 112 ) & 0xffff ) == 0xfe80 )
  if 5 - 5: I11i - II111iiii * iIii1I11I1II1 / iIii1I11I1II1 % IiII * i1IIi
  if 30 - 30: i1IIi % I1IiiI . OOooOOo % iIii1I11I1II1 . I1ii11iIi11i / o0oOOo0O0Ooo
 def is_ipv6_string_link_local ( self , addr_str ) :
  return ( addr_str . find ( "fe80::" ) != - 1 )
  if 53 - 53: OOooOOo % ooOoO0o
  if 94 - 94: OOooOOo - O0 - I1Ii111 / OoooooooOO - iII111i
 def is_ipv6_loopback ( self ) :
  if ( self . is_ipv6 ( ) == False ) : return ( False )
  return ( self . address == 1 )
  if 83 - 83: OOooOOo * I1ii11iIi11i * iII111i * I1ii11iIi11i . OoO0O00
  if 87 - 87: ooOoO0o . O0 - oO0o
 def is_ipv6_multicast ( self ) :
  if ( self . is_ipv6 ( ) == False ) : return ( False )
  return ( ( ( self . address >> 120 ) & 0xff ) == 0xff )
  if 75 - 75: Oo0Ooo
  if 22 - 22: oO0o * I1Ii111 . II111iiii / Ii1I * O0
 def is_ipv6_string ( self , addr_str ) :
  return ( addr_str . find ( ":" ) != - 1 )
  if 33 - 33: oO0o * i1IIi + ooOoO0o * OOooOOo - O0 - iIii1I11I1II1
  if 35 - 35: I1Ii111
 def is_mac ( self ) :
  return ( True if ( self . afi == LISP_AFI_MAC ) else False )
  if 12 - 12: Ii1I % I1IiiI - I11i / iIii1I11I1II1 . I1IiiI % I1ii11iIi11i
  if 12 - 12: Oo0Ooo + I1IiiI
 def is_mac_multicast ( self ) :
  if ( self . is_mac ( ) == False ) : return ( False )
  return ( ( self . address & 0x010000000000 ) != 0 )
  if 12 - 12: OoOoOO00 / II111iiii
  if 100 - 100: I1ii11iIi11i % iIii1I11I1II1 . IiII . OoooooooOO / II111iiii
 def is_mac_broadcast ( self ) :
  if ( self . is_mac ( ) == False ) : return ( False )
  return ( self . address == 0xffffffffffff )
  if 28 - 28: I1IiiI
  if 27 - 27: I1IiiI % oO0o - iIii1I11I1II1 - o0oOOo0O0Ooo - IiII - O0
 def is_mac_string ( self , addr_str ) :
  return ( len ( addr_str ) == 15 and addr_str . find ( "-" ) != - 1 )
  if 46 - 46: II111iiii
  if 24 - 24: i11iIiiIii * i1IIi - I11i + o0oOOo0O0Ooo
 def is_link_local_multicast ( self ) :
  if ( self . is_ipv4 ( ) ) :
   return ( ( 0xe0ffff00 & self . address ) == 0xe0000000 )
   if 60 - 60: ooOoO0o
  if ( self . is_ipv6 ( ) ) :
   return ( ( self . address >> 112 ) & 0xffff == 0xff02 )
   if 62 - 62: i11iIiiIii
  return ( False )
  if 88 - 88: i11iIiiIii
  if 59 - 59: oO0o - OoooooooOO % ooOoO0o
 def is_null ( self ) :
  return ( True if ( self . afi == LISP_AFI_NONE ) else False )
  if 90 - 90: OoOoOO00
  if 96 - 96: II111iiii % Ii1I
 def is_ultimate_root ( self ) :
  return ( True if self . afi == LISP_AFI_ULTIMATE_ROOT else False )
  if 84 - 84: I1IiiI . I1IiiI
  if 82 - 82: OoO0O00 - iIii1I11I1II1 . iIii1I11I1II1 + I1ii11iIi11i
 def is_iid_range ( self ) :
  return ( True if self . afi == LISP_AFI_IID_RANGE else False )
  if 45 - 45: iII111i . oO0o * iII111i
  if 3 - 3: OoOoOO00 / Oo0Ooo - Oo0Ooo
 def is_e164 ( self ) :
  return ( True if ( self . afi == LISP_AFI_E164 ) else False )
  if 54 - 54: Oo0Ooo . OoO0O00 * I1IiiI % IiII
  if 97 - 97: o0oOOo0O0Ooo + Ii1I
 def is_dist_name ( self ) :
  return ( True if ( self . afi == LISP_AFI_NAME ) else False )
  if 77 - 77: I11i - oO0o . Ii1I
  if 75 - 75: I11i * OoooooooOO % OoOoOO00 . i1IIi - Ii1I + iIii1I11I1II1
 def is_geo_prefix ( self ) :
  return ( True if ( self . afi == LISP_AFI_GEO_COORD ) else False )
  if 74 - 74: ooOoO0o
  if 18 - 18: iIii1I11I1II1 - I11i - oO0o
 def is_binary ( self ) :
  if ( self . is_dist_name ( ) ) : return ( False )
  if ( self . is_geo_prefix ( ) ) : return ( False )
  return ( True )
  if 12 - 12: O0 + O0 + ooOoO0o . I1IiiI * II111iiii
  if 47 - 47: i11iIiiIii % OOooOOo / ooOoO0o . IiII - I1IiiI
 def store_address ( self , addr_str ) :
  if ( self . afi == LISP_AFI_NONE ) : self . string_to_afi ( addr_str )
  if 10 - 10: Oo0Ooo / ooOoO0o / I1ii11iIi11i
  if 98 - 98: O0 - I1Ii111 - i11iIiiIii
  if 85 - 85: II111iiii - I1ii11iIi11i % I1IiiI . I1IiiI - OoooooooOO - I11i
  if 38 - 38: i1IIi + oO0o * ooOoO0o % Ii1I % ooOoO0o
  iIi1I1 = addr_str . find ( "[" )
  I1iII = addr_str . find ( "]" )
  if ( iIi1I1 != - 1 and I1iII != - 1 ) :
   self . instance_id = int ( addr_str [ iIi1I1 + 1 : I1iII ] )
   addr_str = addr_str [ I1iII + 1 : : ]
   if ( self . is_dist_name ( ) == False ) :
    addr_str = addr_str . replace ( " " , "" )
    if 80 - 80: OoO0O00 + OoOoOO00 % iII111i % OoooooooOO - ooOoO0o
    if 25 - 25: OoOoOO00 % i11iIiiIii - I1IiiI * iIii1I11I1II1 - Oo0Ooo . O0
    if 48 - 48: I1IiiI + oO0o % i11iIiiIii % iIii1I11I1II1
    if 14 - 14: iIii1I11I1II1
    if 78 - 78: I1Ii111 / Oo0Ooo - I1Ii111
    if 1 - 1: OoO0O00 - I1IiiI * o0oOOo0O0Ooo
  if ( self . is_ipv4 ( ) ) :
   oOoOooO0o00 = addr_str . split ( "." )
   Oo00OO0OO = int ( oOoOooO0o00 [ 0 ] ) << 24
   Oo00OO0OO += int ( oOoOooO0o00 [ 1 ] ) << 16
   Oo00OO0OO += int ( oOoOooO0o00 [ 2 ] ) << 8
   Oo00OO0OO += int ( oOoOooO0o00 [ 3 ] )
   self . address = Oo00OO0OO
  elif ( self . is_ipv6 ( ) ) :
   if 85 - 85: i1IIi
   if 78 - 78: oO0o
   if 6 - 6: IiII
   if 69 - 69: iII111i
   if 87 - 87: i11iIiiIii % o0oOOo0O0Ooo + Ii1I
   if 72 - 72: Ii1I / II111iiii + o0oOOo0O0Ooo
   if 33 - 33: I1Ii111 * OoOoOO00 - OoooooooOO
   if 11 - 11: I1Ii111 - Oo0Ooo / iIii1I11I1II1 - OoooooooOO
   if 71 - 71: Oo0Ooo + Ii1I - OoooooooOO + I11i - iIii1I11I1II1 / O0
   if 76 - 76: i11iIiiIii % o0oOOo0O0Ooo . O0 * I11i
   if 90 - 90: II111iiii + OOooOOo % I1Ii111 * iIii1I11I1II1 % iIii1I11I1II1
   if 55 - 55: II111iiii % O0 * O0 - II111iiii * I1IiiI % Oo0Ooo
   if 48 - 48: I1ii11iIi11i + OoooooooOO % i1IIi
   if 46 - 46: OoOoOO00
   if 75 - 75: I1IiiI
   if 37 - 37: iIii1I11I1II1 % OoO0O00 * ooOoO0o + I11i % ooOoO0o / i11iIiiIii
   if 14 - 14: i1IIi / ooOoO0o
   I1Ii1 = ( addr_str [ 2 : 4 ] == "::" )
   try :
    addr_str = socket . inet_pton ( socket . AF_INET6 , addr_str )
   except :
    addr_str = socket . inet_pton ( socket . AF_INET6 , "0::0" )
    if 96 - 96: I1ii11iIi11i . oO0o - OoooooooOO
   addr_str = binascii . hexlify ( addr_str )
   if 7 - 7: iIii1I11I1II1
   if ( I1Ii1 ) :
    addr_str = addr_str [ 2 : 4 ] + addr_str [ 0 : 2 ] + addr_str [ 4 : : ]
    if 99 - 99: Ii1I
   self . address = int ( addr_str , 16 )
   if 1 - 1: OOooOOo - O0 / OoO0O00 % i11iIiiIii / ooOoO0o
  elif ( self . is_geo_prefix ( ) ) :
   I1Ii1i111I = lisp_geo ( None )
   I1Ii1i111I . name = "geo-prefix-{}" . format ( I1Ii1i111I )
   I1Ii1i111I . parse_geo_string ( addr_str )
   self . address = I1Ii1i111I
  elif ( self . is_mac ( ) ) :
   addr_str = addr_str . replace ( "-" , "" )
   Oo00OO0OO = int ( addr_str , 16 )
   self . address = Oo00OO0OO
  elif ( self . is_e164 ( ) ) :
   addr_str = addr_str [ 1 : : ]
   Oo00OO0OO = int ( addr_str , 16 )
   self . address = Oo00OO0OO << 4
  elif ( self . is_dist_name ( ) ) :
   self . address = addr_str . replace ( "'" , "" )
   if 70 - 70: Ii1I
  self . mask_len = self . host_mask_len ( )
  if 50 - 50: ooOoO0o % O0 . iIii1I11I1II1 - Ii1I * Oo0Ooo
  if 5 - 5: i11iIiiIii - I1ii11iIi11i
 def store_prefix ( self , prefix_str ) :
  if ( self . is_geo_string ( prefix_str ) ) :
   ooo = prefix_str . find ( "]" )
   oO00OO0Ooo00O = len ( prefix_str [ ooo + 1 : : ] ) * 8
  elif ( prefix_str . find ( "/" ) != - 1 ) :
   prefix_str , oO00OO0Ooo00O = prefix_str . split ( "/" )
  else :
   O0OO0 = prefix_str . find ( "'" )
   if ( O0OO0 == - 1 ) : return
   Ii1IiIiIi1IiI = prefix_str . find ( "'" , O0OO0 + 1 )
   if ( Ii1IiIiIi1IiI == - 1 ) : return
   oO00OO0Ooo00O = len ( prefix_str [ O0OO0 + 1 : Ii1IiIiIi1IiI ] ) * 8
   if 83 - 83: OoO0O00 - i11iIiiIii + I1ii11iIi11i - OOooOOo / OoOoOO00 / I11i
   if 53 - 53: I11i * I1IiiI . I1IiiI / o0oOOo0O0Ooo - I1Ii111
  self . string_to_afi ( prefix_str )
  self . store_address ( prefix_str )
  self . mask_len = int ( oO00OO0Ooo00O )
  if 50 - 50: I11i - OoOoOO00 + I1IiiI % Oo0Ooo / OoooooooOO - I1ii11iIi11i
  if 26 - 26: IiII . Ii1I
 def zero_host_bits ( self ) :
  if ( self . mask_len < 0 ) : return
  iI11iii = ( 2 ** self . mask_len ) - 1
  O0oooOo = self . addr_length ( ) * 8 - self . mask_len
  iI11iii <<= O0oooOo
  self . address &= iI11iii
  if 28 - 28: OoOoOO00 / Ii1I % o0oOOo0O0Ooo - Ii1I
  if 40 - 40: I1IiiI * O0 * iIii1I11I1II1 / Oo0Ooo
 def is_geo_string ( self , addr_str ) :
  ooo = addr_str . find ( "]" )
  if ( ooo != - 1 ) : addr_str = addr_str [ ooo + 1 : : ]
  if 15 - 15: iIii1I11I1II1 . OoOoOO00 % Ii1I / i1IIi . o0oOOo0O0Ooo
  I1Ii1i111I = addr_str . split ( "/" )
  if ( len ( I1Ii1i111I ) == 2 ) :
   if ( I1Ii1i111I [ 1 ] . isdigit ( ) == False ) : return ( False )
   if 45 - 45: iIii1I11I1II1 - i1IIi % I1IiiI - I1Ii111 + oO0o
  I1Ii1i111I = I1Ii1i111I [ 0 ]
  I1Ii1i111I = I1Ii1i111I . split ( "-" )
  iiii111I = len ( I1Ii1i111I )
  if ( iiii111I < 8 or iiii111I > 9 ) : return ( False )
  if 87 - 87: ooOoO0o * OoOoOO00
  for IiIIiI11I in range ( 0 , iiii111I ) :
   if ( IiIIiI11I == 3 ) :
    if ( I1Ii1i111I [ IiIIiI11I ] in [ "N" , "S" ] ) : continue
    return ( False )
    if 82 - 82: OOooOOo
   if ( IiIIiI11I == 7 ) :
    if ( I1Ii1i111I [ IiIIiI11I ] in [ "W" , "E" ] ) : continue
    return ( False )
    if 65 - 65: OoooooooOO - I1ii11iIi11i * iII111i . I1Ii111 / OoO0O00 / oO0o
   if ( I1Ii1i111I [ IiIIiI11I ] . isdigit ( ) == False ) : return ( False )
   if 31 - 31: i11iIiiIii / o0oOOo0O0Ooo . OOooOOo + II111iiii
  return ( True )
  if 14 - 14: Ii1I + OoooooooOO - I1Ii111 + I1Ii111 % IiII % OoooooooOO
  if 24 - 24: I1Ii111 . Oo0Ooo / ooOoO0o * O0
 def string_to_afi ( self , addr_str ) :
  if ( addr_str . count ( "'" ) == 2 ) :
   self . afi = LISP_AFI_NAME
   return
   if 85 - 85: I1IiiI - OOooOOo
  if ( addr_str . find ( ":" ) != - 1 ) : self . afi = LISP_AFI_IPV6
  elif ( addr_str . find ( "." ) != - 1 ) : self . afi = LISP_AFI_IPV4
  elif ( addr_str . find ( "+" ) != - 1 ) : self . afi = LISP_AFI_E164
  elif ( self . is_geo_string ( addr_str ) ) : self . afi = LISP_AFI_GEO_COORD
  elif ( addr_str . find ( "-" ) != - 1 ) : self . afi = LISP_AFI_MAC
  else : self . afi = LISP_AFI_NONE
  if 7 - 7: i1IIi % II111iiii
  if 33 - 33: iIii1I11I1II1 . O0 . oO0o
 def print_address ( self ) :
  o0o00O0oOooO0 = self . print_address_no_iid ( )
  IiIIi11i111 = "[" + str ( self . instance_id )
  for iIi1I1 in self . iid_list : IiIIi11i111 += "," + str ( iIi1I1 )
  IiIIi11i111 += "]"
  o0o00O0oOooO0 = "{}{}" . format ( IiIIi11i111 , o0o00O0oOooO0 )
  return ( o0o00O0oOooO0 )
  if 69 - 69: II111iiii * O0 . ooOoO0o * IiII
  if 25 - 25: I11i - I1ii11iIi11i . I1Ii111 . OoooooooOO
 def print_address_no_iid ( self ) :
  if ( self . is_ipv4 ( ) ) :
   o0o00O0oOooO0 = self . address
   I11I1Ii11II1i = o0o00O0oOooO0 >> 24
   Ii1II1I = ( o0o00O0oOooO0 >> 16 ) & 0xff
   IIiII = ( o0o00O0oOooO0 >> 8 ) & 0xff
   Oooii1IiI = o0o00O0oOooO0 & 0xff
   return ( "{}.{}.{}.{}" . format ( I11I1Ii11II1i , Ii1II1I , IIiII , Oooii1IiI ) )
  elif ( self . is_ipv6 ( ) ) :
   oo0o00OO = lisp_hex_string ( self . address ) . zfill ( 32 )
   oo0o00OO = binascii . unhexlify ( oo0o00OO )
   oo0o00OO = socket . inet_ntop ( socket . AF_INET6 , oo0o00OO )
   return ( "{}" . format ( oo0o00OO ) )
  elif ( self . is_geo_prefix ( ) ) :
   return ( "{}" . format ( self . address . print_geo ( ) ) )
  elif ( self . is_mac ( ) ) :
   oo0o00OO = lisp_hex_string ( self . address ) . zfill ( 12 )
   oo0o00OO = "{}-{}-{}" . format ( oo0o00OO [ 0 : 4 ] , oo0o00OO [ 4 : 8 ] ,
 oo0o00OO [ 8 : 12 ] )
   return ( "{}" . format ( oo0o00OO ) )
  elif ( self . is_e164 ( ) ) :
   oo0o00OO = lisp_hex_string ( self . address ) . zfill ( 15 )
   return ( "+{}" . format ( oo0o00OO ) )
  elif ( self . is_dist_name ( ) ) :
   return ( "'{}'" . format ( self . address ) )
  elif ( self . is_null ( ) ) :
   return ( "no-address" )
   if 23 - 23: OoOoOO00
  return ( "unknown-afi:{}" . format ( self . afi ) )
  if 33 - 33: i1IIi / o0oOOo0O0Ooo . OoooooooOO
  if 8 - 8: I1IiiI * OOooOOo * IiII / I1IiiI + i1IIi
 def print_prefix ( self ) :
  if ( self . is_ultimate_root ( ) ) : return ( "[*]" )
  if ( self . is_iid_range ( ) ) :
   if ( self . mask_len == 32 ) : return ( "[{}]" . format ( self . instance_id ) )
   I111Ii1ii1I1i = self . instance_id + ( 2 ** ( 32 - self . mask_len ) - 1 )
   return ( "[{}-{}]" . format ( self . instance_id , I111Ii1ii1I1i ) )
   if 97 - 97: O0 % ooOoO0o . Ii1I - ooOoO0o - I1ii11iIi11i
  o0o00O0oOooO0 = self . print_address ( )
  if ( self . is_dist_name ( ) ) : return ( o0o00O0oOooO0 )
  if ( self . is_geo_prefix ( ) ) : return ( o0o00O0oOooO0 )
  if 80 - 80: I1ii11iIi11i - OoO0O00 % I1ii11iIi11i + i11iIiiIii . oO0o
  ooo = o0o00O0oOooO0 . find ( "no-address" )
  if ( ooo == - 1 ) :
   o0o00O0oOooO0 = "{}/{}" . format ( o0o00O0oOooO0 , str ( self . mask_len ) )
  else :
   o0o00O0oOooO0 = o0o00O0oOooO0 [ 0 : ooo ]
   if 35 - 35: OoooooooOO * ooOoO0o + i11iIiiIii % i1IIi / ooOoO0o
  return ( o0o00O0oOooO0 )
  if 11 - 11: O0 * iII111i
  if 94 - 94: OoOoOO00 + OoooooooOO
 def print_prefix_no_iid ( self ) :
  o0o00O0oOooO0 = self . print_address_no_iid ( )
  if ( self . is_dist_name ( ) ) : return ( o0o00O0oOooO0 )
  if ( self . is_geo_prefix ( ) ) : return ( o0o00O0oOooO0 )
  return ( "{}/{}" . format ( o0o00O0oOooO0 , str ( self . mask_len ) ) )
  if 92 - 92: i11iIiiIii * IiII * I1IiiI - oO0o / iII111i
  if 1 - 1: ooOoO0o - OoO0O00 - o0oOOo0O0Ooo % I1Ii111 . I1ii11iIi11i - I1Ii111
 def print_prefix_url ( self ) :
  if ( self . is_ultimate_root ( ) ) : return ( "0--0" )
  o0o00O0oOooO0 = self . print_address ( )
  ooo = o0o00O0oOooO0 . find ( "]" )
  if ( ooo != - 1 ) : o0o00O0oOooO0 = o0o00O0oOooO0 [ ooo + 1 : : ]
  if ( self . is_geo_prefix ( ) ) :
   o0o00O0oOooO0 = o0o00O0oOooO0 . replace ( "/" , "-" )
   return ( "{}-{}" . format ( self . instance_id , o0o00O0oOooO0 ) )
   if 78 - 78: Oo0Ooo
  return ( "{}-{}-{}" . format ( self . instance_id , o0o00O0oOooO0 , self . mask_len ) )
  if 27 - 27: Ii1I / oO0o - Ii1I / iIii1I11I1II1 + o0oOOo0O0Ooo . Ii1I
  if 79 - 79: Ii1I % O0 * OOooOOo
 def print_sg ( self , g ) :
  OO0o0OO0 = self . print_prefix ( )
  II1IIII1iII = OO0o0OO0 . find ( "]" ) + 1
  g = g . print_prefix ( )
  i1IIIiii1 = g . find ( "]" ) + 1
  iii1IIiI = "[{}]({}, {})" . format ( self . instance_id , OO0o0OO0 [ II1IIII1iII : : ] , g [ i1IIIiii1 : : ] )
  return ( iii1IIiI )
  if 58 - 58: I1IiiI * I1Ii111 + iII111i + iIii1I11I1II1 + I1IiiI
  if 78 - 78: Oo0Ooo + ooOoO0o
 def hash_address ( self , addr ) :
  ooOo0O0 = self . address
  ooo0 = addr . address
  if 56 - 56: OoO0O00 / i1IIi + ooOoO0o . ooOoO0o . iII111i
  if ( self . is_geo_prefix ( ) ) : ooOo0O0 = self . address . print_geo ( )
  if ( addr . is_geo_prefix ( ) ) : ooo0 = addr . address . print_geo ( )
  if 37 - 37: iIii1I11I1II1 * OoOoOO00 . OoOoOO00 + OoooooooOO + OoO0O00
  if ( type ( ooOo0O0 ) == str ) :
   ooOo0O0 = int ( binascii . hexlify ( ooOo0O0 [ 0 : 1 ] ) )
   if 25 - 25: I1IiiI / IiII . OOooOOo . I1ii11iIi11i % i1IIi
  if ( type ( ooo0 ) == str ) :
   ooo0 = int ( binascii . hexlify ( ooo0 [ 0 : 1 ] ) )
   if 12 - 12: O0 % O0
  return ( ooOo0O0 ^ ooo0 )
  if 9 - 9: O0 . I1IiiI + I1ii11iIi11i / OOooOOo * I1ii11iIi11i
  if 10 - 10: IiII % o0oOOo0O0Ooo / O0 / II111iiii
  if 81 - 81: Ii1I / o0oOOo0O0Ooo % OoOoOO00 . I1ii11iIi11i
  if 47 - 47: II111iiii + OOooOOo / II111iiii . OOooOOo
  if 68 - 68: OoooooooOO
  if 63 - 63: I1IiiI
 def is_more_specific ( self , prefix ) :
  if ( prefix . afi == LISP_AFI_ULTIMATE_ROOT ) : return ( True )
  if 80 - 80: oO0o + iIii1I11I1II1
  oO00OO0Ooo00O = prefix . mask_len
  if ( prefix . afi == LISP_AFI_IID_RANGE ) :
   oOo0000OOo = 2 ** ( 32 - oO00OO0Ooo00O )
   O0o0I1ii1iiI1I1I1 = prefix . instance_id
   I111Ii1ii1I1i = O0o0I1ii1iiI1I1I1 + oOo0000OOo
   return ( self . instance_id in range ( O0o0I1ii1iiI1I1I1 , I111Ii1ii1I1i ) )
   if 56 - 56: OoooooooOO * o0oOOo0O0Ooo
   if 42 - 42: Oo0Ooo
  if ( self . instance_id != prefix . instance_id ) : return ( False )
  if ( self . afi != prefix . afi ) :
   if ( prefix . afi != LISP_AFI_NONE ) : return ( False )
   if 97 - 97: IiII / IiII . iII111i * O0 + II111iiii
   if 33 - 33: oO0o * IiII / i11iIiiIii
   if 76 - 76: o0oOOo0O0Ooo
   if 80 - 80: OOooOOo
   if 15 - 15: OOooOOo . OoOoOO00 / oO0o . I1ii11iIi11i % OoO0O00 - oO0o
  if ( self . is_binary ( ) == False ) :
   if ( prefix . afi == LISP_AFI_NONE ) : return ( True )
   if ( type ( self . address ) != type ( prefix . address ) ) : return ( False )
   o0o00O0oOooO0 = self . address
   I1ioo000000o = prefix . address
   if ( self . is_geo_prefix ( ) ) :
    o0o00O0oOooO0 = self . address . print_geo ( )
    I1ioo000000o = prefix . address . print_geo ( )
    if 17 - 17: I1IiiI
   if ( len ( o0o00O0oOooO0 ) < len ( I1ioo000000o ) ) : return ( False )
   return ( o0o00O0oOooO0 . find ( I1ioo000000o ) == 0 )
   if 14 - 14: Ii1I
   if 40 - 40: i1IIi
   if 53 - 53: Ii1I . I1ii11iIi11i - OOooOOo - ooOoO0o
   if 17 - 17: OoooooooOO / I1IiiI * ooOoO0o % I1ii11iIi11i . OoO0O00
   if 5 - 5: OoO0O00 % I1Ii111 . oO0o . Ii1I + I1IiiI
  if ( self . mask_len < oO00OO0Ooo00O ) : return ( False )
  if 95 - 95: II111iiii . iII111i - iIii1I11I1II1 / I11i + ooOoO0o * I1Ii111
  O0oooOo = ( prefix . addr_length ( ) * 8 ) - oO00OO0Ooo00O
  iI11iii = ( 2 ** oO00OO0Ooo00O - 1 ) << O0oooOo
  return ( ( self . address & iI11iii ) == prefix . address )
  if 92 - 92: iII111i * OoooooooOO % I1IiiI / OOooOOo
  if 46 - 46: OoOoOO00
 def mask_address ( self , mask_len ) :
  O0oooOo = ( self . addr_length ( ) * 8 ) - mask_len
  iI11iii = ( 2 ** mask_len - 1 ) << O0oooOo
  self . address &= iI11iii
  if 52 - 52: o0oOOo0O0Ooo - OoO0O00 % i1IIi / Ii1I % IiII
  if 100 - 100: oO0o . i11iIiiIii - ooOoO0o
 def is_exact_match ( self , prefix ) :
  if ( self . instance_id != prefix . instance_id ) : return ( False )
  II11II1111 = self . print_prefix ( )
  IiiiOo = prefix . print_prefix ( ) if prefix else ""
  return ( II11II1111 == IiiiOo )
  if 73 - 73: ooOoO0o - O0 % I11i + OoOoOO00 % ooOoO0o % OoooooooOO
  if 94 - 94: I11i . OoOoOO00 * OoooooooOO - IiII - Oo0Ooo % OoooooooOO
 def is_local ( self ) :
  if ( self . is_ipv4 ( ) ) :
   OoOo0 = lisp_myrlocs [ 0 ]
   if ( OoOo0 == None ) : return ( False )
   OoOo0 = OoOo0 . print_address_no_iid ( )
   return ( self . print_address_no_iid ( ) == OoOo0 )
   if 16 - 16: IiII
  if ( self . is_ipv6 ( ) ) :
   OoOo0 = lisp_myrlocs [ 1 ]
   if ( OoOo0 == None ) : return ( False )
   OoOo0 = OoOo0 . print_address_no_iid ( )
   return ( self . print_address_no_iid ( ) == OoOo0 )
   if 70 - 70: OoO0O00 . I1IiiI - OoOoOO00 + i1IIi / IiII . OoOoOO00
  return ( False )
  if 31 - 31: Ii1I % Ii1I
  if 57 - 57: I11i
 def store_iid_range ( self , iid , mask_len ) :
  if ( self . afi == LISP_AFI_NONE ) :
   if ( iid == 0 and mask_len == 0 ) : self . afi = LISP_AFI_ULTIMATE_ROOT
   else : self . afi = LISP_AFI_IID_RANGE
   if 95 - 95: OoOoOO00 + I11i * i1IIi - ooOoO0o % ooOoO0o
  self . instance_id = iid
  self . mask_len = mask_len
  if 58 - 58: OOooOOo
  if 74 - 74: i1IIi . IiII / ooOoO0o + I11i % i11iIiiIii % iII111i
 def lcaf_length ( self , lcaf_type ) :
  oOOoO0O = self . addr_length ( ) + 2
  if ( lcaf_type == LISP_LCAF_AFI_LIST_TYPE ) : oOOoO0O += 4
  if ( lcaf_type == LISP_LCAF_INSTANCE_ID_TYPE ) : oOOoO0O += 4
  if ( lcaf_type == LISP_LCAF_ASN_TYPE ) : oOOoO0O += 4
  if ( lcaf_type == LISP_LCAF_APP_DATA_TYPE ) : oOOoO0O += 8
  if ( lcaf_type == LISP_LCAF_GEO_COORD_TYPE ) : oOOoO0O += 12
  if ( lcaf_type == LISP_LCAF_OPAQUE_TYPE ) : oOOoO0O += 0
  if ( lcaf_type == LISP_LCAF_NAT_TYPE ) : oOOoO0O += 4
  if ( lcaf_type == LISP_LCAF_NONCE_LOC_TYPE ) : oOOoO0O += 4
  if ( lcaf_type == LISP_LCAF_MCAST_INFO_TYPE ) : oOOoO0O = oOOoO0O * 2 + 8
  if ( lcaf_type == LISP_LCAF_ELP_TYPE ) : oOOoO0O += 0
  if ( lcaf_type == LISP_LCAF_SECURITY_TYPE ) : oOOoO0O += 6
  if ( lcaf_type == LISP_LCAF_SOURCE_DEST_TYPE ) : oOOoO0O += 4
  if ( lcaf_type == LISP_LCAF_RLE_TYPE ) : oOOoO0O += 4
  return ( oOOoO0O )
  if 62 - 62: i1IIi % I1Ii111
  if 94 - 94: i1IIi + iII111i
  if 25 - 25: I1Ii111 . Ii1I - Ii1I . o0oOOo0O0Ooo - IiII
  if 91 - 91: o0oOOo0O0Ooo % I1ii11iIi11i % OoOoOO00 * iIii1I11I1II1
  if 18 - 18: OoOoOO00 * I1ii11iIi11i . i1IIi * iII111i
  if 67 - 67: IiII + i11iIiiIii . II111iiii / OoOoOO00 + OoooooooOO + i11iIiiIii
  if 23 - 23: Oo0Ooo
  if 7 - 7: Oo0Ooo / oO0o . I1Ii111 % I11i
  if 85 - 85: II111iiii / o0oOOo0O0Ooo . iIii1I11I1II1 . OoooooooOO / Ii1I
  if 18 - 18: i11iIiiIii + o0oOOo0O0Ooo . i11iIiiIii
  if 50 - 50: IiII / OoooooooOO . I11i
  if 93 - 93: OOooOOo / OoooooooOO % iII111i % Ii1I / I1Ii111 % OOooOOo
  if 25 - 25: i1IIi % Oo0Ooo . i1IIi * OoOoOO00 . Ii1I % OoO0O00
  if 47 - 47: o0oOOo0O0Ooo - i11iIiiIii / OoooooooOO
  if 93 - 93: I1IiiI * II111iiii * O0 % o0oOOo0O0Ooo + oO0o / ooOoO0o
  if 79 - 79: OoO0O00 + ooOoO0o / oO0o % I1ii11iIi11i
  if 77 - 77: Ii1I / Ii1I / I1ii11iIi11i
 def lcaf_encode_iid ( self ) :
  OOOoooO000O0 = LISP_LCAF_INSTANCE_ID_TYPE
  IiIi11 = socket . htons ( self . lcaf_length ( OOOoooO000O0 ) )
  IiIIi11i111 = self . instance_id
  IiiiII = self . afi
  iiIi = 0
  if ( IiiiII < 0 ) :
   if ( self . afi == LISP_AFI_GEO_COORD ) :
    IiiiII = LISP_AFI_LCAF
    iiIi = 0
   else :
    IiiiII = 0
    iiIi = self . mask_len
    if 92 - 92: O0 * i11iIiiIii . OoOoOO00 * IiII / o0oOOo0O0Ooo * ooOoO0o
    if 74 - 74: O0 - o0oOOo0O0Ooo
    if 68 - 68: I1Ii111
  iIi1i1ii = struct . pack ( "BBBBH" , 0 , 0 , OOOoooO000O0 , iiIi , IiIi11 )
  iIi1i1ii += struct . pack ( "IH" , socket . htonl ( IiIIi11i111 ) , socket . htons ( IiiiII ) )
  if ( IiiiII == 0 ) : return ( iIi1i1ii )
  if 37 - 37: ooOoO0o + I1Ii111 % OoO0O00 * I1Ii111
  if ( self . afi == LISP_AFI_GEO_COORD ) :
   iIi1i1ii = iIi1i1ii [ 0 : - 2 ]
   iIi1i1ii += self . address . encode_geo ( )
   return ( iIi1i1ii )
   if 71 - 71: Ii1I / I11i % iII111i + i11iIiiIii + I1ii11iIi11i * OoO0O00
   if 78 - 78: i11iIiiIii . iIii1I11I1II1 % oO0o + OoooooooOO - OoOoOO00
  iIi1i1ii += self . pack_address ( )
  return ( iIi1i1ii )
  if 9 - 9: I11i / iII111i * i11iIiiIii / OoOoOO00
  if 86 - 86: O0 . O0 - I1Ii111
 def lcaf_decode_iid ( self , packet ) :
  O0O00Oo = "BBBBH"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 95 - 95: Ii1I / Ii1I * OoO0O00 . OoooooooOO . OoooooooOO * I11i
  oOo0oo , IIIi1i1iIIIi , OOOoooO000O0 , OoO000oOo , oOOoO0O = struct . unpack ( O0O00Oo ,
 packet [ : IiIii1i ] )
  packet = packet [ IiIii1i : : ]
  if 55 - 55: i11iIiiIii - IiII * OOooOOo + II111iiii . I1ii11iIi11i / O0
  if ( OOOoooO000O0 != LISP_LCAF_INSTANCE_ID_TYPE ) : return ( None )
  if 16 - 16: II111iiii . Oo0Ooo * I1Ii111 + o0oOOo0O0Ooo - i11iIiiIii
  O0O00Oo = "IH"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( None )
  if 98 - 98: II111iiii - i1IIi - ooOoO0o
  IiIIi11i111 , IiiiII = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  packet = packet [ IiIii1i : : ]
  if 36 - 36: IiII + o0oOOo0O0Ooo
  oOOoO0O = socket . ntohs ( oOOoO0O )
  self . instance_id = socket . ntohl ( IiIIi11i111 )
  IiiiII = socket . ntohs ( IiiiII )
  self . afi = IiiiII
  if ( OoO000oOo != 0 and IiiiII == 0 ) : self . mask_len = OoO000oOo
  if ( IiiiII == 0 ) :
   self . afi = LISP_AFI_IID_RANGE if OoO000oOo else LISP_AFI_ULTIMATE_ROOT
   if 81 - 81: OOooOOo / I11i % oO0o + ooOoO0o
   if 10 - 10: oO0o / i11iIiiIii
   if 73 - 73: OoO0O00 - i1IIi
   if 52 - 52: I1ii11iIi11i
   if 4 - 4: Ii1I - iII111i + i1IIi - I1Ii111 / iII111i . Oo0Ooo
  if ( IiiiII == 0 ) : return ( packet )
  if 18 - 18: oO0o % iIii1I11I1II1 + ooOoO0o
  if 34 - 34: I1IiiI - OoooooooOO . IiII - OOooOOo % IiII
  if 19 - 19: IiII + I1ii11iIi11i % Oo0Ooo
  if 32 - 32: OOooOOo
  if ( self . is_dist_name ( ) ) :
   packet , self . address = lisp_decode_dist_name ( packet )
   self . mask_len = len ( self . address ) * 8
   return ( packet )
   if 46 - 46: II111iiii . OoO0O00
   if 97 - 97: oO0o
   if 45 - 45: i11iIiiIii / IiII + OoO0O00
   if 55 - 55: Ii1I / II111iiii - oO0o
   if 58 - 58: i1IIi . OoooooooOO % iIii1I11I1II1 * o0oOOo0O0Ooo + O0 / oO0o
  if ( IiiiII == LISP_AFI_LCAF ) :
   O0O00Oo = "BBBBH"
   IiIii1i = struct . calcsize ( O0O00Oo )
   if ( len ( packet ) < IiIii1i ) : return ( None )
   if 77 - 77: I11i . I1ii11iIi11i
   iI1i , O0OooO00O0 , OOOoooO000O0 , iiI1i111I1 , iII = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
   if 92 - 92: i11iIiiIii + I11i % I1IiiI / ooOoO0o
   if 28 - 28: i1IIi . I1IiiI
   if ( OOOoooO000O0 != LISP_LCAF_GEO_COORD_TYPE ) : return ( None )
   if 41 - 41: I1ii11iIi11i . I1Ii111 * OoOoOO00 . I1Ii111 / o0oOOo0O0Ooo
   iII = socket . ntohs ( iII )
   packet = packet [ IiIii1i : : ]
   if ( iII > len ( packet ) ) : return ( None )
   if 41 - 41: o0oOOo0O0Ooo / o0oOOo0O0Ooo . Oo0Ooo
   I1Ii1i111I = lisp_geo ( "" )
   self . afi = LISP_AFI_GEO_COORD
   self . address = I1Ii1i111I
   packet = I1Ii1i111I . decode_geo ( packet , iII , iiI1i111I1 )
   self . mask_len = self . host_mask_len ( )
   return ( packet )
   if 4 - 4: I1Ii111
   if 85 - 85: iIii1I11I1II1 % Oo0Ooo
  IiIi11 = self . addr_length ( )
  if ( len ( packet ) < IiIi11 ) : return ( None )
  if 20 - 20: IiII + i11iIiiIii * OOooOOo
  packet = self . unpack_address ( packet )
  return ( packet )
  if 27 - 27: O0 * OoO0O00 * I1ii11iIi11i
  if 40 - 40: O0 + oO0o - ooOoO0o + I1IiiI - IiII
  if 60 - 60: I1Ii111 * OoO0O00 * oO0o + oO0o
  if 34 - 34: o0oOOo0O0Ooo
  if 76 - 76: oO0o + OoooooooOO % OoOoOO00 / OoOoOO00
  if 51 - 51: II111iiii / OoOoOO00
  if 69 - 69: i11iIiiIii
  if 77 - 77: I1ii11iIi11i % OoooooooOO - Oo0Ooo - Ii1I + I11i
  if 93 - 93: I1IiiI % O0 * OoO0O00 % OoOoOO00 . I1Ii111 * I1IiiI
  if 95 - 95: IiII + o0oOOo0O0Ooo - o0oOOo0O0Ooo
  if 83 - 83: ooOoO0o
  if 59 - 59: I1ii11iIi11i
  if 26 - 26: I11i . Ii1I
  if 94 - 94: ooOoO0o . I1IiiI + IiII % I1IiiI / o0oOOo0O0Ooo % o0oOOo0O0Ooo
  if 21 - 21: O0 / OOooOOo - II111iiii + I1ii11iIi11i / OoooooooOO
  if 81 - 81: i11iIiiIii / Oo0Ooo * i1IIi + OoO0O00 + O0 % I1ii11iIi11i
  if 3 - 3: i11iIiiIii * IiII . Oo0Ooo % OoOoOO00 * I11i . iII111i
  if 80 - 80: I11i - IiII
  if 40 - 40: OOooOOo * I1IiiI % I11i . I1Ii111 % O0 . O0
  if 14 - 14: ooOoO0o . OoOoOO00 + ooOoO0o * OoOoOO00 . OoOoOO00 * Oo0Ooo
  if 40 - 40: OoooooooOO
 def lcaf_encode_sg ( self , group ) :
  OOOoooO000O0 = LISP_LCAF_MCAST_INFO_TYPE
  IiIIi11i111 = socket . htonl ( self . instance_id )
  IiIi11 = socket . htons ( self . lcaf_length ( OOOoooO000O0 ) )
  iIi1i1ii = struct . pack ( "BBBBHIHBB" , 0 , 0 , OOOoooO000O0 , 0 , IiIi11 , IiIIi11i111 ,
 0 , self . mask_len , group . mask_len )
  if 14 - 14: o0oOOo0O0Ooo / OOooOOo . OoOoOO00 % iIii1I11I1II1 % OoOoOO00
  iIi1i1ii += struct . pack ( "H" , socket . htons ( self . afi ) )
  iIi1i1ii += self . pack_address ( )
  iIi1i1ii += struct . pack ( "H" , socket . htons ( group . afi ) )
  iIi1i1ii += group . pack_address ( )
  return ( iIi1i1ii )
  if 92 - 92: o0oOOo0O0Ooo + II111iiii
  if 56 - 56: OoOoOO00 - OoOoOO00 / Ii1I
 def lcaf_decode_sg ( self , packet ) :
  O0O00Oo = "BBBBHIHBB"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( [ None , None ] )
  if 92 - 92: iIii1I11I1II1
  oOo0oo , IIIi1i1iIIIi , OOOoooO000O0 , iI111iiI1II , oOOoO0O , IiIIi11i111 , i1iIi , o00oOoOO0 , Oo0OO0oO = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
  if 45 - 45: o0oOOo0O0Ooo . I1Ii111 % Ii1I
  packet = packet [ IiIii1i : : ]
  if 42 - 42: Oo0Ooo + i11iIiiIii - OOooOOo . I1ii11iIi11i % I1Ii111 . I1ii11iIi11i
  if ( OOOoooO000O0 != LISP_LCAF_MCAST_INFO_TYPE ) : return ( [ None , None ] )
  if 59 - 59: OoooooooOO
  self . instance_id = socket . ntohl ( IiIIi11i111 )
  oOOoO0O = socket . ntohs ( oOOoO0O ) - 8
  if 91 - 91: i11iIiiIii / Oo0Ooo % I11i / O0
  if 80 - 80: II111iiii / I1ii11iIi11i % I1IiiI . Ii1I
  if 8 - 8: oO0o
  if 21 - 21: oO0o + iII111i . i11iIiiIii - II111iiii
  if 14 - 14: I1Ii111
  O0O00Oo = "H"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( [ None , None ] )
  if ( oOOoO0O < IiIii1i ) : return ( [ None , None ] )
  if 81 - 81: II111iiii
  IiiiII = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] ) [ 0 ]
  packet = packet [ IiIii1i : : ]
  oOOoO0O -= IiIii1i
  self . afi = socket . ntohs ( IiiiII )
  self . mask_len = o00oOoOO0
  IiIi11 = self . addr_length ( )
  if ( oOOoO0O < IiIi11 ) : return ( [ None , None ] )
  if 55 - 55: O0 + o0oOOo0O0Ooo * I1IiiI - OoooooooOO
  packet = self . unpack_address ( packet )
  if ( packet == None ) : return ( [ None , None ] )
  if 68 - 68: I11i + Oo0Ooo
  oOOoO0O -= IiIi11
  if 15 - 15: O0
  if 75 - 75: iII111i / OoOoOO00
  if 2 - 2: i1IIi + oO0o % iII111i % I1ii11iIi11i + ooOoO0o . iII111i
  if 26 - 26: I11i + o0oOOo0O0Ooo + Ii1I % I11i
  if 95 - 95: IiII - O0 * oO0o * O0
  O0O00Oo = "H"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( [ None , None ] )
  if ( oOOoO0O < IiIii1i ) : return ( [ None , None ] )
  if 47 - 47: I1IiiI
  IiiiII = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] ) [ 0 ]
  packet = packet [ IiIii1i : : ]
  oOOoO0O -= IiIii1i
  OOo0oOOO0 = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  OOo0oOOO0 . afi = socket . ntohs ( IiiiII )
  OOo0oOOO0 . mask_len = Oo0OO0oO
  OOo0oOOO0 . instance_id = self . instance_id
  IiIi11 = self . addr_length ( )
  if ( oOOoO0O < IiIi11 ) : return ( [ None , None ] )
  if 20 - 20: I1Ii111
  packet = OOo0oOOO0 . unpack_address ( packet )
  if ( packet == None ) : return ( [ None , None ] )
  if 40 - 40: OoooooooOO / o0oOOo0O0Ooo + OoOoOO00
  return ( [ packet , OOo0oOOO0 ] )
  if 73 - 73: OOooOOo / Oo0Ooo
  if 80 - 80: OoO0O00 + I1IiiI % i1IIi / I11i % i1IIi * i11iIiiIii
 def lcaf_decode_eid ( self , packet ) :
  O0O00Oo = "BBB"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( [ None , None ] )
  if 27 - 27: OoOoOO00 / I1Ii111 * O0 / I1IiiI - IiII / o0oOOo0O0Ooo
  if 70 - 70: I1ii11iIi11i
  if 11 - 11: I1Ii111
  if 70 - 70: Ii1I
  if 22 - 22: Ii1I
  iI111iiI1II , O0OooO00O0 , OOOoooO000O0 = struct . unpack ( O0O00Oo ,
 packet [ : IiIii1i ] )
  if 59 - 59: I1ii11iIi11i
  if ( OOOoooO000O0 == LISP_LCAF_INSTANCE_ID_TYPE ) :
   return ( [ self . lcaf_decode_iid ( packet ) , None ] )
  elif ( OOOoooO000O0 == LISP_LCAF_MCAST_INFO_TYPE ) :
   packet , OOo0oOOO0 = self . lcaf_decode_sg ( packet )
   return ( [ packet , OOo0oOOO0 ] )
  elif ( OOOoooO000O0 == LISP_LCAF_GEO_COORD_TYPE ) :
   O0O00Oo = "BBBBH"
   IiIii1i = struct . calcsize ( O0O00Oo )
   if ( len ( packet ) < IiIii1i ) : return ( None )
   if 90 - 90: OOooOOo / iII111i
   iI1i , O0OooO00O0 , OOOoooO000O0 , iiI1i111I1 , iII = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] )
   if 70 - 70: o0oOOo0O0Ooo
   if 49 - 49: OOooOOo - I1IiiI + OoooooooOO % iII111i + o0oOOo0O0Ooo + OoOoOO00
   if ( OOOoooO000O0 != LISP_LCAF_GEO_COORD_TYPE ) : return ( None )
   if 37 - 37: II111iiii % I1ii11iIi11i * OoOoOO00
   iII = socket . ntohs ( iII )
   packet = packet [ IiIii1i : : ]
   if ( iII > len ( packet ) ) : return ( None )
   if 35 - 35: i1IIi
   I1Ii1i111I = lisp_geo ( "" )
   self . instance_id = 0
   self . afi = LISP_AFI_GEO_COORD
   self . address = I1Ii1i111I
   packet = I1Ii1i111I . decode_geo ( packet , iII , iiI1i111I1 )
   self . mask_len = self . host_mask_len ( )
   if 81 - 81: OoO0O00
  return ( [ packet , None ] )
  if 45 - 45: OoooooooOO . O0 * oO0o + IiII
  if 18 - 18: II111iiii . O0 - I11i / I11i
  if 71 - 71: OoOoOO00 + iIii1I11I1II1 - II111iiii / i1IIi
  if 39 - 39: Ii1I + I1Ii111 * Oo0Ooo + OoOoOO00 / I1Ii111 - ooOoO0o
  if 66 - 66: I11i * OoO0O00
  if 98 - 98: IiII . Oo0Ooo + I1Ii111
class lisp_elp_node ( ) :
 def __init__ ( self ) :
  self . address = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . probe = False
  self . strict = False
  self . eid = False
  self . we_are_last = False
  if 63 - 63: oO0o * I1IiiI * oO0o
  if 56 - 56: oO0o - Ii1I % I1Ii111
 def copy_elp_node ( self ) :
  IIii = lisp_elp_node ( )
  IIii . copy_address ( self . address )
  IIii . probe = self . probe
  IIii . strict = self . strict
  IIii . eid = self . eid
  IIii . we_are_last = self . we_are_last
  return ( IIii )
  if 100 - 100: OOooOOo * IiII % IiII / o0oOOo0O0Ooo * OoO0O00 % OoOoOO00
  if 12 - 12: I1IiiI
  if 32 - 32: I1Ii111
class lisp_elp ( ) :
 def __init__ ( self , name ) :
  self . elp_name = name
  self . elp_nodes = [ ]
  self . use_elp_node = None
  self . we_are_last = False
  if 35 - 35: O0 + II111iiii + o0oOOo0O0Ooo - OoO0O00 - Ii1I
  if 88 - 88: I1ii11iIi11i . O0 - o0oOOo0O0Ooo . I1ii11iIi11i * iII111i * I11i
 def copy_elp ( self ) :
  O0OoO0O0O0oO = lisp_elp ( self . elp_name )
  O0OoO0O0O0oO . use_elp_node = self . use_elp_node
  O0OoO0O0O0oO . we_are_last = self . we_are_last
  for IIii in self . elp_nodes :
   O0OoO0O0O0oO . elp_nodes . append ( IIii . copy_elp_node ( ) )
   if 89 - 89: Oo0Ooo - oO0o + O0 / i11iIiiIii
  return ( O0OoO0O0O0oO )
  if 64 - 64: OoO0O00 % OoOoOO00 % I1IiiI - Ii1I / IiII * Ii1I
  if 74 - 74: IiII - O0 % OOooOOo % OoooooooOO - I11i
 def print_elp ( self , want_marker ) :
  OoOiIIiI = ""
  for IIii in self . elp_nodes :
   IiIIIi1 = ""
   if ( want_marker ) :
    if ( IIii == self . use_elp_node ) :
     IiIIIi1 = "*"
    elif ( IIii . we_are_last ) :
     IiIIIi1 = "x"
     if 25 - 25: ooOoO0o
     if 87 - 87: iII111i - OoO0O00 . Ii1I / ooOoO0o
   OoOiIIiI += "{}{}({}{}{}), " . format ( IiIIIi1 ,
 IIii . address . print_address_no_iid ( ) ,
 "r" if IIii . eid else "R" , "P" if IIii . probe else "p" ,
 "S" if IIii . strict else "s" )
   if 88 - 88: O0 % OOooOOo . iII111i
  return ( OoOiIIiI [ 0 : - 2 ] if OoOiIIiI != "" else "" )
  if 40 - 40: O0 . Ii1I % IiII % I1ii11iIi11i - OoOoOO00
  if 94 - 94: I1IiiI . I1Ii111
 def select_elp_node ( self ) :
  iiiI1i1I , II11 , OoO0o0OOOO = lisp_myrlocs
  ooo = None
  if 28 - 28: IiII
  for IIii in self . elp_nodes :
   if ( iiiI1i1I and IIii . address . is_exact_match ( iiiI1i1I ) ) :
    ooo = self . elp_nodes . index ( IIii )
    break
    if 42 - 42: oO0o + Oo0Ooo * I1ii11iIi11i . o0oOOo0O0Ooo / iIii1I11I1II1
   if ( II11 and IIii . address . is_exact_match ( II11 ) ) :
    ooo = self . elp_nodes . index ( IIii )
    break
    if 9 - 9: I1Ii111 * II111iiii % Ii1I - Ii1I % OoO0O00 % o0oOOo0O0Ooo
    if 26 - 26: o0oOOo0O0Ooo - I1IiiI / OoooooooOO / ooOoO0o % iIii1I11I1II1 % I1ii11iIi11i
    if 6 - 6: iIii1I11I1II1 * I1ii11iIi11i / I11i % I1Ii111 / Oo0Ooo
    if 94 - 94: OoO0O00 - oO0o + iII111i . ooOoO0o * OoooooooOO
    if 42 - 42: iII111i / i11iIiiIii + II111iiii % IiII / ooOoO0o
    if 100 - 100: ooOoO0o / I1IiiI
    if 69 - 69: ooOoO0o + OoO0O00 * o0oOOo0O0Ooo - ooOoO0o
  if ( ooo == None ) :
   self . use_elp_node = self . elp_nodes [ 0 ]
   IIii . we_are_last = False
   return
   if 66 - 66: OoooooooOO / iII111i / I1IiiI % ooOoO0o / OoO0O00 + OOooOOo
   if 64 - 64: i1IIi
   if 26 - 26: OoOoOO00 / o0oOOo0O0Ooo . OOooOOo + I1IiiI + Ii1I . iII111i
   if 89 - 89: I1Ii111 * I1IiiI . i1IIi - iIii1I11I1II1 * I1Ii111
   if 5 - 5: OoOoOO00 % i1IIi
   if 31 - 31: Oo0Ooo * O0 . OOooOOo . o0oOOo0O0Ooo + OoO0O00 + II111iiii
  if ( self . elp_nodes [ - 1 ] == self . elp_nodes [ ooo ] ) :
   self . use_elp_node = None
   IIii . we_are_last = True
   return
   if 76 - 76: Oo0Ooo + I1IiiI - O0
   if 58 - 58: IiII * i1IIi . I1IiiI - iII111i
   if 73 - 73: Oo0Ooo . OoOoOO00
   if 50 - 50: IiII / o0oOOo0O0Ooo
   if 9 - 9: Oo0Ooo - OoO0O00 + iII111i / OoooooooOO
  self . use_elp_node = self . elp_nodes [ ooo + 1 ]
  return
  if 52 - 52: O0
  if 34 - 34: OoooooooOO + OoOoOO00 - Oo0Ooo . OOooOOo * iIii1I11I1II1
  if 93 - 93: i11iIiiIii / Oo0Ooo * OoOoOO00 / ooOoO0o + OoO0O00 * OOooOOo
class lisp_geo ( ) :
 def __init__ ( self , name ) :
  self . geo_name = name
  self . latitude = 0xffffffff
  self . lat_mins = 0
  self . lat_secs = 0
  self . longitude = 0xffffffff
  self . long_mins = 0
  self . long_secs = 0
  self . altitude = - 1
  self . radius = 0
  if 81 - 81: IiII * iII111i + i1IIi + I1Ii111 / OoO0O00
  if 83 - 83: oO0o / OoO0O00
 def copy_geo ( self ) :
  I1Ii1i111I = lisp_geo ( self . geo_name )
  I1Ii1i111I . latitude = self . latitude
  I1Ii1i111I . lat_mins = self . lat_mins
  I1Ii1i111I . lat_secs = self . lat_secs
  I1Ii1i111I . longitude = self . longitude
  I1Ii1i111I . long_mins = self . long_mins
  I1Ii1i111I . long_secs = self . long_secs
  I1Ii1i111I . altitude = self . altitude
  I1Ii1i111I . radius = self . radius
  return ( I1Ii1i111I )
  if 34 - 34: OoooooooOO - i1IIi * O0
  if 83 - 83: I1IiiI + OoO0O00
 def no_geo_altitude ( self ) :
  return ( self . altitude == - 1 )
  if 41 - 41: Ii1I + II111iiii . OOooOOo * I1Ii111 / II111iiii
  if 32 - 32: Oo0Ooo - Ii1I % o0oOOo0O0Ooo
 def parse_geo_string ( self , geo_str ) :
  ooo = geo_str . find ( "]" )
  if ( ooo != - 1 ) : geo_str = geo_str [ ooo + 1 : : ]
  if 15 - 15: iIii1I11I1II1 * I1ii11iIi11i / ooOoO0o * oO0o % OOooOOo
  if 62 - 62: Ii1I / Oo0Ooo . OoO0O00 - OOooOOo
  if 89 - 89: o0oOOo0O0Ooo % OoO0O00
  if 53 - 53: OoOoOO00 . ooOoO0o - OoO0O00
  if 26 - 26: ooOoO0o - oO0o + OOooOOo * Ii1I - I11i % I1IiiI
  if ( geo_str . find ( "/" ) != - 1 ) :
   geo_str , O0o0oo0 = geo_str . split ( "/" )
   self . radius = int ( O0o0oo0 )
   if 77 - 77: OOooOOo % I1IiiI - iII111i % I1Ii111
   if 29 - 29: iIii1I11I1II1 / i11iIiiIii + Oo0Ooo
  geo_str = geo_str . split ( "-" )
  if ( len ( geo_str ) < 8 ) : return ( False )
  if 99 - 99: I1IiiI - iII111i * Ii1I - OoOoOO00 / i11iIiiIii - i1IIi
  iI1ii11ii111 = geo_str [ 0 : 4 ]
  oO00Oo0oOo = geo_str [ 4 : 8 ]
  if 8 - 8: iII111i + OOooOOo / I1ii11iIi11i . iII111i
  if 45 - 45: i1IIi
  if 28 - 28: iII111i
  if 28 - 28: i1IIi - iII111i + o0oOOo0O0Ooo / Oo0Ooo * oO0o
  if ( len ( geo_str ) > 8 ) : self . altitude = int ( geo_str [ 8 ] )
  if 8 - 8: ooOoO0o + OOooOOo * ooOoO0o / i1IIi . I1ii11iIi11i
  if 4 - 4: Ii1I - Oo0Ooo . i1IIi + iIii1I11I1II1
  if 28 - 28: O0 / ooOoO0o / IiII - I11i + IiII + OoO0O00
  if 84 - 84: Oo0Ooo + OoOoOO00 / iII111i . I1ii11iIi11i
  self . latitude = int ( iI1ii11ii111 [ 0 ] )
  self . lat_mins = int ( iI1ii11ii111 [ 1 ] )
  self . lat_secs = int ( iI1ii11ii111 [ 2 ] )
  if ( iI1ii11ii111 [ 3 ] == "N" ) : self . latitude = - self . latitude
  if 26 - 26: Oo0Ooo
  if 61 - 61: Ii1I * oO0o * i11iIiiIii + OoO0O00
  if 43 - 43: OoO0O00 * OoO0O00 * oO0o
  if 24 - 24: oO0o
  self . longitude = int ( oO00Oo0oOo [ 0 ] )
  self . long_mins = int ( oO00Oo0oOo [ 1 ] )
  self . long_secs = int ( oO00Oo0oOo [ 2 ] )
  if ( oO00Oo0oOo [ 3 ] == "E" ) : self . longitude = - self . longitude
  return ( True )
  if 77 - 77: i11iIiiIii - I1Ii111 - I1ii11iIi11i * Oo0Ooo / i11iIiiIii
  if 79 - 79: Oo0Ooo % Oo0Ooo . oO0o + ooOoO0o * iII111i * I11i
 def print_geo ( self ) :
  OO0OOOo = "N" if self . latitude < 0 else "S"
  oOooo = "E" if self . longitude < 0 else "W"
  if 42 - 42: OoO0O00 + i1IIi
  I1i1iiIII1i1 = "{}-{}-{}-{}-{}-{}-{}-{}" . format ( abs ( self . latitude ) ,
 self . lat_mins , self . lat_secs , OO0OOOo , abs ( self . longitude ) ,
 self . long_mins , self . long_secs , oOooo )
  if 39 - 39: ooOoO0o + Ii1I - oO0o / iII111i % IiII
  if ( self . no_geo_altitude ( ) == False ) :
   I1i1iiIII1i1 += "-" + str ( self . altitude )
   if 22 - 22: II111iiii
   if 76 - 76: i1IIi
   if 60 - 60: iII111i - I1IiiI * I1ii11iIi11i - i1IIi % I1Ii111 % O0
   if 24 - 24: I11i + I11i % I11i
   if 63 - 63: i11iIiiIii + iIii1I11I1II1 / oO0o % IiII - O0
  if ( self . radius != 0 ) : I1i1iiIII1i1 += "/{}" . format ( self . radius )
  return ( I1i1iiIII1i1 )
  if 21 - 21: II111iiii
  if 89 - 89: OOooOOo % i11iIiiIii * OoOoOO00 % oO0o / O0 * i1IIi
 def geo_url ( self ) :
  iIIii11IiI11 = os . getenv ( "LISP_GEO_ZOOM_LEVEL" )
  iIIii11IiI11 = "10" if ( iIIii11IiI11 == "" or iIIii11IiI11 . isdigit ( ) == False ) else iIIii11IiI11
  iiII , OOo0o0ooO0o0o = self . dms_to_decimal ( )
  iIOo00o0oO0 = ( "http://maps.googleapis.com/maps/api/staticmap?center={},{}" + "&markers=color:blue%7Clabel:lisp%7C{},{}" + "&zoom={}&size=1024x1024&sensor=false" ) . format ( iiII , OOo0o0ooO0o0o , iiII , OOo0o0ooO0o0o ,
  # I1IiiI * ooOoO0o % oO0o / i11iIiiIii
  # OOooOOo . o0oOOo0O0Ooo - i11iIiiIii . iIii1I11I1II1 . OOooOOo % IiII
 iIIii11IiI11 )
  return ( iIOo00o0oO0 )
  if 68 - 68: I11i / iII111i - IiII . iIii1I11I1II1 / o0oOOo0O0Ooo
  if 54 - 54: II111iiii * I1IiiI
 def print_geo_url ( self ) :
  I1Ii1i111I = self . print_geo ( )
  if ( self . radius == 0 ) :
   iIOo00o0oO0 = self . geo_url ( )
   O0ooo = "<a href='{}'>{}</a>" . format ( iIOo00o0oO0 , I1Ii1i111I )
  else :
   iIOo00o0oO0 = I1Ii1i111I . replace ( "/" , "-" )
   O0ooo = "<a href='/lisp/geo-map/{}'>{}</a>" . format ( iIOo00o0oO0 , I1Ii1i111I )
   if 49 - 49: I1ii11iIi11i
  return ( O0ooo )
  if 31 - 31: o0oOOo0O0Ooo - OoOoOO00 + I1ii11iIi11i . oO0o - O0
  if 61 - 61: I1ii11iIi11i * II111iiii . i1IIi
 def dms_to_decimal ( self ) :
  Oo000o0o0o , Ii11II , i1II1II1 = self . latitude , self . lat_mins , self . lat_secs
  Oo0o0o0 = float ( abs ( Oo000o0o0o ) )
  Oo0o0o0 += float ( Ii11II * 60 + i1II1II1 ) / 3600
  if ( Oo000o0o0o > 0 ) : Oo0o0o0 = - Oo0o0o0
  Ii111i1I = Oo0o0o0
  if 95 - 95: OoooooooOO - I1IiiI . iIii1I11I1II1
  Oo000o0o0o , Ii11II , i1II1II1 = self . longitude , self . long_mins , self . long_secs
  Oo0o0o0 = float ( abs ( Oo000o0o0o ) )
  Oo0o0o0 += float ( Ii11II * 60 + i1II1II1 ) / 3600
  if ( Oo000o0o0o > 0 ) : Oo0o0o0 = - Oo0o0o0
  i1ii1IiiIIiI = Oo0o0o0
  return ( ( Ii111i1I , i1ii1IiiIIiI ) )
  if 42 - 42: iII111i
  if 51 - 51: I1IiiI - OoOoOO00 * I1Ii111 * iIii1I11I1II1
 def get_distance ( self , geo_point ) :
  iiIIoOo0OooooOoo0 = self . dms_to_decimal ( )
  iiiiIi1 = geo_point . dms_to_decimal ( )
  o000O00 = vincenty ( iiIIoOo0OooooOoo0 , iiiiIi1 )
  return ( o000O00 . km )
  if 94 - 94: OoooooooOO - IiII * Oo0Ooo / I1IiiI / iII111i / I1IiiI
  if 91 - 91: o0oOOo0O0Ooo - I1IiiI . I1IiiI + OOooOOo % oO0o
 def point_in_circle ( self , geo_point ) :
  ooo0II1IIIII1III1 = self . get_distance ( geo_point )
  return ( ooo0II1IIIII1III1 <= self . radius )
  if 67 - 67: I1ii11iIi11i - ooOoO0o - Ii1I - OoO0O00 % OoooooooOO
  if 22 - 22: oO0o * i1IIi
 def encode_geo ( self ) :
  I1i = socket . htons ( LISP_AFI_LCAF )
  iiii111I = socket . htons ( 20 + 2 )
  O0OooO00O0 = 0
  if 54 - 54: I1IiiI * I1IiiI % IiII - i11iIiiIii * o0oOOo0O0Ooo
  iiII = abs ( self . latitude )
  II111 = ( ( self . lat_mins * 60 ) + self . lat_secs ) * 1000
  if ( self . latitude < 0 ) : O0OooO00O0 |= 0x40
  if 16 - 16: IiII . I11i * O0 + OoooooooOO
  OOo0o0ooO0o0o = abs ( self . longitude )
  III = ( ( self . long_mins * 60 ) + self . long_secs ) * 1000
  if ( self . longitude < 0 ) : O0OooO00O0 |= 0x20
  if 5 - 5: OoOoOO00 . I1Ii111 * i11iIiiIii / Ii1I % iII111i
  Oo0OOo00OoOo000 = 0
  if ( self . no_geo_altitude ( ) == False ) :
   Oo0OOo00OoOo000 = socket . htonl ( self . altitude )
   O0OooO00O0 |= 0x10
   if 87 - 87: ooOoO0o . iIii1I11I1II1
  O0o0oo0 = socket . htons ( self . radius )
  if ( O0o0oo0 != 0 ) : O0OooO00O0 |= 0x06
  if 99 - 99: Ii1I + OoooooooOO * IiII * i11iIiiIii - iIii1I11I1II1
  o0oooooO0o = struct . pack ( "HBBBBH" , I1i , 0 , 0 , LISP_LCAF_GEO_COORD_TYPE ,
 0 , iiii111I )
  o0oooooO0o += struct . pack ( "BBHBBHBBHIHHH" , O0OooO00O0 , 0 , 0 , iiII , II111 >> 16 ,
 socket . htons ( II111 & 0x0ffff ) , OOo0o0ooO0o0o , III >> 16 ,
 socket . htons ( III & 0xffff ) , Oo0OOo00OoOo000 , O0o0oo0 , 0 , 0 )
  if 68 - 68: oO0o + o0oOOo0O0Ooo * iIii1I11I1II1 / i1IIi
  return ( o0oooooO0o )
  if 9 - 9: I11i % OoO0O00 . oO0o / I1ii11iIi11i
  if 88 - 88: Oo0Ooo / IiII / II111iiii / I1ii11iIi11i + OoooooooOO
 def decode_geo ( self , packet , lcaf_len , radius_hi ) :
  O0O00Oo = "BBHBBHBBHIHHH"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( lcaf_len < IiIii1i ) : return ( None )
  if 65 - 65: iII111i % oO0o * IiII
  O0OooO00O0 , i111I111i1i , III111Ii , iiII , Ii1IiIiiI11i , II111 , OOo0o0ooO0o0o , iIIII , III , Oo0OOo00OoOo000 , O0o0oo0 , iiI11i , IiiiII = struct . unpack ( O0O00Oo ,
  # i1IIi
 packet [ : IiIii1i ] )
  if 93 - 93: OoOoOO00 - Oo0Ooo + iIii1I11I1II1 % iIii1I11I1II1 / I1ii11iIi11i - I1Ii111
  if 9 - 9: I1ii11iIi11i - o0oOOo0O0Ooo / i11iIiiIii * iII111i / OoOoOO00 . I1IiiI
  if 23 - 23: I1IiiI . iII111i % i1IIi
  if 92 - 92: o0oOOo0O0Ooo % i1IIi / OoooooooOO * OoooooooOO / iIii1I11I1II1
  IiiiII = socket . ntohs ( IiiiII )
  if ( IiiiII == LISP_AFI_LCAF ) : return ( None )
  if 7 - 7: IiII / OOooOOo + Oo0Ooo . I1IiiI
  if ( O0OooO00O0 & 0x40 ) : iiII = - iiII
  self . latitude = iiII
  i1i1ii = ( ( Ii1IiIiiI11i << 16 ) | socket . ntohs ( II111 ) ) / 1000
  self . lat_mins = i1i1ii / 60
  self . lat_secs = i1i1ii % 60
  if 10 - 10: o0oOOo0O0Ooo / I1IiiI . OOooOOo
  if ( O0OooO00O0 & 0x20 ) : OOo0o0ooO0o0o = - OOo0o0ooO0o0o
  self . longitude = OOo0o0ooO0o0o
  i1II1iII = ( ( iIIII << 16 ) | socket . ntohs ( III ) ) / 1000
  self . long_mins = i1II1iII / 60
  self . long_secs = i1II1iII % 60
  if 26 - 26: o0oOOo0O0Ooo * I1Ii111
  self . altitude = socket . ntohl ( Oo0OOo00OoOo000 ) if ( O0OooO00O0 & 0x10 ) else - 1
  O0o0oo0 = socket . ntohs ( O0o0oo0 )
  self . radius = O0o0oo0 if ( O0OooO00O0 & 0x02 ) else O0o0oo0 * 1000
  if 65 - 65: I11i * iIii1I11I1II1 % OoO0O00 % I11i * O0 * i1IIi
  self . geo_name = None
  packet = packet [ IiIii1i : : ]
  if 27 - 27: OoOoOO00 % OoooooooOO
  if ( IiiiII != 0 ) :
   self . rloc . afi = IiiiII
   packet = self . rloc . unpack_address ( packet )
   self . rloc . mask_len = self . rloc . host_mask_len ( )
   if 77 - 77: Ii1I % Oo0Ooo
  return ( packet )
  if 30 - 30: iIii1I11I1II1 * Oo0Ooo * OOooOOo * ooOoO0o
  if 6 - 6: iIii1I11I1II1 / oO0o % ooOoO0o
  if 19 - 19: iIii1I11I1II1 + I11i - iIii1I11I1II1 - Ii1I . Ii1I * OoO0O00
  if 32 - 32: I1IiiI + OOooOOo * oO0o
  if 100 - 100: OoO0O00
  if 20 - 20: Ii1I % OoO0O00
class lisp_rle_node ( ) :
 def __init__ ( self ) :
  self . address = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . level = 0
  self . translated_port = 0
  self . rloc_name = None
  if 85 - 85: i1IIi % iIii1I11I1II1
  if 10 - 10: O0 . oO0o * I1IiiI
 def copy_rle_node ( self ) :
  IiioOoo = lisp_rle_node ( )
  IiioOoo . address . copy_address ( self . address )
  IiioOoo . level = self . level
  IiioOoo . translated_port = self . translated_port
  IiioOoo . rloc_name = self . rloc_name
  return ( IiioOoo )
  if 21 - 21: OoooooooOO
  if 76 - 76: i1IIi * i11iIiiIii / OOooOOo + I1Ii111
 def store_translated_rloc ( self , rloc , port ) :
  self . address . copy_address ( rloc )
  self . translated_port = port
  if 50 - 50: oO0o % OoOoOO00 + I1IiiI
  if 15 - 15: II111iiii - iII111i / I1ii11iIi11i
 def get_encap_keys ( self ) :
  Oo0o = "4341" if self . translated_port == 0 else str ( self . translated_port )
  if 81 - 81: Ii1I - i1IIi % oO0o * Oo0Ooo * OoOoOO00
  oo0o00OO = self . address . print_address_no_iid ( ) + ":" + Oo0o
  if 79 - 79: oO0o + I1IiiI % iII111i + II111iiii % OoO0O00 % iII111i
  try :
   iIi11III = lisp_crypto_keys_by_rloc_encap [ oo0o00OO ]
   if ( iIi11III [ 1 ] ) : return ( iIi11III [ 1 ] . encrypt_key , iIi11III [ 1 ] . icv_key )
   return ( None , None )
  except :
   return ( None , None )
   if 46 - 46: o0oOOo0O0Ooo
   if 61 - 61: OoO0O00 . O0 + I1ii11iIi11i + OoO0O00
   if 44 - 44: I11i . oO0o
   if 65 - 65: I1ii11iIi11i * II111iiii % I11i + II111iiii . i1IIi / ooOoO0o
class lisp_rle ( ) :
 def __init__ ( self , name ) :
  self . rle_name = name
  self . rle_nodes = [ ]
  self . rle_forwarding_list = [ ]
  if 74 - 74: OoOoOO00 % OoO0O00 . OoOoOO00
  if 16 - 16: OoO0O00 / Ii1I * i11iIiiIii / o0oOOo0O0Ooo + I1Ii111
 def copy_rle ( self ) :
  iI1Ii11 = lisp_rle ( self . rle_name )
  for IiioOoo in self . rle_nodes :
   iI1Ii11 . rle_nodes . append ( IiioOoo . copy_rle_node ( ) )
   if 21 - 21: I11i % I1ii11iIi11i
  iI1Ii11 . build_forwarding_list ( )
  return ( iI1Ii11 )
  if 8 - 8: OOooOOo % OoO0O00 + O0 - o0oOOo0O0Ooo
  if 46 - 46: Oo0Ooo . ooOoO0o + OoOoOO00 - I11i / i11iIiiIii . iII111i
 def print_rle ( self , html , do_formatting ) :
  oOOOO0o000OoO = ""
  for IiioOoo in self . rle_nodes :
   Oo0o = IiioOoo . translated_port
   if 80 - 80: II111iiii + OoO0O00 % ooOoO0o + i11iIiiIii
   I11II = ""
   if ( IiioOoo . rloc_name != None ) :
    I11II = IiioOoo . rloc_name
    if ( do_formatting ) : I11II = blue ( I11II , html )
    I11II = "({})" . format ( I11II )
    if 86 - 86: iII111i * IiII . IiII
    if 91 - 91: i11iIiiIii - IiII + Oo0Ooo . Oo0Ooo * oO0o
   oo0o00OO = IiioOoo . address . print_address_no_iid ( )
   if ( IiioOoo . address . is_local ( ) ) : oo0o00OO = red ( oo0o00OO , html )
   oOOOO0o000OoO += "{}{}{}, " . format ( oo0o00OO , "" if Oo0o == 0 else ":" + str ( Oo0o ) , I11II )
   if 89 - 89: iII111i + Oo0Ooo / Oo0Ooo / OoO0O00 + i11iIiiIii
   if 81 - 81: i11iIiiIii . iIii1I11I1II1 - OoooooooOO
  return ( oOOOO0o000OoO [ 0 : - 2 ] if oOOOO0o000OoO != "" else "" )
  if 52 - 52: O0 - I1Ii111 + oO0o % ooOoO0o . oO0o
  if 60 - 60: oO0o + o0oOOo0O0Ooo - OOooOOo % o0oOOo0O0Ooo . I11i + OoO0O00
 def build_forwarding_list ( self ) :
  oOOoOoooOo0o = - 1
  for IiioOoo in self . rle_nodes :
   if ( oOOoOoooOo0o == - 1 ) :
    if ( IiioOoo . address . is_local ( ) ) : oOOoOoooOo0o = IiioOoo . level
   else :
    if ( IiioOoo . level > oOOoOoooOo0o ) : break
    if 27 - 27: i11iIiiIii - I1ii11iIi11i * I1Ii111 . I1IiiI / OoO0O00 * ooOoO0o
    if 42 - 42: OOooOOo
  oOOoOoooOo0o = 0 if oOOoOoooOo0o == - 1 else IiioOoo . level
  if 36 - 36: OoooooooOO + ooOoO0o + iII111i
  self . rle_forwarding_list = [ ]
  for IiioOoo in self . rle_nodes :
   if ( IiioOoo . level == oOOoOoooOo0o or ( oOOoOoooOo0o == 0 and
 IiioOoo . level == 128 ) ) :
    if ( lisp_i_am_rtr == False and IiioOoo . address . is_local ( ) ) :
     oo0o00OO = IiioOoo . address . print_address_no_iid ( )
     lprint ( "Exclude local RLE RLOC {}" . format ( oo0o00OO ) )
     continue
     if 30 - 30: i1IIi % Ii1I
    self . rle_forwarding_list . append ( IiioOoo )
    if 18 - 18: o0oOOo0O0Ooo % I1ii11iIi11i . Ii1I . O0 * II111iiii + I1ii11iIi11i
    if 45 - 45: OoO0O00 / I1ii11iIi11i * ooOoO0o * OOooOOo % i11iIiiIii * iII111i
    if 33 - 33: oO0o . iII111i + Oo0Ooo
    if 33 - 33: ooOoO0o
    if 46 - 46: OoOoOO00 / iII111i - OoO0O00 . o0oOOo0O0Ooo
class lisp_json ( ) :
 def __init__ ( self , name , string , encrypted = False , ms_encrypt = False ) :
  self . json_name = name
  self . json_encrypted = False
  try :
   json . loads ( string )
  except :
   lprint ( "Invalid JSON string: '{}'" . format ( string ) )
   string = '{ "?" : "?" }'
   if 50 - 50: I1Ii111 . O0 . OoOoOO00 + I1Ii111 + OoooooooOO . i11iIiiIii
  self . json_string = string
  if 65 - 65: I1IiiI % iIii1I11I1II1
  if 52 - 52: I1IiiI
  if 19 - 19: I1IiiI
  if 17 - 17: I11i + OoooooooOO
  if 63 - 63: IiII
  if 3 - 3: oO0o * II111iiii . O0
  if 19 - 19: I1IiiI / I1IiiI / Oo0Ooo + oO0o + i1IIi
  if 31 - 31: iII111i / OoooooooOO - I1Ii111 . iII111i
  if 38 - 38: ooOoO0o . OoooooooOO - II111iiii * i11iIiiIii / i1IIi . OoooooooOO
  if 51 - 51: oO0o - I1ii11iIi11i + I1ii11iIi11i
  if ( len ( lisp_ms_json_keys ) != 0 ) :
   if ( ms_encrypt == False ) : return
   self . json_key_id = lisp_ms_json_keys . keys ( ) [ 0 ]
   self . json_key = lisp_ms_json_keys [ self . json_key_id ]
   self . encrypt_json ( )
   if 100 - 100: I11i - I1ii11iIi11i . i1IIi
   if 85 - 85: II111iiii
  if ( lisp_log_id == "lig" and encrypted ) :
   o0Oo = os . getenv ( "LISP_JSON_KEY" )
   if ( o0Oo != None ) :
    ooo = - 1
    if ( o0Oo [ 0 ] == "[" and "]" in o0Oo ) :
     ooo = o0Oo . find ( "]" )
     self . json_key_id = int ( o0Oo [ 1 : ooo ] )
     if 58 - 58: i1IIi - OoO0O00 + ooOoO0o
    self . json_key = o0Oo [ ooo + 1 : : ]
    if 6 - 6: IiII % I1IiiI + OoooooooOO * oO0o . iII111i + oO0o
    self . decrypt_json ( )
    if 4 - 4: I11i % I1IiiI
    if 72 - 72: I1IiiI % II111iiii % iII111i / OoOoOO00
    if 96 - 96: OoOoOO00 % Ii1I
    if 50 - 50: IiII - II111iiii
 def add ( self ) :
  self . delete ( )
  lisp_json_list [ self . json_name ] = self
  if 10 - 10: OoooooooOO % Ii1I * OOooOOo + IiII * oO0o
  if 13 - 13: II111iiii
 def delete ( self ) :
  if ( lisp_json_list . has_key ( self . json_name ) ) :
   del ( lisp_json_list [ self . json_name ] )
   lisp_json_list [ self . json_name ] = None
   if 14 - 14: i11iIiiIii . IiII
   if 70 - 70: Oo0Ooo * OOooOOo + I1Ii111 % OoOoOO00 / O0
   if 23 - 23: O0 * oO0o / I1IiiI + i1IIi * O0 % oO0o
 def print_json ( self , html ) :
  I1ooOO = self . json_string
  IiiiIi = "***"
  if ( html ) : IiiiIi = red ( IiiiIi , html )
  I11Iii11iiI = IiiiIi + self . json_string + IiiiIi
  if ( self . valid_json ( ) ) : return ( I1ooOO )
  return ( I11Iii11iiI )
  if 99 - 99: OoO0O00
  if 49 - 49: iII111i + OoOoOO00
 def valid_json ( self ) :
  try :
   json . loads ( self . json_string )
  except :
   return ( False )
   if 33 - 33: ooOoO0o
  return ( True )
  if 19 - 19: I1Ii111 % IiII
  if 94 - 94: I1Ii111 * I1ii11iIi11i * I1ii11iIi11i - o0oOOo0O0Ooo . i11iIiiIii
 def encrypt_json ( self ) :
  II11iI11i1 = self . json_key . zfill ( 32 )
  OO000OOOo0Oo = "0" * 8
  if 16 - 16: i1IIi
  o0oOO0OOoO = json . loads ( self . json_string )
  for o0Oo in o0oOO0OOoO :
   Oo00OO0OO = o0oOO0OOoO [ o0Oo ]
   if ( type ( Oo00OO0OO ) != str ) : Oo00OO0OO = str ( Oo00OO0OO )
   Oo00OO0OO = chacha . ChaCha ( II11iI11i1 , OO000OOOo0Oo ) . encrypt ( Oo00OO0OO )
   o0oOO0OOoO [ o0Oo ] = binascii . hexlify ( Oo00OO0OO )
   if 51 - 51: iIii1I11I1II1 / I1ii11iIi11i
  self . json_string = json . dumps ( o0oOO0OOoO )
  self . json_encrypted = True
  if 83 - 83: ooOoO0o % I1IiiI - OoOoOO00 - I11i
  if 12 - 12: I1Ii111 . OoO0O00 + I11i * OoO0O00 - IiII + I11i
 def decrypt_json ( self ) :
  II11iI11i1 = self . json_key . zfill ( 32 )
  OO000OOOo0Oo = "0" * 8
  if 98 - 98: iII111i . I1Ii111 * IiII - Ii1I * OoooooooOO
  o0oOO0OOoO = json . loads ( self . json_string )
  for o0Oo in o0oOO0OOoO :
   Oo00OO0OO = binascii . unhexlify ( o0oOO0OOoO [ o0Oo ] )
   o0oOO0OOoO [ o0Oo ] = chacha . ChaCha ( II11iI11i1 , OO000OOOo0Oo ) . encrypt ( Oo00OO0OO )
   if 13 - 13: iII111i
  try :
   self . json_string = json . dumps ( o0oOO0OOoO )
   self . json_encrypted = False
  except :
   pass
   if 76 - 76: iIii1I11I1II1 + Oo0Ooo
   if 40 - 40: oO0o % i1IIi % ooOoO0o . oO0o % oO0o
   if 69 - 69: OoooooooOO . oO0o / OoooooooOO / OoOoOO00
   if 41 - 41: ooOoO0o + o0oOOo0O0Ooo . o0oOOo0O0Ooo / oO0o * IiII
   if 96 - 96: IiII % O0 + Ii1I / o0oOOo0O0Ooo + I1ii11iIi11i * II111iiii
   if 65 - 65: Ii1I * Oo0Ooo * Oo0Ooo . Ii1I
   if 4 - 4: i11iIiiIii - iIii1I11I1II1 % o0oOOo0O0Ooo * oO0o
class lisp_stats ( ) :
 def __init__ ( self ) :
  self . packet_count = 0
  self . byte_count = 0
  self . last_rate_check = 0
  self . last_packet_count = 0
  self . last_byte_count = 0
  self . last_increment = None
  if 19 - 19: Ii1I
  if 47 - 47: IiII - IiII
 def increment ( self , octets ) :
  self . packet_count += 1
  self . byte_count += octets
  self . last_increment = lisp_get_timestamp ( )
  if 33 - 33: ooOoO0o
  if 23 - 23: I1Ii111 + OoO0O00
 def recent_packet_sec ( self ) :
  if ( self . last_increment == None ) : return ( False )
  Ooo0o0oo0 = time . time ( ) - self . last_increment
  return ( Ooo0o0oo0 <= 1 )
  if 35 - 35: Oo0Ooo - iIii1I11I1II1 - I1Ii111 % OOooOOo
  if 59 - 59: i1IIi
 def recent_packet_min ( self ) :
  if ( self . last_increment == None ) : return ( False )
  Ooo0o0oo0 = time . time ( ) - self . last_increment
  return ( Ooo0o0oo0 <= 60 )
  if 38 - 38: Oo0Ooo . o0oOOo0O0Ooo % oO0o / i11iIiiIii * OoO0O00 % OoOoOO00
  if 18 - 18: OOooOOo
 def stat_colors ( self , c1 , c2 , html ) :
  if ( self . recent_packet_sec ( ) ) :
   return ( green_last_sec ( c1 ) , green_last_sec ( c2 ) )
   if 12 - 12: I1Ii111 % II111iiii / o0oOOo0O0Ooo - iIii1I11I1II1 + II111iiii
  if ( self . recent_packet_min ( ) ) :
   return ( green_last_min ( c1 ) , green_last_min ( c2 ) )
   if 41 - 41: OOooOOo
  return ( c1 , c2 )
  if 8 - 8: i11iIiiIii . IiII . I1ii11iIi11i + i1IIi % I1Ii111
  if 64 - 64: I1IiiI . Oo0Ooo * OoO0O00
 def normalize ( self , count ) :
  count = str ( count )
  ooo0o = len ( count )
  if ( ooo0o > 12 ) :
   count = count [ 0 : - 10 ] + "." + count [ - 10 : - 7 ] + "T"
   return ( count )
   if 29 - 29: O0 . ooOoO0o - ooOoO0o * i1IIi * I1IiiI - Oo0Ooo
  if ( ooo0o > 9 ) :
   count = count [ 0 : - 9 ] + "." + count [ - 9 : - 7 ] + "B"
   return ( count )
   if 28 - 28: OoooooooOO . i1IIi . I1Ii111
  if ( ooo0o > 6 ) :
   count = count [ 0 : - 6 ] + "." + count [ - 6 ] + "M"
   return ( count )
   if 53 - 53: OoO0O00 * Oo0Ooo + Oo0Ooo
  return ( count )
  if 62 - 62: OOooOOo - i1IIi + i11iIiiIii * I11i / OoO0O00
  if 84 - 84: IiII * OOooOOo
 def get_stats ( self , summary , html ) :
  I1iiiI1iIi1iI = self . last_rate_check
  iii1Ii1I = self . last_packet_count
  oooI1111I1ii1I1 = self . last_byte_count
  self . last_rate_check = lisp_get_timestamp ( )
  self . last_packet_count = self . packet_count
  self . last_byte_count = self . byte_count
  if 61 - 61: iIii1I11I1II1 / I1Ii111 * OoO0O00 . oO0o
  i1iI1i = self . last_rate_check - I1iiiI1iIi1iI
  if ( i1iI1i == 0 ) :
   IIii1IIi1 = 0
   OoO0o0oOoOo = 0
  else :
   IIii1IIi1 = int ( ( self . packet_count - iii1Ii1I ) / i1iI1i )
   OoO0o0oOoOo = ( self . byte_count - oooI1111I1ii1I1 ) / i1iI1i
   OoO0o0oOoOo = ( OoO0o0oOoOo * 8 ) / 1000000
   OoO0o0oOoOo = round ( OoO0o0oOoOo , 2 )
   if 30 - 30: II111iiii / OOooOOo
   if 42 - 42: IiII + OoO0O00 . i1IIi
   if 88 - 88: OoooooooOO
   if 47 - 47: OOooOOo + Oo0Ooo * I11i
   if 8 - 8: Ii1I % i1IIi
  iIiII1i11iI = self . normalize ( self . packet_count )
  o0O00o0OOoo0 = self . normalize ( self . byte_count )
  if 62 - 62: oO0o + II111iiii - iII111i * I1IiiI . OoO0O00 * I1ii11iIi11i
  if 18 - 18: O0 + I1Ii111 . I1ii11iIi11i
  if 48 - 48: Ii1I . o0oOOo0O0Ooo * O0 / OoooooooOO + I1Ii111 + Oo0Ooo
  if 92 - 92: Ii1I - o0oOOo0O0Ooo % I1IiiI + I1Ii111
  if 3 - 3: iIii1I11I1II1 + i11iIiiIii
  if ( summary ) :
   iIIi1Iii1Ii = "<br>" if html else ""
   iIiII1i11iI , o0O00o0OOoo0 = self . stat_colors ( iIiII1i11iI , o0O00o0OOoo0 , html )
   I11i1I = "packet-count: {}{}byte-count: {}" . format ( iIiII1i11iI , iIIi1Iii1Ii , o0O00o0OOoo0 )
   Iiiiii1 = "packet-rate: {} pps\nbit-rate: {} Mbps" . format ( IIii1IIi1 , OoO0o0oOoOo )
   if 34 - 34: i1IIi . i1IIi / oO0o
   if ( html != "" ) : Iiiiii1 = lisp_span ( I11i1I , Iiiiii1 )
  else :
   IIOO00 = str ( IIii1IIi1 )
   I1I111I1iIiii = str ( OoO0o0oOoOo )
   if ( html ) :
    iIiII1i11iI = lisp_print_cour ( iIiII1i11iI )
    IIOO00 = lisp_print_cour ( IIOO00 )
    o0O00o0OOoo0 = lisp_print_cour ( o0O00o0OOoo0 )
    I1I111I1iIiii = lisp_print_cour ( I1I111I1iIiii )
    if 27 - 27: o0oOOo0O0Ooo * o0oOOo0O0Ooo + OoooooooOO - I1Ii111
   iIIi1Iii1Ii = "<br>" if html else ", "
   if 83 - 83: iIii1I11I1II1
   Iiiiii1 = ( "packet-count: {}{}packet-rate: {} pps{}byte-count: " + "{}{}bit-rate: {} mbps" ) . format ( iIiII1i11iI , iIIi1Iii1Ii , IIOO00 , iIIi1Iii1Ii , o0O00o0OOoo0 , iIIi1Iii1Ii ,
   # OoO0O00 % i11iIiiIii - iII111i
 I1I111I1iIiii )
   if 61 - 61: IiII / oO0o . I1Ii111 - IiII * IiII - iII111i
  return ( Iiiiii1 )
  if 49 - 49: Ii1I
  if 91 - 91: Ii1I / ooOoO0o % iII111i
  if 75 - 75: i1IIi
  if 23 - 23: oO0o + II111iiii % OoOoOO00 / O0 / iIii1I11I1II1 / I1Ii111
  if 47 - 47: I1IiiI / I11i + iIii1I11I1II1 * Oo0Ooo / I1ii11iIi11i
  if 8 - 8: ooOoO0o . O0 / OoO0O00
  if 50 - 50: Ii1I . OoOoOO00 * o0oOOo0O0Ooo
  if 68 - 68: IiII * oO0o / OoOoOO00 / I1Ii111
lisp_decap_stats = {
 "good-packets" : lisp_stats ( ) , "ICV-error" : lisp_stats ( ) ,
 "checksum-error" : lisp_stats ( ) , "lisp-header-error" : lisp_stats ( ) ,
 "no-decrypt-key" : lisp_stats ( ) , "bad-inner-version" : lisp_stats ( ) ,
 "outer-header-error" : lisp_stats ( )
 }
if 72 - 72: I1ii11iIi11i
if 74 - 74: I1Ii111 * iIii1I11I1II1 / oO0o - IiII - I1IiiI
if 84 - 84: iIii1I11I1II1 % Oo0Ooo / I1ii11iIi11i + o0oOOo0O0Ooo * II111iiii
if 81 - 81: I1IiiI / I1ii11iIi11i / OOooOOo
class lisp_rloc ( ) :
 def __init__ ( self , recurse = True ) :
  self . rloc = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . rloc_name = None
  self . interface = None
  self . translated_rloc = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . translated_port = 0
  self . priority = 255
  self . weight = 0
  self . mpriority = 255
  self . mweight = 0
  self . uptime = lisp_get_timestamp ( )
  self . state = LISP_RLOC_UP_STATE
  self . last_state_change = None
  self . rle_name = None
  self . elp_name = None
  self . geo_name = None
  self . json_name = None
  self . geo = None
  self . elp = None
  self . rle = None
  self . json = None
  self . stats = lisp_stats ( )
  self . last_rloc_probe = None
  self . last_rloc_probe_reply = None
  self . rloc_probe_rtt = - 1
  self . recent_rloc_probe_rtts = [ - 1 , - 1 , - 1 ]
  self . rloc_probe_hops = "?/?"
  self . recent_rloc_probe_hops = [ "?/?" , "?/?" , "?/?" ]
  self . rloc_probe_latency = "?/?"
  self . recent_rloc_probe_latencies = [ "?/?" , "?/?" , "?/?" ]
  self . last_rloc_probe_nonce = 0
  self . echo_nonce_capable = False
  self . map_notify_requested = False
  self . rloc_next_hop = None
  self . next_rloc = None
  self . multicast_rloc_probe_list = { }
  if 89 - 89: Oo0Ooo % IiII
  if ( recurse == False ) : return
  if 36 - 36: IiII % OoOoOO00 % I1ii11iIi11i
  if 7 - 7: I1ii11iIi11i % OoOoOO00 - O0 . I1Ii111
  if 9 - 9: Ii1I . OoooooooOO / ooOoO0o + i1IIi
  if 90 - 90: oO0o - OoOoOO00 % ooOoO0o
  if 83 - 83: OOooOOo - I1ii11iIi11i + OoO0O00
  if 99 - 99: iII111i - OoOoOO00 % ooOoO0o
  II1Oo0o00ooOooo = lisp_get_default_route_next_hops ( )
  if ( II1Oo0o00ooOooo == [ ] or len ( II1Oo0o00ooOooo ) == 1 ) : return
  if 39 - 39: oO0o / OoO0O00 - Ii1I + ooOoO0o + OOooOOo
  self . rloc_next_hop = II1Oo0o00ooOooo [ 0 ]
  IiI1i11iiII = self
  for o0OoiIiIIi in II1Oo0o00ooOooo [ 1 : : ] :
   iIIiI11 = lisp_rloc ( False )
   iIIiI11 = copy . deepcopy ( self )
   iIIiI11 . rloc_next_hop = o0OoiIiIIi
   IiI1i11iiII . next_rloc = iIIiI11
   IiI1i11iiII = iIIiI11
   if 59 - 59: OoOoOO00 % O0 * I1Ii111 - i1IIi
   if 68 - 68: OOooOOo % IiII / Oo0Ooo + OoOoOO00
   if 11 - 11: OoO0O00
 def up_state ( self ) :
  return ( self . state == LISP_RLOC_UP_STATE )
  if 70 - 70: o0oOOo0O0Ooo * O0 * II111iiii
  if 38 - 38: OoO0O00 - I1IiiI * OoooooooOO / I11i . O0
 def unreach_state ( self ) :
  return ( self . state == LISP_RLOC_UNREACH_STATE )
  if 77 - 77: OOooOOo + oO0o * iIii1I11I1II1 / oO0o / OOooOOo . i11iIiiIii
  if 92 - 92: Oo0Ooo . o0oOOo0O0Ooo % OoooooooOO * i11iIiiIii * OoO0O00 * o0oOOo0O0Ooo
 def no_echoed_nonce_state ( self ) :
  return ( self . state == LISP_RLOC_NO_ECHOED_NONCE_STATE )
  if 48 - 48: iII111i * I1ii11iIi11i * oO0o % O0 . OoO0O00
  if 11 - 11: OOooOOo / o0oOOo0O0Ooo
 def down_state ( self ) :
  return ( self . state in [ LISP_RLOC_DOWN_STATE , LISP_RLOC_ADMIN_DOWN_STATE ] )
  if 98 - 98: oO0o + I11i . oO0o
  if 10 - 10: iII111i + i1IIi . I11i % ooOoO0o / ooOoO0o
  if 86 - 86: Oo0Ooo
 def print_state ( self ) :
  if ( self . state is LISP_RLOC_UNKNOWN_STATE ) :
   return ( "unknown-state" )
  if ( self . state is LISP_RLOC_UP_STATE ) :
   return ( "up-state" )
  if ( self . state is LISP_RLOC_DOWN_STATE ) :
   return ( "down-state" )
  if ( self . state is LISP_RLOC_ADMIN_DOWN_STATE ) :
   return ( "admin-down-state" )
  if ( self . state is LISP_RLOC_UNREACH_STATE ) :
   return ( "unreach-state" )
  if ( self . state is LISP_RLOC_NO_ECHOED_NONCE_STATE ) :
   return ( "no-echoed-nonce-state" )
  return ( "invalid-state" )
  if 7 - 7: iIii1I11I1II1
  if 86 - 86: IiII + iII111i * II111iiii - IiII - o0oOOo0O0Ooo
 def print_rloc ( self , indent ) :
  i1 = lisp_print_elapsed ( self . uptime )
  lprint ( "{}rloc {}, uptime {}, {}, parms {}/{}/{}/{}" . format ( indent ,
 red ( self . rloc . print_address ( ) , False ) , i1 , self . print_state ( ) ,
 self . priority , self . weight , self . mpriority , self . mweight ) )
  if 8 - 8: OOooOOo . Ii1I
  if 15 - 15: ooOoO0o / OOooOOo + i1IIi / Ii1I / OOooOOo
 def print_rloc_name ( self , cour = False ) :
  if ( self . rloc_name == None ) : return ( "" )
  IIiiI11iI = self . rloc_name
  if ( cour ) : IIiiI11iI = lisp_print_cour ( IIiiI11iI )
  return ( 'rloc-name: {}' . format ( blue ( IIiiI11iI , cour ) ) )
  if 47 - 47: Oo0Ooo + oO0o % OoooooooOO
  if 23 - 23: I1Ii111 / i11iIiiIii - ooOoO0o * iII111i - Ii1I . iIii1I11I1II1
 def store_rloc_from_record ( self , rloc_record , nonce , source ) :
  Oo0o = LISP_DATA_PORT
  self . rloc . copy_address ( rloc_record . rloc )
  self . rloc_name = rloc_record . rloc_name
  if 11 - 11: I11i % OoOoOO00 * Oo0Ooo
  if 48 - 48: OOooOOo
  if 66 - 66: iII111i - I1Ii111 - i11iIiiIii . o0oOOo0O0Ooo + Oo0Ooo
  if 90 - 90: O0 - i11iIiiIii * ooOoO0o . I1ii11iIi11i . Ii1I - OoooooooOO
  I1II = self . rloc
  if ( I1II . is_null ( ) == False ) :
   i1II1iiI = lisp_get_nat_info ( I1II , self . rloc_name )
   if ( i1II1iiI ) :
    Oo0o = i1II1iiI . port
    O0Ooo0O00O = lisp_nat_state_info [ self . rloc_name ] [ 0 ]
    oo0o00OO = I1II . print_address_no_iid ( )
    O0ooo0Ooo = red ( oo0o00OO , False )
    i1i1i1I11 = "" if self . rloc_name == None else blue ( self . rloc_name , False )
    if 86 - 86: iIii1I11I1II1 / I1ii11iIi11i . I11i % II111iiii
    if 55 - 55: OoooooooOO
    if 94 - 94: I1IiiI % I1ii11iIi11i
    if 30 - 30: iIii1I11I1II1 . OoOoOO00
    if 28 - 28: I1IiiI . O0 - oO0o
    if 56 - 56: ooOoO0o
    if ( i1II1iiI . timed_out ( ) ) :
     lprint ( ( "    Matched stored NAT state timed out for " + "RLOC {}:{}, {}" ) . format ( O0ooo0Ooo , Oo0o , i1i1i1I11 ) )
     if 94 - 94: OoOoOO00
     if 12 - 12: I11i * OoooooooOO + ooOoO0o
     i1II1iiI = None if ( i1II1iiI == O0Ooo0O00O ) else O0Ooo0O00O
     if ( i1II1iiI and i1II1iiI . timed_out ( ) ) :
      Oo0o = i1II1iiI . port
      O0ooo0Ooo = red ( i1II1iiI . address , False )
      lprint ( ( "    Youngest stored NAT state timed out " + " for RLOC {}:{}, {}" ) . format ( O0ooo0Ooo , Oo0o ,
      # O0
 i1i1i1I11 ) )
      i1II1iiI = None
      if 90 - 90: I11i + I1ii11iIi11i + OoooooooOO + OoOoOO00 + IiII / iII111i
      if 75 - 75: i11iIiiIii
      if 27 - 27: I11i - IiII - I1Ii111
      if 90 - 90: OoO0O00 . oO0o * O0 / I11i % O0 + I1Ii111
      if 48 - 48: iIii1I11I1II1 . i11iIiiIii / OoooooooOO . i1IIi . o0oOOo0O0Ooo
      if 84 - 84: Ii1I
      if 92 - 92: I11i
    if ( i1II1iiI ) :
     if ( i1II1iiI . address != oo0o00OO ) :
      lprint ( "RLOC conflict, RLOC-record {}, NAT state {}" . format ( O0ooo0Ooo , red ( i1II1iiI . address , False ) ) )
      if 64 - 64: iII111i / iII111i * iII111i % O0 / IiII . I1ii11iIi11i
      self . rloc . store_address ( i1II1iiI . address )
      if 23 - 23: i1IIi / I1ii11iIi11i + o0oOOo0O0Ooo
     O0ooo0Ooo = red ( i1II1iiI . address , False )
     Oo0o = i1II1iiI . port
     lprint ( "    Use NAT translated RLOC {}:{} for {}" . format ( O0ooo0Ooo , Oo0o , i1i1i1I11 ) )
     if 82 - 82: O0 * ooOoO0o * iIii1I11I1II1 . i1IIi
     self . store_translated_rloc ( I1II , Oo0o )
     if 47 - 47: I11i * I11i . OoOoOO00
     if 68 - 68: OoooooooOO + OoOoOO00 + i11iIiiIii
     if 89 - 89: Oo0Ooo + Ii1I * O0 - I1Ii111
     if 33 - 33: iIii1I11I1II1 . I11i
  self . geo = rloc_record . geo
  self . elp = rloc_record . elp
  self . json = rloc_record . json
  if 63 - 63: oO0o - iII111i
  if 13 - 13: I1Ii111 / i1IIi % OoooooooOO / I11i
  if 66 - 66: I1Ii111 % o0oOOo0O0Ooo . iII111i . ooOoO0o + OOooOOo * II111iiii
  if 33 - 33: oO0o
  self . rle = rloc_record . rle
  if ( self . rle ) :
   for IiioOoo in self . rle . rle_nodes :
    IIiiI11iI = IiioOoo . rloc_name
    i1II1iiI = lisp_get_nat_info ( IiioOoo . address , IIiiI11iI )
    if ( i1II1iiI == None ) : continue
    if 64 - 64: OoO0O00 % Oo0Ooo % I11i . iII111i % I1IiiI
    Oo0o = i1II1iiI . port
    Ooooo = IIiiI11iI
    if ( Ooooo ) : Ooooo = blue ( IIiiI11iI , False )
    if 50 - 50: i1IIi + ooOoO0o - iIii1I11I1II1
    lprint ( ( "      Store translated encap-port {} for RLE-" + "node {}, rloc-name '{}'" ) . format ( Oo0o ,
    # i1IIi + II111iiii / o0oOOo0O0Ooo
 IiioOoo . address . print_address_no_iid ( ) , Ooooo ) )
    IiioOoo . translated_port = Oo0o
    if 81 - 81: I1Ii111 . Ii1I * ooOoO0o . IiII - OoOoOO00
    if 79 - 79: ooOoO0o - O0
    if 56 - 56: ooOoO0o
  self . priority = rloc_record . priority
  self . mpriority = rloc_record . mpriority
  self . weight = rloc_record . weight
  self . mweight = rloc_record . mweight
  if ( rloc_record . reach_bit and rloc_record . local_bit and
 rloc_record . probe_bit == False ) : self . state = LISP_RLOC_UP_STATE
  if 89 - 89: O0 % iIii1I11I1II1 / OoOoOO00 - I1Ii111 - I1IiiI
  if 60 - 60: IiII % i11iIiiIii / OOooOOo
  if 43 - 43: i11iIiiIii * II111iiii + ooOoO0o - OoooooooOO * II111iiii / OoO0O00
  if 92 - 92: O0 - ooOoO0o % iII111i
  oO0OIi11iI11 = source . is_exact_match ( rloc_record . rloc ) if source != None else None
  if 37 - 37: i1IIi * I1Ii111 / I11i * II111iiii + OoooooooOO . OoO0O00
  if ( rloc_record . keys != None and oO0OIi11iI11 ) :
   o0Oo = rloc_record . keys [ 1 ]
   if ( o0Oo != None ) :
    oo0o00OO = rloc_record . rloc . print_address_no_iid ( ) + ":" + str ( Oo0o )
    if 22 - 22: OoOoOO00 + OoooooooOO - I1Ii111
    o0Oo . add_key_by_rloc ( oo0o00OO , True )
    lprint ( "    Store encap-keys for nonce 0x{}, RLOC {}" . format ( lisp_hex_string ( nonce ) , red ( oo0o00OO , False ) ) )
    if 82 - 82: Ii1I % I1Ii111 / ooOoO0o
    if 86 - 86: II111iiii - iIii1I11I1II1 + oO0o + I1IiiI
    if 29 - 29: Ii1I % OoooooooOO * II111iiii
  return ( Oo0o )
  if 88 - 88: I1Ii111 + I11i + I1Ii111 % OoO0O00 / I1ii11iIi11i - I11i
  if 15 - 15: Oo0Ooo - i1IIi
 def store_translated_rloc ( self , rloc , port ) :
  self . rloc . copy_address ( rloc )
  self . translated_rloc . copy_address ( rloc )
  self . translated_port = port
  if 87 - 87: O0 . o0oOOo0O0Ooo % OOooOOo / I11i - I1Ii111 % i11iIiiIii
  if 3 - 3: oO0o + iII111i + OOooOOo
 def is_rloc_translated ( self ) :
  return ( self . translated_rloc . is_null ( ) == False )
  if 54 - 54: i11iIiiIii + OoO0O00 - IiII - iII111i / I11i
  if 85 - 85: OOooOOo * OOooOOo * I1Ii111 - ooOoO0o . O0 % iII111i
 def rloc_exists ( self ) :
  if ( self . rloc . is_null ( ) == False ) : return ( True )
  if ( self . rle_name or self . geo_name or self . elp_name or self . json_name ) :
   return ( False )
   if 5 - 5: i1IIi * iII111i . o0oOOo0O0Ooo - I1ii11iIi11i
  return ( True )
  if 84 - 84: i1IIi
  if 17 - 17: IiII + iII111i * OoO0O00 / iII111i
 def is_rtr ( self ) :
  return ( ( self . priority == 254 and self . mpriority == 255 and self . weight == 0 and self . mweight == 0 ) )
  if 67 - 67: i1IIi * IiII . OoOoOO00 % iIii1I11I1II1 - iIii1I11I1II1 * I1ii11iIi11i
  if 96 - 96: iII111i / i11iIiiIii / oO0o + Oo0Ooo
  if 65 - 65: OoOoOO00
 def print_state_change ( self , new_state ) :
  O0Oo0ooO00 = self . print_state ( )
  O0ooo = "{} -> {}" . format ( O0Oo0ooO00 , new_state )
  if ( new_state == "up" and self . unreach_state ( ) ) :
   O0ooo = bold ( O0ooo , False )
   if 41 - 41: II111iiii + oO0o / iII111i % I1IiiI
  return ( O0ooo )
  if 16 - 16: i1IIi + IiII
  if 48 - 48: i11iIiiIii * I11i
 def print_rloc_probe_rtt ( self ) :
  if ( self . rloc_probe_rtt == - 1 ) : return ( "none" )
  return ( self . rloc_probe_rtt )
  if 28 - 28: OOooOOo
  if 82 - 82: II111iiii
 def print_recent_rloc_probe_rtts ( self ) :
  o000O00Ooo = str ( self . recent_rloc_probe_rtts )
  o000O00Ooo = o000O00Ooo . replace ( "-1" , "?" )
  return ( o000O00Ooo )
  if 9 - 9: OoOoOO00 . iIii1I11I1II1 % OOooOOo + O0
  if 39 - 39: i1IIi + i11iIiiIii . II111iiii
 def compute_rloc_probe_rtt ( self ) :
  IiI1i11iiII = self . rloc_probe_rtt
  self . rloc_probe_rtt = - 1
  if ( self . last_rloc_probe_reply == None ) : return
  if ( self . last_rloc_probe == None ) : return
  self . rloc_probe_rtt = self . last_rloc_probe_reply - self . last_rloc_probe
  self . rloc_probe_rtt = round ( self . rloc_probe_rtt , 3 )
  O0OOoOo = self . recent_rloc_probe_rtts
  self . recent_rloc_probe_rtts = [ IiI1i11iiII ] + O0OOoOo [ 0 : - 1 ]
  if 33 - 33: OoooooooOO + o0oOOo0O0Ooo . OoOoOO00 % Oo0Ooo * O0
  if 49 - 49: I1ii11iIi11i * I1Ii111 - OoooooooOO . i1IIi . I1ii11iIi11i
 def print_rloc_probe_hops ( self ) :
  return ( self . rloc_probe_hops )
  if 37 - 37: IiII - oO0o
  if 92 - 92: I1IiiI
 def print_recent_rloc_probe_hops ( self ) :
  OOOOO0 = str ( self . recent_rloc_probe_hops )
  return ( OOOOO0 )
  if 60 - 60: I11i + I1ii11iIi11i
  if 47 - 47: I1Ii111 + OoooooooOO % II111iiii
 def store_rloc_probe_hops ( self , to_hops , from_ttl ) :
  if ( to_hops == 0 ) :
   to_hops = "?"
  elif ( to_hops < LISP_RLOC_PROBE_TTL / 2 ) :
   to_hops = "!"
  else :
   to_hops = str ( LISP_RLOC_PROBE_TTL - to_hops )
   if 5 - 5: OOooOOo
  if ( from_ttl < LISP_RLOC_PROBE_TTL / 2 ) :
   IiiiII1ii1I1 = "!"
  else :
   IiiiII1ii1I1 = str ( LISP_RLOC_PROBE_TTL - from_ttl )
   if 5 - 5: OoooooooOO / o0oOOo0O0Ooo
   if 14 - 14: OOooOOo * Oo0Ooo - o0oOOo0O0Ooo + iIii1I11I1II1 / ooOoO0o % iIii1I11I1II1
  IiI1i11iiII = self . rloc_probe_hops
  self . rloc_probe_hops = to_hops + "/" + IiiiII1ii1I1
  O0OOoOo = self . recent_rloc_probe_hops
  self . recent_rloc_probe_hops = [ IiI1i11iiII ] + O0OOoOo [ 0 : - 1 ]
  if 4 - 4: OoOoOO00 / Oo0Ooo - OoO0O00 . OoOoOO00 / I1Ii111
  if 60 - 60: OOooOOo * I1Ii111
 def store_rloc_probe_latencies ( self , json_telemetry ) :
  I1i1Iii1i1iI = lisp_decode_telemetry ( json_telemetry )
  if 13 - 13: o0oOOo0O0Ooo . II111iiii
  Ooo0oo0 = round ( float ( I1i1Iii1i1iI [ "etr-in" ] ) - float ( I1i1Iii1i1iI [ "itr-out" ] ) , 3 )
  oOo0oO0o00Oo = round ( float ( I1i1Iii1i1iI [ "itr-in" ] ) - float ( I1i1Iii1i1iI [ "etr-out" ] ) , 3 )
  if 43 - 43: I1IiiI - oO0o + OOooOOo * OoooooooOO
  IiI1i11iiII = self . rloc_probe_latency
  self . rloc_probe_latency = str ( Ooo0oo0 ) + "/" + str ( oOo0oO0o00Oo )
  O0OOoOo = self . recent_rloc_probe_latencies
  self . recent_rloc_probe_latencies = [ IiI1i11iiII ] + O0OOoOo [ 0 : - 1 ]
  if 92 - 92: i11iIiiIii / II111iiii * OoO0O00
  if 51 - 51: I1ii11iIi11i
 def print_rloc_probe_latency ( self ) :
  return ( self . rloc_probe_latency )
  if 95 - 95: I1IiiI / iII111i + i1IIi
  if 31 - 31: OoOoOO00
 def print_recent_rloc_probe_latencies ( self ) :
  Iii1IiIIiI = str ( self . recent_rloc_probe_latencies )
  return ( Iii1IiIIiI )
  if 30 - 30: iIii1I11I1II1
  if 3 - 3: o0oOOo0O0Ooo % iII111i - Ii1I
 def process_rloc_probe_reply ( self , ts , nonce , eid , group , hc , ttl , jt ) :
  I1II = self
  while ( True ) :
   if ( I1II . last_rloc_probe_nonce == nonce ) : break
   I1II = I1II . next_rloc
   if ( I1II == None ) :
    lprint ( "    No matching nonce state found for nonce 0x{}" . format ( lisp_hex_string ( nonce ) ) )
    if 29 - 29: Oo0Ooo
    return
    if 91 - 91: oO0o / OoO0O00 + I1IiiI * iIii1I11I1II1
    if 38 - 38: I11i
    if 50 - 50: I1ii11iIi11i * I1IiiI / OoO0O00 / i1IIi / ooOoO0o . ooOoO0o
    if 22 - 22: I11i % iIii1I11I1II1 - i11iIiiIii * OoOoOO00 - I1Ii111
    if 97 - 97: i11iIiiIii . OoOoOO00 + oO0o * O0 % OoO0O00 - Ii1I
    if 46 - 46: I1Ii111
  I1II . last_rloc_probe_reply = ts
  I1II . compute_rloc_probe_rtt ( )
  OO000OoO = I1II . print_state_change ( "up" )
  if ( I1II . state != LISP_RLOC_UP_STATE ) :
   lisp_update_rtr_updown ( I1II . rloc , True )
   I1II . state = LISP_RLOC_UP_STATE
   I1II . last_state_change = lisp_get_timestamp ( )
   o0Oo0 = lisp_map_cache . lookup_cache ( eid , True )
   if ( o0Oo0 ) : lisp_write_ipc_map_cache ( True , o0Oo0 )
   if 23 - 23: OoOoOO00 - oO0o % iII111i . II111iiii
   if 36 - 36: II111iiii - ooOoO0o
   if 52 - 52: i1IIi + i1IIi * i1IIi / OoOoOO00
   if 98 - 98: iII111i . i1IIi + o0oOOo0O0Ooo * OoooooooOO - i11iIiiIii
   if 21 - 21: i11iIiiIii . oO0o * o0oOOo0O0Ooo + Oo0Ooo * OoOoOO00 * o0oOOo0O0Ooo
  I1II . store_rloc_probe_hops ( hc , ttl )
  if 33 - 33: I1IiiI + O0 - I11i
  if 90 - 90: I1Ii111 * OoooooooOO . iIii1I11I1II1 % OoO0O00 / I11i + iII111i
  if 63 - 63: o0oOOo0O0Ooo . IiII . Oo0Ooo - iIii1I11I1II1 / I1Ii111
  if 66 - 66: ooOoO0o * I1Ii111 - II111iiii
  if ( jt ) : I1II . store_rloc_probe_latencies ( jt )
  if 38 - 38: O0 % I1ii11iIi11i + O0
  oO0oo000O = bold ( "RLOC-probe reply" , False )
  oo0o00OO = I1II . rloc . print_address_no_iid ( )
  iIIi = bold ( str ( I1II . print_rloc_probe_rtt ( ) ) , False )
  IiI1i1i1 = ":{}" . format ( self . translated_port ) if self . translated_port != 0 else ""
  if 21 - 21: iII111i / o0oOOo0O0Ooo
  o0OoiIiIIi = ""
  if ( I1II . rloc_next_hop != None ) :
   o0 , O0Oo0o = I1II . rloc_next_hop
   o0OoiIiIIi = ", nh {}({})" . format ( O0Oo0o , o0 )
   if 14 - 14: Oo0Ooo % IiII + Oo0Ooo
   if 59 - 59: OoOoOO00 + O0 / I1IiiI % O0 / OoooooooOO * Ii1I
  iiII = bold ( I1II . print_rloc_probe_latency ( ) , False )
  iiII = ", latency {}" . format ( iiII ) if jt else ""
  if 26 - 26: O0 - II111iiii % IiII - OoOoOO00 * iII111i % OOooOOo
  iIIi1iI1I1IIi = green ( lisp_print_eid_tuple ( eid , group ) , False )
  if 21 - 21: oO0o + II111iiii - I1ii11iIi11i
  lprint ( ( "    Received {} from {}{} for {}, {}, rtt {}{}, " + "to-ttl/from-ttl {}{}" ) . format ( oO0oo000O , red ( oo0o00OO , False ) , IiI1i1i1 , iIIi1iI1I1IIi ,
  # I1Ii111 - O0 - IiII . OOooOOo % IiII . I1IiiI
 OO000OoO , iIIi , o0OoiIiIIi , str ( hc ) + "/" + str ( ttl ) , iiII ) )
  if 31 - 31: i11iIiiIii % IiII + IiII / oO0o
  if ( I1II . rloc_next_hop == None ) : return
  if 53 - 53: IiII
  if 52 - 52: I1Ii111 * I11i - II111iiii + OOooOOo + II111iiii
  if 91 - 91: i1IIi + Oo0Ooo - I1ii11iIi11i + I1ii11iIi11i * O0 / O0
  if 78 - 78: OoooooooOO
  I1II = None
  II1IIii1 = None
  while ( True ) :
   I1II = self if I1II == None else I1II . next_rloc
   if ( I1II == None ) : break
   if ( I1II . up_state ( ) == False ) : continue
   if ( I1II . rloc_probe_rtt == - 1 ) : continue
   if 73 - 73: o0oOOo0O0Ooo + OoooooooOO - I1Ii111 . iIii1I11I1II1
   if ( II1IIii1 == None ) : II1IIii1 = I1II
   if ( I1II . rloc_probe_rtt < II1IIii1 . rloc_probe_rtt ) : II1IIii1 = I1II
   if 25 - 25: OoooooooOO % I1ii11iIi11i % Oo0Ooo % i11iIiiIii
   if 8 - 8: O0 - O0 % Ii1I
  if ( II1IIii1 != None ) :
   o0 , O0Oo0o = II1IIii1 . rloc_next_hop
   o0OoiIiIIi = bold ( "nh {}({})" . format ( O0Oo0o , o0 ) , False )
   lprint ( "    Install host-route via best {}" . format ( o0OoiIiIIi ) )
   lisp_install_host_route ( oo0o00OO , None , False )
   lisp_install_host_route ( oo0o00OO , O0Oo0o , True )
   if 22 - 22: OoOoOO00
   if 85 - 85: II111iiii - II111iiii
   if 95 - 95: II111iiii + II111iiii + iII111i
 def add_to_rloc_probe_list ( self , eid , group ) :
  oo0o00OO = self . rloc . print_address_no_iid ( )
  Oo0o = self . translated_port
  if ( Oo0o != 0 ) : oo0o00OO += ":" + str ( Oo0o )
  if 38 - 38: OoO0O00 * Ii1I * O0 / I1IiiI
  if ( lisp_rloc_probe_list . has_key ( oo0o00OO ) == False ) :
   lisp_rloc_probe_list [ oo0o00OO ] = [ ]
   if 99 - 99: Oo0Ooo + ooOoO0o - I1ii11iIi11i + I1Ii111 + Ii1I * I1IiiI
   if 68 - 68: OoO0O00
  if ( group . is_null ( ) ) : group . instance_id = 0
  for I1I111iIiI , iIIi1iI1I1IIi , i11ii in lisp_rloc_probe_list [ oo0o00OO ] :
   if ( iIIi1iI1I1IIi . is_exact_match ( eid ) and i11ii . is_exact_match ( group ) ) :
    if ( I1I111iIiI == self ) :
     if ( lisp_rloc_probe_list [ oo0o00OO ] == [ ] ) :
      lisp_rloc_probe_list . pop ( oo0o00OO )
      if 79 - 79: Ii1I . IiII + OoOoOO00
     return
     if 10 - 10: OoooooooOO * iII111i * ooOoO0o . Ii1I % I1Ii111 / I1ii11iIi11i
    lisp_rloc_probe_list [ oo0o00OO ] . remove ( [ I1I111iIiI , iIIi1iI1I1IIi , i11ii ] )
    break
    if 71 - 71: Ii1I + IiII
    if 10 - 10: II111iiii % o0oOOo0O0Ooo . o0oOOo0O0Ooo % iII111i
  lisp_rloc_probe_list [ oo0o00OO ] . append ( [ self , eid , group ] )
  if 2 - 2: OoooooooOO / IiII % Oo0Ooo % iIii1I11I1II1
  if 62 - 62: oO0o
  if 47 - 47: I1IiiI - O0 - I1ii11iIi11i . OoOoOO00
  if 98 - 98: o0oOOo0O0Ooo - OoO0O00 . I1ii11iIi11i / OOooOOo
  if 43 - 43: I1IiiI + OOooOOo + o0oOOo0O0Ooo
  I1II = lisp_rloc_probe_list [ oo0o00OO ] [ 0 ] [ 0 ]
  if ( I1II . state == LISP_RLOC_UNREACH_STATE ) :
   self . state = LISP_RLOC_UNREACH_STATE
   self . last_state_change = lisp_get_timestamp ( )
   if 44 - 44: o0oOOo0O0Ooo % OoO0O00 . OoooooooOO
   if 21 - 21: Oo0Ooo * Oo0Ooo - iII111i - O0
   if 87 - 87: OOooOOo / I1Ii111 - Ii1I + O0 - oO0o - O0
 def delete_from_rloc_probe_list ( self , eid , group ) :
  oo0o00OO = self . rloc . print_address_no_iid ( )
  Oo0o = self . translated_port
  if ( Oo0o != 0 ) : oo0o00OO += ":" + str ( Oo0o )
  if ( lisp_rloc_probe_list . has_key ( oo0o00OO ) == False ) : return
  if 68 - 68: iII111i + II111iiii + I1ii11iIi11i * OOooOOo / oO0o
  iI1Iii = [ ]
  for i1ii1i1Ii11 in lisp_rloc_probe_list [ oo0o00OO ] :
   if ( i1ii1i1Ii11 [ 0 ] != self ) : continue
   if ( i1ii1i1Ii11 [ 1 ] . is_exact_match ( eid ) == False ) : continue
   if ( i1ii1i1Ii11 [ 2 ] . is_exact_match ( group ) == False ) : continue
   iI1Iii = i1ii1i1Ii11
   break
   if 20 - 20: Ii1I * OoooooooOO / OoooooooOO + OOooOOo - I1IiiI - O0
  if ( iI1Iii == [ ] ) : return
  if 22 - 22: iII111i - i11iIiiIii + ooOoO0o + oO0o + II111iiii / oO0o
  try :
   lisp_rloc_probe_list [ oo0o00OO ] . remove ( iI1Iii )
   if ( lisp_rloc_probe_list [ oo0o00OO ] == [ ] ) :
    lisp_rloc_probe_list . pop ( oo0o00OO )
    if 7 - 7: iII111i % o0oOOo0O0Ooo
  except :
   return
   if 68 - 68: iIii1I11I1II1 / II111iiii
   if 47 - 47: i11iIiiIii . OOooOOo + I1Ii111 / I1ii11iIi11i . I1IiiI . I1Ii111
   if 79 - 79: OoO0O00 / i11iIiiIii . IiII - I11i / iIii1I11I1II1
 def print_rloc_probe_state ( self , trailing_linefeed ) :
  oOOO = ""
  I1II = self
  while ( True ) :
   OOii1I1iii = I1II . last_rloc_probe
   if ( OOii1I1iii == None ) : OOii1I1iii = 0
   o0oO0o0Oooo = I1II . last_rloc_probe_reply
   if ( o0oO0o0Oooo == None ) : o0oO0o0Oooo = 0
   iIIi = I1II . print_rloc_probe_rtt ( )
   OO0o0OO0 = space ( 4 )
   if 45 - 45: I1ii11iIi11i / iIii1I11I1II1 + OoO0O00 / O0 - O0 - I1Ii111
   if ( I1II . rloc_next_hop == None ) :
    oOOO += "RLOC-Probing:\n"
   else :
    o0 , O0Oo0o = I1II . rloc_next_hop
    oOOO += "RLOC-Probing for nh {}({}):\n" . format ( O0Oo0o , o0 )
    if 88 - 88: o0oOOo0O0Ooo % I1Ii111
    if 4 - 4: i11iIiiIii + o0oOOo0O0Ooo % I11i - I1ii11iIi11i * I1ii11iIi11i
   oOOO += ( "{}RLOC-probe request sent: {}\n{}RLOC-probe reply " + "received: {}, rtt {}" ) . format ( OO0o0OO0 , lisp_print_elapsed ( OOii1I1iii ) ,
   # Ii1I + OoO0O00 * O0 . IiII % OoooooooOO / II111iiii
 OO0o0OO0 , lisp_print_elapsed ( o0oO0o0Oooo ) , iIIi )
   if 25 - 25: ooOoO0o
   if ( trailing_linefeed ) : oOOO += "\n"
   if 63 - 63: i11iIiiIii . i1IIi
   I1II = I1II . next_rloc
   if ( I1II == None ) : break
   oOOO += "\n"
   if 41 - 41: i11iIiiIii / ooOoO0o - Ii1I + I11i
  return ( oOOO )
  if 15 - 15: I1ii11iIi11i
  if 22 - 22: iIii1I11I1II1 - i1IIi - i11iIiiIii / I1IiiI + o0oOOo0O0Ooo
 def get_encap_keys ( self ) :
  Oo0o = "4341" if self . translated_port == 0 else str ( self . translated_port )
  if 56 - 56: I1IiiI . ooOoO0o
  oo0o00OO = self . rloc . print_address_no_iid ( ) + ":" + Oo0o
  if 35 - 35: iIii1I11I1II1 % Oo0Ooo + o0oOOo0O0Ooo * o0oOOo0O0Ooo % ooOoO0o
  try :
   iIi11III = lisp_crypto_keys_by_rloc_encap [ oo0o00OO ]
   if ( iIi11III [ 1 ] ) : return ( iIi11III [ 1 ] . encrypt_key , iIi11III [ 1 ] . icv_key )
   return ( None , None )
  except :
   return ( None , None )
   if 10 - 10: I1ii11iIi11i / II111iiii % II111iiii - OoooooooOO * o0oOOo0O0Ooo / ooOoO0o
   if 26 - 26: OoO0O00 . O0 * iII111i % OoOoOO00 % iIii1I11I1II1
   if 37 - 37: iII111i - ooOoO0o * Ii1I + II111iiii * i11iIiiIii
 def rloc_recent_rekey ( self ) :
  Oo0o = "4341" if self . translated_port == 0 else str ( self . translated_port )
  if 8 - 8: OoooooooOO % I11i - iII111i * OOooOOo . O0
  oo0o00OO = self . rloc . print_address_no_iid ( ) + ":" + Oo0o
  if 40 - 40: I1Ii111 . oO0o + OoO0O00 % Oo0Ooo / II111iiii
  try :
   o0Oo = lisp_crypto_keys_by_rloc_encap [ oo0o00OO ] [ 1 ]
   if ( o0Oo == None ) : return ( False )
   if ( o0Oo . last_rekey == None ) : return ( True )
   return ( time . time ( ) - o0Oo . last_rekey < 1 )
  except :
   return ( False )
   if 19 - 19: i11iIiiIii
   if 20 - 20: i11iIiiIii . II111iiii - I1ii11iIi11i / ooOoO0o % i11iIiiIii
   if 35 - 35: Oo0Ooo - I1ii11iIi11i . Oo0Ooo
   if 13 - 13: II111iiii / OoOoOO00 * iII111i % O0 % I1ii11iIi11i * i11iIiiIii
class lisp_mapping ( ) :
 def __init__ ( self , eid , group , rloc_set ) :
  self . eid = eid
  if ( eid == "" ) : self . eid = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . group = group
  if ( group == "" ) : self . group = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . rloc_set = rloc_set
  self . best_rloc_set = [ ]
  self . build_best_rloc_set ( )
  self . uptime = lisp_get_timestamp ( )
  self . action = LISP_NO_ACTION
  self . expires = None
  self . map_cache_ttl = None
  self . register_ttl = LISP_REGISTER_TTL
  self . last_refresh_time = self . uptime
  self . source_cache = None
  self . map_replies_sent = 0
  self . mapping_source = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . use_mr_name = "all"
  self . use_ms_name = "all"
  self . stats = lisp_stats ( )
  self . dynamic_eids = None
  self . checkpoint_entry = False
  self . secondary_iid = None
  self . signature_eid = False
  self . gleaned = False
  self . recent_sources = { }
  self . last_multicast_map_request = 0
  self . subscribed_eid = None
  self . subscribed_group = None
  if 92 - 92: i11iIiiIii + OoO0O00
  if 94 - 94: I1ii11iIi11i + OoO0O00 . II111iiii + oO0o . II111iiii
 def print_mapping ( self , eid_indent , rloc_indent ) :
  i1 = lisp_print_elapsed ( self . uptime )
  OOo0oOOO0 = "" if self . group . is_null ( ) else ", group {}" . format ( self . group . print_prefix ( ) )
  if 96 - 96: i11iIiiIii
  lprint ( "{}eid {}{}, uptime {}, {} rlocs:" . format ( eid_indent ,
 green ( self . eid . print_prefix ( ) , False ) , OOo0oOOO0 , i1 ,
 len ( self . rloc_set ) ) )
  for I1II in self . rloc_set : I1II . print_rloc ( rloc_indent )
  if 66 - 66: ooOoO0o * iII111i - iII111i - O0 . o0oOOo0O0Ooo
  if 23 - 23: iIii1I11I1II1 / I11i % OoOoOO00 . OoO0O00
 def print_eid_tuple ( self ) :
  return ( lisp_print_eid_tuple ( self . eid , self . group ) )
  if 90 - 90: iIii1I11I1II1 - OOooOOo . Ii1I % OoO0O00
  if 89 - 89: i11iIiiIii
 def print_ttl ( self ) :
  Oo0o0 = self . map_cache_ttl
  if ( Oo0o0 == None ) : return ( "forever" )
  if 86 - 86: Oo0Ooo % iIii1I11I1II1 . II111iiii / I11i % OoO0O00 % OoO0O00
  if ( Oo0o0 >= 3600 ) :
   if ( ( Oo0o0 % 3600 ) == 0 ) :
    Oo0o0 = str ( Oo0o0 / 3600 ) + " hours"
   else :
    Oo0o0 = str ( Oo0o0 * 60 ) + " mins"
    if 40 - 40: o0oOOo0O0Ooo . iIii1I11I1II1 * Oo0Ooo * i1IIi
  elif ( Oo0o0 >= 60 ) :
   if ( ( Oo0o0 % 60 ) == 0 ) :
    Oo0o0 = str ( Oo0o0 / 60 ) + " mins"
   else :
    Oo0o0 = str ( Oo0o0 ) + " secs"
    if 94 - 94: oO0o - II111iiii + OoOoOO00
  else :
   Oo0o0 = str ( Oo0o0 ) + " secs"
   if 90 - 90: Oo0Ooo + Oo0Ooo + I1Ii111
  return ( Oo0o0 )
  if 81 - 81: i1IIi % iIii1I11I1II1 % Ii1I * ooOoO0o % i1IIi * I1IiiI
  if 15 - 15: ooOoO0o
 def refresh ( self ) :
  if ( self . group . is_null ( ) ) : return ( self . refresh_unicast ( ) )
  return ( self . refresh_multicast ( ) )
  if 26 - 26: IiII % ooOoO0o / OOooOOo
  if 14 - 14: i11iIiiIii . I1ii11iIi11i
 def refresh_unicast ( self ) :
  return ( self . is_active ( ) and self . has_ttl_elapsed ( ) and
 self . gleaned == False )
  if 20 - 20: O0 . iIii1I11I1II1 * I1ii11iIi11i - O0 + I1ii11iIi11i / I1IiiI
  if 67 - 67: OoO0O00 / OoOoOO00 / i11iIiiIii % OoOoOO00
 def refresh_multicast ( self ) :
  if 54 - 54: o0oOOo0O0Ooo . i11iIiiIii + I1IiiI * ooOoO0o - ooOoO0o
  if 28 - 28: I1Ii111 . i11iIiiIii * oO0o % ooOoO0o / iII111i . OOooOOo
  if 57 - 57: OoooooooOO . iIii1I11I1II1 % iII111i % Oo0Ooo
  if 92 - 92: I1Ii111 - Ii1I + I1Ii111
  if 8 - 8: Oo0Ooo . iII111i / i11iIiiIii + iIii1I11I1II1 - OoOoOO00
  Ooo0o0oo0 = int ( ( time . time ( ) - self . uptime ) % self . map_cache_ttl )
  iiooo0 = ( Ooo0o0oo0 in [ 0 , 1 , 2 ] )
  if ( iiooo0 == False ) : return ( False )
  if 70 - 70: OoooooooOO + OoO0O00 . iII111i . ooOoO0o
  if 13 - 13: IiII
  if 86 - 86: OoOoOO00 + iIii1I11I1II1 / OoOoOO00 + Oo0Ooo / Ii1I - II111iiii
  if 5 - 5: I1ii11iIi11i / Oo0Ooo
  iii1111ii = ( ( time . time ( ) - self . last_multicast_map_request ) <= 2 )
  if ( iii1111ii ) : return ( False )
  if 71 - 71: iIii1I11I1II1 % ooOoO0o - I1Ii111
  self . last_multicast_map_request = lisp_get_timestamp ( )
  return ( True )
  if 81 - 81: i1IIi . IiII / Oo0Ooo . I1Ii111 . iIii1I11I1II1 + iIii1I11I1II1
  if 35 - 35: I1ii11iIi11i / OoOoOO00 / i1IIi / i11iIiiIii * iIii1I11I1II1 / i1IIi
 def has_ttl_elapsed ( self ) :
  if ( self . map_cache_ttl == None ) : return ( False )
  Ooo0o0oo0 = time . time ( ) - self . last_refresh_time
  if ( Ooo0o0oo0 >= self . map_cache_ttl ) : return ( True )
  if 69 - 69: OOooOOo / I1Ii111 * II111iiii
  if 88 - 88: OOooOOo - I1IiiI + Oo0Ooo
  if 15 - 15: I11i / I1ii11iIi11i - I1Ii111 * O0 % ooOoO0o / I1IiiI
  if 53 - 53: i11iIiiIii * i11iIiiIii % O0 % IiII
  if 57 - 57: I1IiiI % i1IIi * OoO0O00 + I1Ii111 . I11i % I11i
  oOOOii1 = self . map_cache_ttl - ( self . map_cache_ttl / 10 )
  if ( Ooo0o0oo0 >= oOOOii1 ) : return ( True )
  return ( False )
  if 61 - 61: oO0o / OoooooooOO - OoooooooOO + Ii1I % I1Ii111
  if 54 - 54: IiII % oO0o + i11iIiiIii % O0
 def is_active ( self ) :
  if ( self . stats . last_increment == None ) : return ( False )
  Ooo0o0oo0 = time . time ( ) - self . stats . last_increment
  return ( Ooo0o0oo0 <= 60 )
  if 56 - 56: OoOoOO00 / II111iiii . O0
  if 24 - 24: OoooooooOO * Ii1I * II111iiii
 def match_eid_tuple ( self , db ) :
  if ( self . eid . is_exact_match ( db . eid ) == False ) : return ( False )
  if ( self . group . is_exact_match ( db . group ) == False ) : return ( False )
  return ( True )
  if 75 - 75: I1IiiI / o0oOOo0O0Ooo . Ii1I / Ii1I / iII111i - Ii1I
  if 39 - 39: OoO0O00 . iIii1I11I1II1 - oO0o
 def sort_rloc_set ( self ) :
  self . rloc_set . sort ( key = operator . attrgetter ( 'rloc.address' ) )
  if 60 - 60: OOooOOo + OOooOOo - Ii1I / iII111i
  if 42 - 42: IiII % oO0o - o0oOOo0O0Ooo * iII111i - Oo0Ooo
 def delete_rlocs_from_rloc_probe_list ( self ) :
  for I1II in self . best_rloc_set :
   I1II . delete_from_rloc_probe_list ( self . eid , self . group )
   if 19 - 19: I1IiiI - iII111i - oO0o / II111iiii
   if 98 - 98: IiII * OoOoOO00
   if 13 - 13: O0 + oO0o - iIii1I11I1II1 - Oo0Ooo % I1IiiI
 def build_best_rloc_set ( self ) :
  iI1o0O0O0oOOOo = self . best_rloc_set
  self . best_rloc_set = [ ]
  if ( self . rloc_set == None ) : return
  if 52 - 52: o0oOOo0O0Ooo % I1Ii111 % OoO0O00 / iIii1I11I1II1
  if 81 - 81: I1IiiI / ooOoO0o * IiII * Oo0Ooo - oO0o . OOooOOo
  if 48 - 48: I1Ii111 * iII111i
  if 93 - 93: I11i % iIii1I11I1II1 + Ii1I - I1IiiI + OoooooooOO . IiII
  Oo0I1i = 256
  for I1II in self . rloc_set :
   if ( I1II . up_state ( ) ) : Oo0I1i = min ( I1II . priority , Oo0I1i )
   if 86 - 86: i1IIi . oO0o % OOooOOo
   if 99 - 99: oO0o / I1Ii111 * oO0o * I11i
   if 38 - 38: o0oOOo0O0Ooo + OoOoOO00
   if 24 - 24: Ii1I - OOooOOo - o0oOOo0O0Ooo - I1Ii111 / OoooooooOO
   if 17 - 17: OoO0O00
   if 79 - 79: Ii1I - II111iiii
   if 57 - 57: II111iiii / OoooooooOO
   if 4 - 4: I11i * OoOoOO00
   if 18 - 18: iIii1I11I1II1 % OOooOOo - I1ii11iIi11i * i1IIi + Oo0Ooo
   if 87 - 87: oO0o . I11i
  for I1II in self . rloc_set :
   if ( I1II . priority <= Oo0I1i ) :
    if ( I1II . unreach_state ( ) and I1II . last_rloc_probe == None ) :
     I1II . last_rloc_probe = lisp_get_timestamp ( )
     if 15 - 15: oO0o
    self . best_rloc_set . append ( I1II )
    if 45 - 45: Oo0Ooo * IiII * OoO0O00 + iIii1I11I1II1
    if 89 - 89: IiII . IiII . oO0o % iII111i
    if 27 - 27: OoOoOO00 + O0 % i1IIi - Oo0Ooo
    if 96 - 96: O0 % o0oOOo0O0Ooo + OOooOOo % I1IiiI
    if 51 - 51: i1IIi . o0oOOo0O0Ooo % I1IiiI - OoooooooOO / OoOoOO00 - I11i
    if 45 - 45: O0 * II111iiii / i11iIiiIii
    if 38 - 38: OoooooooOO % i11iIiiIii - O0 / O0
    if 59 - 59: OoO0O00 % iII111i + oO0o * II111iiii . OOooOOo
  for I1II in iI1o0O0O0oOOOo :
   if ( I1II . priority < Oo0I1i ) : continue
   I1II . delete_from_rloc_probe_list ( self . eid , self . group )
   if 26 - 26: OOooOOo % OoooooooOO . Ii1I / iIii1I11I1II1 * I1IiiI
  for I1II in self . best_rloc_set :
   if ( I1II . rloc . is_null ( ) ) : continue
   I1II . add_to_rloc_probe_list ( self . eid , self . group )
   if 85 - 85: IiII / Ii1I - I1ii11iIi11i * OOooOOo
   if 19 - 19: I1ii11iIi11i
   if 12 - 12: ooOoO0o * I1ii11iIi11i * O0 / oO0o + iII111i - iIii1I11I1II1
 def select_rloc ( self , lisp_packet , ipc_socket ) :
  IiiiIi1iiii11 = lisp_packet . packet
  o0o0o0Oo0Oo = lisp_packet . inner_version
  oOOoO0O = len ( self . best_rloc_set )
  if ( oOOoO0O == 0 ) :
   self . stats . increment ( len ( IiiiIi1iiii11 ) )
   return ( [ None , None , None , self . action , None , None ] )
   if 75 - 75: Ii1I * Oo0Ooo
   if 47 - 47: O0 - OoO0O00 % I11i * O0
  iIiooooOooOO0 = 4 if lisp_load_split_pings else 0
  I1iI1111ii1I1 = lisp_packet . hash_ports ( )
  if ( o0o0o0Oo0Oo == 4 ) :
   for iIi1I1 in range ( 8 + iIiooooOooOO0 ) :
    I1iI1111ii1I1 = I1iI1111ii1I1 ^ struct . unpack ( "B" , IiiiIi1iiii11 [ iIi1I1 + 12 ] ) [ 0 ]
    if 20 - 20: I11i + IiII
  elif ( o0o0o0Oo0Oo == 6 ) :
   for iIi1I1 in range ( 0 , 32 + iIiooooOooOO0 , 4 ) :
    I1iI1111ii1I1 = I1iI1111ii1I1 ^ struct . unpack ( "I" , IiiiIi1iiii11 [ iIi1I1 + 8 : iIi1I1 + 12 ] ) [ 0 ]
    if 44 - 44: OoooooooOO % I11i / O0
   I1iI1111ii1I1 = ( I1iI1111ii1I1 >> 16 ) + ( I1iI1111ii1I1 & 0xffff )
   I1iI1111ii1I1 = ( I1iI1111ii1I1 >> 8 ) + ( I1iI1111ii1I1 & 0xff )
  else :
   for iIi1I1 in range ( 0 , 12 + iIiooooOooOO0 , 4 ) :
    I1iI1111ii1I1 = I1iI1111ii1I1 ^ struct . unpack ( "I" , IiiiIi1iiii11 [ iIi1I1 : iIi1I1 + 4 ] ) [ 0 ]
    if 94 - 94: IiII
    if 83 - 83: OoO0O00
    if 55 - 55: iII111i
  if ( lisp_data_plane_logging ) :
   IIII1 = [ ]
   for I1I111iIiI in self . best_rloc_set :
    if ( I1I111iIiI . rloc . is_null ( ) ) : continue
    IIII1 . append ( [ I1I111iIiI . rloc . print_address_no_iid ( ) , I1I111iIiI . print_state ( ) ] )
    if 73 - 73: o0oOOo0O0Ooo + i11iIiiIii / ooOoO0o * II111iiii * o0oOOo0O0Ooo % iII111i
   dprint ( "Packet hash {}, index {}, best-rloc-list: {}" . format ( hex ( I1iI1111ii1I1 ) , I1iI1111ii1I1 % oOOoO0O , red ( str ( IIII1 ) , False ) ) )
   if 44 - 44: IiII * OoOoOO00 - OoO0O00 - OoooooooOO - I1ii11iIi11i - II111iiii
   if 26 - 26: ooOoO0o - i1IIi / OOooOOo + OoOoOO00 / iII111i
   if 27 - 27: I11i % Ii1I / iII111i . OoOoOO00
   if 88 - 88: iII111i - i11iIiiIii * I1Ii111 * i11iIiiIii - O0
   if 8 - 8: oO0o + O0
   if 52 - 52: I11i * OOooOOo - OoOoOO00 % iIii1I11I1II1 . II111iiii
  I1II = self . best_rloc_set [ I1iI1111ii1I1 % oOOoO0O ]
  if 1 - 1: OOooOOo / I1IiiI / Ii1I * iII111i
  if 14 - 14: ooOoO0o . O0 * OOooOOo
  if 34 - 34: I1ii11iIi11i . OOooOOo + OoO0O00 % o0oOOo0O0Ooo * O0 * I1IiiI
  if 9 - 9: IiII / i11iIiiIii . o0oOOo0O0Ooo - OOooOOo % I1Ii111
  if 65 - 65: I1IiiI % OoOoOO00
  oooooO0oO0o = lisp_get_echo_nonce ( I1II . rloc , None )
  if ( oooooO0oO0o ) :
   oooooO0oO0o . change_state ( I1II )
   if ( I1II . no_echoed_nonce_state ( ) ) :
    oooooO0oO0o . request_nonce_sent = None
    if 45 - 45: o0oOOo0O0Ooo
    if 33 - 33: ooOoO0o % O0 % I1ii11iIi11i % o0oOOo0O0Ooo + i11iIiiIii . I1Ii111
    if 21 - 21: I1Ii111 * I1ii11iIi11i * ooOoO0o
    if 73 - 73: OoOoOO00 * O0
    if 1 - 1: OOooOOo * OoooooooOO
    if 46 - 46: I1ii11iIi11i * I1Ii111 / OOooOOo / I1IiiI
  if ( I1II . up_state ( ) == False ) :
   iII1I = I1iI1111ii1I1 % oOOoO0O
   ooo = ( iII1I + 1 ) % oOOoO0O
   while ( ooo != iII1I ) :
    I1II = self . best_rloc_set [ ooo ]
    if ( I1II . up_state ( ) ) : break
    ooo = ( ooo + 1 ) % oOOoO0O
    if 86 - 86: I1ii11iIi11i
   if ( ooo == iII1I ) :
    self . build_best_rloc_set ( )
    return ( [ None , None , None , None , None , None ] )
    if 78 - 78: o0oOOo0O0Ooo * iIii1I11I1II1 * iIii1I11I1II1 * I11i % i11iIiiIii
    if 38 - 38: I1IiiI % I1ii11iIi11i * I1IiiI + OOooOOo - OoOoOO00
    if 78 - 78: OOooOOo + I1Ii111
    if 41 - 41: I11i + Oo0Ooo . Oo0Ooo / iII111i . OoOoOO00
    if 1 - 1: ooOoO0o + iII111i % i11iIiiIii / OoOoOO00
    if 98 - 98: IiII
  I1II . stats . increment ( len ( IiiiIi1iiii11 ) )
  if 75 - 75: OoooooooOO % IiII + Ii1I - i1IIi / OoooooooOO
  if 57 - 57: iII111i
  if 18 - 18: II111iiii % i11iIiiIii + I11i - OOooOOo
  if 100 - 100: o0oOOo0O0Ooo / Ii1I - iIii1I11I1II1 / oO0o
  if ( I1II . rle_name and I1II . rle == None ) :
   if ( lisp_rle_list . has_key ( I1II . rle_name ) ) :
    I1II . rle = lisp_rle_list [ I1II . rle_name ]
    if 68 - 68: I11i / II111iiii * oO0o . II111iiii * OOooOOo
    if 78 - 78: I11i * OoO0O00 / II111iiii
  if ( I1II . rle ) : return ( [ None , None , None , None , I1II . rle , None ] )
  if 86 - 86: I1Ii111 % II111iiii
  if 90 - 90: OoO0O00 / I11i - Oo0Ooo
  if 76 - 76: O0 + OoO0O00 / ooOoO0o . II111iiii * iIii1I11I1II1 . I1Ii111
  if 43 - 43: Oo0Ooo + o0oOOo0O0Ooo % o0oOOo0O0Ooo % I1ii11iIi11i / iIii1I11I1II1 . I1ii11iIi11i
  if ( I1II . elp and I1II . elp . use_elp_node ) :
   return ( [ I1II . elp . use_elp_node . address , None , None , None , None ,
 None ] )
   if 59 - 59: IiII . OoO0O00 - OoooooooOO . O0
   if 33 - 33: Ii1I
   if 95 - 95: OoooooooOO + OoO0O00 * ooOoO0o
   if 40 - 40: I1IiiI / OOooOOo * Ii1I
   if 98 - 98: I1IiiI
  IiiiiIi11I1 = None if ( I1II . rloc . is_null ( ) ) else I1II . rloc
  Oo0o = I1II . translated_port
  iI1IIi1I = self . action if ( IiiiiIi11I1 == None ) else None
  if 15 - 15: oO0o
  if 86 - 86: O0
  if 13 - 13: I1ii11iIi11i . IiII - I11i
  if 81 - 81: i11iIiiIii
  if 7 - 7: IiII - OoOoOO00 * i1IIi
  o0OOO = None
  if ( oooooO0oO0o and oooooO0oO0o . request_nonce_timeout ( ) == False ) :
   o0OOO = oooooO0oO0o . get_request_or_echo_nonce ( ipc_socket , IiiiiIi11I1 )
   if 14 - 14: I1ii11iIi11i . OoO0O00
   if 26 - 26: iII111i / ooOoO0o / Oo0Ooo / Oo0Ooo . I1ii11iIi11i * OOooOOo
   if 25 - 25: IiII % I1IiiI / O0 % OOooOOo - OoooooooOO
   if 29 - 29: O0 + iII111i
   if 4 - 4: I11i * I11i - Ii1I * oO0o . I1ii11iIi11i % o0oOOo0O0Ooo
  return ( [ IiiiiIi11I1 , Oo0o , o0OOO , iI1IIi1I , None , I1II ] )
  if 33 - 33: Ii1I * i11iIiiIii / O0 . Oo0Ooo + i1IIi . OoOoOO00
  if 76 - 76: OoooooooOO - O0
 def do_rloc_sets_match ( self , rloc_address_set ) :
  if ( len ( self . rloc_set ) != len ( rloc_address_set ) ) : return ( False )
  if 17 - 17: Oo0Ooo % I1Ii111 . oO0o - O0
  if 32 - 32: O0 % O0
  if 66 - 66: iII111i / i1IIi - Oo0Ooo . Ii1I
  if 65 - 65: I1ii11iIi11i % ooOoO0o - OoOoOO00 + ooOoO0o + Oo0Ooo
  if 95 - 95: I1Ii111 * i11iIiiIii - I1IiiI - OoOoOO00 . ooOoO0o
  for oOO0O in self . rloc_set :
   for I1II in rloc_address_set :
    if ( I1II . is_exact_match ( oOO0O . rloc ) == False ) : continue
    I1II = None
    break
    if 34 - 34: OoooooooOO % I1ii11iIi11i + OoooooooOO % i11iIiiIii / IiII - ooOoO0o
   if ( I1II == rloc_address_set [ - 1 ] ) : return ( False )
   if 74 - 74: iIii1I11I1II1 % II111iiii + IiII
  return ( True )
  if 71 - 71: I1IiiI / O0 * i1IIi . i1IIi + Oo0Ooo
  if 32 - 32: i1IIi * I1Ii111 % I1IiiI / IiII . I1Ii111
 def get_rloc ( self , rloc ) :
  for oOO0O in self . rloc_set :
   I1I111iIiI = oOO0O . rloc
   if ( rloc . is_exact_match ( I1I111iIiI ) ) : return ( oOO0O )
   if 11 - 11: OOooOOo
  return ( None )
  if 25 - 25: i1IIi
  if 99 - 99: OOooOOo + OoooooooOO . I1Ii111 * Oo0Ooo % oO0o
 def get_rloc_by_interface ( self , interface ) :
  for oOO0O in self . rloc_set :
   if ( oOO0O . interface == interface ) : return ( oOO0O )
   if 75 - 75: iII111i
  return ( None )
  if 8 - 8: I1ii11iIi11i . I11i / I1ii11iIi11i - i1IIi
  if 22 - 22: OOooOOo
 def add_db ( self ) :
  if ( self . group . is_null ( ) ) :
   lisp_db_for_lookups . add_cache ( self . eid , self )
  else :
   ii1iii = lisp_db_for_lookups . lookup_cache ( self . group , True )
   if ( ii1iii == None ) :
    ii1iii = lisp_mapping ( self . group , self . group , [ ] )
    lisp_db_for_lookups . add_cache ( self . group , ii1iii )
    if 7 - 7: O0 - I1ii11iIi11i - OoO0O00 * I1Ii111
   ii1iii . add_source_entry ( self )
   if 17 - 17: o0oOOo0O0Ooo % OoO0O00 - I11i * o0oOOo0O0Ooo - i1IIi / I1IiiI
   if 100 - 100: OoO0O00 * i1IIi * o0oOOo0O0Ooo * Oo0Ooo - o0oOOo0O0Ooo
   if 100 - 100: iII111i - i11iIiiIii + OoO0O00
 def add_cache ( self , do_ipc = True ) :
  if ( self . group . is_null ( ) ) :
   lisp_map_cache . add_cache ( self . eid , self )
   if ( lisp_program_hardware ) : lisp_program_vxlan_hardware ( self )
  else :
   o0Oo0 = lisp_map_cache . lookup_cache ( self . group , True )
   if ( o0Oo0 == None ) :
    o0Oo0 = lisp_mapping ( self . group , self . group , [ ] )
    o0Oo0 . eid . copy_address ( self . group )
    o0Oo0 . group . copy_address ( self . group )
    lisp_map_cache . add_cache ( self . group , o0Oo0 )
    if 50 - 50: II111iiii
   if ( self . eid . is_null ( ) ) : self . eid . make_default_route ( o0Oo0 . group )
   o0Oo0 . add_source_entry ( self )
   if 42 - 42: OOooOOo * I1Ii111
  if ( do_ipc ) : lisp_write_ipc_map_cache ( True , self )
  if 53 - 53: II111iiii % OOooOOo / I1ii11iIi11i * OoOoOO00 % I1ii11iIi11i * iII111i
  if 91 - 91: iII111i . OoooooooOO
 def delete_cache ( self ) :
  self . delete_rlocs_from_rloc_probe_list ( )
  lisp_write_ipc_map_cache ( False , self )
  if 90 - 90: i11iIiiIii - I1IiiI
  if ( self . group . is_null ( ) ) :
   lisp_map_cache . delete_cache ( self . eid )
   if ( lisp_program_hardware ) :
    I11i11IIIII = self . eid . print_prefix_no_iid ( )
    os . system ( "ip route delete {}" . format ( I11i11IIIII ) )
    if 53 - 53: Ii1I / o0oOOo0O0Ooo * I1IiiI / i1IIi / iII111i + iII111i
  else :
   o0Oo0 = lisp_map_cache . lookup_cache ( self . group , True )
   if ( o0Oo0 == None ) : return
   if 66 - 66: i1IIi + I1IiiI
   I1IIi1iII11 = o0Oo0 . lookup_source_cache ( self . eid , True )
   if ( I1IIi1iII11 == None ) : return
   if 6 - 6: I11i % i11iIiiIii + iIii1I11I1II1 . i11iIiiIii / OoooooooOO
   o0Oo0 . source_cache . delete_cache ( self . eid )
   if ( o0Oo0 . source_cache . cache_size ( ) == 0 ) :
    lisp_map_cache . delete_cache ( self . group )
    if 66 - 66: iII111i + i11iIiiIii - o0oOOo0O0Ooo * OoooooooOO * IiII
    if 59 - 59: I1ii11iIi11i + i1IIi / I11i . iII111i - II111iiii
    if 66 - 66: Ii1I + OoOoOO00 - I11i / o0oOOo0O0Ooo + iIii1I11I1II1
    if 66 - 66: OOooOOo - I1Ii111 - OoOoOO00 - i1IIi * Ii1I
 def add_source_entry ( self , source_mc ) :
  if ( self . source_cache == None ) : self . source_cache = lisp_cache ( )
  self . source_cache . add_cache ( source_mc . eid , source_mc )
  if 23 - 23: IiII - OoOoOO00 . OoO0O00
  if 81 - 81: I1Ii111 / I1ii11iIi11i
 def lookup_source_cache ( self , source , exact ) :
  if ( self . source_cache == None ) : return ( None )
  return ( self . source_cache . lookup_cache ( source , exact ) )
  if 69 - 69: I1IiiI
  if 79 - 79: ooOoO0o
 def dynamic_eid_configured ( self ) :
  return ( self . dynamic_eids != None )
  if 83 - 83: I1Ii111 % II111iiii
  if 89 - 89: Ii1I . I11i
 def star_secondary_iid ( self , prefix ) :
  if ( self . secondary_iid == None ) : return ( prefix )
  IiIIi11i111 = "," + str ( self . secondary_iid )
  return ( prefix . replace ( IiIIi11i111 , IiIIi11i111 + "*" ) )
  if 98 - 98: I1Ii111 / O0 % ooOoO0o
  if 36 - 36: iIii1I11I1II1 . iII111i * I1IiiI . I1IiiI - IiII
 def increment_decap_stats ( self , packet ) :
  Oo0o = packet . udp_dport
  if ( Oo0o == LISP_DATA_PORT ) :
   I1II = self . get_rloc ( packet . outer_dest )
  else :
   if 39 - 39: O0 / ooOoO0o + I11i - OoOoOO00 * o0oOOo0O0Ooo - OoO0O00
   if 97 - 97: i11iIiiIii / O0 % OoO0O00
   if 88 - 88: i1IIi . I1IiiI
   if 8 - 8: I1ii11iIi11i . OoO0O00 % o0oOOo0O0Ooo / O0
   for I1II in self . rloc_set :
    if ( I1II . translated_port != 0 ) : break
    if 51 - 51: oO0o + Ii1I * Ii1I * I1ii11iIi11i % I11i - I1ii11iIi11i
    if 15 - 15: i1IIi / OoO0O00 - Oo0Ooo
  if ( I1II != None ) : I1II . stats . increment ( len ( packet . packet ) )
  self . stats . increment ( len ( packet . packet ) )
  if 74 - 74: o0oOOo0O0Ooo % Ii1I - II111iiii / ooOoO0o
  if 84 - 84: I1IiiI + OOooOOo
 def rtrs_in_rloc_set ( self ) :
  for I1II in self . rloc_set :
   if ( I1II . is_rtr ( ) ) : return ( True )
   if 80 - 80: OOooOOo / OoOoOO00
  return ( False )
  if 93 - 93: OOooOOo
  if 82 - 82: iIii1I11I1II1 + OoO0O00 / iIii1I11I1II1 . iIii1I11I1II1
 def add_recent_source ( self , source ) :
  self . recent_sources [ source . print_address ( ) ] = lisp_get_timestamp ( )
  if 36 - 36: iII111i % I1ii11iIi11i + OoOoOO00 - i11iIiiIii % II111iiii % I11i
  if 92 - 92: O0 * OoooooooOO + I1ii11iIi11i / IiII
  if 97 - 97: o0oOOo0O0Ooo . Ii1I + I1Ii111
class lisp_dynamic_eid ( ) :
 def __init__ ( self ) :
  self . dynamic_eid = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . uptime = lisp_get_timestamp ( )
  self . interface = None
  self . last_packet = None
  self . timeout = LISP_DEFAULT_DYN_EID_TIMEOUT
  if 72 - 72: i11iIiiIii . iII111i . Ii1I * I1ii11iIi11i
  if 49 - 49: OoOoOO00 - O0 % I11i - ooOoO0o * OOooOOo
 def get_timeout ( self , interface ) :
  try :
   Oo00oOo0 = lisp_myinterfaces [ interface ]
   self . timeout = Oo00oOo0 . dynamic_eid_timeout
  except :
   self . timeout = LISP_DEFAULT_DYN_EID_TIMEOUT
   if 86 - 86: i11iIiiIii - OoOoOO00 * OOooOOo
   if 54 - 54: i11iIiiIii / I11i - i1IIi - ooOoO0o
   if 25 - 25: i11iIiiIii
   if 91 - 91: II111iiii * o0oOOo0O0Ooo
class lisp_group_mapping ( ) :
 def __init__ ( self , group_name , ms_name , group_prefix , sources , rle_addr ) :
  self . group_name = group_name
  self . group_prefix = group_prefix
  self . use_ms_name = ms_name
  self . sources = sources
  self . rle_address = rle_addr
  if 20 - 20: iIii1I11I1II1 % Oo0Ooo * OoOoOO00 % IiII
  if 93 - 93: I11i * iIii1I11I1II1 * oO0o
 def add_group ( self ) :
  lisp_group_mapping_list [ self . group_name ] = self
  if 74 - 74: I1IiiI
  if 39 - 39: iII111i * IiII / iII111i * IiII % I1ii11iIi11i
  if 27 - 27: iIii1I11I1II1 . ooOoO0o
  if 74 - 74: i1IIi % OoOoOO00
  if 98 - 98: IiII * OOooOOo / O0 - I1Ii111 . I1Ii111 + OOooOOo
  if 61 - 61: iII111i * Ii1I % Ii1I + I1IiiI
  if 23 - 23: oO0o + I1Ii111 / OoooooooOO / O0 + IiII
  if 80 - 80: i11iIiiIii - OoooooooOO + II111iiii / i1IIi - oO0o
  if 100 - 100: Ii1I
  if 73 - 73: IiII - O0
def lisp_is_group_more_specific ( group_str , group_mapping ) :
 IiIIi11i111 = group_mapping . group_prefix . instance_id
 oO00OO0Ooo00O = group_mapping . group_prefix . mask_len
 OOo0oOOO0 = lisp_address ( LISP_AFI_IPV4 , group_str , 32 , IiIIi11i111 )
 if ( OOo0oOOO0 . is_more_specific ( group_mapping . group_prefix ) ) : return ( oO00OO0Ooo00O )
 return ( - 1 )
 if 54 - 54: OOooOOo
 if 28 - 28: i1IIi - Oo0Ooo * OoO0O00 + OoooooooOO - Ii1I * i11iIiiIii
 if 71 - 71: iII111i - OOooOOo / iIii1I11I1II1 % i11iIiiIii
 if 39 - 39: o0oOOo0O0Ooo
 if 32 - 32: iIii1I11I1II1 . II111iiii / IiII % O0 / iII111i
 if 97 - 97: iIii1I11I1II1
 if 18 - 18: OOooOOo
def lisp_lookup_group ( group ) :
 IIII1 = None
 for Ooooo000 in lisp_group_mapping_list . values ( ) :
  oO00OO0Ooo00O = lisp_is_group_more_specific ( group , Ooooo000 )
  if ( oO00OO0Ooo00O == - 1 ) : continue
  if ( IIII1 == None or oO00OO0Ooo00O > IIII1 . group_prefix . mask_len ) : IIII1 = Ooooo000
  if 13 - 13: iIii1I11I1II1 - I1IiiI % o0oOOo0O0Ooo * iIii1I11I1II1
 return ( IIII1 )
 if 99 - 99: OoooooooOO / II111iiii . I1Ii111
 if 62 - 62: OOooOOo . iII111i . I1ii11iIi11i
lisp_site_flags = {
 "P" : "ETR is {}Requesting Map-Server to Proxy Map-Reply" ,
 "S" : "ETR is {}LISP-SEC capable" ,
 "I" : "xTR-ID and site-ID are {}included in Map-Register" ,
 "T" : "Use Map-Register TTL field to timeout registration is {}set" ,
 "R" : "Merging registrations are {}requested" ,
 "M" : "ETR is {}a LISP Mobile-Node" ,
 "N" : "ETR is {}requesting Map-Notify messages from Map-Server"
 }
if 23 - 23: O0
class lisp_site ( ) :
 def __init__ ( self ) :
  self . site_name = ""
  self . description = ""
  self . shutdown = False
  self . auth_sha1_or_sha2 = False
  self . auth_key = { }
  self . encryption_key = None
  self . allowed_prefixes = { }
  self . allowed_prefixes_sorted = [ ]
  self . allowed_rlocs = { }
  self . map_notifies_sent = 0
  self . map_notify_acks_received = 0
  if 33 - 33: ooOoO0o - iII111i % IiII
  if 67 - 67: II111iiii
  if 66 - 66: iIii1I11I1II1 / OOooOOo
class lisp_site_eid ( ) :
 def __init__ ( self , site ) :
  self . site = site
  self . eid = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . group = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . first_registered = 0
  self . last_registered = 0
  self . last_registerer = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . register_ttl = LISP_SITE_TIMEOUT_CHECK_INTERVAL * 3
  self . registered = False
  self . registered_rlocs = [ ]
  self . auth_sha1_or_sha2 = False
  self . individual_registrations = { }
  self . map_registers_received = 0
  self . proxy_reply_requested = False
  self . force_proxy_reply = False
  self . force_nat_proxy_reply = False
  self . force_ttl = None
  self . pitr_proxy_reply_drop = False
  self . proxy_reply_action = ""
  self . lisp_sec_present = False
  self . map_notify_requested = False
  self . mobile_node_requested = False
  self . echo_nonce_capable = False
  self . use_register_ttl_requested = False
  self . merge_register_requested = False
  self . xtr_id_present = False
  self . xtr_id = 0
  self . site_id = 0
  self . accept_more_specifics = False
  self . parent_for_more_specifics = None
  self . dynamic = False
  self . more_specific_registrations = [ ]
  self . source_cache = None
  self . inconsistent_registration = False
  self . policy = None
  self . require_signature = False
  self . encrypt_json = False
  if 65 - 65: IiII . oO0o + O0 - i11iIiiIii + iIii1I11I1II1
  if 82 - 82: iIii1I11I1II1 * iII111i + iIii1I11I1II1 / OoO0O00 + O0
 def print_eid_tuple ( self ) :
  return ( lisp_print_eid_tuple ( self . eid , self . group ) )
  if 67 - 67: I1Ii111
  if 94 - 94: I1Ii111 % iIii1I11I1II1 - II111iiii . ooOoO0o + i11iIiiIii - i11iIiiIii
 def print_flags ( self , html ) :
  if ( html == False ) :
   oOOO = "{}-{}-{}-{}-{}-{}-{}" . format ( "P" if self . proxy_reply_requested else "p" ,
   # I11i - Ii1I / OOooOOo . I1ii11iIi11i
 "S" if self . lisp_sec_present else "s" ,
 "I" if self . xtr_id_present else "i" ,
 "T" if self . use_register_ttl_requested else "t" ,
 "R" if self . merge_register_requested else "r" ,
 "M" if self . mobile_node_requested else "m" ,
 "N" if self . map_notify_requested else "n" )
  else :
   O0o0ooo00o00 = self . print_flags ( False )
   O0o0ooo00o00 = O0o0ooo00o00 . split ( "-" )
   oOOO = ""
   for iI1i1iI11I1i1 in O0o0ooo00o00 :
    IiiiiIIi1i1i = lisp_site_flags [ iI1i1iI11I1i1 . upper ( ) ]
    IiiiiIIi1i1i = IiiiiIIi1i1i . format ( "" if iI1i1iI11I1i1 . isupper ( ) else "not " )
    oOOO += lisp_span ( iI1i1iI11I1i1 , IiiiiIIi1i1i )
    if ( iI1i1iI11I1i1 . lower ( ) != "n" ) : oOOO += "-"
    if 64 - 64: OOooOOo . I1ii11iIi11i . IiII
    if 51 - 51: iII111i * I1Ii111 - I11i % iIii1I11I1II1 * o0oOOo0O0Ooo % I1IiiI
  return ( oOOO )
  if 5 - 5: OoO0O00
  if 10 - 10: o0oOOo0O0Ooo % OOooOOo / Ii1I . iIii1I11I1II1 % o0oOOo0O0Ooo + o0oOOo0O0Ooo
 def copy_state_to_parent ( self , child ) :
  self . xtr_id = child . xtr_id
  self . site_id = child . site_id
  self . first_registered = child . first_registered
  self . last_registered = child . last_registered
  self . last_registerer = child . last_registerer
  self . register_ttl = child . register_ttl
  if ( self . registered == False ) :
   self . first_registered = lisp_get_timestamp ( )
   if 63 - 63: i11iIiiIii
  self . auth_sha1_or_sha2 = child . auth_sha1_or_sha2
  self . registered = child . registered
  self . proxy_reply_requested = child . proxy_reply_requested
  self . lisp_sec_present = child . lisp_sec_present
  self . xtr_id_present = child . xtr_id_present
  self . use_register_ttl_requested = child . use_register_ttl_requested
  self . merge_register_requested = child . merge_register_requested
  self . mobile_node_requested = child . mobile_node_requested
  self . map_notify_requested = child . map_notify_requested
  if 34 - 34: OoooooooOO - O0 + ooOoO0o * I1IiiI
  if 75 - 75: OOooOOo % iII111i
 def build_sort_key ( self ) :
  iIiii1 = lisp_cache ( )
  iiIi , o0Oo = iIiii1 . build_key ( self . eid )
  IiIIIIii1i1 = ""
  if ( self . group . is_null ( ) == False ) :
   Oo0OO0oO , IiIIIIii1i1 = iIiii1 . build_key ( self . group )
   IiIIIIii1i1 = "-" + IiIIIIii1i1 [ 0 : 12 ] + "-" + str ( Oo0OO0oO ) + "-" + IiIIIIii1i1 [ 12 : : ]
   if 5 - 5: oO0o . I1IiiI + o0oOOo0O0Ooo
  o0Oo = o0Oo [ 0 : 12 ] + "-" + str ( iiIi ) + "-" + o0Oo [ 12 : : ] + IiIIIIii1i1
  del ( iIiii1 )
  return ( o0Oo )
  if 99 - 99: o0oOOo0O0Ooo . Oo0Ooo
  if 36 - 36: I1ii11iIi11i + II111iiii + oO0o / I1IiiI
 def merge_in_site_eid ( self , child ) :
  I11I1 = False
  if ( self . group . is_null ( ) ) :
   self . merge_rlocs_in_site_eid ( )
  else :
   I11I1 = self . merge_rles_in_site_eid ( )
   if 71 - 71: Ii1I % i11iIiiIii % I1IiiI + oO0o / OoooooooOO
   if 53 - 53: O0
   if 46 - 46: I1Ii111 * I1Ii111 - OoooooooOO * iIii1I11I1II1 - oO0o
   if 34 - 34: IiII + ooOoO0o . IiII * iII111i
   if 42 - 42: oO0o * I1IiiI
   if 65 - 65: ooOoO0o
  if ( child != None ) :
   self . copy_state_to_parent ( child )
   self . map_registers_received += 1
   if 88 - 88: OOooOOo - O0 % o0oOOo0O0Ooo + o0oOOo0O0Ooo % i11iIiiIii * I11i
  return ( I11I1 )
  if 34 - 34: I1IiiI % iIii1I11I1II1 . I1ii11iIi11i * Oo0Ooo * iIii1I11I1II1 / O0
  if 98 - 98: iII111i % IiII + OoO0O00
 def copy_rloc_records ( self ) :
  i11iI1iIiI = [ ]
  for oOO0O in self . registered_rlocs :
   i11iI1iIiI . append ( copy . deepcopy ( oOO0O ) )
   if 90 - 90: I1IiiI * II111iiii + O0
  return ( i11iI1iIiI )
  if 94 - 94: ooOoO0o * ooOoO0o + o0oOOo0O0Ooo . iII111i % iIii1I11I1II1 + Ii1I
  if 88 - 88: Oo0Ooo . iII111i
 def merge_rlocs_in_site_eid ( self ) :
  self . registered_rlocs = [ ]
  for oOoooo in self . individual_registrations . values ( ) :
   if ( self . site_id != oOoooo . site_id ) : continue
   if ( oOoooo . registered == False ) : continue
   self . registered_rlocs += oOoooo . copy_rloc_records ( )
   if 89 - 89: OOooOOo + I1Ii111 % i11iIiiIii + Oo0Ooo / Oo0Ooo + OoO0O00
   if 9 - 9: OoOoOO00 % i1IIi + IiII
   if 19 - 19: I1Ii111 - II111iiii / I1Ii111 + I1IiiI - OoooooooOO + o0oOOo0O0Ooo
   if 100 - 100: OoO0O00 / OoOoOO00 / OOooOOo / OoO0O00
   if 95 - 95: ooOoO0o
   if 95 - 95: Ii1I + i1IIi . I1IiiI % I1Ii111 / Ii1I * O0
  i11iI1iIiI = [ ]
  for oOO0O in self . registered_rlocs :
   if ( oOO0O . rloc . is_null ( ) or len ( i11iI1iIiI ) == 0 ) :
    i11iI1iIiI . append ( oOO0O )
    continue
    if 68 - 68: I1Ii111 - IiII - oO0o - Oo0Ooo - o0oOOo0O0Ooo
   for iIiI111i1i1 in i11iI1iIiI :
    if ( iIiI111i1i1 . rloc . is_null ( ) ) : continue
    if ( oOO0O . rloc . is_exact_match ( iIiI111i1i1 . rloc ) ) : break
    if 88 - 88: II111iiii / o0oOOo0O0Ooo
   if ( iIiI111i1i1 == i11iI1iIiI [ - 1 ] ) : i11iI1iIiI . append ( oOO0O )
   if 44 - 44: I1Ii111 + ooOoO0o
  self . registered_rlocs = i11iI1iIiI
  if 15 - 15: I11i + OoO0O00 + OoOoOO00
  if 100 - 100: I1Ii111
  if 78 - 78: OoOoOO00
  if 16 - 16: I1Ii111 % OoO0O00 - OoO0O00 % OoOoOO00 * OoO0O00
  if ( len ( self . registered_rlocs ) == 0 ) : self . registered = False
  return
  if 36 - 36: OoOoOO00 * II111iiii . OoooooooOO * I11i . I11i
  if 13 - 13: I1ii11iIi11i * II111iiii
 def merge_rles_in_site_eid ( self ) :
  if 93 - 93: OOooOOo / O0 - o0oOOo0O0Ooo + OoO0O00 * I1IiiI
  if 53 - 53: I1ii11iIi11i
  if 91 - 91: o0oOOo0O0Ooo - I1ii11iIi11i . i1IIi
  if 64 - 64: ooOoO0o
  iIIiI1i1iIIIII = { }
  for oOO0O in self . registered_rlocs :
   if ( oOO0O . rle == None ) : continue
   for IiioOoo in oOO0O . rle . rle_nodes :
    o0o00O0oOooO0 = IiioOoo . address . print_address_no_iid ( )
    iIIiI1i1iIIIII [ o0o00O0oOooO0 ] = IiioOoo . address
    if 19 - 19: oO0o - I1ii11iIi11i + iII111i . o0oOOo0O0Ooo . OoO0O00 * Oo0Ooo
   break
   if 39 - 39: i11iIiiIii - iII111i / O0 % Oo0Ooo
   if 40 - 40: O0 * Oo0Ooo % o0oOOo0O0Ooo / OoooooooOO
   if 94 - 94: iII111i
   if 79 - 79: o0oOOo0O0Ooo / I1ii11iIi11i . iII111i . II111iiii + I1ii11iIi11i * I11i
   if 49 - 49: Ii1I * OoooooooOO * i1IIi % OoOoOO00
  self . merge_rlocs_in_site_eid ( )
  if 83 - 83: iIii1I11I1II1 - i1IIi - Ii1I % iII111i
  if 69 - 69: I1Ii111 * oO0o * I1IiiI
  if 74 - 74: O0 / I11i . Oo0Ooo / I11i % OoO0O00 % o0oOOo0O0Ooo
  if 83 - 83: OoO0O00 - i11iIiiIii + iIii1I11I1II1
  if 52 - 52: OoooooooOO
  if 44 - 44: O0 / OoooooooOO + ooOoO0o * I1ii11iIi11i
  if 36 - 36: I1ii11iIi11i / OoO0O00 - oO0o % O0
  if 12 - 12: i1IIi * ooOoO0o / oO0o + I1IiiI / OoooooooOO
  oOO0 = [ ]
  for oOO0O in self . registered_rlocs :
   if ( self . registered_rlocs . index ( oOO0O ) == 0 ) :
    oOO0 . append ( oOO0O )
    continue
    if 18 - 18: I1IiiI / O0 . OoO0O00 - OoooooooOO + Ii1I - Ii1I
   if ( oOO0O . rle == None ) : oOO0 . append ( oOO0O )
   if 67 - 67: II111iiii . Ii1I + I1IiiI
  self . registered_rlocs = oOO0
  if 77 - 77: O0 % I1ii11iIi11i + i11iIiiIii . OOooOOo % o0oOOo0O0Ooo + OoO0O00
  if 31 - 31: ooOoO0o * I1ii11iIi11i
  if 23 - 23: OoOoOO00 - I11i . iIii1I11I1II1
  if 87 - 87: OoO0O00 - i11iIiiIii / O0 % OOooOOo % OOooOOo * i1IIi
  if 18 - 18: IiII
  if 50 - 50: i1IIi / o0oOOo0O0Ooo * OoO0O00
  if 98 - 98: I11i . II111iiii
  iI1Ii11 = lisp_rle ( "" )
  iI11ii1i = { }
  IIiiI11iI = None
  for oOoooo in self . individual_registrations . values ( ) :
   if ( oOoooo . registered == False ) : continue
   oOOooooOOOo = oOoooo . registered_rlocs [ 0 ] . rle
   if ( oOOooooOOOo == None ) : continue
   if 98 - 98: Oo0Ooo * ooOoO0o * I11i + oO0o - O0
   IIiiI11iI = oOoooo . registered_rlocs [ 0 ] . rloc_name
   for iiIII11 in oOOooooOOOo . rle_nodes :
    o0o00O0oOooO0 = iiIII11 . address . print_address_no_iid ( )
    if ( iI11ii1i . has_key ( o0o00O0oOooO0 ) ) : break
    if 27 - 27: o0oOOo0O0Ooo + Oo0Ooo * II111iiii + IiII
    IiioOoo = lisp_rle_node ( )
    IiioOoo . address . copy_address ( iiIII11 . address )
    IiioOoo . level = iiIII11 . level
    IiioOoo . rloc_name = IIiiI11iI
    iI1Ii11 . rle_nodes . append ( IiioOoo )
    iI11ii1i [ o0o00O0oOooO0 ] = iiIII11 . address
    if 76 - 76: I1ii11iIi11i / o0oOOo0O0Ooo + oO0o * i11iIiiIii / II111iiii
    if 86 - 86: Ii1I
    if 69 - 69: oO0o % o0oOOo0O0Ooo / o0oOOo0O0Ooo
    if 1 - 1: Ii1I
    if 43 - 43: o0oOOo0O0Ooo
    if 78 - 78: I1Ii111 % i1IIi * I11i
  if ( len ( iI1Ii11 . rle_nodes ) == 0 ) : iI1Ii11 = None
  if ( len ( self . registered_rlocs ) != 0 ) :
   self . registered_rlocs [ 0 ] . rle = iI1Ii11
   if ( IIiiI11iI ) : self . registered_rlocs [ 0 ] . rloc_name = None
   if 59 - 59: OoOoOO00 % OoO0O00 % i11iIiiIii . II111iiii % I1ii11iIi11i + i1IIi
   if 99 - 99: I11i + IiII * I1Ii111 - OOooOOo - i1IIi
   if 77 - 77: I11i . IiII / OoO0O00 / I1Ii111
   if 8 - 8: o0oOOo0O0Ooo + iII111i / OoO0O00 * ooOoO0o - oO0o . iII111i
   if 32 - 32: OoooooooOO . I1Ii111 - I1ii11iIi11i
  if ( iIIiI1i1iIIIII . keys ( ) == iI11ii1i . keys ( ) ) : return ( False )
  if 29 - 29: OoO0O00
  lprint ( "{} {} from {} to {}" . format ( green ( self . print_eid_tuple ( ) , False ) , bold ( "RLE change" , False ) ,
  # OOooOOo / I1ii11iIi11i
 iIIiI1i1iIIIII . keys ( ) , iI11ii1i . keys ( ) ) )
  if 10 - 10: IiII + o0oOOo0O0Ooo + I11i % O0 % I1Ii111
  return ( True )
  if 85 - 85: O0 % OoOoOO00 . I1ii11iIi11i
  if 46 - 46: OOooOOo * iIii1I11I1II1
 def add_cache ( self ) :
  if ( self . group . is_null ( ) ) :
   lisp_sites_by_eid . add_cache ( self . eid , self )
  else :
   iIiIi1I = lisp_sites_by_eid . lookup_cache ( self . group , True )
   if ( iIiIi1I == None ) :
    iIiIi1I = lisp_site_eid ( self . site )
    iIiIi1I . eid . copy_address ( self . group )
    iIiIi1I . group . copy_address ( self . group )
    lisp_sites_by_eid . add_cache ( self . group , iIiIi1I )
    if 33 - 33: OoO0O00 * II111iiii / i1IIi
    if 93 - 93: I1Ii111 % I11i
    if 64 - 64: I1IiiI % OoOoOO00 / Oo0Ooo
    if 40 - 40: Ii1I + iIii1I11I1II1 / oO0o . II111iiii % O0 - IiII
    if 49 - 49: IiII - OOooOOo * OOooOOo . O0
    iIiIi1I . parent_for_more_specifics = self . parent_for_more_specifics
    if 60 - 60: OoOoOO00 % iIii1I11I1II1 + IiII % o0oOOo0O0Ooo
   if ( self . eid . is_null ( ) ) : self . eid . make_default_route ( iIiIi1I . group )
   iIiIi1I . add_source_entry ( self )
   if 64 - 64: OoOoOO00 * I1ii11iIi11i . OoooooooOO . i1IIi
   if 61 - 61: OoO0O00
   if 100 - 100: OoOoOO00
 def delete_cache ( self ) :
  if ( self . group . is_null ( ) ) :
   lisp_sites_by_eid . delete_cache ( self . eid )
  else :
   iIiIi1I = lisp_sites_by_eid . lookup_cache ( self . group , True )
   if ( iIiIi1I == None ) : return
   if 97 - 97: OoooooooOO
   oOoooo = iIiIi1I . lookup_source_cache ( self . eid , True )
   if ( oOoooo == None ) : return
   if 91 - 91: o0oOOo0O0Ooo / O0 % OoO0O00
   if ( iIiIi1I . source_cache == None ) : return
   if 35 - 35: iII111i % OoO0O00 * O0
   iIiIi1I . source_cache . delete_cache ( self . eid )
   if ( iIiIi1I . source_cache . cache_size ( ) == 0 ) :
    lisp_sites_by_eid . delete_cache ( self . group )
    if 37 - 37: OOooOOo
    if 100 - 100: Oo0Ooo * I1IiiI . ooOoO0o
    if 53 - 53: OOooOOo + o0oOOo0O0Ooo * Ii1I + O0
    if 75 - 75: OoooooooOO
 def add_source_entry ( self , source_se ) :
  if ( self . source_cache == None ) : self . source_cache = lisp_cache ( )
  self . source_cache . add_cache ( source_se . eid , source_se )
  if 24 - 24: I1Ii111 % i11iIiiIii % oO0o . OOooOOo % IiII
  if 23 - 23: o0oOOo0O0Ooo * II111iiii - Oo0Ooo - I1IiiI
 def lookup_source_cache ( self , source , exact ) :
  if ( self . source_cache == None ) : return ( None )
  return ( self . source_cache . lookup_cache ( source , exact ) )
  if 86 - 86: I1IiiI - II111iiii * II111iiii * oO0o % OoooooooOO * OoOoOO00
  if 93 - 93: I1IiiI + OoO0O00 % O0 - ooOoO0o * i1IIi
 def is_star_g ( self ) :
  if ( self . group . is_null ( ) ) : return ( False )
  return ( self . eid . is_exact_match ( self . group ) )
  if 60 - 60: I1IiiI
  if 9 - 9: I11i % i1IIi / ooOoO0o % iII111i - oO0o - II111iiii
 def eid_record_matches ( self , eid_record ) :
  if ( self . eid . is_exact_match ( eid_record . eid ) == False ) : return ( False )
  if ( eid_record . group . is_null ( ) ) : return ( True )
  return ( eid_record . group . is_exact_match ( self . group ) )
  if 29 - 29: ooOoO0o . II111iiii . i1IIi % oO0o
  if 11 - 11: OoOoOO00 . OoO0O00 % I11i * iII111i % I1Ii111 . O0
 def inherit_from_ams_parent ( self ) :
  O0Ii1IiiiI = self . parent_for_more_specifics
  if ( O0Ii1IiiiI == None ) : return
  self . force_proxy_reply = O0Ii1IiiiI . force_proxy_reply
  self . force_nat_proxy_reply = O0Ii1IiiiI . force_nat_proxy_reply
  self . force_ttl = O0Ii1IiiiI . force_ttl
  self . pitr_proxy_reply_drop = O0Ii1IiiiI . pitr_proxy_reply_drop
  self . proxy_reply_action = O0Ii1IiiiI . proxy_reply_action
  self . echo_nonce_capable = O0Ii1IiiiI . echo_nonce_capable
  self . policy = O0Ii1IiiiI . policy
  self . require_signature = O0Ii1IiiiI . require_signature
  self . encrypt_json = O0Ii1IiiiI . encrypt_json
  if 17 - 17: OOooOOo / i11iIiiIii - i11iIiiIii . II111iiii . ooOoO0o
  if 38 - 38: OOooOOo . OoooooooOO . II111iiii + OoO0O00 / oO0o . OoooooooOO
 def rtrs_in_rloc_set ( self ) :
  for oOO0O in self . registered_rlocs :
   if ( oOO0O . is_rtr ( ) ) : return ( True )
   if 100 - 100: OoO0O00
  return ( False )
  if 36 - 36: oO0o + Ii1I - O0
  if 19 - 19: O0 + I1Ii111 . I1Ii111 * IiII * ooOoO0o + i1IIi
 def is_rtr_in_rloc_set ( self , rtr_rloc ) :
  for oOO0O in self . registered_rlocs :
   if ( oOO0O . rloc . is_exact_match ( rtr_rloc ) == False ) : continue
   if ( oOO0O . is_rtr ( ) ) : return ( True )
   if 51 - 51: ooOoO0o % OoOoOO00 % i1IIi / O0
  return ( False )
  if 11 - 11: OOooOOo . I1ii11iIi11i * OOooOOo * OoO0O00
  if 11 - 11: I11i
 def is_rloc_in_rloc_set ( self , rloc ) :
  for oOO0O in self . registered_rlocs :
   if ( oOO0O . rle ) :
    for iI1Ii11 in oOO0O . rle . rle_nodes :
     if ( iI1Ii11 . address . is_exact_match ( rloc ) ) : return ( True )
     if 85 - 85: OoOoOO00 - Ii1I / Oo0Ooo % I1ii11iIi11i
     if 12 - 12: i1IIi + o0oOOo0O0Ooo / oO0o . O0
   if ( oOO0O . rloc . is_exact_match ( rloc ) ) : return ( True )
   if 37 - 37: IiII
  return ( False )
  if 99 - 99: i11iIiiIii % i11iIiiIii . I11i * I1ii11iIi11i . OoO0O00 / I1IiiI
  if 44 - 44: iII111i - OoO0O00 / i11iIiiIii
 def do_rloc_sets_match ( self , prev_rloc_set ) :
  if ( len ( self . registered_rlocs ) != len ( prev_rloc_set ) ) : return ( False )
  if 55 - 55: O0 * OoO0O00 * i1IIi
  for oOO0O in prev_rloc_set :
   OOO00O0O000 = oOO0O . rloc
   if ( self . is_rloc_in_rloc_set ( OOO00O0O000 ) == False ) : return ( False )
   if 9 - 9: IiII
  return ( True )
  if 64 - 64: ooOoO0o + OoooooooOO
  if 99 - 99: iIii1I11I1II1 * II111iiii * i11iIiiIii
  if 10 - 10: OOooOOo
class lisp_mr ( ) :
 def __init__ ( self , addr_str , dns_name , mr_name ) :
  self . mr_name = mr_name if ( mr_name != None ) else "all"
  self . dns_name = dns_name
  self . map_resolver = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . last_dns_resolve = None
  self . a_record_index = 0
  if ( addr_str ) :
   self . map_resolver . store_address ( addr_str )
   self . insert_mr ( )
  else :
   self . resolve_dns_name ( )
   if 75 - 75: I11i * ooOoO0o * Oo0Ooo . i1IIi . ooOoO0o . ooOoO0o
  self . last_used = 0
  self . last_reply = 0
  self . last_nonce = 0
  self . map_requests_sent = 0
  self . neg_map_replies_received = 0
  self . total_rtt = 0
  if 24 - 24: iIii1I11I1II1
  if 72 - 72: i11iIiiIii + o0oOOo0O0Ooo % ooOoO0o * I1ii11iIi11i . i1IIi
 def resolve_dns_name ( self ) :
  if ( self . dns_name == None ) : return
  if ( self . last_dns_resolve and
 time . time ( ) - self . last_dns_resolve < 30 ) : return
  if 59 - 59: OoooooooOO - OoooooooOO - o0oOOo0O0Ooo + i1IIi % I1Ii111
  try :
   IIiiI = socket . gethostbyname_ex ( self . dns_name )
   self . last_dns_resolve = lisp_get_timestamp ( )
   o0OooOoOO0ooO = IIiiI [ 2 ]
  except :
   return
   if 20 - 20: o0oOOo0O0Ooo
   if 65 - 65: OOooOOo / OoOoOO00
   if 31 - 31: OoOoOO00 * I1IiiI + i11iIiiIii % OOooOOo * OoOoOO00
   if 36 - 36: I1Ii111 * OoO0O00
   if 84 - 84: OoOoOO00
   if 80 - 80: oO0o
  if ( len ( o0OooOoOO0ooO ) <= self . a_record_index ) :
   self . delete_mr ( )
   return
   if 59 - 59: iIii1I11I1II1 / IiII % I1ii11iIi11i + OoO0O00 - I11i % OOooOOo
   if 92 - 92: iII111i
  o0o00O0oOooO0 = o0OooOoOO0ooO [ self . a_record_index ]
  if ( o0o00O0oOooO0 != self . map_resolver . print_address_no_iid ( ) ) :
   self . delete_mr ( )
   self . map_resolver . store_address ( o0o00O0oOooO0 )
   self . insert_mr ( )
   if 96 - 96: OoOoOO00 / OoOoOO00 / OoOoOO00 + OoooooooOO + Oo0Ooo
   if 91 - 91: OoOoOO00 + II111iiii / I11i * iIii1I11I1II1
   if 92 - 92: I1Ii111 - IiII / IiII
   if 42 - 42: IiII
   if 7 - 7: iIii1I11I1II1
   if 35 - 35: IiII + O0 % I1Ii111 - I1ii11iIi11i - i1IIi
  if ( lisp_is_decent_dns_suffix ( self . dns_name ) == False ) : return
  if ( self . a_record_index != 0 ) : return
  if 100 - 100: I1Ii111 + i11iIiiIii - IiII / I1ii11iIi11i / iII111i
  for o0o00O0oOooO0 in o0OooOoOO0ooO [ 1 : : ] :
   oO0OO = lisp_address ( LISP_AFI_NONE , o0o00O0oOooO0 , 0 , 0 )
   I1III11iIIIi = lisp_get_map_resolver ( oO0OO , None )
   if ( I1III11iIIIi != None and I1III11iIIIi . a_record_index == o0OooOoOO0ooO . index ( o0o00O0oOooO0 ) ) :
    continue
    if 56 - 56: iII111i
   I1III11iIIIi = lisp_mr ( o0o00O0oOooO0 , None , None )
   I1III11iIIIi . a_record_index = o0OooOoOO0ooO . index ( o0o00O0oOooO0 )
   I1III11iIIIi . dns_name = self . dns_name
   I1III11iIIIi . last_dns_resolve = lisp_get_timestamp ( )
   if 91 - 91: Oo0Ooo . I11i . I1ii11iIi11i
   if 60 - 60: i11iIiiIii - OOooOOo
   if 78 - 78: I1IiiI * ooOoO0o % iIii1I11I1II1 / I1ii11iIi11i
   if 61 - 61: I1Ii111 . Ii1I + OoooooooOO
   if 98 - 98: OOooOOo . ooOoO0o . OoOoOO00 - I1Ii111 . i1IIi - iIii1I11I1II1
  ooOOoOOo00O0o = [ ]
  for I1III11iIIIi in lisp_map_resolvers_list . values ( ) :
   if ( self . dns_name != I1III11iIIIi . dns_name ) : continue
   oO0OO = I1III11iIIIi . map_resolver . print_address_no_iid ( )
   if ( oO0OO in o0OooOoOO0ooO ) : continue
   ooOOoOOo00O0o . append ( I1III11iIIIi )
   if 99 - 99: II111iiii
  for I1III11iIIIi in ooOOoOOo00O0o : I1III11iIIIi . delete_mr ( )
  if 75 - 75: iIii1I11I1II1 - Oo0Ooo - OoOoOO00 % I1ii11iIi11i . II111iiii
  if 11 - 11: I1ii11iIi11i - I1ii11iIi11i . ooOoO0o * Oo0Ooo + I1Ii111
 def insert_mr ( self ) :
  o0Oo = self . mr_name + self . map_resolver . print_address ( )
  lisp_map_resolvers_list [ o0Oo ] = self
  if 59 - 59: iII111i - OOooOOo - OoO0O00 . I1IiiI % o0oOOo0O0Ooo + iII111i
  if 10 - 10: iIii1I11I1II1 - Ii1I
 def delete_mr ( self ) :
  o0Oo = self . mr_name + self . map_resolver . print_address ( )
  if ( lisp_map_resolvers_list . has_key ( o0Oo ) == False ) : return
  lisp_map_resolvers_list . pop ( o0Oo )
  if 84 - 84: iII111i
  if 21 - 21: i11iIiiIii
  if 30 - 30: OoO0O00 + OoooooooOO
class lisp_ddt_root ( ) :
 def __init__ ( self ) :
  self . root_address = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . public_key = ""
  self . priority = 0
  self . weight = 0
  if 98 - 98: I1ii11iIi11i % I1IiiI
  if 9 - 9: o0oOOo0O0Ooo / I1Ii111 % i1IIi - OOooOOo % I1IiiI / I1ii11iIi11i
  if 66 - 66: IiII
class lisp_referral ( ) :
 def __init__ ( self ) :
  self . eid = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . group = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . referral_set = { }
  self . referral_type = LISP_DDT_ACTION_NULL
  self . referral_source = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . referral_ttl = 0
  self . uptime = lisp_get_timestamp ( )
  self . expires = 0
  self . source_cache = None
  if 56 - 56: oO0o + OoooooooOO
  if 75 - 75: O0 % Ii1I
 def print_referral ( self , eid_indent , referral_indent ) :
  IiIiiIiii = lisp_print_elapsed ( self . uptime )
  IiiI1iiiI1Ii1Ii = lisp_print_future ( self . expires )
  lprint ( "{}Referral EID {}, uptime/expires {}/{}, {} referrals:" . format ( eid_indent , green ( self . eid . print_prefix ( ) , False ) , IiIiiIiii ,
  # oO0o
 IiiI1iiiI1Ii1Ii , len ( self . referral_set ) ) )
  if 75 - 75: OoO0O00 % I1Ii111 * O0 . oO0o + I1IiiI
  for iiI111I in self . referral_set . values ( ) :
   iiI111I . print_ref_node ( referral_indent )
   if 91 - 91: I1IiiI
   if 6 - 6: O0 - OoOoOO00 - i11iIiiIii / iII111i
   if 63 - 63: OOooOOo
 def print_referral_type ( self ) :
  if ( self . eid . afi == LISP_AFI_ULTIMATE_ROOT ) : return ( "root" )
  if ( self . referral_type == LISP_DDT_ACTION_NULL ) :
   return ( "null-referral" )
   if 84 - 84: i11iIiiIii * iIii1I11I1II1 % I11i % iII111i + OoooooooOO . o0oOOo0O0Ooo
  if ( self . referral_type == LISP_DDT_ACTION_SITE_NOT_FOUND ) :
   return ( "no-site-action" )
   if 78 - 78: o0oOOo0O0Ooo . iII111i + O0 / I1ii11iIi11i + I1ii11iIi11i + II111iiii
  if ( self . referral_type > LISP_DDT_ACTION_MAX ) :
   return ( "invalid-action" )
   if 96 - 96: iIii1I11I1II1 * II111iiii . iIii1I11I1II1
  return ( lisp_map_referral_action_string [ self . referral_type ] )
  if 13 - 13: Ii1I - OoOoOO00 . Ii1I
  if 7 - 7: Ii1I - I11i / I1ii11iIi11i + iII111i
 def print_eid_tuple ( self ) :
  return ( lisp_print_eid_tuple ( self . eid , self . group ) )
  if 47 - 47: I11i * IiII / oO0o - OoooooooOO . OoooooooOO / I11i
  if 73 - 73: Ii1I . IiII % IiII
 def print_ttl ( self ) :
  Oo0o0 = self . referral_ttl
  if ( Oo0o0 < 60 ) : return ( str ( Oo0o0 ) + " secs" )
  if 56 - 56: I1Ii111 + iII111i + iII111i
  if ( ( Oo0o0 % 60 ) == 0 ) :
   Oo0o0 = str ( Oo0o0 / 60 ) + " mins"
  else :
   Oo0o0 = str ( Oo0o0 ) + " secs"
   if 99 - 99: o0oOOo0O0Ooo % I1ii11iIi11i / Oo0Ooo . O0 + OoO0O00 * OoOoOO00
  return ( Oo0o0 )
  if 48 - 48: iIii1I11I1II1 + O0 * I11i * i11iIiiIii . Ii1I / i1IIi
  if 48 - 48: i1IIi % iIii1I11I1II1 + I1IiiI - OoOoOO00 % I11i . I1Ii111
 def is_referral_negative ( self ) :
  return ( self . referral_type in ( LISP_DDT_ACTION_MS_NOT_REG , LISP_DDT_ACTION_DELEGATION_HOLE ,
  # IiII - OoO0O00 * iII111i . I1IiiI
 LISP_DDT_ACTION_NOT_AUTH ) )
  if 27 - 27: I11i / o0oOOo0O0Ooo / II111iiii
  if 93 - 93: II111iiii - I11i
 def add_cache ( self ) :
  if ( self . group . is_null ( ) ) :
   lisp_referral_cache . add_cache ( self . eid , self )
  else :
   IiII111IiII1 = lisp_referral_cache . lookup_cache ( self . group , True )
   if ( IiII111IiII1 == None ) :
    IiII111IiII1 = lisp_referral ( )
    IiII111IiII1 . eid . copy_address ( self . group )
    IiII111IiII1 . group . copy_address ( self . group )
    lisp_referral_cache . add_cache ( self . group , IiII111IiII1 )
    if 17 - 17: i1IIi + O0 * ooOoO0o
   if ( self . eid . is_null ( ) ) : self . eid . make_default_route ( IiII111IiII1 . group )
   IiII111IiII1 . add_source_entry ( self )
   if 53 - 53: IiII / II111iiii / oO0o % O0 / I1Ii111
   if 91 - 91: oO0o * OoOoOO00 + O0 % Oo0Ooo
   if 62 - 62: iIii1I11I1II1 - i11iIiiIii % iIii1I11I1II1 . ooOoO0o / OOooOOo * OoOoOO00
 def delete_cache ( self ) :
  if ( self . group . is_null ( ) ) :
   lisp_referral_cache . delete_cache ( self . eid )
  else :
   IiII111IiII1 = lisp_referral_cache . lookup_cache ( self . group , True )
   if ( IiII111IiII1 == None ) : return
   if 45 - 45: OOooOOo - OOooOOo % iII111i - IiII . O0
   OOoOoOO = IiII111IiII1 . lookup_source_cache ( self . eid , True )
   if ( OOoOoOO == None ) : return
   if 6 - 6: iIii1I11I1II1 * II111iiii / O0 % IiII - I1Ii111
   IiII111IiII1 . source_cache . delete_cache ( self . eid )
   if ( IiII111IiII1 . source_cache . cache_size ( ) == 0 ) :
    lisp_referral_cache . delete_cache ( self . group )
    if 64 - 64: ooOoO0o
    if 28 - 28: i11iIiiIii - IiII * I1ii11iIi11i + IiII * iII111i
    if 75 - 75: o0oOOo0O0Ooo * OoOoOO00 % I1ii11iIi11i + OOooOOo . II111iiii
    if 12 - 12: ooOoO0o
 def add_source_entry ( self , source_ref ) :
  if ( self . source_cache == None ) : self . source_cache = lisp_cache ( )
  self . source_cache . add_cache ( source_ref . eid , source_ref )
  if 83 - 83: I1Ii111 % ooOoO0o + OoooooooOO
  if 50 - 50: i11iIiiIii % I1IiiI * iII111i / Ii1I
 def lookup_source_cache ( self , source , exact ) :
  if ( self . source_cache == None ) : return ( None )
  return ( self . source_cache . lookup_cache ( source , exact ) )
  if 12 - 12: iII111i / OoO0O00 - II111iiii + Oo0Ooo
  if 78 - 78: i1IIi
  if 25 - 25: Ii1I * II111iiii / OoOoOO00
class lisp_referral_node ( ) :
 def __init__ ( self ) :
  self . referral_address = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . priority = 0
  self . weight = 0
  self . updown = True
  self . map_requests_sent = 0
  self . no_responses = 0
  self . uptime = lisp_get_timestamp ( )
  if 86 - 86: i1IIi + I1IiiI + I1Ii111 % II111iiii . IiII - iIii1I11I1II1
  if 54 - 54: i11iIiiIii . Ii1I % I1IiiI . I1Ii111 . OoooooooOO
 def print_ref_node ( self , indent ) :
  i1 = lisp_print_elapsed ( self . uptime )
  lprint ( "{}referral {}, uptime {}, {}, priority/weight: {}/{}" . format ( indent , red ( self . referral_address . print_address ( ) , False ) , i1 ,
  # Ii1I * I1ii11iIi11i % I11i
 "up" if self . updown else "down" , self . priority , self . weight ) )
  if 50 - 50: Ii1I . I1ii11iIi11i + iIii1I11I1II1 * i11iIiiIii . iII111i
  if 47 - 47: o0oOOo0O0Ooo * oO0o % I1ii11iIi11i
  if 59 - 59: IiII
class lisp_ms ( ) :
 def __init__ ( self , addr_str , dns_name , ms_name , alg_id , key_id , pw , pr ,
 mr , rr , wmn , site_id , ekey_id , ekey ) :
  self . ms_name = ms_name if ( ms_name != None ) else "all"
  self . dns_name = dns_name
  self . map_server = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . last_dns_resolve = None
  self . a_record_index = 0
  if ( lisp_map_servers_list == { } ) :
   self . xtr_id = lisp_get_control_nonce ( )
  else :
   self . xtr_id = lisp_map_servers_list . values ( ) [ 0 ] . xtr_id
   if 22 - 22: i11iIiiIii . oO0o * OoOoOO00 . OoooooooOO
  self . alg_id = alg_id
  self . key_id = key_id
  self . password = pw
  self . proxy_reply = pr
  self . merge_registrations = mr
  self . refresh_registrations = rr
  self . want_map_notify = wmn
  self . site_id = site_id
  self . map_registers_sent = 0
  self . map_registers_multicast_sent = 0
  self . map_notifies_received = 0
  self . map_notify_acks_sent = 0
  self . ekey_id = ekey_id
  self . ekey = ekey
  if ( addr_str ) :
   self . map_server . store_address ( addr_str )
   self . insert_ms ( )
  else :
   self . resolve_dns_name ( )
   if 100 - 100: I1Ii111 + O0
   if 69 - 69: I11i + OoO0O00 + o0oOOo0O0Ooo - o0oOOo0O0Ooo - Ii1I
   if 24 - 24: i11iIiiIii + I11i . O0
 def resolve_dns_name ( self ) :
  if ( self . dns_name == None ) : return
  if ( self . last_dns_resolve and
 time . time ( ) - self . last_dns_resolve < 30 ) : return
  if 96 - 96: OoOoOO00 . I1ii11iIi11i - oO0o
  try :
   IIiiI = socket . gethostbyname_ex ( self . dns_name )
   self . last_dns_resolve = lisp_get_timestamp ( )
   o0OooOoOO0ooO = IIiiI [ 2 ]
  except :
   return
   if 81 - 81: iII111i - II111iiii * O0
   if 55 - 55: II111iiii * i1IIi
   if 7 - 7: OOooOOo - I1ii11iIi11i * O0 * iIii1I11I1II1 + OoO0O00 / I11i
   if 25 - 25: OoooooooOO . O0 % OoO0O00
   if 52 - 52: i11iIiiIii
   if 97 - 97: Oo0Ooo % IiII
  if ( len ( o0OooOoOO0ooO ) <= self . a_record_index ) :
   self . delete_ms ( )
   return
   if 24 - 24: iIii1I11I1II1
   if 97 - 97: o0oOOo0O0Ooo - iIii1I11I1II1 + I1Ii111 / ooOoO0o + Ii1I
  o0o00O0oOooO0 = o0OooOoOO0ooO [ self . a_record_index ]
  if ( o0o00O0oOooO0 != self . map_server . print_address_no_iid ( ) ) :
   self . delete_ms ( )
   self . map_server . store_address ( o0o00O0oOooO0 )
   self . insert_ms ( )
   if 22 - 22: oO0o + O0 + I11i . OoO0O00 - II111iiii
   if 20 - 20: Ii1I * I1Ii111 . I1IiiI % OoOoOO00 / OoO0O00 % II111iiii
   if 43 - 43: IiII + II111iiii + oO0o / I1ii11iIi11i % i1IIi - OoO0O00
   if 59 - 59: Oo0Ooo + O0 + iII111i
   if 71 - 71: IiII - OoO0O00
   if 90 - 90: Oo0Ooo
  if ( lisp_is_decent_dns_suffix ( self . dns_name ) == False ) : return
  if ( self . a_record_index != 0 ) : return
  if 83 - 83: iIii1I11I1II1 % ooOoO0o % OOooOOo * i1IIi - o0oOOo0O0Ooo * i1IIi
  for o0o00O0oOooO0 in o0OooOoOO0ooO [ 1 : : ] :
   oO0OO = lisp_address ( LISP_AFI_NONE , o0o00O0oOooO0 , 0 , 0 )
   ii1i = lisp_get_map_server ( oO0OO )
   if ( ii1i != None and ii1i . a_record_index == o0OooOoOO0ooO . index ( o0o00O0oOooO0 ) ) :
    continue
    if 60 - 60: Ii1I . I1ii11iIi11i - I11i + i11iIiiIii / iII111i
   ii1i = copy . deepcopy ( self )
   ii1i . map_server . store_address ( o0o00O0oOooO0 )
   ii1i . a_record_index = o0OooOoOO0ooO . index ( o0o00O0oOooO0 )
   ii1i . last_dns_resolve = lisp_get_timestamp ( )
   ii1i . insert_ms ( )
   if 9 - 9: I1Ii111 . oO0o . OoO0O00 / IiII - oO0o / oO0o
   if 50 - 50: II111iiii + OoOoOO00
   if 17 - 17: ooOoO0o + I1ii11iIi11i
   if 34 - 34: Ii1I / II111iiii + OoOoOO00 . II111iiii + OoooooooOO * o0oOOo0O0Ooo
   if 48 - 48: O0
  ooOOoOOo00O0o = [ ]
  for ii1i in lisp_map_servers_list . values ( ) :
   if ( self . dns_name != ii1i . dns_name ) : continue
   oO0OO = ii1i . map_server . print_address_no_iid ( )
   if ( oO0OO in o0OooOoOO0ooO ) : continue
   ooOOoOOo00O0o . append ( ii1i )
   if 99 - 99: II111iiii * oO0o / I1ii11iIi11i - i1IIi
  for ii1i in ooOOoOOo00O0o : ii1i . delete_ms ( )
  if 84 - 84: i11iIiiIii . OoooooooOO
  if 69 - 69: I1Ii111 * II111iiii % I1Ii111 * i11iIiiIii . ooOoO0o / Oo0Ooo
 def insert_ms ( self ) :
  o0Oo = self . ms_name + self . map_server . print_address ( )
  lisp_map_servers_list [ o0Oo ] = self
  if 5 - 5: Ii1I
  if 19 - 19: oO0o
 def delete_ms ( self ) :
  o0Oo = self . ms_name + self . map_server . print_address ( )
  if ( lisp_map_servers_list . has_key ( o0Oo ) == False ) : return
  lisp_map_servers_list . pop ( o0Oo )
  if 61 - 61: OoOoOO00 + iIii1I11I1II1 / I1ii11iIi11i - i1IIi
  if 11 - 11: oO0o * o0oOOo0O0Ooo . I1IiiI
  if 12 - 12: I1IiiI % OoO0O00 / I1Ii111 / O0 % o0oOOo0O0Ooo
class lisp_interface ( ) :
 def __init__ ( self , device ) :
  self . interface_name = ""
  self . device = device
  self . instance_id = None
  self . bridge_socket = None
  self . raw_socket = None
  self . dynamic_eid = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  self . dynamic_eid_device = None
  self . dynamic_eid_timeout = LISP_DEFAULT_DYN_EID_TIMEOUT
  self . multi_tenant_eid = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
  if 1 - 1: OoOoOO00 / I11i
  if 43 - 43: o0oOOo0O0Ooo - i1IIi / Ii1I . OoOoOO00 + i11iIiiIii
 def add_interface ( self ) :
  lisp_myinterfaces [ self . device ] = self
  if 69 - 69: i11iIiiIii - iIii1I11I1II1
  if 40 - 40: I1IiiI / oO0o + ooOoO0o
 def get_instance_id ( self ) :
  return ( self . instance_id )
  if 100 - 100: OoOoOO00 % iII111i * ooOoO0o . O0
  if 37 - 37: I1ii11iIi11i
 def get_socket ( self ) :
  return ( self . raw_socket )
  if 24 - 24: O0 . I1Ii111 * i11iIiiIii
  if 84 - 84: ooOoO0o / I1ii11iIi11i - o0oOOo0O0Ooo . OoooooooOO * iIii1I11I1II1
 def get_bridge_socket ( self ) :
  return ( self . bridge_socket )
  if 16 - 16: I11i % O0
  if 56 - 56: Ii1I * OoOoOO00 . i1IIi
 def does_dynamic_eid_match ( self , eid ) :
  if ( self . dynamic_eid . is_null ( ) ) : return ( False )
  return ( eid . is_more_specific ( self . dynamic_eid ) )
  if 15 - 15: I1Ii111
  if 64 - 64: OOooOOo * Oo0Ooo
 def set_socket ( self , device ) :
  OO0o0OO0 = socket . socket ( socket . AF_INET , socket . SOCK_RAW , socket . IPPROTO_RAW )
  OO0o0OO0 . setsockopt ( socket . SOL_IP , socket . IP_HDRINCL , 1 )
  try :
   OO0o0OO0 . setsockopt ( socket . SOL_SOCKET , socket . SO_BINDTODEVICE , device )
  except :
   OO0o0OO0 . close ( )
   OO0o0OO0 = None
   if 96 - 96: Oo0Ooo / I1ii11iIi11i * iIii1I11I1II1 / iII111i
  self . raw_socket = OO0o0OO0
  if 18 - 18: I1Ii111
  if 29 - 29: i1IIi - I1IiiI / i1IIi
 def set_bridge_socket ( self , device ) :
  OO0o0OO0 = socket . socket ( socket . PF_PACKET , socket . SOCK_RAW )
  try :
   OO0o0OO0 = OO0o0OO0 . bind ( ( device , 0 ) )
   self . bridge_socket = OO0o0OO0
  except :
   return
   if 64 - 64: IiII
   if 69 - 69: OOooOOo . I1IiiI
   if 11 - 11: I1Ii111 * I1IiiI - I1Ii111 / iII111i
   if 22 - 22: iII111i % I11i % O0 - I11i
class lisp_datetime ( ) :
 def __init__ ( self , datetime_str ) :
  self . datetime_name = datetime_str
  self . datetime = None
  self . parse_datetime ( )
  if 71 - 71: I1Ii111 / II111iiii - OoooooooOO % i1IIi + OoOoOO00 % OoooooooOO
  if 52 - 52: Ii1I . OoOoOO00 / o0oOOo0O0Ooo / iII111i
 def valid_datetime ( self ) :
  OOOOo0O0O = self . datetime_name
  if ( OOOOo0O0O . find ( ":" ) == - 1 ) : return ( False )
  if ( OOOOo0O0O . find ( "-" ) == - 1 ) : return ( False )
  I11iIi , IiII1 , IiIi1i1i1Ii , time = OOOOo0O0O [ 0 : 4 ] , OOOOo0O0O [ 5 : 7 ] , OOOOo0O0O [ 8 : 10 ] , OOOOo0O0O [ 11 : : ]
  if 15 - 15: I1Ii111 / oO0o % Oo0Ooo + Oo0Ooo + IiII . O0
  if ( ( I11iIi + IiII1 + IiIi1i1i1Ii ) . isdigit ( ) == False ) : return ( False )
  if ( IiII1 < "01" and IiII1 > "12" ) : return ( False )
  if ( IiIi1i1i1Ii < "01" and IiIi1i1i1Ii > "31" ) : return ( False )
  if 63 - 63: o0oOOo0O0Ooo
  OOoO , oOO , IiiiiiIiII = time . split ( ":" )
  if 14 - 14: I1Ii111
  if ( ( OOoO + oOO + IiiiiiIiII ) . isdigit ( ) == False ) : return ( False )
  if ( OOoO < "00" and OOoO > "23" ) : return ( False )
  if ( oOO < "00" and oOO > "59" ) : return ( False )
  if ( IiiiiiIiII < "00" and IiiiiiIiII > "59" ) : return ( False )
  return ( True )
  if 23 - 23: IiII * Ii1I - Ii1I . oO0o - IiII
  if 56 - 56: i1IIi + i11iIiiIii % OoO0O00 - ooOoO0o / OoO0O00
 def parse_datetime ( self ) :
  I1iI1II1I = self . datetime_name
  I1iI1II1I = I1iI1II1I . replace ( "-" , "" )
  I1iI1II1I = I1iI1II1I . replace ( ":" , "" )
  self . datetime = int ( I1iI1II1I )
  if 97 - 97: i11iIiiIii
  if 62 - 62: i1IIi - I1IiiI * i1IIi % I1Ii111
 def now ( self ) :
  i1 = datetime . datetime . now ( ) . strftime ( "%Y-%m-%d-%H:%M:%S" )
  i1 = lisp_datetime ( i1 )
  return ( i1 )
  if 37 - 37: I11i
  if 61 - 61: OoooooooOO % iIii1I11I1II1 % O0 % I1Ii111 / Oo0Ooo . I1IiiI
 def print_datetime ( self ) :
  return ( self . datetime_name )
  if 20 - 20: ooOoO0o - I1Ii111
  if 97 - 97: O0
 def future ( self ) :
  return ( self . datetime > self . now ( ) . datetime )
  if 56 - 56: Ii1I * I1IiiI * ooOoO0o
  if 39 - 39: iII111i % Ii1I * iIii1I11I1II1 - Ii1I - I1Ii111
 def past ( self ) :
  return ( self . future ( ) == False )
  if 60 - 60: i11iIiiIii + i11iIiiIii - OoooooooOO + OoooooooOO
  if 5 - 5: o0oOOo0O0Ooo
 def now_in_range ( self , upper ) :
  return ( self . past ( ) and upper . future ( ) )
  if 78 - 78: OOooOOo * O0 * II111iiii % OoOoOO00
  if 12 - 12: Oo0Ooo . o0oOOo0O0Ooo - i1IIi - oO0o % IiII . I11i
 def this_year ( self ) :
  IiII1i11i1I = str ( self . now ( ) . datetime ) [ 0 : 4 ]
  i1 = str ( self . datetime ) [ 0 : 4 ]
  return ( i1 == IiII1i11i1I )
  if 64 - 64: O0 - iII111i
  if 82 - 82: O0
 def this_month ( self ) :
  IiII1i11i1I = str ( self . now ( ) . datetime ) [ 0 : 6 ]
  i1 = str ( self . datetime ) [ 0 : 6 ]
  return ( i1 == IiII1i11i1I )
  if 37 - 37: I1Ii111
  if 98 - 98: iII111i - OoOoOO00 / I1Ii111 . OOooOOo - OOooOOo - ooOoO0o
 def today ( self ) :
  IiII1i11i1I = str ( self . now ( ) . datetime ) [ 0 : 8 ]
  i1 = str ( self . datetime ) [ 0 : 8 ]
  return ( i1 == IiII1i11i1I )
  if 84 - 84: OOooOOo * ooOoO0o / O0
  if 96 - 96: I11i . I11i % II111iiii
  if 14 - 14: iII111i / OoooooooOO
  if 8 - 8: OOooOOo + I1IiiI - Oo0Ooo + i1IIi . Ii1I . I1Ii111
  if 38 - 38: I1IiiI / II111iiii * OoOoOO00 / I1Ii111
  if 80 - 80: I1ii11iIi11i / ooOoO0o * ooOoO0o . Oo0Ooo
class lisp_policy_match ( ) :
 def __init__ ( self ) :
  self . source_eid = None
  self . dest_eid = None
  self . source_rloc = None
  self . dest_rloc = None
  self . rloc_record_name = None
  self . geo_name = None
  self . elp_name = None
  self . rle_name = None
  self . json_name = None
  self . datetime_lower = None
  self . datetime_upper = None
  if 44 - 44: Ii1I * i1IIi % OoOoOO00 . OoOoOO00
  if 16 - 16: Oo0Ooo / i1IIi / iIii1I11I1II1 / iIii1I11I1II1 % o0oOOo0O0Ooo / I1ii11iIi11i
class lisp_policy ( ) :
 def __init__ ( self , policy_name ) :
  self . policy_name = policy_name
  self . match_clauses = [ ]
  self . set_action = None
  self . set_record_ttl = None
  self . set_source_eid = None
  self . set_dest_eid = None
  self . set_rloc_address = None
  self . set_rloc_record_name = None
  self . set_geo_name = None
  self . set_elp_name = None
  self . set_rle_name = None
  self . set_json_name = None
  if 11 - 11: I1IiiI
  if 45 - 45: OOooOOo / i1IIi * IiII * I1Ii111
 def match_policy_map_request ( self , mr , srloc ) :
  for ii11I1iiii1I in self . match_clauses :
   IiI1i1i1 = ii11I1iiii1I . source_eid
   oO0Oo0O = mr . source_eid
   if ( IiI1i1i1 and oO0Oo0O and oO0Oo0O . is_more_specific ( IiI1i1i1 ) == False ) : continue
   if 34 - 34: ooOoO0o / iIii1I11I1II1 . iII111i
   IiI1i1i1 = ii11I1iiii1I . dest_eid
   oO0Oo0O = mr . target_eid
   if ( IiI1i1i1 and oO0Oo0O and oO0Oo0O . is_more_specific ( IiI1i1i1 ) == False ) : continue
   if 91 - 91: OoO0O00
   IiI1i1i1 = ii11I1iiii1I . source_rloc
   oO0Oo0O = srloc
   if ( IiI1i1i1 and oO0Oo0O and oO0Oo0O . is_more_specific ( IiI1i1i1 ) == False ) : continue
   IIi1I1 = ii11I1iiii1I . datetime_lower
   i1i1I111I = ii11I1iiii1I . datetime_upper
   if ( IIi1I1 and i1i1I111I and IIi1I1 . now_in_range ( i1i1I111I ) == False ) : continue
   return ( True )
   if 2 - 2: oO0o . iIii1I11I1II1 + I1IiiI / o0oOOo0O0Ooo . i1IIi
  return ( False )
  if 62 - 62: IiII * I1ii11iIi11i % iIii1I11I1II1 / II111iiii - OoO0O00
  if 52 - 52: iII111i . I11i - I11i + oO0o + iIii1I11I1II1
 def set_policy_map_reply ( self ) :
  o0OoO0000o0OO = ( self . set_rloc_address == None and
 self . set_rloc_record_name == None and self . set_geo_name == None and
 self . set_elp_name == None and self . set_rle_name == None )
  if ( o0OoO0000o0OO ) : return ( None )
  if 79 - 79: Oo0Ooo * oO0o % I1ii11iIi11i . OoooooooOO
  I1II = lisp_rloc ( )
  if ( self . set_rloc_address ) :
   I1II . rloc . copy_address ( self . set_rloc_address )
   o0o00O0oOooO0 = I1II . rloc . print_address_no_iid ( )
   lprint ( "Policy set-rloc-address to {}" . format ( o0o00O0oOooO0 ) )
   if 85 - 85: oO0o / ooOoO0o % o0oOOo0O0Ooo
  if ( self . set_rloc_record_name ) :
   I1II . rloc_name = self . set_rloc_record_name
   II1 = blue ( I1II . rloc_name , False )
   lprint ( "Policy set-rloc-record-name to {}" . format ( II1 ) )
   if 34 - 34: Oo0Ooo / II111iiii
  if ( self . set_geo_name ) :
   I1II . geo_name = self . set_geo_name
   II1 = I1II . geo_name
   OooOOo0000Ooo = "" if lisp_geo_list . has_key ( II1 ) else "(not configured)"
   if 27 - 27: II111iiii . i1IIi % OoooooooOO * oO0o - iII111i * iII111i
   lprint ( "Policy set-geo-name '{}' {}" . format ( II1 , OooOOo0000Ooo ) )
   if 14 - 14: I1ii11iIi11i + iII111i * I11i . i11iIiiIii . OoooooooOO
  if ( self . set_elp_name ) :
   I1II . elp_name = self . set_elp_name
   II1 = I1II . elp_name
   OooOOo0000Ooo = "" if lisp_elp_list . has_key ( II1 ) else "(not configured)"
   if 5 - 5: iII111i + oO0o % O0 . OoooooooOO + i1IIi
   lprint ( "Policy set-elp-name '{}' {}" . format ( II1 , OooOOo0000Ooo ) )
   if 55 - 55: I1ii11iIi11i
  if ( self . set_rle_name ) :
   I1II . rle_name = self . set_rle_name
   II1 = I1II . rle_name
   OooOOo0000Ooo = "" if lisp_rle_list . has_key ( II1 ) else "(not configured)"
   if 34 - 34: OoO0O00 * iIii1I11I1II1 . iIii1I11I1II1
   lprint ( "Policy set-rle-name '{}' {}" . format ( II1 , OooOOo0000Ooo ) )
   if 39 - 39: o0oOOo0O0Ooo
  if ( self . set_json_name ) :
   I1II . json_name = self . set_json_name
   II1 = I1II . json_name
   OooOOo0000Ooo = "" if lisp_json_list . has_key ( II1 ) else "(not configured)"
   if 29 - 29: Oo0Ooo . Oo0Ooo * OoO0O00 % Ii1I - ooOoO0o
   lprint ( "Policy set-json-name '{}' {}" . format ( II1 , OooOOo0000Ooo ) )
   if 67 - 67: I1IiiI % O0 + I1IiiI * I1Ii111 * OoOoOO00 * II111iiii
  return ( I1II )
  if 79 - 79: I1IiiI
  if 37 - 37: I1Ii111 + Ii1I
 def save_policy ( self ) :
  lisp_policies [ self . policy_name ] = self
  if 50 - 50: i11iIiiIii
  if 57 - 57: O0 * i1IIi - I1IiiI
  if 48 - 48: IiII / iIii1I11I1II1
class lisp_pubsub ( ) :
 def __init__ ( self , itr , port , nonce , ttl , xtr_id ) :
  self . itr = itr
  self . port = port
  self . nonce = nonce
  self . uptime = lisp_get_timestamp ( )
  self . ttl = ttl
  self . xtr_id = xtr_id
  self . map_notify_count = 0
  self . eid_prefix = None
  if 20 - 20: oO0o / OoooooooOO
  if 95 - 95: Oo0Ooo . i11iIiiIii
 def add ( self , eid_prefix ) :
  self . eid_prefix = eid_prefix
  Oo0o0 = self . ttl
  iiI1I1IIi = eid_prefix . print_prefix ( )
  if ( lisp_pubsub_cache . has_key ( iiI1I1IIi ) == False ) :
   lisp_pubsub_cache [ iiI1I1IIi ] = { }
   if 50 - 50: iII111i . i11iIiiIii - i1IIi
  I1IIiI = lisp_pubsub_cache [ iiI1I1IIi ]
  if 24 - 24: i11iIiiIii % iII111i . oO0o
  iiIIiI11I = "Add"
  if ( I1IIiI . has_key ( self . xtr_id ) ) :
   iiIIiI11I = "Replace"
   del ( I1IIiI [ self . xtr_id ] )
   if 28 - 28: II111iiii * O0 % O0 - OoooooooOO - oO0o - I1ii11iIi11i
  I1IIiI [ self . xtr_id ] = self
  if 16 - 16: I1IiiI . OoO0O00 * Ii1I / oO0o
  iiI1I1IIi = green ( iiI1I1IIi , False )
  OooO0OO0 = red ( self . itr . print_address_no_iid ( ) , False )
  IIiiII11i11I = "0x" + lisp_hex_string ( self . xtr_id )
  lprint ( "{} pubsub state {} for {}, xtr-id: {}, ttl {}" . format ( iiIIiI11I , iiI1I1IIi ,
 OooO0OO0 , IIiiII11i11I , Oo0o0 ) )
  if 27 - 27: iII111i - ooOoO0o - i11iIiiIii
  if 39 - 39: i11iIiiIii / oO0o
 def delete ( self , eid_prefix ) :
  iiI1I1IIi = eid_prefix . print_prefix ( )
  OooO0OO0 = red ( self . itr . print_address_no_iid ( ) , False )
  IIiiII11i11I = "0x" + lisp_hex_string ( self . xtr_id )
  if ( lisp_pubsub_cache . has_key ( iiI1I1IIi ) ) :
   I1IIiI = lisp_pubsub_cache [ iiI1I1IIi ]
   if ( I1IIiI . has_key ( self . xtr_id ) ) :
    I1IIiI . pop ( self . xtr_id )
    lprint ( "Remove pubsub state {} for {}, xtr-id: {}" . format ( iiI1I1IIi ,
 OooO0OO0 , IIiiII11i11I ) )
    if 71 - 71: I1Ii111 * iIii1I11I1II1 - I1Ii111
    if 87 - 87: I1IiiI / Ii1I
    if 54 - 54: OoooooooOO / Ii1I
    if 26 - 26: o0oOOo0O0Ooo + OoO0O00
    if 59 - 59: Ii1I * IiII
    if 64 - 64: ooOoO0o . Oo0Ooo - OoOoOO00
    if 66 - 66: OoOoOO00
    if 83 - 83: OOooOOo . IiII
    if 98 - 98: i11iIiiIii
    if 74 - 74: iIii1I11I1II1 * O0 + OOooOOo . o0oOOo0O0Ooo
    if 17 - 17: I1Ii111
    if 59 - 59: OoOoOO00 . OoOoOO00 * iII111i - Ii1I . i11iIiiIii
    if 68 - 68: iII111i
    if 68 - 68: I1Ii111 - OoO0O00 % OoO0O00 % OOooOOo - OoO0O00
    if 3 - 3: iIii1I11I1II1 + iIii1I11I1II1 + OoO0O00
    if 59 - 59: iII111i
    if 7 - 7: o0oOOo0O0Ooo * OoooooooOO - Ii1I * II111iiii % I1Ii111
    if 82 - 82: OoOoOO00 - OoOoOO00 + iIii1I11I1II1 + o0oOOo0O0Ooo + IiII - o0oOOo0O0Ooo
    if 65 - 65: I1Ii111 + OOooOOo
    if 97 - 97: oO0o % OoOoOO00 * oO0o % II111iiii + iIii1I11I1II1
    if 11 - 11: ooOoO0o . o0oOOo0O0Ooo
    if 94 - 94: ooOoO0o . oO0o * OoooooooOO % oO0o
class lisp_trace ( ) :
 def __init__ ( self ) :
  self . nonce = lisp_get_control_nonce ( )
  self . packet_json = [ ]
  self . local_rloc = None
  self . local_port = None
  self . lisp_socket = None
  if 77 - 77: ooOoO0o % I1IiiI
  if 26 - 26: o0oOOo0O0Ooo
 def print_trace ( self ) :
  o0oOO0OOoO = self . packet_json
  lprint ( "LISP-Trace JSON: '{}'" . format ( o0oOO0OOoO ) )
  if 72 - 72: I1IiiI
  if 90 - 90: ooOoO0o
 def encode ( self ) :
  i1OOoO0OO0oO = socket . htonl ( 0x90000000 )
  IiiiIi1iiii11 = struct . pack ( "II" , i1OOoO0OO0oO , 0 )
  IiiiIi1iiii11 += struct . pack ( "Q" , self . nonce )
  IiiiIi1iiii11 += json . dumps ( self . packet_json )
  return ( IiiiIi1iiii11 )
  if 67 - 67: iIii1I11I1II1 + i1IIi * I1IiiI * OoooooooOO
  if 23 - 23: IiII
 def decode ( self , packet ) :
  O0O00Oo = "I"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( False )
  i1OOoO0OO0oO = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] ) [ 0 ]
  packet = packet [ IiIii1i : : ]
  i1OOoO0OO0oO = socket . ntohl ( i1OOoO0OO0oO )
  if ( ( i1OOoO0OO0oO & 0xff000000 ) != 0x90000000 ) : return ( False )
  if 32 - 32: OoOoOO00 - iII111i % oO0o / I1ii11iIi11i - o0oOOo0O0Ooo
  if ( len ( packet ) < IiIii1i ) : return ( False )
  o0o00O0oOooO0 = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] ) [ 0 ]
  packet = packet [ IiIii1i : : ]
  if 52 - 52: Ii1I / OoooooooOO % i11iIiiIii + iII111i
  o0o00O0oOooO0 = socket . ntohl ( o0o00O0oOooO0 )
  O0oOOOOOO00ooOOo0 = o0o00O0oOooO0 >> 24
  oOooooO0O00Oo = ( o0o00O0oOooO0 >> 16 ) & 0xff
  OoI1oooO0OOO0OoO = ( o0o00O0oOooO0 >> 8 ) & 0xff
  iiiI1i1I = o0o00O0oOooO0 & 0xff
  self . local_rloc = "{}.{}.{}.{}" . format ( O0oOOOOOO00ooOOo0 , oOooooO0O00Oo , OoI1oooO0OOO0OoO , iiiI1i1I )
  self . local_port = str ( i1OOoO0OO0oO & 0xffff )
  if 84 - 84: OoO0O00 . oO0o * OoO0O00 - IiII
  O0O00Oo = "Q"
  IiIii1i = struct . calcsize ( O0O00Oo )
  if ( len ( packet ) < IiIii1i ) : return ( False )
  self . nonce = struct . unpack ( O0O00Oo , packet [ : IiIii1i ] ) [ 0 ]
  packet = packet [ IiIii1i : : ]
  if ( len ( packet ) == 0 ) : return ( True )
  if 24 - 24: O0 * OOooOOo . OoO0O00 + iII111i + i1IIi + oO0o
  try :
   self . packet_json = json . loads ( packet )
  except :
   return ( False )
   if 57 - 57: OOooOOo * OOooOOo
  return ( True )
  if 63 - 63: o0oOOo0O0Ooo * iIii1I11I1II1 - II111iiii
  if 72 - 72: o0oOOo0O0Ooo * I1ii11iIi11i
 def myeid ( self , eid ) :
  return ( lisp_is_myeid ( eid ) )
  if 57 - 57: IiII * OOooOOo
  if 28 - 28: I1Ii111
 def return_to_sender ( self , lisp_socket , rts_rloc , packet ) :
  I1II , Oo0o = self . rtr_cache_nat_trace_find ( rts_rloc )
  if ( I1II == None ) :
   I1II , Oo0o = rts_rloc . split ( ":" )
   Oo0o = int ( Oo0o )
   lprint ( "Send LISP-Trace to address {}:{}" . format ( I1II , Oo0o ) )
  else :
   lprint ( "Send LISP-Trace to translated address {}:{}" . format ( I1II ,
 Oo0o ) )
   if 27 - 27: OoOoOO00 - OoO0O00 - iIii1I11I1II1 + OoOoOO00 - I11i
   if 10 - 10: I1ii11iIi11i
  if ( lisp_socket == None ) :
   OO0o0OO0 = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
   OO0o0OO0 . bind ( ( "0.0.0.0" , LISP_TRACE_PORT ) )
   OO0o0OO0 . sendto ( packet , ( I1II , Oo0o ) )
   OO0o0OO0 . close ( )
  else :
   lisp_socket . sendto ( packet , ( I1II , Oo0o ) )
   if 6 - 6: OoO0O00 + OoO0O00 * OOooOOo / IiII % ooOoO0o - I1IiiI
   if 17 - 17: II111iiii
   if 66 - 66: O0 % OoOoOO00 + IiII % I1Ii111
 def packet_length ( self ) :
  oOoO0OOO00O = 8 ; OO0oO0 = 4 + 4 + 8
  return ( oOoO0OOO00O + OO0oO0 + len ( json . dumps ( self . packet_json ) ) )
  if 35 - 35: Ii1I . O0 % i11iIiiIii * oO0o - OoooooooOO
  if 87 - 87: iII111i * ooOoO0o - OOooOOo . O0
 def rtr_cache_nat_trace ( self , translated_rloc , translated_port ) :
  o0Oo = self . local_rloc + ":" + self . local_port
  Oo00OO0OO = ( translated_rloc , translated_port )
  lisp_rtr_nat_trace_cache [ o0Oo ] = Oo00OO0OO
  lprint ( "Cache NAT Trace addresses {} -> {}" . format ( o0Oo , Oo00OO0OO ) )
  if 20 - 20: OoOoOO00 - IiII
  if 9 - 9: O0 . I11i % I1ii11iIi11i * oO0o - I1Ii111 - i1IIi
 def rtr_cache_nat_trace_find ( self , local_rloc_and_port ) :
  o0Oo = local_rloc_and_port
  try : Oo00OO0OO = lisp_rtr_nat_trace_cache [ o0Oo ]
  except : Oo00OO0OO = ( None , None )
  return ( Oo00OO0OO )
  if 66 - 66: II111iiii / Oo0Ooo
  if 93 - 93: iII111i + I11i * OoooooooOO . OoO0O00
  if 40 - 40: ooOoO0o * I1Ii111 + iII111i
  if 52 - 52: iII111i % I11i
  if 95 - 95: IiII + Ii1I / OoO0O00 - iII111i / I1IiiI
  if 27 - 27: Oo0Ooo + i1IIi + i11iIiiIii . OoO0O00 . OoO0O00
  if 56 - 56: I1Ii111 / OoO0O00 + o0oOOo0O0Ooo . OoooooooOO * Oo0Ooo
  if 14 - 14: OoO0O00
  if 21 - 21: II111iiii + i11iIiiIii + I11i % I1IiiI
  if 65 - 65: IiII + I1ii11iIi11i / iII111i / I1IiiI + Ii1I
  if 88 - 88: IiII % iIii1I11I1II1
def lisp_get_map_server ( address ) :
 for ii1i in lisp_map_servers_list . values ( ) :
  if ( ii1i . map_server . is_exact_match ( address ) ) : return ( ii1i )
  if 3 - 3: ooOoO0o / I1Ii111 % iIii1I11I1II1 % I11i * oO0o / iIii1I11I1II1
 return ( None )
 if 75 - 75: i11iIiiIii . iII111i
 if 68 - 68: OOooOOo . I1ii11iIi11i % I1ii11iIi11i . i11iIiiIii
 if 45 - 45: oO0o % I1ii11iIi11i * I1Ii111
 if 21 - 21: O0 + i11iIiiIii
 if 72 - 72: OoOoOO00 * OoooooooOO % O0 / I1ii11iIi11i % Ii1I - I11i
 if 65 - 65: iIii1I11I1II1 + II111iiii * OoO0O00 * i11iIiiIii / IiII
 if 15 - 15: OoOoOO00 % O0 - OOooOOo - oO0o . iII111i . OoO0O00
def lisp_get_any_map_server ( ) :
 for ii1i in lisp_map_servers_list . values ( ) : return ( ii1i )
 return ( None )
 if 52 - 52: II111iiii * o0oOOo0O0Ooo
 if 95 - 95: I1Ii111 - OoooooooOO
 if 99 - 99: OoooooooOO % IiII . I11i + OoooooooOO
 if 57 - 57: Ii1I / I1IiiI * i1IIi
 if 21 - 21: I11i . O0 * OoooooooOO + ooOoO0o * oO0o % i11iIiiIii
 if 30 - 30: ooOoO0o * I1Ii111 + OoO0O00
 if 30 - 30: Ii1I / iII111i * Ii1I
 if 11 - 11: OoOoOO00 - OoOoOO00 % oO0o
 if 3 - 3: I1IiiI - OoooooooOO % iIii1I11I1II1 + I1Ii111 + OoOoOO00
 if 71 - 71: i1IIi % O0 % ooOoO0o
def lisp_get_map_resolver ( address , eid ) :
 if ( address != None ) :
  o0o00O0oOooO0 = address . print_address ( )
  I1III11iIIIi = None
  for o0Oo in lisp_map_resolvers_list :
   if ( o0Oo . find ( o0o00O0oOooO0 ) == - 1 ) : continue
   I1III11iIIIi = lisp_map_resolvers_list [ o0Oo ]
   if 24 - 24: O0
  return ( I1III11iIIIi )
  if 88 - 88: OoooooooOO / Oo0Ooo / oO0o
  if 99 - 99: I1Ii111 % OoOoOO00 % IiII - Ii1I
  if 79 - 79: ooOoO0o + Oo0Ooo
  if 80 - 80: OoOoOO00 % OoO0O00 . OoO0O00 * OoO0O00 * O0
  if 18 - 18: II111iiii . o0oOOo0O0Ooo + OoO0O00
  if 69 - 69: OoO0O00 . ooOoO0o * ooOoO0o * iIii1I11I1II1
  if 8 - 8: iII111i . oO0o . OOooOOo + iII111i . Ii1I
 if ( eid == "" ) :
  iiiIi1i = ""
 elif ( eid == None ) :
  iiiIi1i = "all"
 else :
  ii1iii = lisp_db_for_lookups . lookup_cache ( eid , False )
  iiiIi1i = "all" if ii1iii == None else ii1iii . use_mr_name
  if 49 - 49: OoO0O00 . i11iIiiIii * I1IiiI
  if 35 - 35: i11iIiiIii . I11i . OoOoOO00 - i11iIiiIii / oO0o / IiII
 o0OOo00O00oOO = None
 for I1III11iIIIi in lisp_map_resolvers_list . values ( ) :
  if ( iiiIi1i == "" ) : return ( I1III11iIIIi )
  if ( I1III11iIIIi . mr_name != iiiIi1i ) : continue
  if ( o0OOo00O00oOO == None or I1III11iIIIi . last_used < o0OOo00O00oOO . last_used ) : o0OOo00O00oOO = I1III11iIIIi
  if 22 - 22: O0 % I11i + OoO0O00 - iII111i + I1IiiI . O0
 return ( o0OOo00O00oOO )
 if 73 - 73: ooOoO0o + O0 - I11i . I1IiiI + OOooOOo
 if 36 - 36: I11i % OoO0O00 * OoOoOO00 - I1Ii111
 if 16 - 16: ooOoO0o % OOooOOo . OoO0O00 % II111iiii . iIii1I11I1II1
 if 21 - 21: oO0o + II111iiii / OoOoOO00 * I11i
 if 90 - 90: OoOoOO00 % OoOoOO00 + I11i
 if 70 - 70: I1IiiI . ooOoO0o / I11i / OoO0O00
 if 40 - 40: oO0o % iIii1I11I1II1 * iIii1I11I1II1 / Oo0Ooo * OoO0O00
 if 61 - 61: OOooOOo
def lisp_get_decent_map_resolver ( eid ) :
 ooo = lisp_get_decent_index ( eid )
 ooOOO000 = str ( ooo ) + "." + lisp_decent_dns_suffix
 if 65 - 65: iIii1I11I1II1 % i1IIi / I1IiiI / oO0o % ooOoO0o / I11i
 lprint ( "Use LISP-Decent map-resolver {} for EID {}" . format ( bold ( ooOOO000 , False ) , eid . print_prefix ( ) ) )
 if 2 - 2: I1ii11iIi11i
 if 90 - 90: II111iiii * I1Ii111 . ooOoO0o - I1ii11iIi11i % I11i * o0oOOo0O0Ooo
 o0OOo00O00oOO = None
 for I1III11iIIIi in lisp_map_resolvers_list . values ( ) :
  if ( ooOOO000 != I1III11iIIIi . dns_name ) : continue
  if ( o0OOo00O00oOO == None or I1III11iIIIi . last_used < o0OOo00O00oOO . last_used ) : o0OOo00O00oOO = I1III11iIIIi
  if 85 - 85: iIii1I11I1II1
 return ( o0OOo00O00oOO )
 if 76 - 76: i11iIiiIii % I1IiiI / I11i
 if 42 - 42: o0oOOo0O0Ooo . I1IiiI + I11i . OoOoOO00 - O0 / Ii1I
 if 66 - 66: IiII + OoOoOO00 + I1IiiI + i1IIi + OoooooooOO % I1IiiI
 if 80 - 80: iII111i / O0 % OoooooooOO / Oo0Ooo
 if 75 - 75: ooOoO0o
 if 72 - 72: oO0o . OoooooooOO % ooOoO0o % OoO0O00 * oO0o * OoO0O00
 if 14 - 14: I11i / I11i
def lisp_ipv4_input ( packet ) :
 if 90 - 90: O0 * OOooOOo / oO0o . Oo0Ooo * I11i
 if 93 - 93: oO0o / ooOoO0o - I1Ii111
 if 70 - 70: OOooOOo / Ii1I - ooOoO0o + OoooooooOO / OoO0O00 - i11iIiiIii
 if 26 - 26: O0 + Oo0Ooo
 if ( ord ( packet [ 9 ] ) == 2 ) : return ( [ True , packet ] )
 if 30 - 30: IiII
 if 6 - 6: O0
 if 92 - 92: I11i
 if 76 - 76: I11i / iIii1I11I1II1 - i11iIiiIii / O0 / O0
 oO0oOoo0O = struct . unpack ( "H" , packet [ 10 : 12 ] ) [ 0 ]
 if ( oO0oOoo0O == 0 ) :
  dprint ( "Packet arrived with checksum of 0!" )
 else :
  packet = lisp_ip_checksum ( packet )
  oO0oOoo0O = struct . unpack ( "H" , packet [ 10 : 12 ] ) [ 0 ]
  if ( oO0oOoo0O != 0 ) :
   dprint ( "IPv4 header checksum failed for inner header" )
   packet = lisp_format_packet ( packet [ 0 : 20 ] )
   dprint ( "Packet header: {}" . format ( packet ) )
   return ( [ False , None ] )
   if 19 - 19: Ii1I . I1IiiI - i1IIi * ooOoO0o . iIii1I11I1II1
   if 87 - 87: ooOoO0o % I1ii11iIi11i . I1IiiI
   if 42 - 42: iII111i % i11iIiiIii % o0oOOo0O0Ooo . O0 % iII111i
   if 72 - 72: Oo0Ooo . Oo0Ooo . IiII . Oo0Ooo
   if 80 - 80: I1Ii111 + IiII + O0 - I1Ii111 . iIii1I11I1II1
   if 53 - 53: OoO0O00 / i11iIiiIii * I1Ii111
   if 62 - 62: oO0o / Oo0Ooo / IiII + I11i * ooOoO0o
 Oo0o0 = struct . unpack ( "B" , packet [ 8 : 9 ] ) [ 0 ]
 if ( Oo0o0 == 0 ) :
  dprint ( "IPv4 packet arrived with ttl 0, packet discarded" )
  return ( [ False , None ] )
 elif ( Oo0o0 == 1 ) :
  dprint ( "IPv4 packet {}, packet discarded" . format ( bold ( "ttl expiry" , False ) ) )
  if 84 - 84: ooOoO0o + OoOoOO00 * I1ii11iIi11i % OoooooooOO . O0
  return ( [ False , None ] )
  if 27 - 27: OoO0O00 * OoooooooOO - II111iiii / o0oOOo0O0Ooo
  if 76 - 76: I11i % I1Ii111 % iII111i + IiII * iII111i + OoOoOO00
 Oo0o0 -= 1
 packet = packet [ 0 : 8 ] + struct . pack ( "B" , Oo0o0 ) + packet [ 9 : : ]
 packet = packet [ 0 : 10 ] + struct . pack ( "H" , 0 ) + packet [ 12 : : ]
 packet = lisp_ip_checksum ( packet )
 return ( [ False , packet ] )
 if 83 - 83: OOooOOo . ooOoO0o / IiII
 if 80 - 80: I1Ii111 . I11i - I11i + I1ii11iIi11i
 if 42 - 42: I11i / IiII % O0 - Oo0Ooo
 if 33 - 33: I1Ii111
 if 1 - 1: IiII - iIii1I11I1II1 % OoooooooOO
 if 1 - 1: o0oOOo0O0Ooo - i11iIiiIii + I11i
 if 47 - 47: O0 + IiII + ooOoO0o + OOooOOo / OoOoOO00
def lisp_ipv6_input ( packet ) :
 Ii1II1I11i1I = packet . inner_dest
 packet = packet . packet
 if 31 - 31: oO0o * iII111i % OoOoOO00
 if 80 - 80: ooOoO0o % I1ii11iIi11i % I11i . I1Ii111
 if 3 - 3: ooOoO0o - Oo0Ooo
 if 2 - 2: iII111i . iII111i
 if 77 - 77: OOooOOo
 Oo0o0 = struct . unpack ( "B" , packet [ 7 : 8 ] ) [ 0 ]
 if ( Oo0o0 == 0 ) :
  dprint ( "IPv6 packet arrived with hop-limit 0, packet discarded" )
  return ( None )
 elif ( Oo0o0 == 1 ) :
  dprint ( "IPv6 packet {}, packet discarded" . format ( bold ( "ttl expiry" , False ) ) )
  if 74 - 74: O0
  return ( None )
  if 86 - 86: OoOoOO00
  if 4 - 4: OoooooooOO * OoO0O00
  if 93 - 93: OoO0O00 - I1Ii111 - OoO0O00
  if 1 - 1: o0oOOo0O0Ooo . oO0o * i11iIiiIii * IiII - OoO0O00 - OoooooooOO
  if 29 - 29: iIii1I11I1II1 + OoO0O00 * II111iiii * Ii1I * iII111i . O0
 if ( Ii1II1I11i1I . is_ipv6_link_local ( ) ) :
  dprint ( "Do not encapsulate IPv6 link-local packets" )
  return ( None )
  if 6 - 6: I1IiiI - OoOoOO00
  if 63 - 63: OOooOOo - oO0o * I1IiiI
 Oo0o0 -= 1
 packet = packet [ 0 : 7 ] + struct . pack ( "B" , Oo0o0 ) + packet [ 8 : : ]
 return ( packet )
 if 60 - 60: II111iiii - Oo0Ooo
 if 43 - 43: I1IiiI - IiII - OOooOOo
 if 19 - 19: I1Ii111 / I1Ii111 - i1IIi
 if 99 - 99: O0
 if 37 - 37: iIii1I11I1II1 / I1Ii111 + OoO0O00
 if 85 - 85: ooOoO0o / I1IiiI
 if 7 - 7: Oo0Ooo - iIii1I11I1II1 / I1ii11iIi11i * I1IiiI + Ii1I
 if 99 - 99: i11iIiiIii - I1ii11iIi11i
def lisp_mac_input ( packet ) :
 return ( packet )
 if 64 - 64: IiII . OoOoOO00 . Oo0Ooo . I1Ii111 / I11i / Ii1I
 if 95 - 95: iIii1I11I1II1 . Ii1I % oO0o - I11i % IiII
 if 42 - 42: OoOoOO00 + oO0o * i1IIi + i11iIiiIii
 if 25 - 25: Ii1I - Ii1I - I1ii11iIi11i / i1IIi . OoOoOO00 % Oo0Ooo
 if 76 - 76: I1Ii111 / OoOoOO00
 if 61 - 61: Oo0Ooo . i1IIi
 if 78 - 78: i11iIiiIii
 if 20 - 20: Ii1I
 if 100 - 100: OoooooooOO . I1Ii111
def lisp_rate_limit_map_request ( dest ) :
 IiII1i11i1I = lisp_get_timestamp ( )
 if 32 - 32: iIii1I11I1II1 . iIii1I11I1II1 % II111iiii / Oo0Ooo . iIii1I11I1II1 . O0
 if 63 - 63: I1IiiI . iIii1I11I1II1 . Oo0Ooo % OOooOOo - iII111i + ooOoO0o
 if 64 - 64: o0oOOo0O0Ooo / Ii1I % I1Ii111 % iII111i + OOooOOo * IiII
 if 87 - 87: I1ii11iIi11i . i1IIi - I11i + OoOoOO00 . O0
 Ooo0o0oo0 = IiII1i11i1I - lisp_no_map_request_rate_limit
 if ( Ooo0o0oo0 < LISP_NO_MAP_REQUEST_RATE_LIMIT_TIME ) :
  O0OO0 = int ( LISP_NO_MAP_REQUEST_RATE_LIMIT_TIME - Ooo0o0oo0 )
  dprint ( "No Rate-Limit Mode for another {} secs" . format ( O0OO0 ) )
  return ( False )
  if 37 - 37: IiII
  if 65 - 65: ooOoO0o * Ii1I / I1IiiI . i1IIi % ooOoO0o . OoooooooOO
  if 17 - 17: ooOoO0o / OoO0O00 / I1IiiI / OOooOOo % IiII
  if 88 - 88: i1IIi - OoOoOO00
  if 66 - 66: OoooooooOO - OoooooooOO * I11i / II111iiii + oO0o / Ii1I
 if ( lisp_last_map_request_sent == None ) : return ( False )
 Ooo0o0oo0 = IiII1i11i1I - lisp_last_map_request_sent
 iii1111ii = ( Ooo0o0oo0 < LISP_MAP_REQUEST_RATE_LIMIT )
 if 7 - 7: Ii1I / iIii1I11I1II1
 if ( iii1111ii ) :
  dprint ( "Rate-limiting Map-Request for {}, sent {} secs ago" . format ( green ( dest . print_address ( ) , False ) , round ( Ooo0o0oo0 , 3 ) ) )
  if 36 - 36: iIii1I11I1II1 % i11iIiiIii
  if 35 - 35: Oo0Ooo + I1IiiI - O0 - I1Ii111
 return ( iii1111ii )
 if 64 - 64: i1IIi * OoOoOO00 / II111iiii * oO0o
 if 35 - 35: i1IIi - Ii1I - Ii1I . O0 % iII111i * iII111i
 if 15 - 15: OoooooooOO . Ii1I * I1Ii111 . ooOoO0o % OoO0O00 * Oo0Ooo
 if 10 - 10: iII111i + i11iIiiIii . OOooOOo % iII111i - i1IIi
 if 10 - 10: iIii1I11I1II1 * i11iIiiIii - O0
 if 45 - 45: oO0o % OOooOOo - IiII + o0oOOo0O0Ooo + i11iIiiIii
 if 79 - 79: IiII % I1Ii111 . I1IiiI + O0 * oO0o * ooOoO0o
def lisp_send_map_request ( lisp_sockets , lisp_ephem_port , seid , deid , rloc ,
 pubsub = False ) :
 global lisp_last_map_request_sent
 if 38 - 38: IiII
 if 78 - 78: Oo0Ooo * I1ii11iIi11i % OOooOOo / Oo0Ooo + I1ii11iIi11i * IiII
 if 2 - 2: Oo0Ooo - OoOoOO00
 if 22 - 22: OoO0O00 - oO0o - O0
 if 49 - 49: iIii1I11I1II1 + I1Ii111 / i11iIiiIii
 if 62 - 62: ooOoO0o . I1IiiI * i11iIiiIii
 i1iIiiiiiI1I1II = o0oOO = None
 if ( rloc ) :
  i1iIiiiiiI1I1II = rloc . rloc
  o0oOO = rloc . translated_port if lisp_i_am_rtr else LISP_DATA_PORT
  if 70 - 70: OOooOOo * IiII * iII111i
  if 45 - 45: iII111i * i11iIiiIii - IiII + I1ii11iIi11i % I1ii11iIi11i
  if 26 - 26: i11iIiiIii + ooOoO0o / OoOoOO00
  if 15 - 15: II111iiii - IiII
  if 74 - 74: i1IIi * OoooooooOO . Oo0Ooo . I1IiiI / o0oOOo0O0Ooo . OoOoOO00
 IIIiI , IIO0OooOo00o00 , OoO0o0OOOO = lisp_myrlocs
 if ( IIIiI == None ) :
  lprint ( "Suppress sending Map-Request, IPv4 RLOC not found" )
  return
  if 36 - 36: I1IiiI
 if ( IIO0OooOo00o00 == None and i1iIiiiiiI1I1II != None and i1iIiiiiiI1I1II . is_ipv6 ( ) ) :
  lprint ( "Suppress sending Map-Request, IPv6 RLOC not found" )
  return
  if 71 - 71: OoooooooOO . Oo0Ooo * I1IiiI . I1Ii111
  if 76 - 76: OOooOOo - OoOoOO00
 OoOOoO = lisp_map_request ( )
 OoOOoO . record_count = 1
 OoOOoO . nonce = lisp_get_control_nonce ( )
 OoOOoO . rloc_probe = ( i1iIiiiiiI1I1II != None )
 OoOOoO . subscribe_bit = pubsub
 OoOOoO . xtr_id_present = pubsub
 if 21 - 21: O0 * ooOoO0o / ooOoO0o + i1IIi * IiII
 if 12 - 12: o0oOOo0O0Ooo * OoO0O00 / I11i . oO0o
 if 52 - 52: OoO0O00 % i1IIi * oO0o
 if 3 - 3: o0oOOo0O0Ooo - iIii1I11I1II1 / oO0o - I1Ii111
 if 44 - 44: I1Ii111 . I1ii11iIi11i . OoOoOO00 % o0oOOo0O0Ooo * i11iIiiIii - OOooOOo
 if 68 - 68: iII111i + I1ii11iIi11i / II111iiii * I1ii11iIi11i
 if 45 - 45: II111iiii . iII111i
 if ( rloc ) : rloc . last_rloc_probe_nonce = OoOOoO . nonce
 if 55 - 55: ooOoO0o / iII111i / O0
 Oo0ooO = deid . is_multicast_address ( )
 if ( Oo0ooO ) :
  OoOOoO . target_eid = seid
  OoOOoO . target_group = deid
 else :
  OoOOoO . target_eid = deid
  if 98 - 98: O0 % iII111i + II111iiii
  if 13 - 13: I1IiiI * oO0o - o0oOOo0O0Ooo
  if 23 - 23: iIii1I11I1II1 + oO0o . oO0o / o0oOOo0O0Ooo
  if 77 - 77: i1IIi * o0oOOo0O0Ooo * IiII
  if 24 - 24: i11iIiiIii / iIii1I11I1II1 / iII111i
  if 31 - 31: OOooOOo . iIii1I11I1II1 - oO0o
  if 36 - 36: O0
  if 30 - 30: i11iIiiIii * Oo0Ooo . IiII
  if 65 - 65: oO0o * IiII * OOooOOo / OoooooooOO % I11i / I1Ii111
 if ( OoOOoO . rloc_probe == False ) :
  ii1iii = lisp_get_signature_eid ( )
  if ( ii1iii ) :
   OoOOoO . signature_eid . copy_address ( ii1iii . eid )
   OoOOoO . privkey_filename = "./lisp-sig.pem"
   if 21 - 21: i1IIi * iII111i + OoO0O00
   if 27 - 27: I11i / oO0o . iII111i + o0oOOo0O0Ooo - OOooOOo
   if 85 - 85: OoooooooOO
   if 83 - 83: iII111i * I11i . OOooOOo - OoO0O00 % IiII
   if 8 - 8: I1Ii111
   if 86 - 86: ooOoO0o + iII111i * O0 % OoO0O00 + OoOoOO00
 if ( seid == None or Oo0ooO ) :
  OoOOoO . source_eid . afi = LISP_AFI_NONE
 else :
  OoOOoO . source_eid = seid
  if 49 - 49: OOooOOo / i1IIi - II111iiii . iIii1I11I1II1 + I11i . OOooOOo
  if 9 - 9: iIii1I11I1II1 + Ii1I + I11i
  if 96 - 96: OoO0O00 + i11iIiiIii + OoO0O00
  if 7 - 7: i1IIi . I1IiiI
  if 68 - 68: OoooooooOO
  if 91 - 91: IiII . ooOoO0o * I11i
  if 39 - 39: o0oOOo0O0Ooo + i11iIiiIii
  if 69 - 69: iIii1I11I1II1 . II111iiii
  if 36 - 36: I1IiiI * i1IIi + OoOoOO00
  if 63 - 63: OoOoOO00 - iII111i
  if 83 - 83: i1IIi / iII111i % ooOoO0o % i11iIiiIii + I1ii11iIi11i
  if 82 - 82: iIii1I11I1II1 / OOooOOo
 if ( i1iIiiiiiI1I1II != None and lisp_nat_traversal and lisp_i_am_rtr == False ) :
  if ( i1iIiiiiiI1I1II . is_private_address ( ) == False ) :
   IIIiI = lisp_get_any_translated_rloc ( )
   if 7 - 7: OoooooooOO
  if ( IIIiI == None ) :
   lprint ( "Suppress sending Map-Request, translated RLOC not found" )
   return
   if 71 - 71: OOooOOo * Oo0Ooo . Oo0Ooo % iIii1I11I1II1
   if 56 - 56: IiII * iIii1I11I1II1 - iIii1I11I1II1 . O0
   if 56 - 56: I1Ii111 / iIii1I11I1II1 % IiII * iIii1I11I1II1 . I1ii11iIi11i . OOooOOo
   if 1 - 1: Ii1I . Ii1I % II111iiii + I11i + OoOoOO00
   if 52 - 52: OoooooooOO - OoO0O00
   if 24 - 24: iII111i / Oo0Ooo - I1ii11iIi11i + o0oOOo0O0Ooo
   if 44 - 44: OoOoOO00 + I1IiiI . I1ii11iIi11i / i1IIi + II111iiii . Oo0Ooo
   if 39 - 39: o0oOOo0O0Ooo
 if ( i1iIiiiiiI1I1II == None or i1iIiiiiiI1I1II . is_ipv4 ( ) ) :
  if ( lisp_nat_traversal and i1iIiiiiiI1I1II == None ) :
   oOoO0Ooo = lisp_get_any_translated_rloc ( )
   if ( oOoO0Ooo != None ) : IIIiI = oOoO0Ooo
   if 20 - 20: i11iIiiIii + iIii1I11I1II1 / iII111i . I1IiiI
  OoOOoO . itr_rlocs . append ( IIIiI )
  if 8 - 8: O0 - iII111i - i1IIi * oO0o / II111iiii
 if ( i1iIiiiiiI1I1II == None or i1iIiiiiiI1I1II . is_ipv6 ( ) ) :
  if ( IIO0OooOo00o00 == None or IIO0OooOo00o00 . is_ipv6_link_local ( ) ) :
   IIO0OooOo00o00 = None
  else :
   OoOOoO . itr_rloc_count = 1 if ( i1iIiiiiiI1I1II == None ) else 0
   OoOOoO . itr_rlocs . append ( IIO0OooOo00o00 )
   if 48 - 48: I1ii11iIi11i . IiII * oO0o
   if 92 - 92: OoOoOO00 + oO0o % Ii1I / Ii1I - iII111i
   if 11 - 11: Oo0Ooo % II111iiii * Ii1I + II111iiii
   if 9 - 9: I1Ii111
   if 69 - 69: i1IIi + ooOoO0o + Ii1I
   if 88 - 88: OoOoOO00 + iII111i % O0 + OOooOOo / OoooooooOO / OOooOOo
   if 95 - 95: ooOoO0o . Oo0Ooo % IiII + iII111i
   if 16 - 16: I11i * OoO0O00 % o0oOOo0O0Ooo - O0 % II111iiii - I1IiiI
   if 72 - 72: OoooooooOO * OoOoOO00 . OOooOOo + Ii1I . OOooOOo / II111iiii
 if ( i1iIiiiiiI1I1II != None and OoOOoO . itr_rlocs != [ ] ) :
  o00O00oOO00 = OoOOoO . itr_rlocs [ 0 ]
 else :
  if ( deid . is_ipv4 ( ) ) :
   o00O00oOO00 = IIIiI
  elif ( deid . is_ipv6 ( ) ) :
   o00O00oOO00 = IIO0OooOo00o00
  else :
   o00O00oOO00 = IIIiI
   if 8 - 8: i1IIi
   if 1 - 1: OoOoOO00 . OoO0O00 . OoO0O00 * O0
   if 97 - 97: OoooooooOO % ooOoO0o . I1Ii111 / iII111i
   if 59 - 59: II111iiii + O0 . I1ii11iIi11i . Oo0Ooo * OoO0O00
   if 35 - 35: oO0o / I1Ii111 * OOooOOo + OoooooooOO . IiII
   if 1 - 1: I1IiiI + I1Ii111 / OOooOOo . Ii1I . oO0o / I1ii11iIi11i
 IiiiIi1iiii11 = OoOOoO . encode ( i1iIiiiiiI1I1II , o0oOO )
 OoOOoO . print_map_request ( )
 if 54 - 54: OOooOOo
 if 86 - 86: oO0o * Oo0Ooo / OOooOOo
 if 18 - 18: II111iiii - I1Ii111
 if 13 - 13: i11iIiiIii - O0 % OoOoOO00 + OOooOOo * ooOoO0o
 if 55 - 55: i1IIi - OOooOOo / I11i * Ii1I
 if 20 - 20: OoOoOO00 * iIii1I11I1II1 % O0 - i1IIi
 if ( i1iIiiiiiI1I1II != None ) :
  if ( rloc . is_rloc_translated ( ) ) :
   i1II1iiI = lisp_get_nat_info ( i1iIiiiiiI1I1II , rloc . rloc_name )
   if 51 - 51: I1ii11iIi11i * Ii1I - oO0o / O0 * OoooooooOO
   if 12 - 12: i1IIi / iIii1I11I1II1 / O0 * OoO0O00
   if 15 - 15: i11iIiiIii / IiII + Ii1I % OOooOOo % I1ii11iIi11i * oO0o
   if 24 - 24: OOooOOo / OOooOOo + I11i / iII111i . oO0o - iII111i
   if ( i1II1iiI == None ) :
    I1I111iIiI = rloc . rloc . print_address_no_iid ( )
    i11ii = "gleaned-{}" . format ( I1I111iIiI )
    IiI1i1i1 = rloc . translated_port
    i1II1iiI = lisp_nat_info ( I1I111iIiI , i11ii , IiI1i1i1 )
    if 59 - 59: I1ii11iIi11i % II111iiii - i11iIiiIii - I1Ii111
   lisp_encapsulate_rloc_probe ( lisp_sockets , i1iIiiiiiI1I1II , i1II1iiI ,
 IiiiIi1iiii11 )
   return
   if 34 - 34: II111iiii + iII111i / IiII
   if 47 - 47: OoO0O00
  oo0o00OO = i1iIiiiiiI1I1II . print_address_no_iid ( )
  Ii1II1I11i1I = lisp_convert_4to6 ( oo0o00OO )
  lisp_send ( lisp_sockets , Ii1II1I11i1I , LISP_CTRL_PORT , IiiiIi1iiii11 )
  return
  if 40 - 40: o0oOOo0O0Ooo / iII111i . o0oOOo0O0Ooo
  if 63 - 63: o0oOOo0O0Ooo * iIii1I11I1II1 * II111iiii . OoO0O00 - oO0o / OoOoOO00
  if 78 - 78: i11iIiiIii / OoO0O00 / i1IIi . i11iIiiIii
  if 100 - 100: II111iiii . IiII . I11i
  if 60 - 60: OoOoOO00 % OOooOOo * i1IIi
  if 3 - 3: OoooooooOO
 Oo00OOoOoooo0 = None if lisp_i_am_rtr else seid
 if ( lisp_decent_pull_xtr_configured ( ) ) :
  I1III11iIIIi = lisp_get_decent_map_resolver ( deid )
 else :
  I1III11iIIIi = lisp_get_map_resolver ( None , Oo00OOoOoooo0 )
  if 51 - 51: O0 * IiII + i11iIiiIii * Ii1I
 if ( I1III11iIIIi == None ) :
  lprint ( "Cannot find Map-Resolver for source-EID {}" . format ( green ( seid . print_address ( ) , False ) ) )
  if 8 - 8: ooOoO0o / II111iiii . I1ii11iIi11i * ooOoO0o % oO0o
  return
  if 36 - 36: I1ii11iIi11i % OOooOOo - ooOoO0o - I11i + I1IiiI
 I1III11iIIIi . last_used = lisp_get_timestamp ( )
 I1III11iIIIi . map_requests_sent += 1
 if ( I1III11iIIIi . last_nonce == 0 ) : I1III11iIIIi . last_nonce = OoOOoO . nonce
 if 37 - 37: I1ii11iIi11i * IiII
 if 65 - 65: OOooOOo / O0 . I1ii11iIi11i % i1IIi % Oo0Ooo
 if 36 - 36: i11iIiiIii - OOooOOo + iII111i + iII111i * I11i * oO0o
 if 14 - 14: O0 - iII111i * I1Ii111 - I1IiiI + IiII
 if ( seid == None ) : seid = o00O00oOO00
 lisp_send_ecm ( lisp_sockets , IiiiIi1iiii11 , seid , lisp_ephem_port , deid ,
 I1III11iIIIi . map_resolver )
 if 46 - 46: OoooooooOO * OoO0O00 . I1Ii111
 if 95 - 95: ooOoO0o . I1ii11iIi11i . ooOoO0o / I1IiiI * OoOoOO00 . O0
 if 78 - 78: oO0o
 if 33 - 33: oO0o + i1IIi
 lisp_last_map_request_sent = lisp_get_timestamp ( )
 if 32 - 32: iIii1I11I1II1
 if 71 - 71: Ii1I * I1IiiI
 if 62 - 62: II111iiii / I1IiiI . I1ii11iIi11i
 if 49 - 49: IiII / OoOoOO00 / O0 * i11iIiiIii
 I1III11iIIIi . resolve_dns_name ( )
 return
 if 47 - 47: i11iIiiIii + iII111i + i11iIiiIii
 if 66 - 66: o0oOOo0O0Ooo . I1IiiI + OoooooooOO . iII111i / OoooooooOO - IiII
 if 47 - 47: o0oOOo0O0Ooo / II111iiii * i11iIiiIii * OoO0O00 . iIii1I11I1II1
 if 34 - 34: I11i / o0oOOo0O0Ooo * OOooOOo * OOooOOo
 if 89 - 89: I1ii11iIi11i . OoooooooOO
 if 61 - 61: i1IIi + i11iIiiIii
 if 59 - 59: i11iIiiIii * OOooOOo + i1IIi * iIii1I11I1II1 + I11i
 if 97 - 97: OoO0O00 - I11i . OoooooooOO
def lisp_send_info_request ( lisp_sockets , dest , port , device_name ) :
 if 58 - 58: I1ii11iIi11i / II111iiii / i11iIiiIii
 if 27 - 27: iIii1I11I1II1 - O0 + OoOoOO00
 if 28 - 28: oO0o . IiII * iII111i % Oo0Ooo - OoO0O00 / I11i
 if 67 - 67: i11iIiiIii + i11iIiiIii / ooOoO0o - o0oOOo0O0Ooo
 OooO0o0 = lisp_info ( )
 OooO0o0 . nonce = lisp_get_control_nonce ( )
 if ( device_name ) : OooO0o0 . hostname += "-" + device_name
 if 29 - 29: o0oOOo0O0Ooo
 oo0o00OO = dest . print_address_no_iid ( )
 if 51 - 51: OoOoOO00 / Ii1I . I1IiiI / Ii1I . II111iiii - iIii1I11I1II1
 if 78 - 78: I11i
 if 42 - 42: Ii1I
 if 50 - 50: iIii1I11I1II1 / Ii1I . ooOoO0o / ooOoO0o * OoOoOO00 * iII111i
 if 15 - 15: o0oOOo0O0Ooo % II111iiii + I1IiiI
 if 21 - 21: I1ii11iIi11i - ooOoO0o
 if 81 - 81: iII111i / i11iIiiIii / I1Ii111
 if 70 - 70: I1ii11iIi11i / i11iIiiIii
 if 90 - 90: II111iiii / OoOoOO00 . Ii1I . OoooooooOO
 if 76 - 76: OoooooooOO
 if 78 - 78: IiII % i11iIiiIii
 if 23 - 23: iIii1I11I1II1 - o0oOOo0O0Ooo - Ii1I % OOooOOo
 if 100 - 100: oO0o . OoO0O00 . i11iIiiIii % II111iiii * IiII
 if 81 - 81: OOooOOo - OOooOOo + OoOoOO00
 if 19 - 19: o0oOOo0O0Ooo
 if 20 - 20: I1Ii111 + iIii1I11I1II1 % I1IiiI + ooOoO0o
 oOOo00oOO00o = False
 if ( device_name ) :
  III1Iii1iIi = lisp_get_host_route_next_hop ( oo0o00OO )
  if 71 - 71: oO0o % i11iIiiIii + I1Ii111 . OoooooooOO * i1IIi
  if 85 - 85: II111iiii - Oo0Ooo . OoOoOO00 - i1IIi - I1ii11iIi11i
  if 24 - 24: ooOoO0o % ooOoO0o - I1ii11iIi11i - OoO0O00 % I1IiiI
  if 8 - 8: iIii1I11I1II1 - O0 - i11iIiiIii . O0
  if 35 - 35: Ii1I . II111iiii % OoOoOO00
  if 3 - 3: OOooOOo - OoOoOO00
  if 49 - 49: IiII / i11iIiiIii
  if 84 - 84: iIii1I11I1II1 / i1IIi + OoOoOO00
  if 40 - 40: Ii1I % OoO0O00
  if ( port == LISP_CTRL_PORT and III1Iii1iIi != None ) :
   while ( True ) :
    time . sleep ( .01 )
    III1Iii1iIi = lisp_get_host_route_next_hop ( oo0o00OO )
    if ( III1Iii1iIi == None ) : break
    if 93 - 93: iII111i . I1Ii111 . oO0o % o0oOOo0O0Ooo . Oo0Ooo
    if 51 - 51: OOooOOo * OoO0O00 * Oo0Ooo
    if 61 - 61: II111iiii / OoOoOO00 % II111iiii / I1ii11iIi11i % I1Ii111 - i1IIi
  i1I1iiii111 = lisp_get_default_route_next_hops ( )
  for OoO0o0OOOO , o0OoiIiIIi in i1I1iiii111 :
   if ( OoO0o0OOOO != device_name ) : continue
   if 34 - 34: oO0o * I1ii11iIi11i . OoOoOO00 - I1ii11iIi11i * I1IiiI * Ii1I
   if 41 - 41: OoOoOO00 . OOooOOo / OoOoOO00 % iIii1I11I1II1
   if 47 - 47: ooOoO0o . i11iIiiIii / OoO0O00
   if 48 - 48: O0
   if 89 - 89: i11iIiiIii % OoO0O00 . OoOoOO00 + Oo0Ooo + OoOoOO00
   if 53 - 53: Ii1I / OoOoOO00 % iII111i * OoooooooOO + Oo0Ooo
   if ( III1Iii1iIi != o0OoiIiIIi ) :
    if ( III1Iii1iIi != None ) :
     lisp_install_host_route ( oo0o00OO , III1Iii1iIi , False )
     if 70 - 70: OoO0O00 % OoO0O00 * OoooooooOO
    lisp_install_host_route ( oo0o00OO , o0OoiIiIIi , True )
    oOOo00oOO00o = True
    if 96 - 96: ooOoO0o * Ii1I + I11i + II111iiii * I1IiiI / iII111i
   break
   if 40 - 40: OoooooooOO - I11i % OOooOOo - I1IiiI . I1IiiI + Ii1I
   if 97 - 97: OOooOOo . OoooooooOO . OOooOOo . i11iIiiIii
   if 71 - 71: oO0o + I1ii11iIi11i * I1ii11iIi11i
   if 79 - 79: oO0o
   if 47 - 47: OoooooooOO - i1IIi * OOooOOo
   if 11 - 11: I11i / OOooOOo . o0oOOo0O0Ooo - O0 * OoooooooOO % iII111i
 IiiiIi1iiii11 = OooO0o0 . encode ( )
 OooO0o0 . print_info ( )
 if 7 - 7: OoOoOO00 . IiII + OoooooooOO - I1Ii111 / oO0o
 if 32 - 32: iIii1I11I1II1 + I11i + OOooOOo - OoooooooOO + i11iIiiIii * o0oOOo0O0Ooo
 if 8 - 8: iII111i
 if 10 - 10: OoOoOO00 % I11i
 iII1iiIIiiI = "(for control)" if port == LISP_CTRL_PORT else "(for data)"
 iII1iiIIiiI = bold ( iII1iiIIiiI , False )
 IiI1i1i1 = bold ( "{}" . format ( port ) , False )
 oO0OO = red ( oo0o00OO , False )
 iIi = "RTR " if port == LISP_DATA_PORT else "MS "
 lprint ( "Send Info-Request to {}{}, port {} {}" . format ( iIi , oO0OO , IiI1i1i1 , iII1iiIIiiI ) )
 if 63 - 63: ooOoO0o + O0
 if 47 - 47: i1IIi - II111iiii - II111iiii
 if 31 - 31: Ii1I
 if 37 - 37: I1ii11iIi11i - Ii1I / oO0o . I1IiiI % I1Ii111
 if 8 - 8: oO0o
 if 46 - 46: I1Ii111 + IiII + II111iiii . o0oOOo0O0Ooo + i11iIiiIii
 if ( port == LISP_CTRL_PORT ) :
  lisp_send ( lisp_sockets , dest , LISP_CTRL_PORT , IiiiIi1iiii11 )
 else :
  O00O0OO = lisp_data_header ( )
  O00O0OO . instance_id ( 0xffffff )
  O00O0OO = O00O0OO . encode ( )
  if ( O00O0OO ) :
   IiiiIi1iiii11 = O00O0OO + IiiiIi1iiii11
   if 97 - 97: o0oOOo0O0Ooo % OoOoOO00 * O0 / iIii1I11I1II1 * OoO0O00 / i11iIiiIii
   if 1 - 1: OoooooooOO . Ii1I
   if 68 - 68: Ii1I
   if 98 - 98: iII111i
   if 33 - 33: OoO0O00 - ooOoO0o % O0 % iIii1I11I1II1 * iII111i - iII111i
   if 27 - 27: i11iIiiIii + I1ii11iIi11i + i1IIi
   if 67 - 67: o0oOOo0O0Ooo
   if 58 - 58: IiII % o0oOOo0O0Ooo + i1IIi
   if 33 - 33: II111iiii
   lisp_send ( lisp_sockets , dest , LISP_DATA_PORT , IiiiIi1iiii11 )
   if 61 - 61: I1Ii111
   if 56 - 56: I1ii11iIi11i - OoooooooOO
   if 52 - 52: Oo0Ooo - I11i - IiII - OoOoOO00
   if 21 - 21: oO0o % o0oOOo0O0Ooo + I1Ii111 . OOooOOo / OOooOOo
   if 41 - 41: Oo0Ooo . ooOoO0o * oO0o
   if 31 - 31: Oo0Ooo * IiII / IiII
   if 3 - 3: I1Ii111
 if ( oOOo00oOO00o ) :
  lisp_install_host_route ( oo0o00OO , None , False )
  if ( III1Iii1iIi != None ) : lisp_install_host_route ( oo0o00OO , III1Iii1iIi , True )
  if 65 - 65: iIii1I11I1II1 % Oo0Ooo % I11i / OoooooooOO
 return
 if 82 - 82: o0oOOo0O0Ooo
 if 33 - 33: OoOoOO00 / i11iIiiIii - I1IiiI - OoooooooOO + i1IIi * I1Ii111
 if 92 - 92: iII111i + OoO0O00
 if 70 - 70: iIii1I11I1II1
 if 100 - 100: OOooOOo . oO0o % ooOoO0o * ooOoO0o . I1Ii111 - oO0o
 if 33 - 33: Oo0Ooo . i1IIi - OoooooooOO
 if 14 - 14: I1Ii111 + Oo0Ooo
def lisp_process_info_request ( lisp_sockets , packet , addr_str , sport , rtr_list ) :
 if 35 - 35: i11iIiiIii * Ii1I
 if 100 - 100: O0 . iII111i / iIii1I11I1II1
 if 47 - 47: ooOoO0o + OoOoOO00
 if 67 - 67: IiII - I1ii11iIi11i * i1IIi - ooOoO0o
 OooO0o0 = lisp_info ( )
 packet = OooO0o0 . decode ( packet )
 if ( packet == None ) : return
 OooO0o0 . print_info ( )
 if 91 - 91: I11i
 if 54 - 54: I1ii11iIi11i / i1IIi
 if 14 - 14: iIii1I11I1II1 * I11i . I11i * ooOoO0o * iII111i
 if 60 - 60: iIii1I11I1II1 + i1IIi + oO0o - iIii1I11I1II1 . i11iIiiIii * OoooooooOO
 if 23 - 23: iII111i - IiII % i11iIiiIii
 OooO0o0 . info_reply = True
 OooO0o0 . global_etr_rloc . store_address ( addr_str )
 OooO0o0 . etr_port = sport
 if 81 - 81: OoooooooOO % OoOoOO00 / IiII / OoooooooOO + i1IIi - O0
 if 60 - 60: OOooOOo - I1Ii111 * Oo0Ooo
 if 9 - 9: OoooooooOO * OOooOOo % OoO0O00 - ooOoO0o + Ii1I
 if 39 - 39: iIii1I11I1II1 / i1IIi % I11i % I1ii11iIi11i * IiII
 if 11 - 11: II111iiii + i1IIi
 if ( OooO0o0 . hostname != None ) :
  OooO0o0 . private_etr_rloc . afi = LISP_AFI_NAME
  OooO0o0 . private_etr_rloc . store_address ( OooO0o0 . hostname )
  if 1 - 1: OOooOOo
  if 23 - 23: i1IIi + OoooooooOO * OOooOOo . Oo0Ooo
 if ( rtr_list != None ) : OooO0o0 . rtr_list = rtr_list
 packet = OooO0o0 . encode ( )
 OooO0o0 . print_info ( )
 if 83 - 83: OoooooooOO
 if 53 - 53: o0oOOo0O0Ooo - Oo0Ooo / IiII + O0
 if 88 - 88: Oo0Ooo % I1Ii111 * O0 - i1IIi * OoO0O00
 if 74 - 74: Oo0Ooo % iIii1I11I1II1 + OOooOOo
 if 50 - 50: OoO0O00 . OoooooooOO
 lprint ( "Send Info-Reply to {}" . format ( red ( addr_str , False ) ) )
 Ii1II1I11i1I = lisp_convert_4to6 ( addr_str )
 lisp_send ( lisp_sockets , Ii1II1I11i1I , sport , packet )
 if 31 - 31: OoO0O00
 if 55 - 55: OoOoOO00 + I1Ii111 * o0oOOo0O0Ooo - I1ii11iIi11i + OoOoOO00
 if 6 - 6: II111iiii % iIii1I11I1II1 * I1Ii111
 if 2 - 2: IiII - I1Ii111 . iIii1I11I1II1 - Ii1I * I11i
 if 58 - 58: i1IIi % iIii1I11I1II1 % i11iIiiIii - o0oOOo0O0Ooo + ooOoO0o
 iIiI1I1111I = lisp_info_source ( OooO0o0 . hostname , addr_str , sport )
 iIiI1I1111I . cache_address_for_info_source ( )
 return
 if 66 - 66: Oo0Ooo % i11iIiiIii . OoO0O00 / i11iIiiIii - iIii1I11I1II1 % I1Ii111
 if 10 - 10: i11iIiiIii - Ii1I - OoooooooOO % II111iiii
 if 42 - 42: OoOoOO00 + iII111i % Oo0Ooo
 if 25 - 25: IiII % O0 * I11i * OoOoOO00 / OoooooooOO
 if 80 - 80: I1IiiI . oO0o - I1IiiI - OoOoOO00 * ooOoO0o / O0
 if 54 - 54: Oo0Ooo % iIii1I11I1II1 * Oo0Ooo
 if 80 - 80: I1ii11iIi11i - I1ii11iIi11i
 if 26 - 26: I1ii11iIi11i - I1IiiI * I1Ii111 % iIii1I11I1II1
def lisp_get_signature_eid ( ) :
 for ii1iii in lisp_db_list :
  if ( ii1iii . signature_eid ) : return ( ii1iii )
  if 77 - 77: o0oOOo0O0Ooo + I1Ii111 . OOooOOo . i1IIi . I1IiiI
 return ( None )
 if 100 - 100: ooOoO0o . i11iIiiIii + Ii1I - OOooOOo - i11iIiiIii - OoooooooOO
 if 42 - 42: OoOoOO00 . I1IiiI / OoOoOO00 / I1ii11iIi11i . OoO0O00
 if 67 - 67: Ii1I - O0 . OoooooooOO . I1Ii111 . o0oOOo0O0Ooo
 if 73 - 73: I11i - oO0o . I1Ii111 + oO0o
 if 48 - 48: IiII . IiII * o0oOOo0O0Ooo * II111iiii % ooOoO0o
 if 40 - 40: I1ii11iIi11i
 if 76 - 76: Oo0Ooo - I11i
 if 82 - 82: OoO0O00 % oO0o . I11i / O0 - I1Ii111
def lisp_get_any_translated_port ( ) :
 for ii1iii in lisp_db_list :
  for oOO0O in ii1iii . rloc_set :
   if ( oOO0O . translated_rloc . is_null ( ) ) : continue
   return ( oOO0O . translated_port )
   if 39 - 39: I1IiiI
   if 8 - 8: IiII * i1IIi * i1IIi * O0
 return ( None )
 if 69 - 69: Oo0Ooo
 if 48 - 48: iII111i
 if 11 - 11: i11iIiiIii * OoOoOO00 . OoO0O00
 if 47 - 47: Oo0Ooo % I1Ii111 + ooOoO0o
 if 89 - 89: iII111i
 if 29 - 29: I1ii11iIi11i . ooOoO0o * II111iiii / iII111i . OoooooooOO - OoOoOO00
 if 99 - 99: IiII % O0 - I1Ii111 * OoO0O00
 if 77 - 77: OoooooooOO - I11i / I1IiiI % OoOoOO00 - OOooOOo
 if 37 - 37: ooOoO0o
def lisp_get_any_translated_rloc ( ) :
 for ii1iii in lisp_db_list :
  for oOO0O in ii1iii . rloc_set :
   if ( oOO0O . translated_rloc . is_null ( ) ) : continue
   return ( oOO0O . translated_rloc )
   if 22 - 22: I1ii11iIi11i + II111iiii / OoooooooOO % o0oOOo0O0Ooo * OoOoOO00 . Oo0Ooo
   if 26 - 26: OoO0O00 % oO0o * Ii1I % OoooooooOO - oO0o
 return ( None )
 if 46 - 46: I1IiiI + OoO0O00 - O0 * O0
 if 75 - 75: OOooOOo + iIii1I11I1II1 * OOooOOo
 if 82 - 82: iII111i - I1Ii111 - OoOoOO00
 if 96 - 96: Oo0Ooo . Oo0Ooo % o0oOOo0O0Ooo - I1IiiI * iIii1I11I1II1
 if 29 - 29: i1IIi / Ii1I / oO0o * iII111i
 if 44 - 44: O0
 if 95 - 95: OOooOOo + OOooOOo - OoOoOO00
def lisp_get_all_translated_rlocs ( ) :
 OoO0OooO0Oo0o = [ ]
 for ii1iii in lisp_db_list :
  for oOO0O in ii1iii . rloc_set :
   if ( oOO0O . is_rloc_translated ( ) == False ) : continue
   o0o00O0oOooO0 = oOO0O . translated_rloc . print_address_no_iid ( )
   OoO0OooO0Oo0o . append ( o0o00O0oOooO0 )
   if 83 - 83: Oo0Ooo
   if 83 - 83: ooOoO0o * iIii1I11I1II1
 return ( OoO0OooO0Oo0o )
 if 60 - 60: OoOoOO00 . OoOoOO00 - O0 % OoooooooOO % II111iiii - iII111i
 if 89 - 89: O0 - OoO0O00
 if 8 - 8: I1ii11iIi11i / oO0o - OoooooooOO + ooOoO0o + o0oOOo0O0Ooo % i11iIiiIii
 if 32 - 32: O0 + IiII
 if 93 - 93: OoOoOO00 - I11i / iII111i - iIii1I11I1II1 + I11i % oO0o
 if 24 - 24: Ii1I / iIii1I11I1II1 + o0oOOo0O0Ooo
 if 17 - 17: OOooOOo
 if 75 - 75: Ii1I / i1IIi % I1ii11iIi11i . Ii1I
def lisp_update_default_routes ( map_resolver , iid , rtr_list ) :
 OOOo0O00OO00O = ( os . getenv ( "LISP_RTR_BEHIND_NAT" ) != None )
 if 46 - 46: II111iiii * OoO0O00
 o00000OO0ooOo = { }
 for I1II in rtr_list :
  if ( I1II == None ) : continue
  o0o00O0oOooO0 = rtr_list [ I1II ]
  if ( OOOo0O00OO00O and o0o00O0oOooO0 . is_private_address ( ) ) : continue
  o00000OO0ooOo [ I1II ] = o0o00O0oOooO0
  if 47 - 47: Ii1I % II111iiii
 rtr_list = o00000OO0ooOo
 if 88 - 88: OoOoOO00 / oO0o - OoOoOO00 / OoOoOO00 % II111iiii
 IiII11IiIiiI = [ ]
 for IiiiII in [ LISP_AFI_IPV4 , LISP_AFI_IPV6 , LISP_AFI_MAC ] :
  if ( IiiiII == LISP_AFI_MAC and lisp_l2_overlay == False ) : break
  if 64 - 64: I1Ii111 - I11i + oO0o . oO0o
  if 22 - 22: Oo0Ooo / OOooOOo - iIii1I11I1II1 / ooOoO0o
  if 7 - 7: ooOoO0o . OoooooooOO . iII111i * II111iiii . II111iiii / OOooOOo
  if 46 - 46: Ii1I - Oo0Ooo / i1IIi % IiII - I1ii11iIi11i + OOooOOo
  if 42 - 42: i1IIi - IiII % OOooOOo % iIii1I11I1II1
  I11i11IIIII = lisp_address ( IiiiII , "" , 0 , iid )
  I11i11IIIII . make_default_route ( I11i11IIIII )
  o0Oo0 = lisp_map_cache . lookup_cache ( I11i11IIIII , True )
  if ( o0Oo0 ) :
   if ( o0Oo0 . checkpoint_entry ) :
    lprint ( "Updating checkpoint entry for {}" . format ( green ( o0Oo0 . print_eid_tuple ( ) , False ) ) )
    if 71 - 71: OoO0O00
   elif ( o0Oo0 . do_rloc_sets_match ( rtr_list . values ( ) ) ) :
    continue
    if 72 - 72: II111iiii + o0oOOo0O0Ooo / i1IIi * Oo0Ooo / i1IIi
   o0Oo0 . delete_cache ( )
   if 52 - 52: I1Ii111 % OoO0O00 . I1Ii111 * I1ii11iIi11i * OoOoOO00 + i1IIi
   if 54 - 54: Ii1I / I1IiiI
  IiII11IiIiiI . append ( [ I11i11IIIII , "" ] )
  if 7 - 7: iIii1I11I1II1 . O0 + OOooOOo . Ii1I * Oo0Ooo
  if 25 - 25: I1Ii111 . Oo0Ooo % II111iiii . IiII - O0
  if 18 - 18: oO0o * OOooOOo
  if 19 - 19: iIii1I11I1II1 / I1ii11iIi11i - I1ii11iIi11i / iIii1I11I1II1
  OOo0oOOO0 = lisp_address ( IiiiII , "" , 0 , iid )
  OOo0oOOO0 . make_default_multicast_route ( OOo0oOOO0 )
  IiI11 = lisp_map_cache . lookup_cache ( OOo0oOOO0 , True )
  if ( IiI11 ) : IiI11 = IiI11 . source_cache . lookup_cache ( I11i11IIIII , True )
  if ( IiI11 ) : IiI11 . delete_cache ( )
  if 6 - 6: i1IIi / I1IiiI
  IiII11IiIiiI . append ( [ I11i11IIIII , OOo0oOOO0 ] )
  if 79 - 79: OOooOOo
 if ( len ( IiII11IiIiiI ) == 0 ) : return
 if 75 - 75: OoO0O00 - I1Ii111 . ooOoO0o . o0oOOo0O0Ooo
 if 82 - 82: I11i / I1ii11iIi11i
 if 79 - 79: oO0o
 if 6 - 6: IiII . o0oOOo0O0Ooo
 OoO0oOOooOO = [ ]
 for iIi in rtr_list :
  I1IiiI11 = rtr_list [ iIi ]
  oOO0O = lisp_rloc ( )
  oOO0O . rloc . copy_address ( I1IiiI11 )
  oOO0O . priority = 254
  oOO0O . mpriority = 255
  oOO0O . rloc_name = "RTR"
  OoO0oOOooOO . append ( oOO0O )
  if 23 - 23: I1IiiI
  if 51 - 51: i11iIiiIii / ooOoO0o - OoooooooOO + OoOoOO00 + oO0o
 for I11i11IIIII in IiII11IiIiiI :
  o0Oo0 = lisp_mapping ( I11i11IIIII [ 0 ] , I11i11IIIII [ 1 ] , OoO0oOOooOO )
  o0Oo0 . mapping_source = map_resolver
  o0Oo0 . map_cache_ttl = LISP_MR_TTL * 60
  o0Oo0 . add_cache ( )
  lprint ( "Add {} to map-cache with RTR RLOC-set: {}" . format ( green ( o0Oo0 . print_eid_tuple ( ) , False ) , rtr_list . keys ( ) ) )
  if 57 - 57: iIii1I11I1II1
  OoO0oOOooOO = copy . deepcopy ( OoO0oOOooOO )
  if 19 - 19: Ii1I / o0oOOo0O0Ooo + O0 / iIii1I11I1II1 + II111iiii
 return
 if 3 - 3: oO0o % OoO0O00 % OOooOOo
 if 64 - 64: o0oOOo0O0Ooo . II111iiii * IiII % Oo0Ooo + I11i - OoooooooOO
 if 58 - 58: ooOoO0o
 if 15 - 15: O0 * OOooOOo * I11i + Ii1I * OoooooooOO + OOooOOo
 if 77 - 77: O0
 if 98 - 98: iII111i - iII111i % i1IIi - I1Ii111 . I1IiiI % o0oOOo0O0Ooo
 if 38 - 38: IiII % OoOoOO00 . OOooOOo . I1ii11iIi11i
 if 34 - 34: iII111i . i11iIiiIii + OoO0O00 + o0oOOo0O0Ooo / ooOoO0o - i11iIiiIii
 if 63 - 63: ooOoO0o % OoO0O00 % ooOoO0o
 if 28 - 28: IiII * I1Ii111 * o0oOOo0O0Ooo + ooOoO0o - IiII / IiII
def lisp_process_info_reply ( source , packet , store ) :
 if 73 - 73: iIii1I11I1II1 . I1ii11iIi11i + OOooOOo
 if 51 - 51: I11i % Oo0Ooo * OOooOOo % OoooooooOO - OoOoOO00 % Ii1I
 if 60 - 60: OoOoOO00 - IiII + OoO0O00
 if 77 - 77: iIii1I11I1II1
 OooO0o0 = lisp_info ( )
 packet = OooO0o0 . decode ( packet )
 if ( packet == None ) : return ( [ None , None , False ] )
 if 92 - 92: IiII
 OooO0o0 . print_info ( )
 if 68 - 68: OOooOOo . IiII / iIii1I11I1II1 % i11iIiiIii
 if 74 - 74: iII111i + i11iIiiIii
 if 95 - 95: Ii1I
 if 49 - 49: I1ii11iIi11i . i1IIi + OoO0O00 % O0 + OoO0O00
 I1iI1ii1iiIII = False
 for iIi in OooO0o0 . rtr_list :
  oo0o00OO = iIi . print_address_no_iid ( )
  if ( lisp_rtr_list . has_key ( oo0o00OO ) ) :
   if ( lisp_register_all_rtrs == False ) : continue
   if ( lisp_rtr_list [ oo0o00OO ] != None ) : continue
   if 32 - 32: IiII
  I1iI1ii1iiIII = True
  lisp_rtr_list [ oo0o00OO ] = iIi
  if 2 - 2: iII111i / IiII % iIii1I11I1II1 . iII111i + iIii1I11I1II1 + O0
  if 96 - 96: I1ii11iIi11i - IiII % OoooooooOO . iII111i
  if 30 - 30: Oo0Ooo . OoooooooOO / Oo0Ooo / oO0o
  if 44 - 44: I1ii11iIi11i % o0oOOo0O0Ooo / iIii1I11I1II1 - o0oOOo0O0Ooo / I11i * I1Ii111
  if 49 - 49: iII111i / iII111i - OoOoOO00
 if ( lisp_i_am_itr and I1iI1ii1iiIII ) :
  if ( lisp_iid_to_interface == { } ) :
   lisp_update_default_routes ( source , lisp_default_iid , lisp_rtr_list )
  else :
   for IiIIi11i111 in lisp_iid_to_interface . keys ( ) :
    lisp_update_default_routes ( source , int ( IiIIi11i111 ) , lisp_rtr_list )
    if 89 - 89: ooOoO0o
    if 16 - 16: oO0o + oO0o + i1IIi + iIii1I11I1II1
    if 93 - 93: I1IiiI - i11iIiiIii * I1Ii111 - O0 + iII111i
    if 11 - 11: iII111i
    if 100 - 100: OoooooooOO / ooOoO0o . OoO0O00
    if 89 - 89: I11i % II111iiii
    if 35 - 35: oO0o
 if ( store == False ) :
  return ( [ OooO0o0 . global_etr_rloc , OooO0o0 . etr_port , I1iI1ii1iiIII ] )
  if 65 - 65: II111iiii
  if 87 - 87: oO0o / OoO0O00 - oO0o
  if 69 - 69: i11iIiiIii
  if 29 - 29: IiII . ooOoO0o / iII111i - OOooOOo / OOooOOo % Oo0Ooo
  if 42 - 42: OoO0O00 . I1Ii111 . I1IiiI + Oo0Ooo * O0
  if 35 - 35: Oo0Ooo / iII111i - O0 - OOooOOo * Oo0Ooo . i11iIiiIii
 for ii1iii in lisp_db_list :
  for oOO0O in ii1iii . rloc_set :
   I1II = oOO0O . rloc
   II1i = oOO0O . interface
   if ( II1i == None ) :
    if ( I1II . is_null ( ) ) : continue
    if ( I1II . is_local ( ) == False ) : continue
    if ( OooO0o0 . private_etr_rloc . is_null ( ) == False and
 I1II . is_exact_match ( OooO0o0 . private_etr_rloc ) == False ) :
     continue
     if 43 - 43: OoOoOO00 % oO0o % OoO0O00 / Ii1I . I11i
   elif ( OooO0o0 . private_etr_rloc . is_dist_name ( ) ) :
    IIiiI11iI = OooO0o0 . private_etr_rloc . address
    if ( IIiiI11iI != oOO0O . rloc_name ) : continue
    if 86 - 86: I1Ii111 * i1IIi + IiII - OoOoOO00
    if 14 - 14: I1ii11iIi11i / i11iIiiIii * I11i % o0oOOo0O0Ooo + IiII / I1ii11iIi11i
   Ii1i1 = green ( ii1iii . eid . print_prefix ( ) , False )
   O0ooo0Ooo = red ( I1II . print_address_no_iid ( ) , False )
   if 82 - 82: OOooOOo . oO0o
   iiiIiiI = OooO0o0 . global_etr_rloc . is_exact_match ( I1II )
   if ( oOO0O . translated_port == 0 and iiiIiiI ) :
    lprint ( "No NAT for {} ({}), EID-prefix {}" . format ( O0ooo0Ooo ,
 II1i , Ii1i1 ) )
    continue
    if 67 - 67: i1IIi
    if 51 - 51: O0 + O0 / I1Ii111 % Oo0Ooo * iIii1I11I1II1 - o0oOOo0O0Ooo
    if 95 - 95: O0 * OoooooooOO / II111iiii - i1IIi
    if 36 - 36: i1IIi * oO0o / i1IIi % oO0o
    if 9 - 9: Ii1I / iIii1I11I1II1
   O0oO = OooO0o0 . global_etr_rloc
   iII111I = oOO0O . translated_rloc
   if ( iII111I . is_exact_match ( O0oO ) and
 OooO0o0 . etr_port == oOO0O . translated_port ) : continue
   if 66 - 66: IiII * i11iIiiIii
   lprint ( "Store translation {}:{} for {} ({}), EID-prefix {}" . format ( red ( OooO0o0 . global_etr_rloc . print_address_no_iid ( ) , False ) ,
   # iIii1I11I1II1 - I11i . I11i * i11iIiiIii
 OooO0o0 . etr_port , O0ooo0Ooo , II1i , Ii1i1 ) )
   if 73 - 73: Oo0Ooo + I1IiiI - OoooooooOO * oO0o
   oOO0O . store_translated_rloc ( OooO0o0 . global_etr_rloc ,
 OooO0o0 . etr_port )
   if 20 - 20: OoOoOO00 % II111iiii
   if 46 - 46: o0oOOo0O0Ooo % i11iIiiIii * ooOoO0o / i1IIi * i1IIi
 return ( [ OooO0o0 . global_etr_rloc , OooO0o0 . etr_port , I1iI1ii1iiIII ] )
 if 71 - 71: I1IiiI + i1IIi
 if 96 - 96: I1Ii111 . Oo0Ooo % I11i % I1ii11iIi11i % II111iiii * IiII
 if 69 - 69: OoO0O00 * Oo0Ooo * iII111i
 if 2 - 2: iII111i - Ii1I
 if 1 - 1: I1Ii111 / oO0o + iIii1I11I1II1
 if 88 - 88: o0oOOo0O0Ooo
 if 3 - 3: i11iIiiIii / I1ii11iIi11i
 if 49 - 49: IiII
def lisp_test_mr ( lisp_sockets , port ) :
 return
 lprint ( "Test Map-Resolvers" )
 if 1 - 1: oO0o / I11i
 iiI1I1IIi = lisp_address ( LISP_AFI_IPV4 , "" , 0 , 0 )
 OOO0O0Oo0O0 = lisp_address ( LISP_AFI_IPV6 , "" , 0 , 0 )
 if 53 - 53: iII111i
 if 7 - 7: OoooooooOO . Ii1I - OoooooooOO / i1IIi / i1IIi / iIii1I11I1II1
 if 78 - 78: i11iIiiIii / O0 . OoooooooOO % i11iIiiIii / iIii1I11I1II1 . OoooooooOO
 if 1 - 1: oO0o - i11iIiiIii . OoOoOO00
 iiI1I1IIi . store_address ( "10.0.0.1" )
 lisp_send_map_request ( lisp_sockets , port , None , iiI1I1IIi , None )
 iiI1I1IIi . store_address ( "192.168.0.1" )
 lisp_send_map_request ( lisp_sockets , port , None , iiI1I1IIi , None )
 if 16 - 16: OOooOOo
 if 33 - 33: o0oOOo0O0Ooo / OoO0O00 + OoooooooOO
 if 82 - 82: o0oOOo0O0Ooo / i1IIi / i11iIiiIii * Oo0Ooo / OoO0O00
 if 95 - 95: I11i . OoOoOO00 * Ii1I
 OOO0O0Oo0O0 . store_address ( "0100::1" )
 lisp_send_map_request ( lisp_sockets , port , None , OOO0O0Oo0O0 , None )
 OOO0O0Oo0O0 . store_address ( "8000::1" )
 lisp_send_map_request ( lisp_sockets , port , None , OOO0O0Oo0O0 , None )
 if 94 - 94: OoOoOO00 / OoO0O00 / ooOoO0o + II111iiii
 if 55 - 55: II111iiii - IiII
 if 24 - 24: oO0o % Ii1I / i1IIi
 if 84 - 84: i1IIi
 ooOo00OO = threading . Timer ( LISP_TEST_MR_INTERVAL , lisp_test_mr ,
 [ lisp_sockets , port ] )
 ooOo00OO . start ( )
 return
 if 59 - 59: o0oOOo0O0Ooo % Ii1I / o0oOOo0O0Ooo % IiII % OOooOOo + o0oOOo0O0Ooo
 if 19 - 19: O0 + i11iIiiIii % O0 / II111iiii
 if 56 - 56: O0 + Oo0Ooo * II111iiii * iII111i * iII111i / I1Ii111
 if 52 - 52: oO0o
 if 73 - 73: IiII - II111iiii - OOooOOo % II111iiii + iIii1I11I1II1
 if 81 - 81: i11iIiiIii - O0 + I1IiiI
 if 39 - 39: IiII * OOooOOo . OoooooooOO + Oo0Ooo + iIii1I11I1II1
 if 67 - 67: iII111i . OOooOOo / ooOoO0o * iIii1I11I1II1
 if 29 - 29: I1Ii111 / OoOoOO00 % I1ii11iIi11i * IiII / II111iiii
 if 10 - 10: O0 / I11i
 if 29 - 29: i11iIiiIii % I11i
 if 49 - 49: I11i
 if 69 - 69: o0oOOo0O0Ooo . O0 * I11i
def lisp_update_local_rloc ( rloc ) :
 if ( rloc . interface == None ) : return
 if 92 - 92: OoO0O00 . O0 / Ii1I % Oo0Ooo . Ii1I
 o0o00O0oOooO0 = lisp_get_interface_address ( rloc . interface )
 if ( o0o00O0oOooO0 == None ) : return
 if 40 - 40: o0oOOo0O0Ooo - Ii1I . iII111i - O0
 OO0oooo00 = rloc . rloc . print_address_no_iid ( )
 Ooo00O0ooOo = o0o00O0oOooO0 . print_address_no_iid ( )
 if 60 - 60: Ii1I . Ii1I . I11i / OoooooooOO + I1IiiI % iIii1I11I1II1
 if ( OO0oooo00 == Ooo00O0ooOo ) : return
 if 8 - 8: IiII + IiII / I1ii11iIi11i
 lprint ( "Local interface address changed on {} from {} to {}" . format ( rloc . interface , OO0oooo00 , Ooo00O0ooOo ) )
 if 49 - 49: I11i + OOooOOo - I1ii11iIi11i
 if 23 - 23: OOooOOo % I1ii11iIi11i + iIii1I11I1II1 + iII111i
 rloc . rloc . copy_address ( o0o00O0oOooO0 )
 lisp_myrlocs [ 0 ] = o0o00O0oOooO0
 return
 if 9 - 9: OOooOOo * o0oOOo0O0Ooo / I11i . i11iIiiIii
 if 44 - 44: iII111i - II111iiii
 if 45 - 45: OoO0O00 % iII111i / iIii1I11I1II1 % I1IiiI + OOooOOo
 if 62 - 62: OOooOOo . OOooOOo . oO0o
 if 18 - 18: iII111i . I1IiiI . ooOoO0o * oO0o / OoooooooOO
 if 85 - 85: i1IIi
 if 79 - 79: I11i - I11i
 if 25 - 25: OOooOOo / O0 / iIii1I11I1II1 + II111iiii * Ii1I
def lisp_update_encap_port ( mc ) :
 for I1II in mc . rloc_set :
  i1II1iiI = lisp_get_nat_info ( I1II . rloc , I1II . rloc_name )
  if ( i1II1iiI == None ) : continue
  if ( I1II . translated_port == i1II1iiI . port ) : continue
  if 74 - 74: i1IIi . I1Ii111 / O0 + Oo0Ooo * OOooOOo
  lprint ( ( "Encap-port changed from {} to {} for RLOC {}, " + "EID-prefix {}" ) . format ( I1II . translated_port , i1II1iiI . port ,
  # ooOoO0o - O0 + Ii1I / I1IiiI + Ii1I * OOooOOo
 red ( I1II . rloc . print_address_no_iid ( ) , False ) ,
 green ( mc . print_eid_tuple ( ) , False ) ) )
  if 14 - 14: I1ii11iIi11i / i1IIi . ooOoO0o % OoO0O00 * OoO0O00 + oO0o
  I1II . store_translated_rloc ( I1II . rloc , i1II1iiI . port )
  if 65 - 65: Oo0Ooo % iIii1I11I1II1
 return
 if 40 - 40: iII111i + Ii1I . OoooooooOO . i1IIi
 if 7 - 7: I1ii11iIi11i - Ii1I % Ii1I
 if 75 - 75: O0 . II111iiii + Oo0Ooo * O0 - IiII % OoOoOO00
 if 85 - 85: I1Ii111 - Ii1I . I1ii11iIi11i - OoooooooOO
 if 10 - 10: Ii1I . iII111i
 if 62 - 62: o0oOOo0O0Ooo + OoooooooOO + IiII
 if 98 - 98: OoO0O00 . o0oOOo0O0Ooo + ooOoO0o + OOooOOo + oO0o
 if 29 - 29: i11iIiiIii - I11i
 if 94 - 94: Oo0Ooo
 if 39 - 39: I11i - oO0o % iII111i - ooOoO0o - OoOoOO00
 if 8 - 8: i1IIi % i1IIi % OoooooooOO % i1IIi . iIii1I11I1II1
 if 70 - 70: O0 + II111iiii % IiII / I1Ii111 - IiII
def lisp_timeout_map_cache_entry ( mc , delete_list ) :
 if ( mc . map_cache_ttl == None ) :
  lisp_update_encap_port ( mc )
  return ( [ True , delete_list ] )
  if 58 - 58: II111iiii * oO0o - i1IIi . I11i
  if 23 - 23: OoO0O00 - I1IiiI * i11iIiiIii
 IiII1i11i1I = lisp_get_timestamp ( )
 if 62 - 62: OoO0O00 . i11iIiiIii / i1IIi
 if 3 - 3: OoO0O00 + O0 % Oo0Ooo * Oo0Ooo % i11iIiiIii
 if 29 - 29: ooOoO0o / iII111i / OOooOOo - iIii1I11I1II1
 if 31 - 31: i1IIi * Ii1I
 if 94 - 94: oO0o / Ii1I % iIii1I11I1II1 + i1IIi / O0 - iII111i
 if 77 - 77: o0oOOo0O0Ooo - IiII . i1IIi
 if ( mc . last_refresh_time + mc . map_cache_ttl > IiII1i11i1I ) :
  if ( mc . action == LISP_NO_ACTION ) : lisp_update_encap_port ( mc )
  return ( [ True , delete_list ] )
  if 70 - 70: i1IIi . I1Ii111 . iII111i - OoOoOO00 + II111iiii + OOooOOo
  if 52 - 52: OOooOOo . OoOoOO00 - ooOoO0o % i1IIi
  if 15 - 15: oO0o
  if 6 - 6: oO0o . iIii1I11I1II1 - I1ii11iIi11i % IiII
  if 58 - 58: iII111i * oO0o / iII111i - Oo0Ooo / I1Ii111 * oO0o
 if ( lisp_nat_traversal and mc . eid . address == 0 and mc . eid . mask_len == 0 ) :
  return ( [ True , delete_list ] )
  if 63 - 63: oO0o . IiII . o0oOOo0O0Ooo
  if 16 - 16: iII111i . I11i - Oo0Ooo / I1IiiI + OoOoOO00
  if 14 - 14: iIii1I11I1II1 / i11iIiiIii - o0oOOo0O0Ooo . iII111i * OoO0O00
  if 5 - 5: Ii1I + OoOoOO00 % I11i + IiII
  if 55 - 55: OoooooooOO + oO0o . o0oOOo0O0Ooo % iIii1I11I1II1 - I1Ii111
 Ooo0o0oo0 = lisp_print_elapsed ( mc . last_refresh_time )
 iIIiIIiII111 = mc . print_eid_tuple ( )
 lprint ( "Map-cache entry for EID-prefix {} has {}, had uptime of {}" . format ( green ( iIIiIIiII111 , False ) , bold ( "timed out" , False ) , Ooo0o0oo0 ) )
 if 40 - 40: I1IiiI . o0oOOo0O0Ooo - Oo0Ooo
 if 44 - 44: Ii1I % OoO0O00 * oO0o * OoO0O00
 if 7 - 7: I1Ii111 % i1IIi . I11i . O0 / i1IIi
 if 56 - 56: Oo0Ooo
 if 21 - 21: i11iIiiIii * o0oOOo0O0Ooo + Oo0Ooo
 delete_list . append ( mc )
 return ( [ True , delete_list ] )
 if 20 - 20: IiII / OoooooooOO / O0 / I1Ii111 * ooOoO0o
 if 45 - 45: ooOoO0o / Oo0Ooo % o0oOOo0O0Ooo . ooOoO0o
 if 19 - 19: o0oOOo0O0Ooo % I11i . I1ii11iIi11i
 if 70 - 70: Oo0Ooo - I11i / I1ii11iIi11i % OoO0O00 % II111iiii
 if 72 - 72: i11iIiiIii * I11i
 if 69 - 69: I1Ii111 . Ii1I * I1ii11iIi11i % I11i - o0oOOo0O0Ooo
 if 30 - 30: ooOoO0o / Oo0Ooo * iII111i % OoooooooOO / I1ii11iIi11i
 if 64 - 64: OoooooooOO
def lisp_timeout_map_cache_walk ( mc , parms ) :
 ooOOoOOo00O0o = parms [ 0 ]
 I1iOo0OOOOoo = parms [ 1 ]
 if 71 - 71: O0 - OoooooooOO
 if 82 - 82: i11iIiiIii * II111iiii % IiII
 if 80 - 80: Ii1I . i11iIiiIii % oO0o * o0oOOo0O0Ooo
 if 56 - 56: I1Ii111 % iII111i / II111iiii - Oo0Ooo - Oo0Ooo - iIii1I11I1II1
 if ( mc . group . is_null ( ) ) :
  O00OO , ooOOoOOo00O0o = lisp_timeout_map_cache_entry ( mc , ooOOoOOo00O0o )
  if ( ooOOoOOo00O0o == [ ] or mc != ooOOoOOo00O0o [ - 1 ] ) :
   I1iOo0OOOOoo = lisp_write_checkpoint_entry ( I1iOo0OOOOoo , mc )
   if 67 - 67: iII111i
  return ( [ O00OO , parms ] )
  if 80 - 80: Ii1I . iII111i * I1IiiI * Ii1I
  if 82 - 82: OoO0O00 % OoOoOO00 * i11iIiiIii . OoO0O00 . I1ii11iIi11i + Ii1I
 if ( mc . source_cache == None ) : return ( [ True , parms ] )
 if 60 - 60: i1IIi / iII111i
 if 10 - 10: I1Ii111 / OoOoOO00 * Ii1I % o0oOOo0O0Ooo . OoOoOO00 / I1ii11iIi11i
 if 2 - 2: iIii1I11I1II1
 if 85 - 85: O0 - ooOoO0o
 if 35 - 35: o0oOOo0O0Ooo - I1IiiI
 parms = mc . source_cache . walk_cache ( lisp_timeout_map_cache_entry , parms )
 return ( [ True , parms ] )
 if 47 - 47: i11iIiiIii * iII111i . OoOoOO00 * I1Ii111 % i11iIiiIii + Ii1I
 if 65 - 65: Ii1I % i11iIiiIii
 if 98 - 98: iII111i * o0oOOo0O0Ooo % Oo0Ooo
 if 7 - 7: oO0o * OoooooooOO % o0oOOo0O0Ooo . I1Ii111 + O0
 if 14 - 14: I11i * II111iiii % o0oOOo0O0Ooo / iII111i . OoooooooOO % iII111i
 if 88 - 88: iII111i
 if 94 - 94: OoooooooOO
def lisp_timeout_map_cache ( lisp_map_cache ) :
 I1I1i = [ [ ] , [ ] ]
 I1I1i = lisp_map_cache . walk_cache ( lisp_timeout_map_cache_walk , I1I1i )
 if 32 - 32: I1ii11iIi11i
 if 8 - 8: I11i * i11iIiiIii - ooOoO0o
 if 47 - 47: ooOoO0o . I1IiiI / i11iIiiIii * iII111i * I1IiiI
 if 8 - 8: oO0o % oO0o . iII111i / i1IIi % IiII
 if 71 - 71: OoOoOO00 + oO0o % O0 + Oo0Ooo
 ooOOoOOo00O0o = I1I1i [ 0 ]
 for o0Oo0 in ooOOoOOo00O0o : o0Oo0 . delete_cache ( )
 if 62 - 62: i1IIi . Ii1I * i1IIi * O0 . I1IiiI % o0oOOo0O0Ooo
 if 16 - 16: I11i . Ii1I - ooOoO0o . OOooOOo % O0 / oO0o
 if 42 - 42: II111iiii . iII111i
 if 67 - 67: i1IIi - i11iIiiIii / ooOoO0o * oO0o
 I1iOo0OOOOoo = I1I1i [ 1 ]
 lisp_checkpoint ( I1iOo0OOOOoo )
 return
 if 64 - 64: oO0o / IiII
 if 86 - 86: I11i
 if 36 - 36: o0oOOo0O0Ooo / OoO0O00
 if 6 - 6: I11i % I1IiiI + iII111i * OoooooooOO . O0
 if 87 - 87: ooOoO0o / Ii1I % O0 . OoO0O00
 if 55 - 55: i1IIi . o0oOOo0O0Ooo % OoooooooOO + II111iiii . OoOoOO00
 if 32 - 32: IiII * I1Ii111 * Oo0Ooo . i1IIi * OoooooooOO
 if 12 - 12: I1IiiI . OOooOOo % Oo0Ooo
 if 86 - 86: i11iIiiIii
 if 57 - 57: iII111i - OoooooooOO - ooOoO0o % II111iiii
 if 62 - 62: i11iIiiIii . Oo0Ooo / Oo0Ooo . IiII . OoooooooOO
 if 86 - 86: I1ii11iIi11i * OoOoOO00 + iII111i
 if 79 - 79: I11i - II111iiii
 if 27 - 27: I1IiiI + o0oOOo0O0Ooo * oO0o % I1IiiI
 if 66 - 66: OoO0O00 + IiII . o0oOOo0O0Ooo . IiII
 if 88 - 88: oO0o + oO0o % OoO0O00 . OoooooooOO - OoooooooOO . Oo0Ooo
def lisp_store_nat_info ( hostname , rloc , port ) :
 oo0o00OO = rloc . print_address_no_iid ( )
 iii1iI1I1i11 = "{} NAT state for {}, RLOC {}, port {}" . format ( "{}" ,
 blue ( hostname , False ) , red ( oo0o00OO , False ) , port )
 if 3 - 3: OoOoOO00 / o0oOOo0O0Ooo * O0
 iII1 = lisp_nat_info ( oo0o00OO , hostname , port )
 if 95 - 95: IiII % I1Ii111 . OoOoOO00 - OoooooooOO / OoooooooOO
 if ( lisp_nat_state_info . has_key ( hostname ) == False ) :
  lisp_nat_state_info [ hostname ] = [ iII1 ]
  lprint ( iii1iI1I1i11 . format ( "Store initial" ) )
  return ( True )
  if 79 - 79: I11i % i11iIiiIii % I1IiiI . OoooooooOO * oO0o . Ii1I
  if 14 - 14: iIii1I11I1II1 / I11i - o0oOOo0O0Ooo / IiII / o0oOOo0O0Ooo . OoO0O00
  if 2 - 2: I11i
  if 12 - 12: i1IIi . I1Ii111
  if 99 - 99: Oo0Ooo / i11iIiiIii
  if 81 - 81: Ii1I . i1IIi % iII111i . OoO0O00 % IiII
 i1II1iiI = lisp_nat_state_info [ hostname ] [ 0 ]
 if ( i1II1iiI . address == oo0o00OO and i1II1iiI . port == port ) :
  i1II1iiI . uptime = lisp_get_timestamp ( )
  lprint ( iii1iI1I1i11 . format ( "Refresh existing" ) )
  return ( False )
  if 42 - 42: iII111i / Oo0Ooo
  if 14 - 14: O0 . Oo0Ooo
  if 8 - 8: i11iIiiIii
  if 80 - 80: I1ii11iIi11i + Ii1I
  if 16 - 16: i11iIiiIii * Oo0Ooo
  if 76 - 76: iII111i . oO0o - i1IIi
  if 94 - 94: O0 % iII111i
 oo00OoOoO0oO = None
 for i1II1iiI in lisp_nat_state_info [ hostname ] :
  if ( i1II1iiI . address == oo0o00OO and i1II1iiI . port == port ) :
   oo00OoOoO0oO = i1II1iiI
   break
   if 65 - 65: I1IiiI + I1IiiI + OoO0O00 - iIii1I11I1II1 + O0
   if 46 - 46: ooOoO0o % iIii1I11I1II1 / Oo0Ooo * I1Ii111 / iII111i
   if 89 - 89: ooOoO0o + OoooooooOO - O0 * o0oOOo0O0Ooo . o0oOOo0O0Ooo * i11iIiiIii
 if ( oo00OoOoO0oO == None ) :
  lprint ( iii1iI1I1i11 . format ( "Store new" ) )
 else :
  lisp_nat_state_info [ hostname ] . remove ( oo00OoOoO0oO )
  lprint ( iii1iI1I1i11 . format ( "Use previous" ) )
  if 10 - 10: Oo0Ooo % II111iiii
  if 28 - 28: OoooooooOO / iII111i / iIii1I11I1II1
 oOooO0oo0 = lisp_nat_state_info [ hostname ]
 lisp_nat_state_info [ hostname ] = [ iII1 ] + oOooO0oo0
 return ( True )
 if 27 - 27: Ii1I / OoooooooOO . O0
 if 53 - 53: OoooooooOO / I1ii11iIi11i
 if 46 - 46: Ii1I . i11iIiiIii / I1Ii111 - I1ii11iIi11i
 if 13 - 13: IiII % I1Ii111
 if 9 - 9: OoooooooOO * ooOoO0o % I1ii11iIi11i . I1IiiI % O0
 if 91 - 91: OOooOOo * OoooooooOO * I1IiiI . i1IIi
 if 9 - 9: oO0o / i11iIiiIii + IiII / IiII - I11i
 if 87 - 87: iII111i
def lisp_get_nat_info ( rloc , hostname ) :
 if ( lisp_nat_state_info . has_key ( hostname ) == False ) : return ( None )
 if 37 - 37: oO0o + OoO0O00
 oo0o00OO = rloc . print_address_no_iid ( )
 for i1II1iiI in lisp_nat_state_info [ hostname ] :
  if ( i1II1iiI . address == oo0o00OO ) : return ( i1II1iiI )
  if 66 - 66: iIii1I11I1II1 * iIii1I11I1II1 + IiII % I1IiiI
 return ( None )
 if 60 - 60: I1Ii111 . IiII / Oo0Ooo
 if 32 - 32: OoOoOO00 + Ii1I * iII111i % Oo0Ooo
 if 61 - 61: OoooooooOO % iII111i - O0
 if 62 - 62: iIii1I11I1II1
 if 14 - 14: I1Ii111
 if 95 - 95: II111iiii / o0oOOo0O0Ooo * OOooOOo
 if 81 - 81: i11iIiiIii / iIii1I11I1II1
 if 73 - 73: i11iIiiIii . I1ii11iIi11i * OoOoOO00
 if 95 - 95: i1IIi + iIii1I11I1II1 . I1Ii111 / I1Ii111
 if 84 - 84: Oo0Ooo . OoO0O00 * IiII
 if 95 - 95: OoO0O00
 if 100 - 100: II111iiii
 if 34 - 34: I11i % OOooOOo - iII111i % II111iiii
 if 14 - 14: I11i * o0oOOo0O0Ooo % II111iiii
 if 36 - 36: ooOoO0o - iIii1I11I1II1 / IiII + OoOoOO00
 if 42 - 42: ooOoO0o + I1IiiI * iII111i / OoOoOO00 . i1IIi - OoooooooOO
 if 8 - 8: iIii1I11I1II1 - Oo0Ooo + iII111i
 if 40 - 40: o0oOOo0O0Ooo * I1IiiI
 if 75 - 75: O0 * OOooOOo / ooOoO0o + I11i
 if 56 - 56: I1IiiI % OoooooooOO % Oo0Ooo
def lisp_build_info_requests ( lisp_sockets , dest , port ) :
 if ( lisp_nat_traversal == False ) : return
 if 19 - 19: i11iIiiIii - iIii1I11I1II1 . i1IIi . I1Ii111 / I1IiiI * I1Ii111
 if 41 - 41: oO0o . o0oOOo0O0Ooo . I11i * OoOoOO00
 if 16 - 16: oO0o
 if 32 - 32: OoooooooOO
 if 77 - 77: Oo0Ooo . i1IIi - I11i
 if 98 - 98: O0
 OOO0O0Oo0Oo = [ ]
 oooOoOO0oOOO = [ ]
 if ( dest == None ) :
  for I1III11iIIIi in lisp_map_resolvers_list . values ( ) :
   oooOoOO0oOOO . append ( I1III11iIIIi . map_resolver )
   if 46 - 46: I11i . iII111i - I1IiiI / iIii1I11I1II1
  OOO0O0Oo0Oo = oooOoOO0oOOO
  if ( OOO0O0Oo0Oo == [ ] ) :
   for ii1i in lisp_map_servers_list . values ( ) :
    OOO0O0Oo0Oo . append ( ii1i . map_server )
    if 80 - 80: Ii1I % oO0o / I1Ii111
    if 12 - 12: II111iiii / ooOoO0o . Oo0Ooo / I1Ii111
  if ( OOO0O0Oo0Oo == [ ] ) : return
 else :
  OOO0O0Oo0Oo . append ( dest )
  if 59 - 59: I1IiiI % O0
  if 93 - 93: OoooooooOO % IiII % Ii1I - i11iIiiIii
  if 74 - 74: ooOoO0o + OoOoOO00
  if 94 - 94: i11iIiiIii
  if 88 - 88: ooOoO0o + ooOoO0o / I1Ii111
 OoO0OooO0Oo0o = { }
 for ii1iii in lisp_db_list :
  for oOO0O in ii1iii . rloc_set :
   lisp_update_local_rloc ( oOO0O )
   if ( oOO0O . rloc . is_null ( ) ) : continue
   if ( oOO0O . interface == None ) : continue
   if 69 - 69: O0 * o0oOOo0O0Ooo + i1IIi * ooOoO0o . o0oOOo0O0Ooo
   o0o00O0oOooO0 = oOO0O . rloc . print_address_no_iid ( )
   if ( o0o00O0oOooO0 in OoO0OooO0Oo0o ) : continue
   OoO0OooO0Oo0o [ o0o00O0oOooO0 ] = oOO0O . interface
   if 46 - 46: Oo0Ooo / Oo0Ooo * IiII
   if 65 - 65: iIii1I11I1II1 * o0oOOo0O0Ooo - iII111i % II111iiii - I1ii11iIi11i
 if ( OoO0OooO0Oo0o == { } ) :
  lprint ( 'Suppress Info-Request, no "interface = <device>" RLOC ' + "found in any database-mappings" )
  if 65 - 65: I11i
  return
  if 92 - 92: iII111i . IiII + i1IIi % i1IIi
  if 11 - 11: I1ii11iIi11i + iIii1I11I1II1 - I1Ii111 * iIii1I11I1II1 * IiII + oO0o
  if 6 - 6: I1Ii111 * OOooOOo + i1IIi - Ii1I / oO0o
  if 81 - 81: I1Ii111 % oO0o * i1IIi * OoooooooOO / Oo0Ooo
  if 70 - 70: I1IiiI
  if 35 - 35: i11iIiiIii
 for o0o00O0oOooO0 in OoO0OooO0Oo0o :
  II1i = OoO0OooO0Oo0o [ o0o00O0oOooO0 ]
  oO0OO = red ( o0o00O0oOooO0 , False )
  lprint ( "Build Info-Request for private address {} ({})" . format ( oO0OO ,
 II1i ) )
  OoO0o0OOOO = II1i if len ( OoO0OooO0Oo0o ) > 1 else None
  for dest in OOO0O0Oo0Oo :
   lisp_send_info_request ( lisp_sockets , dest , port , OoO0o0OOOO )
   if 59 - 59: ooOoO0o . iII111i - II111iiii
   if 30 - 30: o0oOOo0O0Ooo % iII111i - i11iIiiIii
   if 25 - 25: i11iIiiIii + OoOoOO00 + oO0o / Ii1I * Oo0Ooo + Oo0Ooo
   if 26 - 26: I1IiiI % I1ii11iIi11i + o0oOOo0O0Ooo / I1ii11iIi11i - I1IiiI
   if 55 - 55: OoooooooOO
   if 2 - 2: Oo0Ooo + I11i / OOooOOo + OOooOOo
 if ( oooOoOO0oOOO != [ ] ) :
  for I1III11iIIIi in lisp_map_resolvers_list . values ( ) :
   I1III11iIIIi . resolve_dns_name ( )
   if 62 - 62: OOooOOo . iIii1I11I1II1 + I1IiiI / OOooOOo
   if 90 - 90: OOooOOo
 return
 if 29 - 29: OoOoOO00 - I1IiiI / oO0o + Oo0Ooo + I1Ii111 + O0
 if 65 - 65: oO0o
 if 38 - 38: iIii1I11I1II1 / I1Ii111 + ooOoO0o . II111iiii - iIii1I11I1II1
 if 13 - 13: Ii1I
 if 34 - 34: I1IiiI / iIii1I11I1II1
 if 35 - 35: oO0o / oO0o
 if 86 - 86: o0oOOo0O0Ooo . Oo0Ooo - Ii1I / i11iIiiIii
 if 63 - 63: oO0o - O0 + I1ii11iIi11i + Ii1I / i1IIi
def lisp_valid_address_format ( kw , value ) :
 if ( kw != "address" ) : return ( True )
 if 77 - 77: O0
 if 49 - 49: o0oOOo0O0Ooo / i11iIiiIii
 if 36 - 36: II111iiii
 if 78 - 78: OoO0O00 + iIii1I11I1II1 * i1IIi
 if 7 - 7: i11iIiiIii
 if ( value [ 0 ] == "'" and value [ - 1 ] == "'" ) : return ( True )
 if 49 - 49: I1IiiI - oO0o % OOooOOo / O0 / II111iiii
 if 41 - 41: IiII % II111iiii
 if 99 - 99: IiII - O0
 if 59 - 59: iII111i % O0 + OOooOOo * ooOoO0o
 if ( value . find ( "." ) != - 1 ) :
  o0o00O0oOooO0 = value . split ( "." )
  if ( len ( o0o00O0oOooO0 ) != 4 ) : return ( False )
  if 27 - 27: I1Ii111 % i11iIiiIii * I1IiiI
  for IIII in o0o00O0oOooO0 :
   if ( IIII . isdigit ( ) == False ) : return ( False )
   if ( int ( IIII ) > 255 ) : return ( False )
   if 23 - 23: iIii1I11I1II1 + I1ii11iIi11i * ooOoO0o - OOooOOo % O0
  return ( True )
  if 47 - 47: O0 - II111iiii
  if 13 - 13: iII111i / OOooOOo * i11iIiiIii / oO0o / OoooooooOO
  if 89 - 89: Ii1I * Oo0Ooo / I1Ii111 * I1ii11iIi11i + O0 * Oo0Ooo
  if 74 - 74: I11i . I11i
  if 74 - 74: OoOoOO00 * ooOoO0o * I1Ii111
 if ( value . find ( "-" ) != - 1 ) :
  o0o00O0oOooO0 = value . split ( "-" )
  for iIi1I1 in [ "N" , "S" , "W" , "E" ] :
   if ( iIi1I1 in o0o00O0oOooO0 ) :
    if ( len ( o0o00O0oOooO0 ) < 8 ) : return ( False )
    return ( True )
    if 56 - 56: iIii1I11I1II1 * OoO0O00 - oO0o * Ii1I
    if 62 - 62: i1IIi + I11i / OOooOOo - OoooooooOO % i1IIi . I1IiiI
    if 13 - 13: O0 * iII111i
    if 26 - 26: i1IIi - I1Ii111 - ooOoO0o
    if 73 - 73: o0oOOo0O0Ooo . OoooooooOO
    if 96 - 96: i1IIi - OOooOOo / I11i % OoOoOO00 - i11iIiiIii % II111iiii
    if 47 - 47: I1Ii111 * iII111i
 if ( value . find ( "-" ) != - 1 ) :
  o0o00O0oOooO0 = value . split ( "-" )
  if ( len ( o0o00O0oOooO0 ) != 3 ) : return ( False )
  if 90 - 90: i1IIi * Ii1I . OoO0O00 % I11i * ooOoO0o . OOooOOo
  for Oo0I1Iii in o0o00O0oOooO0 :
   try : int ( Oo0I1Iii , 16 )
   except : return ( False )
   if 52 - 52: I1Ii111
  return ( True )
  if 82 - 82: iII111i + II111iiii
  if 29 - 29: O0 % Ii1I * ooOoO0o % O0
  if 83 - 83: oO0o
  if 95 - 95: Oo0Ooo * O0 % i1IIi / iII111i + oO0o
  if 85 - 85: iIii1I11I1II1 / I11i
 if ( value . find ( ":" ) != - 1 ) :
  o0o00O0oOooO0 = value . split ( ":" )
  if ( len ( o0o00O0oOooO0 ) < 2 ) : return ( False )
  if 65 - 65: I11i / i1IIi * OoOoOO00 * Ii1I * OoO0O00
  OO0oo00O0oO000o = False
  I1I1 = 0
  for Oo0I1Iii in o0o00O0oOooO0 :
   I1I1 += 1
   if ( Oo0I1Iii == "" ) :
    if ( OO0oo00O0oO000o ) :
     if ( len ( o0o00O0oOooO0 ) == I1I1 ) : break
     if ( I1I1 > 2 ) : return ( False )
     if 29 - 29: IiII . ooOoO0o . OOooOOo % I11i . I1Ii111
    OO0oo00O0oO000o = True
    continue
    if 75 - 75: OOooOOo % Oo0Ooo + iIii1I11I1II1 . I11i
   try : int ( Oo0I1Iii , 16 )
   except : return ( False )
   if 92 - 92: I1ii11iIi11i / ooOoO0o
  return ( True )
  if 21 - 21: OoO0O00 % II111iiii / OoooooooOO
  if 4 - 4: i11iIiiIii + OoooooooOO * i1IIi * iIii1I11I1II1 - OOooOOo
  if 23 - 23: ooOoO0o + Oo0Ooo
  if 43 - 43: Ii1I
  if 87 - 87: OoO0O00
 if ( value [ 0 ] == "+" ) :
  o0o00O0oOooO0 = value [ 1 : : ]
  for i1i111iIIi in o0o00O0oOooO0 :
   if ( i1i111iIIi . isdigit ( ) == False ) : return ( False )
   if 10 - 10: i1IIi . ooOoO0o . i1IIi - Ii1I
  return ( True )
  if 58 - 58: II111iiii * I1IiiI / i11iIiiIii * I1IiiI
 return ( False )
 if 65 - 65: o0oOOo0O0Ooo - IiII
 if 3 - 3: OOooOOo * ooOoO0o / i11iIiiIii . OoO0O00 * ooOoO0o
 if 58 - 58: i1IIi - OoO0O00 * II111iiii
 if 92 - 92: ooOoO0o / I1Ii111 . iII111i
 if 59 - 59: Ii1I - OoO0O00 % iII111i + I1ii11iIi11i * iII111i
 if 51 - 51: ooOoO0o - Oo0Ooo / iII111i . I11i - Ii1I / OOooOOo
 if 4 - 4: II111iiii + OoOoOO00 . ooOoO0o - I11i . I1IiiI
 if 46 - 46: II111iiii
 if 38 - 38: OOooOOo % II111iiii
 if 82 - 82: i11iIiiIii . OoooooooOO % OoOoOO00 * O0 - I1Ii111
 if 78 - 78: OoOoOO00 % Ii1I % OOooOOo % Oo0Ooo % I11i . Ii1I
 if 73 - 73: OoooooooOO / i1IIi . iIii1I11I1II1
def lisp_process_api ( process , lisp_socket , data_structure ) :
 ooO00O0o0O0o , I1I1i = data_structure . split ( "%" )
 if 28 - 28: OOooOOo - oO0o
 lprint ( "Process API request '{}', parameters: '{}'" . format ( ooO00O0o0O0o ,
 I1I1i ) )
 if 83 - 83: o0oOOo0O0Ooo . OoO0O00 % iIii1I11I1II1 % OoOoOO00 - i11iIiiIii
 oOO00o0 = [ ]
 if ( ooO00O0o0O0o == "map-cache" ) :
  if ( I1I1i == "" ) :
   oOO00o0 = lisp_map_cache . walk_cache ( lisp_process_api_map_cache , oOO00o0 )
  else :
   oOO00o0 = lisp_process_api_map_cache_entry ( json . loads ( I1I1i ) )
   if 71 - 71: I1ii11iIi11i - II111iiii / O0 % i1IIi + oO0o
   if 73 - 73: OoooooooOO
 if ( ooO00O0o0O0o == "site-cache" ) :
  if ( I1I1i == "" ) :
   oOO00o0 = lisp_sites_by_eid . walk_cache ( lisp_process_api_site_cache ,
 oOO00o0 )
  else :
   oOO00o0 = lisp_process_api_site_cache_entry ( json . loads ( I1I1i ) )
   if 25 - 25: i1IIi . II111iiii . I1Ii111
   if 81 - 81: II111iiii + OoOoOO00 * II111iiii / iIii1I11I1II1 - Oo0Ooo % oO0o
 if ( ooO00O0o0O0o == "site-cache-summary" ) :
  oOO00o0 = lisp_process_api_site_cache_summary ( lisp_sites_by_eid )
  if 66 - 66: ooOoO0o % O0 + iIii1I11I1II1 * I1Ii111 - I1Ii111
 if ( ooO00O0o0O0o == "map-server" ) :
  I1I1i = { } if ( I1I1i == "" ) else json . loads ( I1I1i )
  oOO00o0 = lisp_process_api_ms_or_mr ( True , I1I1i )
  if 61 - 61: I1ii11iIi11i
 if ( ooO00O0o0O0o == "map-resolver" ) :
  I1I1i = { } if ( I1I1i == "" ) else json . loads ( I1I1i )
  oOO00o0 = lisp_process_api_ms_or_mr ( False , I1I1i )
  if 12 - 12: OoO0O00
 if ( ooO00O0o0O0o == "database-mapping" ) :
  oOO00o0 = lisp_process_api_database_mapping ( )
  if 97 - 97: OOooOOo . Oo0Ooo . oO0o * i1IIi
  if 7 - 7: Oo0Ooo
  if 38 - 38: Oo0Ooo - I1ii11iIi11i
  if 19 - 19: Ii1I * OoO0O00 / OoO0O00 . II111iiii % iIii1I11I1II1
  if 61 - 61: I1ii11iIi11i * oO0o % iII111i + IiII + i11iIiiIii * I11i
 oOO00o0 = json . dumps ( oOO00o0 )
 oOOO0oo0 = lisp_api_ipc ( process , oOO00o0 )
 lisp_ipc ( oOOO0oo0 , lisp_socket , "lisp-core" )
 return
 if 3 - 3: Ii1I
 if 71 - 71: iIii1I11I1II1 . OOooOOo / I11i / i1IIi
 if 69 - 69: i1IIi / iII111i + Ii1I + I11i + IiII
 if 86 - 86: Oo0Ooo
 if 97 - 97: I1IiiI
 if 91 - 91: ooOoO0o / oO0o * OOooOOo . II111iiii - I11i - I11i
 if 5 - 5: O0 + OoooooooOO + i11iIiiIii * Oo0Ooo * OoOoOO00 . oO0o
def lisp_process_api_map_cache ( mc , data ) :
 if 6 - 6: OoO0O00 % Oo0Ooo % I1IiiI % o0oOOo0O0Ooo % O0 % Oo0Ooo
 if 94 - 94: I11i . i1IIi / II111iiii + OOooOOo
 if 64 - 64: I1IiiI % ooOoO0o
 if 72 - 72: O0 * II111iiii % OoO0O00 - I1IiiI * OOooOOo
 if ( mc . group . is_null ( ) ) : return ( lisp_gather_map_cache_data ( mc , data ) )
 if 80 - 80: OOooOOo * I11i / OOooOOo - oO0o
 if ( mc . source_cache == None ) : return ( [ True , data ] )
 if 18 - 18: i1IIi - OOooOOo - o0oOOo0O0Ooo - iIii1I11I1II1
 if 72 - 72: OoooooooOO % I1IiiI . OoO0O00
 if 28 - 28: II111iiii / iIii1I11I1II1 / iII111i - o0oOOo0O0Ooo . I1IiiI / O0
 if 16 - 16: ooOoO0o * oO0o . OoooooooOO
 if 44 - 44: iIii1I11I1II1 * OOooOOo + OoO0O00 - OoooooooOO
 data = mc . source_cache . walk_cache ( lisp_gather_map_cache_data , data )
 return ( [ True , data ] )
 if 13 - 13: Oo0Ooo . I11i . II111iiii
 if 6 - 6: OOooOOo . IiII / OoO0O00 * oO0o - I1Ii111 . OoOoOO00
 if 85 - 85: i11iIiiIii + OoOoOO00
 if 4 - 4: OOooOOo . OoO0O00 * II111iiii + OoO0O00 % Oo0Ooo
 if 60 - 60: OOooOOo . Ii1I
 if 13 - 13: i1IIi . iII111i / OoOoOO00 . I1Ii111
 if 65 - 65: oO0o % I1Ii111 % OoO0O00 . iIii1I11I1II1
def lisp_gather_map_cache_data ( mc , data ) :
 i1ii1i1Ii11 = { }
 i1ii1i1Ii11 [ "instance-id" ] = str ( mc . eid . instance_id )
 i1ii1i1Ii11 [ "eid-prefix" ] = mc . eid . print_prefix_no_iid ( )
 if ( mc . group . is_null ( ) == False ) :
  i1ii1i1Ii11 [ "group-prefix" ] = mc . group . print_prefix_no_iid ( )
  if 38 - 38: IiII / I11i / IiII * iII111i
 i1ii1i1Ii11 [ "uptime" ] = lisp_print_elapsed ( mc . uptime )
 i1ii1i1Ii11 [ "expires" ] = lisp_print_elapsed ( mc . uptime )
 i1ii1i1Ii11 [ "action" ] = lisp_map_reply_action_string [ mc . action ]
 i1ii1i1Ii11 [ "ttl" ] = "--" if mc . map_cache_ttl == None else str ( mc . map_cache_ttl / 60 )
 if 30 - 30: oO0o
 if 30 - 30: IiII / OoO0O00
 if 89 - 89: oO0o . OoOoOO00 . IiII / iIii1I11I1II1 . iIii1I11I1II1 / OoOoOO00
 if 86 - 86: OoooooooOO - iIii1I11I1II1 . OoO0O00 * Ii1I / I1Ii111 + I1Ii111
 if 52 - 52: iIii1I11I1II1 % OoO0O00 - IiII % i11iIiiIii - o0oOOo0O0Ooo
 OoO0oOOooOO = [ ]
 for I1II in mc . rloc_set :
  I1I111iIiI = lisp_fill_rloc_in_json ( I1II )
  if 25 - 25: Oo0Ooo - OOooOOo . i1IIi * OoOoOO00 / I11i / o0oOOo0O0Ooo
  if 54 - 54: OoOoOO00 / i1IIi + OOooOOo - I1ii11iIi11i - I1IiiI * I1Ii111
  if 91 - 91: OoooooooOO * OoooooooOO
  if 27 - 27: ooOoO0o / I1IiiI * I1ii11iIi11i . o0oOOo0O0Ooo
  if 30 - 30: o0oOOo0O0Ooo / i11iIiiIii
  if ( I1II . rloc . is_multicast_address ( ) ) :
   I1I111iIiI [ "multicast-rloc-set" ] = [ ]
   for O0oOO in I1II . multicast_rloc_probe_list . values ( ) :
    I1III11iIIIi = lisp_fill_rloc_in_json ( O0oOO )
    I1I111iIiI [ "multicast-rloc-set" ] . append ( I1III11iIIIi )
    if 33 - 33: OOooOOo % OoooooooOO
    if 98 - 98: Ii1I
    if 38 - 38: ooOoO0o - iII111i * OOooOOo % I1ii11iIi11i + Oo0Ooo
  OoO0oOOooOO . append ( I1I111iIiI )
  if 95 - 95: iIii1I11I1II1 / O0 % O0
 i1ii1i1Ii11 [ "rloc-set" ] = OoO0oOOooOO
 if 53 - 53: ooOoO0o . ooOoO0o
 data . append ( i1ii1i1Ii11 )
 return ( [ True , data ] )
 if 80 - 80: i11iIiiIii % I1Ii111 % I1IiiI / I1IiiI + oO0o + iII111i
 if 18 - 18: OoO0O00 * ooOoO0o
 if 32 - 32: oO0o . OoooooooOO - o0oOOo0O0Ooo + II111iiii
 if 4 - 4: OOooOOo * I1IiiI - I11i - I11i
 if 67 - 67: I1IiiI
 if 32 - 32: oO0o * i11iIiiIii - I11i % Oo0Ooo * I1ii11iIi11i
 if 79 - 79: II111iiii / Oo0Ooo / I1ii11iIi11i
 if 30 - 30: I11i . o0oOOo0O0Ooo / II111iiii
def lisp_fill_rloc_in_json ( rloc ) :
 I1I111iIiI = { }
 if ( rloc . rloc_exists ( ) ) :
  I1I111iIiI [ "address" ] = rloc . rloc . print_address_no_iid ( )
  if 59 - 59: i11iIiiIii
  if 5 - 5: i11iIiiIii + o0oOOo0O0Ooo . OoO0O00 % OoOoOO00 + I11i
 if ( rloc . translated_port != 0 ) :
  I1I111iIiI [ "encap-port" ] = str ( rloc . translated_port )
  if 59 - 59: I1ii11iIi11i
 I1I111iIiI [ "state" ] = rloc . print_state ( )
 if ( rloc . geo ) : I1I111iIiI [ "geo" ] = rloc . geo . print_geo ( )
 if ( rloc . elp ) : I1I111iIiI [ "elp" ] = rloc . elp . print_elp ( False )
 if ( rloc . rle ) : I1I111iIiI [ "rle" ] = rloc . rle . print_rle ( False , False )
 if ( rloc . json ) : I1I111iIiI [ "json" ] = rloc . json . print_json ( False )
 if ( rloc . rloc_name ) : I1I111iIiI [ "rloc-name" ] = rloc . rloc_name
 Iiiiii1 = rloc . stats . get_stats ( False , False )
 if ( Iiiiii1 ) : I1I111iIiI [ "stats" ] = Iiiiii1
 I1I111iIiI [ "uptime" ] = lisp_print_elapsed ( rloc . uptime )
 I1I111iIiI [ "upriority" ] = str ( rloc . priority )
 I1I111iIiI [ "uweight" ] = str ( rloc . weight )
 I1I111iIiI [ "mpriority" ] = str ( rloc . mpriority )
 I1I111iIiI [ "mweight" ] = str ( rloc . mweight )
 iII1Iii = rloc . last_rloc_probe_reply
 if ( iII1Iii ) :
  I1I111iIiI [ "last-rloc-probe-reply" ] = lisp_print_elapsed ( iII1Iii )
  I1I111iIiI [ "rloc-probe-rtt" ] = str ( rloc . rloc_probe_rtt )
  if 69 - 69: ooOoO0o * O0 + iII111i + i1IIi
 I1I111iIiI [ "rloc-hop-count" ] = rloc . rloc_probe_hops
 I1I111iIiI [ "recent-rloc-hop-counts" ] = rloc . recent_rloc_probe_hops
 if 18 - 18: ooOoO0o % OoooooooOO - OOooOOo * oO0o - OOooOOo / oO0o
 I1I111iIiI [ "rloc-probe-latency" ] = rloc . rloc_probe_latency
 I1I111iIiI [ "recent-rloc-probe-latencies" ] = rloc . recent_rloc_probe_latencies
 if 83 - 83: ooOoO0o % iIii1I11I1II1 + Oo0Ooo
 ii1iiiiI1II1 = [ ]
 for iIIi in rloc . recent_rloc_probe_rtts : ii1iiiiI1II1 . append ( str ( iIIi ) )
 I1I111iIiI [ "recent-rloc-probe-rtts" ] = ii1iiiiI1II1
 return ( I1I111iIiI )
 if 34 - 34: I1ii11iIi11i . i1IIi * O0 / OoooooooOO
 if 22 - 22: OOooOOo % o0oOOo0O0Ooo - i11iIiiIii
 if 58 - 58: IiII . Ii1I + II111iiii
 if 31 - 31: i11iIiiIii + i11iIiiIii + I11i * Oo0Ooo . I11i
 if 28 - 28: OOooOOo * iIii1I11I1II1 * OoOoOO00
 if 75 - 75: Oo0Ooo % IiII + II111iiii + oO0o
 if 35 - 35: I1ii11iIi11i - oO0o - O0 / iII111i % IiII
def lisp_process_api_map_cache_entry ( parms ) :
 IiIIi11i111 = parms [ "instance-id" ]
 IiIIi11i111 = 0 if ( IiIIi11i111 == "" ) else int ( IiIIi11i111 )
 if 10 - 10: OOooOOo + oO0o - I1Ii111 . I1IiiI
 if 11 - 11: I1ii11iIi11i . I1Ii111 / o0oOOo0O0Ooo + IiII
 if 73 - 73: OoO0O00 . i11iIiiIii * OoO0O00 * i1IIi + I11i
 if 27 - 27: i11iIiiIii / OoOoOO00 % O0 / II111iiii . I11i - ooOoO0o
 iiI1I1IIi = lisp_address ( LISP_AFI_NONE , "" , 0 , IiIIi11i111 )
 iiI1I1IIi . store_prefix ( parms [ "eid-prefix" ] )
 Ii1II1I11i1I = iiI1I1IIi
 iI1Iii1i1 = iiI1I1IIi
 if 54 - 54: oO0o * II111iiii
 if 79 - 79: o0oOOo0O0Ooo . ooOoO0o . Oo0Ooo * OoooooooOO
 if 98 - 98: ooOoO0o
 if 73 - 73: I1Ii111
 if 97 - 97: OoO0O00 * Ii1I + Oo0Ooo
 OOo0oOOO0 = lisp_address ( LISP_AFI_NONE , "" , 0 , IiIIi11i111 )
 if ( parms . has_key ( "group-prefix" ) ) :
  OOo0oOOO0 . store_prefix ( parms [ "group-prefix" ] )
  Ii1II1I11i1I = OOo0oOOO0
  if 83 - 83: II111iiii - Oo0Ooo % II111iiii * o0oOOo0O0Ooo
  if 51 - 51: iII111i * iIii1I11I1II1 % Ii1I * Ii1I + i11iIiiIii . OoooooooOO
 oOO00o0 = [ ]
 o0Oo0 = lisp_map_cache_lookup ( iI1Iii1i1 , Ii1II1I11i1I )
 if ( o0Oo0 ) : O00OO , oOO00o0 = lisp_process_api_map_cache ( o0Oo0 , oOO00o0 )
 return ( oOO00o0 )
 if 54 - 54: i11iIiiIii . iIii1I11I1II1 * iIii1I11I1II1 + Ii1I % I11i - OoO0O00
 if 16 - 16: IiII % iIii1I11I1II1 * i11iIiiIii + O0
 if 76 - 76: iII111i * OOooOOo
 if 7 - 7: ooOoO0o + o0oOOo0O0Ooo + o0oOOo0O0Ooo
 if 73 - 73: IiII % I11i % i11iIiiIii + ooOoO0o
 if 83 - 83: Ii1I * I1Ii111 * i11iIiiIii / iIii1I11I1II1 % I1ii11iIi11i
 if 40 - 40: iII111i
 if 21 - 21: I1Ii111 / iII111i + Oo0Ooo / I1ii11iIi11i / I1Ii111
 if 33 - 33: OoooooooOO
 if 59 - 59: i11iIiiIii - OoooooooOO . ooOoO0o / i11iIiiIii % iIii1I11I1II1 * I1ii11iIi11i
 if 45 - 45: I1ii11iIi11i * I1ii11iIi11i
def lisp_process_api_site_cache_summary ( site_cache ) :
 ooo000O0O = { "site" : "" , "registrations" : [ ] }
 i1ii1i1Ii11 = { "eid-prefix" : "" , "count" : 0 , "registered-count" : 0 }
 if 31 - 31: OoO0O00 - OOooOOo . iII111i * I1Ii111 * iII111i + I1ii11iIi11i
 iIOooo00OO = { }
 for iiIi in site_cache . cache_sorted :
  for iIiIi1I in site_cache . cache [ iiIi ] . entries . values ( ) :
   if ( iIiIi1I . accept_more_specifics == False ) : continue
   if ( iIOooo00OO . has_key ( iIiIi1I . site . site_name ) == False ) :
    iIOooo00OO [ iIiIi1I . site . site_name ] = [ ]
    if 83 - 83: Ii1I % iIii1I11I1II1 / I1ii11iIi11i + I11i
   iIIi1iI1I1IIi = copy . deepcopy ( i1ii1i1Ii11 )
   iIIi1iI1I1IIi [ "eid-prefix" ] = iIiIi1I . eid . print_prefix ( )
   iIIi1iI1I1IIi [ "count" ] = len ( iIiIi1I . more_specific_registrations )
   for iiiI1iii1 in iIiIi1I . more_specific_registrations :
    if ( iiiI1iii1 . registered ) : iIIi1iI1I1IIi [ "registered-count" ] += 1
    if 7 - 7: Oo0Ooo - o0oOOo0O0Ooo * Oo0Ooo . ooOoO0o
   iIOooo00OO [ iIiIi1I . site . site_name ] . append ( iIIi1iI1I1IIi )
   if 25 - 25: IiII . O0 / OoOoOO00
   if 33 - 33: OoO0O00
   if 55 - 55: ooOoO0o + ooOoO0o
 oOO00o0 = [ ]
 for OOOO0OOo0oOoo in iIOooo00OO :
  OO0o0OO0 = copy . deepcopy ( ooo000O0O )
  OO0o0OO0 [ "site" ] = OOOO0OOo0oOoo
  OO0o0OO0 [ "registrations" ] = iIOooo00OO [ OOOO0OOo0oOoo ]
  oOO00o0 . append ( OO0o0OO0 )
  if 93 - 93: oO0o - I1IiiI / I1ii11iIi11i % o0oOOo0O0Ooo / OoooooooOO + II111iiii
 return ( oOO00o0 )
 if 10 - 10: o0oOOo0O0Ooo - iII111i . O0 + OoO0O00 - Oo0Ooo - i11iIiiIii
 if 37 - 37: iIii1I11I1II1
 if 37 - 37: II111iiii % OoOoOO00 . IiII * ooOoO0o . I1IiiI
 if 25 - 25: OoooooooOO % i1IIi . I1Ii111 / OoOoOO00 - I1ii11iIi11i
 if 15 - 15: iIii1I11I1II1
 if 72 - 72: OoO0O00 . IiII * Ii1I - I1IiiI
 if 81 - 81: oO0o . OOooOOo - Ii1I . OoOoOO00
def lisp_process_api_site_cache ( se , data ) :
 if 100 - 100: Ii1I * i1IIi * i1IIi - iII111i + OoO0O00 + OoO0O00
 if 9 - 9: oO0o / OoO0O00 . I1IiiI
 if 24 - 24: IiII * i11iIiiIii % o0oOOo0O0Ooo - ooOoO0o + ooOoO0o . II111iiii
 if 69 - 69: I1IiiI . i11iIiiIii - o0oOOo0O0Ooo
 if ( se . group . is_null ( ) ) : return ( lisp_gather_site_cache_data ( se , data ) )
 if 40 - 40: OOooOOo * Ii1I
 if ( se . source_cache == None ) : return ( [ True , data ] )
 if 38 - 38: ooOoO0o
 if 5 - 5: OoooooooOO + iII111i - I11i
 if 95 - 95: OOooOOo / i11iIiiIii - Ii1I + I1ii11iIi11i
 if 7 - 7: I1ii11iIi11i
 if 37 - 37: O0 . II111iiii
 data = se . source_cache . walk_cache ( lisp_gather_site_cache_data , data )
 return ( [ True , data ] )
 if 70 - 70: o0oOOo0O0Ooo / iII111i + i1IIi + I11i % iIii1I11I1II1 % Oo0Ooo
 if 1 - 1: O0 + OoO0O00 . i11iIiiIii + I1Ii111 - OoO0O00 - IiII
 if 1 - 1: I1ii11iIi11i / i1IIi . I1IiiI / Ii1I
 if 19 - 19: iIii1I11I1II1 / Oo0Ooo . O0 - Oo0Ooo
 if 74 - 74: I1ii11iIi11i * OoooooooOO . iII111i
 if 45 - 45: I1IiiI - IiII % ooOoO0o - IiII . Oo0Ooo - o0oOOo0O0Ooo
 if 27 - 27: iII111i
def lisp_process_api_ms_or_mr ( ms_or_mr , data ) :
 ii1i1II11II1i = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
 ooOOO000 = data [ "dns-name" ] if data . has_key ( "dns-name" ) else None
 if ( data . has_key ( "address" ) ) :
  ii1i1II11II1i . store_address ( data [ "address" ] )
  if 64 - 64: iIii1I11I1II1 - OOooOOo . iII111i % o0oOOo0O0Ooo / II111iiii % OoooooooOO
  if 87 - 87: OoooooooOO
 Oo00OO0OO = { }
 if ( ms_or_mr ) :
  for ii1i in lisp_map_servers_list . values ( ) :
   if ( ooOOO000 ) :
    if ( ooOOO000 != ii1i . dns_name ) : continue
   else :
    if ( ii1i1II11II1i . is_exact_match ( ii1i . map_server ) == False ) : continue
    if 70 - 70: o0oOOo0O0Ooo % OoooooooOO % I1IiiI . OoOoOO00 * I1IiiI - ooOoO0o
    if 92 - 92: I1IiiI . I11i
   Oo00OO0OO [ "dns-name" ] = ii1i . dns_name
   Oo00OO0OO [ "address" ] = ii1i . map_server . print_address_no_iid ( )
   Oo00OO0OO [ "ms-name" ] = "" if ii1i . ms_name == None else ii1i . ms_name
   return ( [ Oo00OO0OO ] )
   if 66 - 66: I1Ii111 / I11i / OoooooooOO % OoOoOO00 . oO0o * iII111i
 else :
  for I1III11iIIIi in lisp_map_resolvers_list . values ( ) :
   if ( ooOOO000 ) :
    if ( ooOOO000 != I1III11iIIIi . dns_name ) : continue
   else :
    if ( ii1i1II11II1i . is_exact_match ( I1III11iIIIi . map_resolver ) == False ) : continue
    if 34 - 34: I1ii11iIi11i * I1ii11iIi11i % I11i / OOooOOo % oO0o . OoOoOO00
    if 25 - 25: I1ii11iIi11i / I11i + i1IIi . I1IiiI + ooOoO0o
   Oo00OO0OO [ "dns-name" ] = I1III11iIIIi . dns_name
   Oo00OO0OO [ "address" ] = I1III11iIIIi . map_resolver . print_address_no_iid ( )
   Oo00OO0OO [ "mr-name" ] = "" if I1III11iIIIi . mr_name == None else I1III11iIIIi . mr_name
   return ( [ Oo00OO0OO ] )
   if 29 - 29: IiII + I1ii11iIi11i
   if 8 - 8: IiII % I1IiiI
 return ( [ ] )
 if 10 - 10: OoooooooOO / OoOoOO00
 if 77 - 77: OoOoOO00
 if 10 - 10: IiII / i11iIiiIii
 if 19 - 19: OoO0O00
 if 100 - 100: I1ii11iIi11i - I1ii11iIi11i
 if 38 - 38: I1Ii111
 if 23 - 23: Ii1I . I1ii11iIi11i + I1Ii111 + i1IIi * o0oOOo0O0Ooo - i11iIiiIii
 if 92 - 92: I1Ii111 - I1IiiI + Ii1I / iII111i % OOooOOo
def lisp_process_api_database_mapping ( ) :
 oOO00o0 = [ ]
 if 32 - 32: i1IIi . iII111i - Ii1I % iII111i % II111iiii - oO0o
 for ii1iii in lisp_db_list :
  i1ii1i1Ii11 = { }
  i1ii1i1Ii11 [ "eid-prefix" ] = ii1iii . eid . print_prefix ( )
  if ( ii1iii . group . is_null ( ) == False ) :
   i1ii1i1Ii11 [ "group-prefix" ] = ii1iii . group . print_prefix ( )
   if 36 - 36: OoooooooOO * OoooooooOO . ooOoO0o . O0
   if 5 - 5: I11i % I1IiiI - OoO0O00 . Oo0Ooo
  ooOOo = [ ]
  for I1I111iIiI in ii1iii . rloc_set :
   I1II = { }
   if ( I1I111iIiI . rloc . is_null ( ) == False ) :
    I1II [ "rloc" ] = I1I111iIiI . rloc . print_address_no_iid ( )
    if 79 - 79: iII111i + IiII % I11i . Oo0Ooo / IiII * iII111i
   if ( I1I111iIiI . rloc_name != None ) : I1II [ "rloc-name" ] = I1I111iIiI . rloc_name
   if ( I1I111iIiI . interface != None ) : I1II [ "interface" ] = I1I111iIiI . interface
   i1IiIiII1 = I1I111iIiI . translated_rloc
   if ( i1IiIiII1 . is_null ( ) == False ) :
    I1II [ "translated-rloc" ] = i1IiIiII1 . print_address_no_iid ( )
    if 18 - 18: II111iiii * oO0o
   if ( I1II != { } ) : ooOOo . append ( I1II )
   if 55 - 55: I1ii11iIi11i * i11iIiiIii + Oo0Ooo
   if 29 - 29: I1ii11iIi11i / IiII . I1Ii111 + Ii1I + OoO0O00
   if 76 - 76: ooOoO0o . I11i * OoO0O00
   if 53 - 53: II111iiii / OoOoOO00 / IiII * oO0o
   if 52 - 52: O0 % iII111i * iIii1I11I1II1 / I11i / I1IiiI * ooOoO0o
  i1ii1i1Ii11 [ "rlocs" ] = ooOOo
  if 93 - 93: iIii1I11I1II1 . II111iiii * OOooOOo - iIii1I11I1II1 . oO0o % Oo0Ooo
  if 92 - 92: OoO0O00
  if 42 - 42: I1ii11iIi11i - iIii1I11I1II1 % ooOoO0o
  if 7 - 7: Oo0Ooo / ooOoO0o + o0oOOo0O0Ooo
  oOO00o0 . append ( i1ii1i1Ii11 )
  if 38 - 38: o0oOOo0O0Ooo . O0 - OoO0O00 % I11i
 return ( oOO00o0 )
 if 80 - 80: o0oOOo0O0Ooo
 if 100 - 100: iIii1I11I1II1 . OoOoOO00 . OoooooooOO / I1ii11iIi11i - I1IiiI * I11i
 if 5 - 5: i1IIi * o0oOOo0O0Ooo - I1Ii111 + I1IiiI - II111iiii
 if 15 - 15: I1Ii111
 if 38 - 38: O0
 if 50 - 50: i11iIiiIii * OoO0O00 + iII111i / O0 * oO0o % ooOoO0o
 if 6 - 6: OoO0O00 . o0oOOo0O0Ooo / Ii1I + Ii1I
def lisp_gather_site_cache_data ( se , data ) :
 i1ii1i1Ii11 = { }
 i1ii1i1Ii11 [ "site-name" ] = se . site . site_name
 i1ii1i1Ii11 [ "instance-id" ] = str ( se . eid . instance_id )
 i1ii1i1Ii11 [ "eid-prefix" ] = se . eid . print_prefix_no_iid ( )
 if ( se . group . is_null ( ) == False ) :
  i1ii1i1Ii11 [ "group-prefix" ] = se . group . print_prefix_no_iid ( )
  if 59 - 59: II111iiii - o0oOOo0O0Ooo * OoooooooOO
 i1ii1i1Ii11 [ "registered" ] = "yes" if se . registered else "no"
 i1ii1i1Ii11 [ "first-registered" ] = lisp_print_elapsed ( se . first_registered )
 i1ii1i1Ii11 [ "last-registered" ] = lisp_print_elapsed ( se . last_registered )
 if 83 - 83: oO0o . iIii1I11I1II1 . iII111i % Oo0Ooo
 o0o00O0oOooO0 = se . last_registerer
 o0o00O0oOooO0 = "none" if o0o00O0oOooO0 . is_null ( ) else o0o00O0oOooO0 . print_address ( )
 i1ii1i1Ii11 [ "last-registerer" ] = o0o00O0oOooO0
 i1ii1i1Ii11 [ "ams" ] = "yes" if ( se . accept_more_specifics ) else "no"
 i1ii1i1Ii11 [ "dynamic" ] = "yes" if ( se . dynamic ) else "no"
 i1ii1i1Ii11 [ "site-id" ] = str ( se . site_id )
 if ( se . xtr_id_present ) :
  i1ii1i1Ii11 [ "xtr-id" ] = "0x" + lisp_hex_string ( se . xtr_id )
  if 48 - 48: oO0o % OoO0O00 - OoooooooOO . IiII
  if 11 - 11: I1Ii111 % o0oOOo0O0Ooo - o0oOOo0O0Ooo % OoooooooOO . o0oOOo0O0Ooo - I1ii11iIi11i
  if 33 - 33: OoO0O00 + II111iiii . Oo0Ooo * I1Ii111
  if 63 - 63: OoooooooOO + OoOoOO00 - OoooooooOO
  if 54 - 54: OoO0O00 + I1IiiI % O0 + OoO0O00
 OoO0oOOooOO = [ ]
 for I1II in se . registered_rlocs :
  I1I111iIiI = { }
  I1I111iIiI [ "address" ] = I1II . rloc . print_address_no_iid ( ) if I1II . rloc_exists ( ) else "none"
  if 37 - 37: II111iiii / I1ii11iIi11i * I1IiiI - OoooooooOO
  if 55 - 55: IiII / ooOoO0o * I1IiiI / I1Ii111 - Oo0Ooo % o0oOOo0O0Ooo
  if ( I1II . geo ) : I1I111iIiI [ "geo" ] = I1II . geo . print_geo ( )
  if ( I1II . elp ) : I1I111iIiI [ "elp" ] = I1II . elp . print_elp ( False )
  if ( I1II . rle ) : I1I111iIiI [ "rle" ] = I1II . rle . print_rle ( False , True )
  if ( I1II . json ) : I1I111iIiI [ "json" ] = I1II . json . print_json ( False )
  if ( I1II . rloc_name ) : I1I111iIiI [ "rloc-name" ] = I1II . rloc_name
  I1I111iIiI [ "uptime" ] = lisp_print_elapsed ( I1II . uptime )
  I1I111iIiI [ "upriority" ] = str ( I1II . priority )
  I1I111iIiI [ "uweight" ] = str ( I1II . weight )
  I1I111iIiI [ "mpriority" ] = str ( I1II . mpriority )
  I1I111iIiI [ "mweight" ] = str ( I1II . mweight )
  if 82 - 82: OoO0O00 - iIii1I11I1II1 . Oo0Ooo / IiII . OoO0O00
  OoO0oOOooOO . append ( I1I111iIiI )
  if 47 - 47: OOooOOo + IiII
 i1ii1i1Ii11 [ "registered-rlocs" ] = OoO0oOOooOO
 if 11 - 11: Oo0Ooo + I1IiiI % i11iIiiIii % Oo0Ooo + ooOoO0o + i1IIi
 data . append ( i1ii1i1Ii11 )
 return ( [ True , data ] )
 if 100 - 100: II111iiii - OOooOOo + iII111i - i11iIiiIii . O0 / iII111i
 if 64 - 64: Ii1I
 if 4 - 4: OoOoOO00
 if 78 - 78: i1IIi - iII111i + O0 - I1IiiI % o0oOOo0O0Ooo
 if 48 - 48: iII111i / II111iiii * I1Ii111 + I11i / ooOoO0o . OoOoOO00
 if 45 - 45: OOooOOo / Ii1I % O0
 if 7 - 7: oO0o * i11iIiiIii + OoooooooOO + I11i
def lisp_process_api_site_cache_entry ( parms ) :
 IiIIi11i111 = parms [ "instance-id" ]
 IiIIi11i111 = 0 if ( IiIIi11i111 == "" ) else int ( IiIIi11i111 )
 if 9 - 9: II111iiii * Oo0Ooo * I1Ii111 . IiII
 if 80 - 80: i11iIiiIii . i11iIiiIii . i11iIiiIii . OoooooooOO - OOooOOo * OoooooooOO
 if 96 - 96: oO0o
 if 80 - 80: IiII - oO0o % Ii1I - iIii1I11I1II1 . OoO0O00
 iiI1I1IIi = lisp_address ( LISP_AFI_NONE , "" , 0 , IiIIi11i111 )
 iiI1I1IIi . store_prefix ( parms [ "eid-prefix" ] )
 if 64 - 64: I1IiiI % i11iIiiIii / oO0o
 if 78 - 78: II111iiii - Oo0Ooo . iIii1I11I1II1 - ooOoO0o . oO0o
 if 84 - 84: iII111i . ooOoO0o * I1IiiI * Oo0Ooo / I1Ii111
 if 93 - 93: i1IIi * i11iIiiIii % OoOoOO00 % iII111i
 if 31 - 31: OoO0O00
 OOo0oOOO0 = lisp_address ( LISP_AFI_NONE , "" , 0 , IiIIi11i111 )
 if ( parms . has_key ( "group-prefix" ) ) :
  OOo0oOOO0 . store_prefix ( parms [ "group-prefix" ] )
  if 89 - 89: II111iiii
  if 33 - 33: OOooOOo / oO0o % OoOoOO00 * O0
 oOO00o0 = [ ]
 iIiIi1I = lisp_site_eid_lookup ( iiI1I1IIi , OOo0oOOO0 , False )
 if ( iIiIi1I ) : lisp_gather_site_cache_data ( iIiIi1I , oOO00o0 )
 return ( oOO00o0 )
 if 65 - 65: OoO0O00 % OoOoOO00 % I1ii11iIi11i / OoooooooOO
 if 85 - 85: O0 * OOooOOo % I1Ii111
 if 33 - 33: O0
 if 30 - 30: II111iiii . O0 . oO0o * I1ii11iIi11i + oO0o . o0oOOo0O0Ooo
 if 43 - 43: iIii1I11I1II1
 if 88 - 88: I1IiiI - OoO0O00 . O0 . oO0o
 if 75 - 75: II111iiii % OOooOOo / iIii1I11I1II1 / OoO0O00 + oO0o
def lisp_get_interface_instance_id ( device , source_eid ) :
 II1i = None
 if ( lisp_myinterfaces . has_key ( device ) ) :
  II1i = lisp_myinterfaces [ device ]
  if 16 - 16: oO0o + I1Ii111 - II111iiii - o0oOOo0O0Ooo / i11iIiiIii
  if 59 - 59: OOooOOo - o0oOOo0O0Ooo
  if 82 - 82: IiII % ooOoO0o - OoO0O00 % ooOoO0o
  if 51 - 51: ooOoO0o % iII111i . o0oOOo0O0Ooo . o0oOOo0O0Ooo
  if 20 - 20: i1IIi - ooOoO0o % OoooooooOO * I1ii11iIi11i + II111iiii % i1IIi
  if 30 - 30: i11iIiiIii - I1IiiI + o0oOOo0O0Ooo + IiII
 if ( II1i == None or II1i . instance_id == None ) :
  return ( lisp_default_iid )
  if 16 - 16: I1ii11iIi11i / Ii1I + I1ii11iIi11i * I1Ii111
  if 49 - 49: ooOoO0o * OoOoOO00 . OoooooooOO . ooOoO0o + Oo0Ooo * IiII
  if 47 - 47: iII111i . i1IIi . I1ii11iIi11i / OoooooooOO
  if 84 - 84: o0oOOo0O0Ooo * I11i
  if 22 - 22: i1IIi + OOooOOo % OoooooooOO
  if 34 - 34: oO0o / O0 - II111iiii % Oo0Ooo + I11i
  if 23 - 23: o0oOOo0O0Ooo + i11iIiiIii . I1IiiI + iIii1I11I1II1
  if 18 - 18: o0oOOo0O0Ooo . O0 + I1Ii111
  if 66 - 66: OoooooooOO
 IiIIi11i111 = II1i . get_instance_id ( )
 if ( source_eid == None ) : return ( IiIIi11i111 )
 if 90 - 90: IiII - OoOoOO00
 oOoO = source_eid . instance_id
 IIII1 = None
 for II1i in lisp_multi_tenant_interfaces :
  if ( II1i . device != device ) : continue
  I11i11IIIII = II1i . multi_tenant_eid
  source_eid . instance_id = I11i11IIIII . instance_id
  if ( source_eid . is_more_specific ( I11i11IIIII ) == False ) : continue
  if ( IIII1 == None or IIII1 . multi_tenant_eid . mask_len < I11i11IIIII . mask_len ) :
   IIII1 = II1i
   if 80 - 80: OOooOOo * IiII * Ii1I + i11iIiiIii
   if 68 - 68: I1IiiI - Oo0Ooo - o0oOOo0O0Ooo + O0 % oO0o % OoOoOO00
 source_eid . instance_id = oOoO
 if 97 - 97: i11iIiiIii * I1ii11iIi11i
 if ( IIII1 == None ) : return ( IiIIi11i111 )
 return ( IIII1 . get_instance_id ( ) )
 if 12 - 12: ooOoO0o + OOooOOo . i1IIi % i11iIiiIii
 if 61 - 61: o0oOOo0O0Ooo - Ii1I % o0oOOo0O0Ooo
 if 59 - 59: OoooooooOO . iIii1I11I1II1 * OoooooooOO + ooOoO0o
 if 56 - 56: OoOoOO00 . iII111i / OOooOOo
 if 39 - 39: iIii1I11I1II1 % ooOoO0o
 if 75 - 75: i1IIi * II111iiii * O0 * i11iIiiIii % iII111i / iII111i
 if 36 - 36: IiII / I1IiiI % iII111i / iII111i
 if 38 - 38: OOooOOo * I1ii11iIi11i * I1Ii111 + I11i
 if 65 - 65: O0 + O0 * I1Ii111
def lisp_allow_dynamic_eid ( device , eid ) :
 if ( lisp_myinterfaces . has_key ( device ) == False ) : return ( None )
 if 66 - 66: OOooOOo / O0 + i1IIi . O0 % I1ii11iIi11i - OoooooooOO
 II1i = lisp_myinterfaces [ device ]
 i11i1Ii11i = device if II1i . dynamic_eid_device == None else II1i . dynamic_eid_device
 if 43 - 43: IiII . o0oOOo0O0Ooo + I1Ii111 + OoO0O00 * II111iiii
 if 67 - 67: i11iIiiIii * i1IIi + OOooOOo - I11i - I1Ii111
 if ( II1i . does_dynamic_eid_match ( eid ) ) : return ( i11i1Ii11i )
 return ( None )
 if 9 - 9: I1IiiI - I11i . ooOoO0o % i11iIiiIii
 if 27 - 27: iIii1I11I1II1 . OoooooooOO
 if 92 - 92: ooOoO0o + IiII * II111iiii
 if 41 - 41: I1IiiI + OoOoOO00 . OOooOOo
 if 57 - 57: II111iiii . iIii1I11I1II1
 if 32 - 32: o0oOOo0O0Ooo
 if 75 - 75: I1IiiI . II111iiii - iII111i % IiII * OoO0O00 % ooOoO0o
def lisp_start_rloc_probe_timer ( interval , lisp_sockets ) :
 global lisp_rloc_probe_timer
 if 38 - 38: I1IiiI / OoooooooOO
 if ( lisp_rloc_probe_timer != None ) : lisp_rloc_probe_timer . cancel ( )
 if 16 - 16: i1IIi . i11iIiiIii . oO0o - I11i
 o0OO0OO0 = lisp_process_rloc_probe_timer
 iiI1I = threading . Timer ( interval , o0OO0OO0 , [ lisp_sockets ] )
 lisp_rloc_probe_timer = iiI1I
 iiI1I . start ( )
 return
 if 93 - 93: O0 . OoOoOO00 - O0 * I1ii11iIi11i % iII111i
 if 98 - 98: o0oOOo0O0Ooo . OoO0O00 * iII111i * oO0o * ooOoO0o / OOooOOo
 if 8 - 8: o0oOOo0O0Ooo - I1Ii111 % iIii1I11I1II1 - O0 + o0oOOo0O0Ooo
 if 56 - 56: i1IIi
 if 71 - 71: I1IiiI . OOooOOo . I1ii11iIi11i
 if 90 - 90: i11iIiiIii + I1Ii111 % II111iiii
 if 67 - 67: OoOoOO00 / iII111i * OoO0O00 % i11iIiiIii
def lisp_show_rloc_probe_list ( ) :
 lprint ( bold ( "----- RLOC-probe-list -----" , False ) )
 for o0Oo in lisp_rloc_probe_list :
  o0O0o0o = lisp_rloc_probe_list [ o0Oo ]
  lprint ( "RLOC {}:" . format ( o0Oo ) )
  for I1I111iIiI , iIIi1iI1I1IIi , i11ii in o0O0o0o :
   lprint ( "  [{}, {}, {}, {}]" . format ( hex ( id ( I1I111iIiI ) ) , iIIi1iI1I1IIi . print_prefix ( ) ,
 i11ii . print_prefix ( ) , I1I111iIiI . translated_port ) )
   if 74 - 74: Oo0Ooo / oO0o + IiII * IiII % iII111i / iIii1I11I1II1
   if 15 - 15: Ii1I
 lprint ( bold ( "---------------------------" , False ) )
 return
 if 50 - 50: II111iiii * O0 / I1IiiI
 if 11 - 11: I1IiiI
 if 92 - 92: iIii1I11I1II1 - I11i - OOooOOo / Ii1I . o0oOOo0O0Ooo . OoO0O00
 if 33 - 33: oO0o / I11i % ooOoO0o * I11i / oO0o - OoOoOO00
 if 89 - 89: iIii1I11I1II1 . II111iiii + IiII
 if 8 - 8: I1ii11iIi11i / II111iiii / II111iiii
 if 62 - 62: I11i - iII111i . Ii1I
 if 20 - 20: I1ii11iIi11i
 if 99 - 99: o0oOOo0O0Ooo + I1ii11iIi11i * IiII
def lisp_mark_rlocs_for_other_eids ( eid_list ) :
 if 67 - 67: I1IiiI
 if 93 - 93: ooOoO0o . Ii1I + IiII / Oo0Ooo % I11i
 if 40 - 40: Oo0Ooo % OoOoOO00 . IiII / I1IiiI % OoooooooOO
 if 33 - 33: OOooOOo - OoooooooOO . iII111i
 I1II , iIIi1iI1I1IIi , i11ii = eid_list [ 0 ]
 i1iIII = [ lisp_print_eid_tuple ( iIIi1iI1I1IIi , i11ii ) ]
 if 72 - 72: iIii1I11I1II1 + OOooOOo * ooOoO0o * O0 - I1IiiI
 for I1II , iIIi1iI1I1IIi , i11ii in eid_list [ 1 : : ] :
  I1II . state = LISP_RLOC_UNREACH_STATE
  I1II . last_state_change = lisp_get_timestamp ( )
  i1iIII . append ( lisp_print_eid_tuple ( iIIi1iI1I1IIi , i11ii ) )
  if 36 - 36: I11i / II111iiii . oO0o - ooOoO0o % iII111i % OoOoOO00
  if 13 - 13: iIii1I11I1II1 - Oo0Ooo % IiII / iII111i - I1Ii111
 iI1i1 = bold ( "unreachable" , False )
 O0ooo0Ooo = red ( I1II . rloc . print_address_no_iid ( ) , False )
 if 17 - 17: IiII
 for iiI1I1IIi in i1iIII :
  iIIi1iI1I1IIi = green ( iiI1I1IIi , False )
  lprint ( "RLOC {} went {} for EID {}" . format ( O0ooo0Ooo , iI1i1 , iIIi1iI1I1IIi ) )
  if 94 - 94: O0 - Oo0Ooo
  if 40 - 40: o0oOOo0O0Ooo
  if 50 - 50: i11iIiiIii . I1ii11iIi11i * I1Ii111
  if 22 - 22: I1ii11iIi11i . i1IIi + I1ii11iIi11i / OoooooooOO - i11iIiiIii / iIii1I11I1II1
  if 96 - 96: o0oOOo0O0Ooo . I1Ii111 + Oo0Ooo . I11i + ooOoO0o
  if 33 - 33: OoO0O00 / OOooOOo % Oo0Ooo . o0oOOo0O0Ooo % II111iiii
 for I1II , iIIi1iI1I1IIi , i11ii in eid_list :
  o0Oo0 = lisp_map_cache . lookup_cache ( iIIi1iI1I1IIi , True )
  if ( o0Oo0 ) : lisp_write_ipc_map_cache ( True , o0Oo0 )
  if 62 - 62: iII111i . OoooooooOO - i1IIi
 return
 if 59 - 59: OoOoOO00 + i1IIi * OoooooooOO . oO0o
 if 38 - 38: I1ii11iIi11i / o0oOOo0O0Ooo
 if 95 - 95: iIii1I11I1II1 / OoOoOO00 % I1Ii111
 if 54 - 54: OoooooooOO % Ii1I
 if 100 - 100: OOooOOo - I11i . O0 * i1IIi % OoooooooOO - ooOoO0o
 if 54 - 54: O0 + I11i
 if 71 - 71: OoOoOO00
 if 29 - 29: O0 . i11iIiiIii
 if 51 - 51: IiII
 if 53 - 53: O0
def lisp_process_rloc_probe_timer ( lisp_sockets ) :
 lisp_set_exception ( )
 if 19 - 19: o0oOOo0O0Ooo / iII111i % OoOoOO00
 lisp_start_rloc_probe_timer ( LISP_RLOC_PROBE_INTERVAL , lisp_sockets )
 if ( lisp_rloc_probing == False ) : return
 if 65 - 65: o0oOOo0O0Ooo
 if 89 - 89: iIii1I11I1II1 + OoooooooOO + i1IIi + OoooooooOO % IiII * OoO0O00
 if 53 - 53: OOooOOo . IiII % I11i - OoO0O00 - Oo0Ooo
 if 58 - 58: I1Ii111 / OoooooooOO . I11i % I1Ii111
 if ( lisp_print_rloc_probe_list ) : lisp_show_rloc_probe_list ( )
 if 8 - 8: Oo0Ooo % ooOoO0o / i11iIiiIii
 if 54 - 54: IiII
 if 85 - 85: OOooOOo - i1IIi
 if 10 - 10: I1ii11iIi11i
 i1iiIi1IIi111 = lisp_get_default_route_next_hops ( )
 if 59 - 59: I11i
 lprint ( "---------- Start RLOC Probing for {} entries ----------" . format ( len ( lisp_rloc_probe_list ) ) )
 if 23 - 23: OoOoOO00 * I1Ii111
 if 18 - 18: o0oOOo0O0Ooo % i11iIiiIii . Ii1I . O0
 if 85 - 85: I1ii11iIi11i * iIii1I11I1II1 + o0oOOo0O0Ooo * OoO0O00
 if 25 - 25: o0oOOo0O0Ooo / Ii1I / Oo0Ooo . ooOoO0o - ooOoO0o * O0
 if 14 - 14: O0 - Ii1I + iIii1I11I1II1 + II111iiii . ooOoO0o + Ii1I
 I1I1 = 0
 oO0oo000O = bold ( "RLOC-probe" , False )
 for iIIiIIII11iii in lisp_rloc_probe_list . values ( ) :
  if 39 - 39: ooOoO0o . OOooOOo . ooOoO0o + oO0o + Oo0Ooo
  if 25 - 25: IiII * OoO0O00 - OOooOOo
  if 100 - 100: oO0o % i1IIi + iII111i * oO0o / iIii1I11I1II1
  if 26 - 26: OoOoOO00 + oO0o + IiII / Ii1I - O0
  if 25 - 25: iIii1I11I1II1 . i1IIi
  OO0OO0000O = None
  for O0Oooo0O0ooOooO , iiI1I1IIi , OOo0oOOO0 in iIIiIIII11iii :
   oo0o00OO = O0Oooo0O0ooOooO . rloc . print_address_no_iid ( )
   if 45 - 45: I1Ii111 % OoOoOO00 / I1Ii111 % OoO0O00 . I1IiiI
   if 100 - 100: OoO0O00 - Ii1I + i1IIi / o0oOOo0O0Ooo / IiII
   if 85 - 85: OoOoOO00
   if 90 - 90: o0oOOo0O0Ooo . OoOoOO00 - i11iIiiIii * IiII
   o0O0OoO , Iii1i11i , IIIi1i1iIIIi = lisp_allow_gleaning ( iiI1I1IIi , None , O0Oooo0O0ooOooO )
   if ( o0O0OoO and Iii1i11i == False ) :
    iIIi1iI1I1IIi = green ( iiI1I1IIi . print_address ( ) , False )
    oo0o00OO += ":{}" . format ( O0Oooo0O0ooOooO . translated_port )
    lprint ( "Suppress probe to RLOC {} for gleaned EID {}" . format ( red ( oo0o00OO , False ) , iIIi1iI1I1IIi ) )
    if 30 - 30: iIii1I11I1II1 * OoooooooOO . I1ii11iIi11i . i11iIiiIii . I1Ii111 * iIii1I11I1II1
    continue
    if 53 - 53: OoOoOO00 * I1ii11iIi11i % OoOoOO00 - OoO0O00 / I1ii11iIi11i / I1Ii111
    if 23 - 23: i11iIiiIii * OoooooooOO % OoooooooOO % i11iIiiIii . iIii1I11I1II1 + II111iiii
    if 49 - 49: i11iIiiIii - OoO0O00
    if 81 - 81: I11i - OOooOOo / oO0o - ooOoO0o
    if 60 - 60: OoO0O00 / I1ii11iIi11i % iII111i % i11iIiiIii * OoooooooOO * iII111i
    if 92 - 92: I11i % iIii1I11I1II1 * iII111i - OoooooooOO - I11i
    if 34 - 34: I1Ii111 / i1IIi / O0 / OoooooooOO
   if ( O0Oooo0O0ooOooO . down_state ( ) ) : continue
   if 55 - 55: I1Ii111 . I1IiiI * iIii1I11I1II1 / Ii1I . I1IiiI
   if 63 - 63: ooOoO0o . Ii1I - I1Ii111 - oO0o * I1Ii111 + ooOoO0o
   if 85 - 85: II111iiii + I1ii11iIi11i
   if 33 - 33: iII111i
   if 14 - 14: O0 * Oo0Ooo / i1IIi
   if 95 - 95: O0 % i1IIi % ooOoO0o % oO0o - I1IiiI
   if 78 - 78: II111iiii % OOooOOo
   if 6 - 6: OOooOOo
   if 21 - 21: I1Ii111 - Ii1I - i1IIi % oO0o
   if 55 - 55: OOooOOo + oO0o - II111iiii
   if 5 - 5: iII111i * OoooooooOO . OoO0O00 % ooOoO0o + Ii1I
   if ( OO0OO0000O ) :
    O0Oooo0O0ooOooO . last_rloc_probe_nonce = OO0OO0000O . last_rloc_probe_nonce
    if 59 - 59: OoOoOO00
    if ( OO0OO0000O . translated_port == O0Oooo0O0ooOooO . translated_port and OO0OO0000O . rloc_name == O0Oooo0O0ooOooO . rloc_name ) :
     if 96 - 96: I1IiiI
     iIIi1iI1I1IIi = green ( lisp_print_eid_tuple ( iiI1I1IIi , OOo0oOOO0 ) , False )
     lprint ( "Suppress probe to duplicate RLOC {} for {}" . format ( red ( oo0o00OO , False ) , iIIi1iI1I1IIi ) )
     if 3 - 3: OoooooooOO
     if 3 - 3: IiII / O0 * i11iIiiIii . iII111i - iIii1I11I1II1
     if 56 - 56: ooOoO0o
     if 82 - 82: ooOoO0o . IiII . I1Ii111 - iIii1I11I1II1 + II111iiii . OoOoOO00
     if 59 - 59: Oo0Ooo
     if 98 - 98: I1Ii111 * II111iiii / Oo0Ooo . Oo0Ooo % I1Ii111
     O0Oooo0O0ooOooO . last_rloc_probe = OO0OO0000O . last_rloc_probe
     continue
     if 52 - 52: OoOoOO00
     if 59 - 59: ooOoO0o / OoooooooOO
     if 71 - 71: OOooOOo + I11i * O0 / o0oOOo0O0Ooo + I1IiiI + Ii1I
   o0OoiIiIIi = None
   I1II = None
   while ( True ) :
    I1II = O0Oooo0O0ooOooO if I1II == None else I1II . next_rloc
    if ( I1II == None ) : break
    if 41 - 41: ooOoO0o * I1Ii111
    if 40 - 40: OoOoOO00
    if 60 - 60: IiII . i11iIiiIii * II111iiii . Ii1I
    if 10 - 10: O0
    if 65 - 65: I11i % i11iIiiIii + i11iIiiIii % II111iiii
    if ( I1II . rloc_next_hop != None ) :
     if ( I1II . rloc_next_hop not in i1iiIi1IIi111 ) :
      if ( I1II . up_state ( ) ) :
       o0 , O0Oo0o = I1II . rloc_next_hop
       I1II . state = LISP_RLOC_UNREACH_STATE
       I1II . last_state_change = lisp_get_timestamp ( )
       lisp_update_rtr_updown ( I1II . rloc , False )
       if 95 - 95: I1Ii111 - I11i . II111iiii . i1IIi / II111iiii + Oo0Ooo
      iI1i1 = bold ( "unreachable" , False )
      lprint ( "Next-hop {}({}) for RLOC {} is {}" . format ( O0Oo0o , o0 ,
 red ( oo0o00OO , False ) , iI1i1 ) )
      continue
      if 96 - 96: iIii1I11I1II1 * iII111i / OOooOOo * iIii1I11I1II1 - O0
      if 28 - 28: I11i / I1IiiI - I1Ii111 + I1ii11iIi11i % iIii1I11I1II1
      if 35 - 35: iIii1I11I1II1 % Oo0Ooo % iII111i / iIii1I11I1II1 - I1ii11iIi11i . Oo0Ooo
      if 81 - 81: II111iiii + oO0o
      if 67 - 67: ooOoO0o + I11i - I1ii11iIi11i - OoooooooOO
      if 37 - 37: I11i % I1IiiI
    IiI1i11iiII = I1II . last_rloc_probe
    I1iii1 = 0 if IiI1i11iiII == None else time . time ( ) - IiI1i11iiII
    if ( I1II . unreach_state ( ) and I1iii1 < LISP_RLOC_PROBE_INTERVAL ) :
     lprint ( "Waiting for probe-reply from RLOC {}" . format ( red ( oo0o00OO , False ) ) )
     if 87 - 87: IiII % iIii1I11I1II1 * I1ii11iIi11i
     continue
     if 43 - 43: Ii1I - IiII / i11iIiiIii + OoOoOO00 + I1ii11iIi11i - o0oOOo0O0Ooo
     if 39 - 39: OoOoOO00 - i1IIi / oO0o % I11i * o0oOOo0O0Ooo * I1IiiI
     if 79 - 79: Ii1I
     if 56 - 56: I1ii11iIi11i
     if 40 - 40: OoooooooOO
     if 100 - 100: IiII - I11i
    oooooO0oO0o = lisp_get_echo_nonce ( None , oo0o00OO )
    if ( oooooO0oO0o and oooooO0oO0o . request_nonce_timeout ( ) ) :
     I1II . state = LISP_RLOC_NO_ECHOED_NONCE_STATE
     I1II . last_state_change = lisp_get_timestamp ( )
     iI1i1 = bold ( "unreachable" , False )
     lprint ( "RLOC {} went {}, nonce-echo failed" . format ( red ( oo0o00OO , False ) , iI1i1 ) )
     if 79 - 79: iII111i % O0
     lisp_update_rtr_updown ( I1II . rloc , False )
     continue
     if 73 - 73: Oo0Ooo
     if 13 - 13: OOooOOo - ooOoO0o
     if 8 - 8: I1Ii111 % oO0o
     if 19 - 19: O0 + OoO0O00 - i1IIi % OoOoOO00 / Oo0Ooo + OoooooooOO
     if 93 - 93: i11iIiiIii % OOooOOo . I11i * ooOoO0o
     if 90 - 90: OoO0O00
    if ( oooooO0oO0o and oooooO0oO0o . recently_echoed ( ) ) :
     lprint ( ( "Suppress RLOC-probe to {}, nonce-echo " + "received" ) . format ( red ( oo0o00OO , False ) ) )
     if 54 - 54: OOooOOo + Oo0Ooo * o0oOOo0O0Ooo - iIii1I11I1II1 * ooOoO0o
     continue
     if 76 - 76: i11iIiiIii * I1IiiI - IiII . o0oOOo0O0Ooo % iII111i . i11iIiiIii
     if 69 - 69: O0 + o0oOOo0O0Ooo / ooOoO0o
     if 7 - 7: Ii1I . Ii1I . iIii1I11I1II1 / ooOoO0o
     if 70 - 70: O0
     if 42 - 42: I1Ii111 + OoooooooOO + I11i
     if 48 - 48: Oo0Ooo . IiII / ooOoO0o + I11i
    if ( I1II . last_rloc_probe != None ) :
     IiI1i11iiII = I1II . last_rloc_probe_reply
     if ( IiI1i11iiII == None ) : IiI1i11iiII = 0
     I1iii1 = time . time ( ) - IiI1i11iiII
     if ( I1II . up_state ( ) and I1iii1 >= LISP_RLOC_PROBE_REPLY_WAIT ) :
      if 40 - 40: I1IiiI + I1ii11iIi11i * I1IiiI % Ii1I
      I1II . state = LISP_RLOC_UNREACH_STATE
      I1II . last_state_change = lisp_get_timestamp ( )
      lisp_update_rtr_updown ( I1II . rloc , False )
      iI1i1 = bold ( "unreachable" , False )
      lprint ( "RLOC {} went {}, probe it" . format ( red ( oo0o00OO , False ) , iI1i1 ) )
      if 27 - 27: O0 / Oo0Ooo . oO0o
      if 34 - 34: I1Ii111 % Ii1I / Oo0Ooo % ooOoO0o / i11iIiiIii * I1IiiI
      lisp_mark_rlocs_for_other_eids ( iIIiIIII11iii )
      if 36 - 36: i11iIiiIii * i1IIi % iII111i . Oo0Ooo
      if 54 - 54: o0oOOo0O0Ooo % i1IIi % I1ii11iIi11i . o0oOOo0O0Ooo / OoOoOO00
      if 55 - 55: O0 / OoooooooOO % Ii1I * O0 + iIii1I11I1II1 . iIii1I11I1II1
    I1II . last_rloc_probe = lisp_get_timestamp ( )
    if 55 - 55: Ii1I . OoooooooOO % Ii1I . IiII
    oooOoooOO = "" if I1II . unreach_state ( ) == False else " unreachable"
    if 12 - 12: I1IiiI
    if 50 - 50: ooOoO0o
    if 19 - 19: OoooooooOO / IiII
    if 40 - 40: OoOoOO00 / OoooooooOO * iIii1I11I1II1 / i1IIi . OoooooooOO
    if 88 - 88: I1IiiI % I1IiiI / II111iiii - IiII
    if 72 - 72: OoO0O00 - I1ii11iIi11i . Oo0Ooo / OoO0O00
    if 86 - 86: i11iIiiIii - oO0o . i11iIiiIii
    oO0O0oooo = ""
    O0Oo0o = None
    if ( I1II . rloc_next_hop != None ) :
     o0 , O0Oo0o = I1II . rloc_next_hop
     lisp_install_host_route ( oo0o00OO , O0Oo0o , True )
     oO0O0oooo = ", send on nh {}({})" . format ( O0Oo0o , o0 )
     if 28 - 28: i11iIiiIii / O0 / iIii1I11I1II1 / I1IiiI % OoooooooOO % ooOoO0o
     if 29 - 29: I1ii11iIi11i
     if 12 - 12: I11i . o0oOOo0O0Ooo . iIii1I11I1II1
     if 93 - 93: ooOoO0o - OoooooooOO + iIii1I11I1II1 / o0oOOo0O0Ooo + iIii1I11I1II1
     if 9 - 9: OoOoOO00 + ooOoO0o
    iIIi = I1II . print_rloc_probe_rtt ( )
    ooOOoo = oo0o00OO
    if ( I1II . translated_port != 0 ) :
     ooOOoo += ":{}" . format ( I1II . translated_port )
     if 86 - 86: i1IIi - I1Ii111
    ooOOoo = red ( ooOOoo , False )
    if ( I1II . rloc_name != None ) :
     ooOOoo += " (" + blue ( I1II . rloc_name , False ) + ")"
     if 29 - 29: iII111i * i11iIiiIii % OoOoOO00 * ooOoO0o
    lprint ( "Send {}{} {}, last rtt: {}{}" . format ( oO0oo000O , oooOoooOO ,
 ooOOoo , iIIi , oO0O0oooo ) )
    if 41 - 41: iIii1I11I1II1
    if 52 - 52: ooOoO0o - O0 * OoO0O00 / oO0o
    if 36 - 36: iII111i - oO0o + iIii1I11I1II1 / IiII + i11iIiiIii % I11i
    if 89 - 89: iIii1I11I1II1 . I11i + OOooOOo / i11iIiiIii / I1ii11iIi11i * i11iIiiIii
    if 20 - 20: I1Ii111 . II111iiii % II111iiii
    if 79 - 79: II111iiii . I11i + o0oOOo0O0Ooo % I1ii11iIi11i + I1ii11iIi11i
    if 4 - 4: I1ii11iIi11i % OoooooooOO
    if 43 - 43: IiII - I1Ii111 % ooOoO0o
    if ( I1II . rloc_next_hop != None ) :
     o0OoiIiIIi = lisp_get_host_route_next_hop ( oo0o00OO )
     if ( o0OoiIiIIi ) : lisp_install_host_route ( oo0o00OO , o0OoiIiIIi , False )
     if 49 - 49: OoOoOO00
     if 43 - 43: I1Ii111 - Oo0Ooo % i1IIi . II111iiii
     if 80 - 80: IiII . iII111i + I1Ii111 + iII111i % Oo0Ooo
     if 98 - 98: i11iIiiIii . II111iiii + OoOoOO00
     if 25 - 25: I1IiiI + i11iIiiIii . I1Ii111 - I1ii11iIi11i
     if 67 - 67: OOooOOo - OOooOOo * I1IiiI - II111iiii . i1IIi + Oo0Ooo
    if ( I1II . rloc . is_null ( ) ) :
     I1II . rloc . copy_address ( O0Oooo0O0ooOooO . rloc )
     if 97 - 97: O0 / i11iIiiIii - o0oOOo0O0Ooo - OoOoOO00 . oO0o
     if 77 - 77: oO0o * oO0o . OoOoOO00 . i1IIi
     if 90 - 90: OOooOOo . Ii1I . II111iiii + Ii1I
     if 2 - 2: I1Ii111 * OOooOOo + II111iiii - OoOoOO00
     if 94 - 94: Ii1I - iII111i . I1ii11iIi11i - Oo0Ooo % o0oOOo0O0Ooo + I1Ii111
    i1IiIiii = None if ( OOo0oOOO0 . is_null ( ) ) else iiI1I1IIi
    OOoo0OOo = iiI1I1IIi if ( OOo0oOOO0 . is_null ( ) ) else OOo0oOOO0
    lisp_send_map_request ( lisp_sockets , 0 , i1IiIiii , OOoo0OOo , I1II )
    OO0OO0000O = O0Oooo0O0ooOooO
    if 82 - 82: iII111i + OoooooooOO % iIii1I11I1II1 - o0oOOo0O0Ooo - i1IIi / Oo0Ooo
    if 13 - 13: iII111i % oO0o - I11i . i11iIiiIii / iIii1I11I1II1
    if 11 - 11: iII111i % OoO0O00 % iIii1I11I1II1 + IiII * Ii1I
    if 93 - 93: OOooOOo / iII111i
    if ( O0Oo0o ) : lisp_install_host_route ( oo0o00OO , O0Oo0o , False )
    if 74 - 74: I1ii11iIi11i
    if 83 - 83: iII111i + i1IIi - OoooooooOO
    if 16 - 16: i1IIi
    if 86 - 86: OoOoOO00 - iII111i - Oo0Ooo
    if 33 - 33: Ii1I - OoO0O00
   if ( o0OoiIiIIi ) : lisp_install_host_route ( oo0o00OO , o0OoiIiIIi , True )
   if 15 - 15: O0 . iIii1I11I1II1 - I1Ii111 + O0 + ooOoO0o / I1IiiI
   if 8 - 8: iII111i % O0 - OoOoOO00
   if 49 - 49: oO0o - OOooOOo / Ii1I / I1Ii111 . o0oOOo0O0Ooo . iII111i
   if 58 - 58: IiII + Ii1I
   I1I1 += 1
   if ( ( I1I1 % 10 ) == 0 ) : time . sleep ( 0.020 )
   if 89 - 89: Ii1I / Oo0Ooo * o0oOOo0O0Ooo / OoO0O00 + I11i
   if 4 - 4: I11i
   if 59 - 59: OoOoOO00 * I1ii11iIi11i / I1IiiI * II111iiii + OoOoOO00
 lprint ( "---------- End RLOC Probing ----------" )
 return
 if 6 - 6: OoOoOO00 % oO0o + I11i * Ii1I
 if 13 - 13: I1ii11iIi11i / Oo0Ooo - I1Ii111 * OoOoOO00
 if 47 - 47: IiII
 if 76 - 76: iII111i / II111iiii / I11i
 if 62 - 62: I1ii11iIi11i
 if 100 - 100: iII111i / ooOoO0o / IiII % II111iiii
 if 6 - 6: OoooooooOO - I1IiiI + OoooooooOO
 if 89 - 89: oO0o % Oo0Ooo . O0 . ooOoO0o
def lisp_update_rtr_updown ( rtr , updown ) :
 global lisp_ipc_socket
 if 46 - 46: IiII * I11i - OoO0O00 - Ii1I
 if 93 - 93: iIii1I11I1II1 / o0oOOo0O0Ooo - I11i - OOooOOo % ooOoO0o
 if 16 - 16: ooOoO0o * o0oOOo0O0Ooo - IiII + I1ii11iIi11i / o0oOOo0O0Ooo - O0
 if 71 - 71: i1IIi
 if ( lisp_i_am_itr == False ) : return
 if 79 - 79: iII111i * O0 / Ii1I / O0 % i1IIi
 if 52 - 52: OoooooooOO % oO0o - I11i % OoOoOO00 . II111iiii
 if 62 - 62: Ii1I . I1ii11iIi11i . iII111i + I11i * o0oOOo0O0Ooo
 if 56 - 56: oO0o * iIii1I11I1II1 . II111iiii - II111iiii + II111iiii - i11iIiiIii
 if 79 - 79: iII111i
 if ( lisp_register_all_rtrs ) : return
 if 29 - 29: Ii1I * I1Ii111 / OoO0O00 - O0 - i11iIiiIii * I1IiiI
 iI1O0oOOO = rtr . print_address_no_iid ( )
 if 62 - 62: IiII - I1Ii111
 if 68 - 68: Oo0Ooo + oO0o - OoO0O00
 if 17 - 17: I11i % I1ii11iIi11i - I1IiiI % oO0o + I1ii11iIi11i
 if 68 - 68: i1IIi . ooOoO0o . Oo0Ooo + iII111i . I1IiiI * i1IIi
 if 88 - 88: iII111i + i11iIiiIii
 if ( lisp_rtr_list . has_key ( iI1O0oOOO ) == False ) : return
 if 42 - 42: I1Ii111 * O0 / OoO0O00 + iII111i
 updown = "up" if updown else "down"
 lprint ( "Send ETR IPC message, RTR {} has done {}" . format (
 red ( iI1O0oOOO , False ) , bold ( updown , False ) ) )
 if 86 - 86: OOooOOo
 if 6 - 6: oO0o % iII111i * Oo0Ooo - i11iIiiIii . OoooooooOO
 if 85 - 85: O0 * i1IIi
 if 29 - 29: i11iIiiIii
 oOOO0oo0 = "rtr%{}%{}" . format ( iI1O0oOOO , updown )
 oOOO0oo0 = lisp_command_ipc ( oOOO0oo0 , "lisp-itr" )
 lisp_ipc ( oOOO0oo0 , lisp_ipc_socket , "lisp-etr" )
 return
 if 34 - 34: OoOoOO00
 if 17 - 17: oO0o * OoOoOO00 % OoO0O00 % I1IiiI * I11i
 if 78 - 78: OoooooooOO . I1Ii111 + Ii1I - II111iiii - IiII / iIii1I11I1II1
 if 92 - 92: Ii1I
 if 34 - 34: OOooOOo * OoooooooOO / I1ii11iIi11i
 if 41 - 41: i1IIi
 if 75 - 75: o0oOOo0O0Ooo . I1Ii111 - I1Ii111 % Ii1I * OoooooooOO
def lisp_process_rloc_probe_reply ( rloc_entry , source , port , map_reply , ttl ,
 mrloc ) :
 I1II = rloc_entry . rloc
 o0OOO = map_reply . nonce
 O0OOo0o = map_reply . hop_count
 oO0oo000O = bold ( "RLOC-probe reply" , False )
 O0OOOoOoO00 = I1II . print_address_no_iid ( )
 oOOiI1Ii1 = source . print_address_no_iid ( )
 o0O0O00ooo = lisp_rloc_probe_list
 oOooo0o = rloc_entry . json . json_string if rloc_entry . json else None
 i1 = lisp_get_timestamp ( )
 if 14 - 14: I1IiiI * Ii1I % OoOoOO00 / I1IiiI
 if 87 - 87: OOooOOo - i1IIi
 if 65 - 65: I11i - ooOoO0o / i1IIi - OOooOOo
 if 74 - 74: O0 - II111iiii + iIii1I11I1II1 % I1IiiI % OoOoOO00
 if 57 - 57: O0 * Ii1I / I1IiiI
 if 54 - 54: iIii1I11I1II1 + iII111i % OoOoOO00 % OOooOOo
 if ( mrloc != None ) :
  O0O = mrloc . rloc . print_address_no_iid ( )
  if ( mrloc . multicast_rloc_probe_list . has_key ( O0OOOoOoO00 ) == False ) :
   ii11II = lisp_rloc ( )
   ii11II = copy . deepcopy ( mrloc )
   ii11II . rloc . copy_address ( I1II )
   ii11II . multicast_rloc_probe_list = { }
   mrloc . multicast_rloc_probe_list [ O0OOOoOoO00 ] = ii11II
   if 84 - 84: I1Ii111 % Oo0Ooo
  ii11II = mrloc . multicast_rloc_probe_list [ O0OOOoOoO00 ]
  ii11II . last_rloc_probe_nonce = mrloc . last_rloc_probe_nonce
  ii11II . last_rloc_probe = mrloc . last_rloc_probe
  I1I111iIiI , iiI1I1IIi , OOo0oOOO0 = lisp_rloc_probe_list [ O0O ] [ 0 ]
  ii11II . process_rloc_probe_reply ( i1 , o0OOO , iiI1I1IIi , OOo0oOOO0 , O0OOo0o , ttl , oOooo0o )
  mrloc . process_rloc_probe_reply ( i1 , o0OOO , iiI1I1IIi , OOo0oOOO0 , O0OOo0o , ttl , oOooo0o )
  return
  if 81 - 81: Oo0Ooo % Oo0Ooo / OoOoOO00 - I1IiiI - i11iIiiIii
  if 82 - 82: O0 / oO0o - I1IiiI . oO0o % oO0o / OOooOOo
  if 20 - 20: OoOoOO00 / I1Ii111 + I1ii11iIi11i
  if 36 - 36: I1ii11iIi11i % OoO0O00 + I11i / iII111i % OOooOOo
  if 5 - 5: oO0o % OOooOOo
  if 95 - 95: OoOoOO00 + OoooooooOO - O0 + o0oOOo0O0Ooo
  if 88 - 88: i11iIiiIii . iIii1I11I1II1
 o0o00O0oOooO0 = O0OOOoOoO00
 if ( o0O0O00ooo . has_key ( o0o00O0oOooO0 ) == False ) :
  o0o00O0oOooO0 += ":" + str ( port )
  if ( o0O0O00ooo . has_key ( o0o00O0oOooO0 ) == False ) :
   o0o00O0oOooO0 = oOOiI1Ii1
   if ( o0O0O00ooo . has_key ( o0o00O0oOooO0 ) == False ) :
    o0o00O0oOooO0 += ":" + str ( port )
    lprint ( "    Received unsolicited {} from {}/{}, port {}" . format ( oO0oo000O , red ( O0OOOoOoO00 , False ) , red ( oOOiI1Ii1 ,
    # IiII / iIii1I11I1II1 % iII111i * I11i
 False ) , port ) )
    return
    if 77 - 77: Ii1I
    if 20 - 20: i1IIi % i1IIi + I1ii11iIi11i - I1ii11iIi11i - OoO0O00
    if 54 - 54: II111iiii * IiII - OOooOOo
    if 91 - 91: OoooooooOO % O0 * OoooooooOO . OOooOOo * I1Ii111 + OoO0O00
    if 6 - 6: IiII + I11i / Ii1I / Oo0Ooo - oO0o
    if 31 - 31: i11iIiiIii % oO0o + ooOoO0o - i1IIi
    if 87 - 87: IiII + oO0o
    if 87 - 87: ooOoO0o
 for I1II , iiI1I1IIi , OOo0oOOO0 in lisp_rloc_probe_list [ o0o00O0oOooO0 ] :
  if ( lisp_i_am_rtr ) :
   if ( I1II . translated_port != 0 and I1II . translated_port != port ) :
    continue
    if 47 - 47: i11iIiiIii
    if 84 - 84: Ii1I + ooOoO0o
  I1II . process_rloc_probe_reply ( i1 , o0OOO , iiI1I1IIi , OOo0oOOO0 , O0OOo0o , ttl , oOooo0o )
  if 81 - 81: I1ii11iIi11i - iIii1I11I1II1
 return
 if 31 - 31: I11i * oO0o % I1ii11iIi11i * I1Ii111 % OoOoOO00 + oO0o
 if 33 - 33: I1Ii111
 if 96 - 96: i1IIi
 if 52 - 52: OoO0O00 * Ii1I + OOooOOo + ooOoO0o * OoooooooOO
 if 34 - 34: I1Ii111 . I1Ii111 * ooOoO0o % OoOoOO00
 if 71 - 71: I1Ii111 - I1Ii111
 if 13 - 13: iII111i + I1ii11iIi11i - oO0o / IiII * i1IIi * Oo0Ooo
 if 65 - 65: Ii1I - OOooOOo % O0 * I1ii11iIi11i . II111iiii
def lisp_db_list_length ( ) :
 I1I1 = 0
 for ii1iii in lisp_db_list :
  I1I1 += len ( ii1iii . dynamic_eids ) if ii1iii . dynamic_eid_configured ( ) else 1
  I1I1 += len ( ii1iii . eid . iid_list )
  if 59 - 59: O0 . O0 / i11iIiiIii * Oo0Ooo . I11i . Ii1I
 return ( I1I1 )
 if 89 - 89: O0 + OoO0O00
 if 3 - 3: Oo0Ooo * OoooooooOO * oO0o % OoOoOO00 * OoOoOO00 . ooOoO0o
 if 16 - 16: ooOoO0o / o0oOOo0O0Ooo - O0 * I1IiiI
 if 13 - 13: iII111i . iII111i % O0 % o0oOOo0O0Ooo
 if 99 - 99: OoO0O00 - OoOoOO00 + OoO0O00
 if 67 - 67: I1Ii111
 if 31 - 31: OoO0O00 * Oo0Ooo % O0 * II111iiii + ooOoO0o * I1IiiI
 if 77 - 77: ooOoO0o
def lisp_is_myeid ( eid ) :
 for ii1iii in lisp_db_list :
  if ( eid . is_more_specific ( ii1iii . eid ) ) : return ( True )
  if 98 - 98: I1Ii111 + I1ii11iIi11i % OoO0O00 * Ii1I + iII111i
 return ( False )
 if 6 - 6: iII111i / iII111i . i11iIiiIii
 if 12 - 12: I11i - OoO0O00
 if 68 - 68: IiII - OoOoOO00
 if 22 - 22: i1IIi . IiII
 if 8 - 8: IiII % o0oOOo0O0Ooo . i11iIiiIii
 if 69 - 69: I1Ii111 / Ii1I - ooOoO0o
 if 38 - 38: II111iiii % OoooooooOO / OoooooooOO . Ii1I . Ii1I
 if 13 - 13: oO0o - i1IIi / i1IIi + OoooooooOO
 if 57 - 57: OoooooooOO / O0 + I1ii11iIi11i % I11i * oO0o / Ii1I
def lisp_format_macs ( sa , da ) :
 sa = sa [ 0 : 4 ] + "-" + sa [ 4 : 8 ] + "-" + sa [ 8 : 12 ]
 da = da [ 0 : 4 ] + "-" + da [ 4 : 8 ] + "-" + da [ 8 : 12 ]
 return ( "{} -> {}" . format ( sa , da ) )
 if 49 - 49: I1IiiI * ooOoO0o * OOooOOo + OoO0O00 + ooOoO0o
 if 42 - 42: i1IIi . OoO0O00 % iII111i
 if 57 - 57: I1ii11iIi11i / I1IiiI
 if 69 - 69: iII111i - iII111i . OoO0O00 / oO0o - OoO0O00 + I1Ii111
 if 98 - 98: iII111i . oO0o - O0 % I1IiiI . I1ii11iIi11i / i1IIi
 if 72 - 72: I1IiiI / Oo0Ooo % IiII - O0 / O0 * O0
 if 83 - 83: O0 / I1Ii111 - OoooooooOO
def lisp_get_echo_nonce ( rloc , rloc_str ) :
 if ( lisp_nonce_echoing == False ) : return ( None )
 if 42 - 42: Ii1I / i1IIi - IiII / I1Ii111
 if ( rloc ) : rloc_str = rloc . print_address_no_iid ( )
 oooooO0oO0o = None
 if ( lisp_nonce_echo_list . has_key ( rloc_str ) ) :
  oooooO0oO0o = lisp_nonce_echo_list [ rloc_str ]
  if 39 - 39: OoooooooOO
 return ( oooooO0oO0o )
 if 4 - 4: iIii1I11I1II1 - Oo0Ooo / OOooOOo % OoooooooOO . Oo0Ooo - Oo0Ooo
 if 41 - 41: II111iiii . o0oOOo0O0Ooo
 if 92 - 92: Ii1I - O0 - i11iIiiIii + IiII % I1Ii111 + II111iiii
 if 71 - 71: ooOoO0o * I1Ii111 + i11iIiiIii + i1IIi . I1IiiI
 if 15 - 15: OoO0O00
 if 37 - 37: OoO0O00 . OoooooooOO - OOooOOo
 if 34 - 34: o0oOOo0O0Ooo + iIii1I11I1II1 / o0oOOo0O0Ooo / ooOoO0o
 if 53 - 53: II111iiii / iIii1I11I1II1
def lisp_decode_dist_name ( packet ) :
 I1I1 = 0
 iIi1Iiii11Ii1 = ""
 if 27 - 27: II111iiii - i1IIi
 while ( packet [ 0 : 1 ] != "\0" ) :
  if ( I1I1 == 255 ) : return ( [ None , None ] )
  iIi1Iiii11Ii1 += packet [ 0 : 1 ]
  packet = packet [ 1 : : ]
  I1I1 += 1
  if 4 - 4: I1IiiI
  if 5 - 5: Ii1I / O0 + iIii1I11I1II1
 packet = packet [ 1 : : ]
 return ( packet , iIi1Iiii11Ii1 )
 if 22 - 22: ooOoO0o . ooOoO0o * OOooOOo % OoOoOO00
 if 51 - 51: OoOoOO00 . oO0o - OoOoOO00
 if 79 - 79: iII111i
 if 71 - 71: i1IIi / OoO0O00 / OOooOOo + I1Ii111
 if 80 - 80: Oo0Ooo . iIii1I11I1II1 . OoooooooOO % iII111i . oO0o
 if 10 - 10: i11iIiiIii * OoooooooOO . i11iIiiIii
 if 35 - 35: OOooOOo * OOooOOo + o0oOOo0O0Ooo / i1IIi - I11i
 if 12 - 12: I1ii11iIi11i - i11iIiiIii + I1IiiI . Oo0Ooo
def lisp_write_flow_log ( flow_log ) :
 I1ii1ii = open ( "./logs/lisp-flow.log" , "a" )
 if 26 - 26: oO0o + I1Ii111 + IiII * o0oOOo0O0Ooo . oO0o
 I1I1 = 0
 for o00oo00O0OoOo in flow_log :
  IiiiIi1iiii11 = o00oo00O0OoOo [ 3 ]
  OOI1 = IiiiIi1iiii11 . print_flow ( o00oo00O0OoOo [ 0 ] , o00oo00O0OoOo [ 1 ] , o00oo00O0OoOo [ 2 ] )
  I1ii1ii . write ( OOI1 )
  I1I1 += 1
  if 71 - 71: OoooooooOO + OoooooooOO - I1IiiI % o0oOOo0O0Ooo + OoooooooOO / iIii1I11I1II1
 I1ii1ii . close ( )
 del ( flow_log )
 if 32 - 32: OoooooooOO % O0
 I1I1 = bold ( str ( I1I1 ) , False )
 lprint ( "Wrote {} flow entries to ./logs/lisp-flow.log" . format ( I1I1 ) )
 return
 if 27 - 27: ooOoO0o / OoooooooOO % II111iiii % iII111i
 if 31 - 31: IiII + OoO0O00 + Ii1I % IiII * iII111i * O0
 if 65 - 65: ooOoO0o
 if 78 - 78: IiII - i1IIi - i11iIiiIii * o0oOOo0O0Ooo / I1IiiI
 if 98 - 98: i11iIiiIii / ooOoO0o * OOooOOo
 if 34 - 34: I1IiiI * oO0o + i1IIi * Oo0Ooo / ooOoO0o . Ii1I
 if 47 - 47: I11i * oO0o % I11i * i1IIi * II111iiii
def lisp_policy_command ( kv_pair ) :
 IiI1i1i1 = lisp_policy ( "" )
 I1I11iii1I1 = None
 if 98 - 98: IiII % I1IiiI
 IiI1I1I1i = [ ]
 for iIi1I1 in range ( len ( kv_pair [ "datetime-range" ] ) ) :
  IiI1I1I1i . append ( lisp_policy_match ( ) )
  if 89 - 89: OOooOOo + ooOoO0o * OoooooooOO * ooOoO0o % OoO0O00 - OoooooooOO
  if 8 - 8: OoOoOO00 / OoooooooOO
 for ooooooO0 in kv_pair . keys ( ) :
  Oo00OO0OO = kv_pair [ ooooooO0 ]
  if 83 - 83: iII111i % o0oOOo0O0Ooo * OoOoOO00
  if 49 - 49: II111iiii / OoO0O00
  if 69 - 69: Ii1I * II111iiii
  if 24 - 24: I1Ii111 * I1ii11iIi11i . OOooOOo . I1IiiI - I1ii11iIi11i
  if ( ooooooO0 == "instance-id" ) :
   for iIi1I1 in range ( len ( IiI1I1I1i ) ) :
    OOOOOO0O00O00 = Oo00OO0OO [ iIi1I1 ]
    if ( OOOOOO0O00O00 == "" ) : continue
    o00oOo0OOoo = IiI1I1I1i [ iIi1I1 ]
    if ( o00oOo0OOoo . source_eid == None ) :
     o00oOo0OOoo . source_eid = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
     if 19 - 19: iII111i % Ii1I / II111iiii + IiII / Oo0Ooo * OOooOOo
    if ( o00oOo0OOoo . dest_eid == None ) :
     o00oOo0OOoo . dest_eid = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
     if 34 - 34: OOooOOo . oO0o + I11i / I1Ii111 . I11i
    o00oOo0OOoo . source_eid . instance_id = int ( OOOOOO0O00O00 )
    o00oOo0OOoo . dest_eid . instance_id = int ( OOOOOO0O00O00 )
    if 59 - 59: Ii1I
    if 47 - 47: iII111i % iII111i
  if ( ooooooO0 == "source-eid" ) :
   for iIi1I1 in range ( len ( IiI1I1I1i ) ) :
    OOOOOO0O00O00 = Oo00OO0OO [ iIi1I1 ]
    if ( OOOOOO0O00O00 == "" ) : continue
    o00oOo0OOoo = IiI1I1I1i [ iIi1I1 ]
    if ( o00oOo0OOoo . source_eid == None ) :
     o00oOo0OOoo . source_eid = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
     if 81 - 81: oO0o / I1ii11iIi11i . OoooooooOO % II111iiii / oO0o
    IiIIi11i111 = o00oOo0OOoo . source_eid . instance_id
    o00oOo0OOoo . source_eid . store_prefix ( OOOOOO0O00O00 )
    o00oOo0OOoo . source_eid . instance_id = IiIIi11i111
    if 23 - 23: IiII + oO0o + o0oOOo0O0Ooo . I1ii11iIi11i / i11iIiiIii + iIii1I11I1II1
    if 74 - 74: I11i % OOooOOo
  if ( ooooooO0 == "destination-eid" ) :
   for iIi1I1 in range ( len ( IiI1I1I1i ) ) :
    OOOOOO0O00O00 = Oo00OO0OO [ iIi1I1 ]
    if ( OOOOOO0O00O00 == "" ) : continue
    o00oOo0OOoo = IiI1I1I1i [ iIi1I1 ]
    if ( o00oOo0OOoo . dest_eid == None ) :
     o00oOo0OOoo . dest_eid = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
     if 57 - 57: O0 + I1IiiI + i11iIiiIii
    IiIIi11i111 = o00oOo0OOoo . dest_eid . instance_id
    o00oOo0OOoo . dest_eid . store_prefix ( OOOOOO0O00O00 )
    o00oOo0OOoo . dest_eid . instance_id = IiIIi11i111
    if 90 - 90: I1ii11iIi11i . OoO0O00 * iIii1I11I1II1 - Oo0Ooo
    if 28 - 28: I1IiiI . ooOoO0o - ooOoO0o * OOooOOo . IiII
  if ( ooooooO0 == "source-rloc" ) :
   for iIi1I1 in range ( len ( IiI1I1I1i ) ) :
    OOOOOO0O00O00 = Oo00OO0OO [ iIi1I1 ]
    if ( OOOOOO0O00O00 == "" ) : continue
    o00oOo0OOoo = IiI1I1I1i [ iIi1I1 ]
    o00oOo0OOoo . source_rloc = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
    o00oOo0OOoo . source_rloc . store_prefix ( OOOOOO0O00O00 )
    if 16 - 16: iIii1I11I1II1 % i11iIiiIii / Ii1I % iIii1I11I1II1 / iII111i
    if 27 - 27: II111iiii * OoooooooOO / Oo0Ooo % O0
  if ( ooooooO0 == "destination-rloc" ) :
   for iIi1I1 in range ( len ( IiI1I1I1i ) ) :
    OOOOOO0O00O00 = Oo00OO0OO [ iIi1I1 ]
    if ( OOOOOO0O00O00 == "" ) : continue
    o00oOo0OOoo = IiI1I1I1i [ iIi1I1 ]
    o00oOo0OOoo . dest_rloc = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
    o00oOo0OOoo . dest_rloc . store_prefix ( OOOOOO0O00O00 )
    if 41 - 41: oO0o / iIii1I11I1II1 % iII111i - I1Ii111 % I11i * i11iIiiIii
    if 21 - 21: O0
  if ( ooooooO0 == "rloc-record-name" ) :
   for iIi1I1 in range ( len ( IiI1I1I1i ) ) :
    OOOOOO0O00O00 = Oo00OO0OO [ iIi1I1 ]
    if ( OOOOOO0O00O00 == "" ) : continue
    o00oOo0OOoo = IiI1I1I1i [ iIi1I1 ]
    o00oOo0OOoo . rloc_record_name = OOOOOO0O00O00
    if 14 - 14: IiII / I1ii11iIi11i + Ii1I
    if 48 - 48: I1Ii111 * oO0o / o0oOOo0O0Ooo * OoOoOO00 * ooOoO0o
  if ( ooooooO0 == "geo-name" ) :
   for iIi1I1 in range ( len ( IiI1I1I1i ) ) :
    OOOOOO0O00O00 = Oo00OO0OO [ iIi1I1 ]
    if ( OOOOOO0O00O00 == "" ) : continue
    o00oOo0OOoo = IiI1I1I1i [ iIi1I1 ]
    o00oOo0OOoo . geo_name = OOOOOO0O00O00
    if 38 - 38: I1IiiI * Ii1I + Oo0Ooo - OoooooooOO
    if 63 - 63: I1ii11iIi11i
  if ( ooooooO0 == "elp-name" ) :
   for iIi1I1 in range ( len ( IiI1I1I1i ) ) :
    OOOOOO0O00O00 = Oo00OO0OO [ iIi1I1 ]
    if ( OOOOOO0O00O00 == "" ) : continue
    o00oOo0OOoo = IiI1I1I1i [ iIi1I1 ]
    o00oOo0OOoo . elp_name = OOOOOO0O00O00
    if 99 - 99: I1Ii111 % oO0o - II111iiii . ooOoO0o
    if 26 - 26: I1ii11iIi11i * iII111i . OoooooooOO - Oo0Ooo - IiII
  if ( ooooooO0 == "rle-name" ) :
   for iIi1I1 in range ( len ( IiI1I1I1i ) ) :
    OOOOOO0O00O00 = Oo00OO0OO [ iIi1I1 ]
    if ( OOOOOO0O00O00 == "" ) : continue
    o00oOo0OOoo = IiI1I1I1i [ iIi1I1 ]
    o00oOo0OOoo . rle_name = OOOOOO0O00O00
    if 6 - 6: OOooOOo - I1IiiI . IiII
    if 40 - 40: II111iiii
  if ( ooooooO0 == "json-name" ) :
   for iIi1I1 in range ( len ( IiI1I1I1i ) ) :
    OOOOOO0O00O00 = Oo00OO0OO [ iIi1I1 ]
    if ( OOOOOO0O00O00 == "" ) : continue
    o00oOo0OOoo = IiI1I1I1i [ iIi1I1 ]
    o00oOo0OOoo . json_name = OOOOOO0O00O00
    if 13 - 13: OoOoOO00
    if 23 - 23: Oo0Ooo / II111iiii % OOooOOo % iII111i - Oo0Ooo / OoO0O00
  if ( ooooooO0 == "datetime-range" ) :
   for iIi1I1 in range ( len ( IiI1I1I1i ) ) :
    OOOOOO0O00O00 = Oo00OO0OO [ iIi1I1 ]
    o00oOo0OOoo = IiI1I1I1i [ iIi1I1 ]
    if ( OOOOOO0O00O00 == "" ) : continue
    IIi1I1 = lisp_datetime ( OOOOOO0O00O00 [ 0 : 19 ] )
    i1i1I111I = lisp_datetime ( OOOOOO0O00O00 [ 19 : : ] )
    if ( IIi1I1 . valid_datetime ( ) and i1i1I111I . valid_datetime ( ) ) :
     o00oOo0OOoo . datetime_lower = IIi1I1
     o00oOo0OOoo . datetime_upper = i1i1I111I
     if 7 - 7: Ii1I / I11i / II111iiii % I11i * I11i + iIii1I11I1II1
     if 6 - 6: iIii1I11I1II1 * oO0o - iIii1I11I1II1 . O0 . O0
     if 96 - 96: I1Ii111 * II111iiii % i11iIiiIii - oO0o
     if 32 - 32: i11iIiiIii * o0oOOo0O0Ooo . OoooooooOO / O0
     if 14 - 14: i11iIiiIii . I1Ii111 % I1ii11iIi11i . I1ii11iIi11i % IiII
     if 93 - 93: iIii1I11I1II1 / IiII
     if 91 - 91: i11iIiiIii % ooOoO0o - iII111i * I1Ii111 . i11iIiiIii
  if ( ooooooO0 == "set-action" ) :
   IiI1i1i1 . set_action = Oo00OO0OO
   if 1 - 1: IiII + iIii1I11I1II1 * I1ii11iIi11i - IiII - i1IIi
  if ( ooooooO0 == "set-record-ttl" ) :
   IiI1i1i1 . set_record_ttl = int ( Oo00OO0OO )
   if 75 - 75: II111iiii * o0oOOo0O0Ooo / I1ii11iIi11i
  if ( ooooooO0 == "set-instance-id" ) :
   if ( IiI1i1i1 . set_source_eid == None ) :
    IiI1i1i1 . set_source_eid = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
    if 46 - 46: OOooOOo
   if ( IiI1i1i1 . set_dest_eid == None ) :
    IiI1i1i1 . set_dest_eid = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
    if 67 - 67: OoO0O00 . I11i % OOooOOo + Oo0Ooo
   I1I11iii1I1 = int ( Oo00OO0OO )
   IiI1i1i1 . set_source_eid . instance_id = I1I11iii1I1
   IiI1i1i1 . set_dest_eid . instance_id = I1I11iii1I1
   if 40 - 40: OoO0O00 / I11i % iIii1I11I1II1 - ooOoO0o
  if ( ooooooO0 == "set-source-eid" ) :
   if ( IiI1i1i1 . set_source_eid == None ) :
    IiI1i1i1 . set_source_eid = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
    if 51 - 51: Oo0Ooo % iIii1I11I1II1 % oO0o + o0oOOo0O0Ooo
   IiI1i1i1 . set_source_eid . store_prefix ( Oo00OO0OO )
   if ( I1I11iii1I1 != None ) : IiI1i1i1 . set_source_eid . instance_id = I1I11iii1I1
   if 32 - 32: I1Ii111 * I1IiiI + Ii1I
  if ( ooooooO0 == "set-destination-eid" ) :
   if ( IiI1i1i1 . set_dest_eid == None ) :
    IiI1i1i1 . set_dest_eid = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
    if 30 - 30: OoooooooOO / I1IiiI . iIii1I11I1II1 / ooOoO0o
   IiI1i1i1 . set_dest_eid . store_prefix ( Oo00OO0OO )
   if ( I1I11iii1I1 != None ) : IiI1i1i1 . set_dest_eid . instance_id = I1I11iii1I1
   if 20 - 20: OoooooooOO * OOooOOo
  if ( ooooooO0 == "set-rloc-address" ) :
   IiI1i1i1 . set_rloc_address = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
   IiI1i1i1 . set_rloc_address . store_address ( Oo00OO0OO )
   if 77 - 77: Ii1I - OoooooooOO . OoOoOO00
  if ( ooooooO0 == "set-rloc-record-name" ) :
   IiI1i1i1 . set_rloc_record_name = Oo00OO0OO
   if 93 - 93: OoooooooOO / I1Ii111
  if ( ooooooO0 == "set-elp-name" ) :
   IiI1i1i1 . set_elp_name = Oo00OO0OO
   if 91 - 91: I1Ii111
  if ( ooooooO0 == "set-geo-name" ) :
   IiI1i1i1 . set_geo_name = Oo00OO0OO
   if 18 - 18: ooOoO0o * I11i
  if ( ooooooO0 == "set-rle-name" ) :
   IiI1i1i1 . set_rle_name = Oo00OO0OO
   if 53 - 53: I11i . i11iIiiIii - iIii1I11I1II1 / I1Ii111
  if ( ooooooO0 == "set-json-name" ) :
   IiI1i1i1 . set_json_name = Oo00OO0OO
   if 86 - 86: i1IIi % OoO0O00 - OoooooooOO
  if ( ooooooO0 == "policy-name" ) :
   IiI1i1i1 . policy_name = Oo00OO0OO
   if 63 - 63: o0oOOo0O0Ooo . iIii1I11I1II1 % IiII * i11iIiiIii
   if 70 - 70: iIii1I11I1II1
   if 12 - 12: OoOoOO00 / o0oOOo0O0Ooo - I1ii11iIi11i + oO0o + O0
   if 9 - 9: I1ii11iIi11i * OoooooooOO . O0 . ooOoO0o * i11iIiiIii / i1IIi
   if 38 - 38: OoOoOO00 . OoooooooOO % I1ii11iIi11i . oO0o % oO0o
   if 80 - 80: i11iIiiIii / OoOoOO00 . OOooOOo . iIii1I11I1II1
 IiI1i1i1 . match_clauses = IiI1I1I1i
 IiI1i1i1 . save_policy ( )
 return
 if 81 - 81: I1ii11iIi11i * OoO0O00 . o0oOOo0O0Ooo . OoooooooOO
 if 64 - 64: Oo0Ooo . I1ii11iIi11i / ooOoO0o % oO0o . iIii1I11I1II1
lisp_policy_commands = {
 "lisp policy" : [ lisp_policy_command , {
 "policy-name" : [ True ] ,
 "match" : [ ] ,
 "instance-id" : [ True , 0 , 0xffffffff ] ,
 "source-eid" : [ True ] ,
 "destination-eid" : [ True ] ,
 "source-rloc" : [ True ] ,
 "destination-rloc" : [ True ] ,
 "rloc-record-name" : [ True ] ,
 "elp-name" : [ True ] ,
 "geo-name" : [ True ] ,
 "rle-name" : [ True ] ,
 "json-name" : [ True ] ,
 "datetime-range" : [ True ] ,
 "set-action" : [ False , "process" , "drop" ] ,
 "set-record-ttl" : [ True , 0 , 0x7fffffff ] ,
 "set-instance-id" : [ True , 0 , 0xffffffff ] ,
 "set-source-eid" : [ True ] ,
 "set-destination-eid" : [ True ] ,
 "set-rloc-address" : [ True ] ,
 "set-rloc-record-name" : [ True ] ,
 "set-elp-name" : [ True ] ,
 "set-geo-name" : [ True ] ,
 "set-rle-name" : [ True ] ,
 "set-json-name" : [ True ] } ]
 }
if 84 - 84: II111iiii . oO0o * O0 / iII111i + OoooooooOO
if 99 - 99: I1ii11iIi11i . oO0o + Oo0Ooo + I1ii11iIi11i / I1Ii111 . I1ii11iIi11i
if 95 - 95: OoOoOO00 * iIii1I11I1II1 / OoooooooOO % i1IIi
if 91 - 91: OOooOOo - OoOoOO00
if 58 - 58: II111iiii . OOooOOo % II111iiii * oO0o % OoO0O00 % I11i
if 71 - 71: Ii1I * II111iiii * I1IiiI
if 22 - 22: oO0o
def lisp_send_to_arista ( command , interface ) :
 interface = "" if ( interface == None ) else "interface " + interface
 if 96 - 96: ooOoO0o * iII111i . IiII
 oO00OO00 = command
 if ( interface != "" ) : oO00OO00 = interface + ": " + oO00OO00
 lprint ( "Send CLI command '{}' to hardware" . format ( oO00OO00 ) )
 if 35 - 35: oO0o
 commands = '''
        enable
        configure
        {}
        {}
    ''' . format ( interface , command )
 if 8 - 8: IiII / o0oOOo0O0Ooo
 os . system ( "FastCli -c '{}'" . format ( commands ) )
 return
 if 75 - 75: I1IiiI + oO0o
 if 50 - 50: iIii1I11I1II1 / I1IiiI / O0 . I1IiiI
 if 35 - 35: I1Ii111
 if 80 - 80: I1Ii111 * I11i + O0 - OOooOOo . ooOoO0o - i11iIiiIii
 if 49 - 49: iIii1I11I1II1 + iIii1I11I1II1 - I1ii11iIi11i % o0oOOo0O0Ooo - i11iIiiIii
 if 52 - 52: I1Ii111 . o0oOOo0O0Ooo / iIii1I11I1II1 - I11i
 if 23 - 23: i11iIiiIii / OoooooooOO + I1ii11iIi11i + O0 + I1ii11iIi11i / i11iIiiIii
def lisp_arista_is_alive ( prefix ) :
 ooO0ooooO = "enable\nsh plat trident l3 software routes {}\n" . format ( prefix )
 oOOO = commands . getoutput ( "FastCli -c '{}'" . format ( ooO0ooooO ) )
 if 14 - 14: OoOoOO00 . II111iiii / iII111i / oO0o - oO0o
 if 12 - 12: O0
 if 77 - 77: oO0o % o0oOOo0O0Ooo % iII111i
 if 28 - 28: OoOoOO00 . O0 - II111iiii - I1IiiI / OOooOOo % O0
 oOOO = oOOO . split ( "\n" ) [ 1 ]
 i111IIIiii = oOOO . split ( " " )
 i111IIIiii = i111IIIiii [ - 1 ] . replace ( "\r" , "" )
 if 30 - 30: O0 / oO0o * i11iIiiIii + iIii1I11I1II1 + O0 % I1IiiI
 if 95 - 95: ooOoO0o % OOooOOo
 if 17 - 17: i1IIi + Ii1I
 if 35 - 35: iIii1I11I1II1 - Oo0Ooo - OoooooooOO % I1ii11iIi11i
 return ( i111IIIiii == "Y" )
 if 27 - 27: Oo0Ooo * II111iiii - OOooOOo + o0oOOo0O0Ooo
 if 26 - 26: oO0o / I1ii11iIi11i - oO0o
 if 9 - 9: ooOoO0o * iIii1I11I1II1 * OoooooooOO
 if 13 - 13: iII111i . i11iIiiIii * o0oOOo0O0Ooo . iII111i
 if 96 - 96: Ii1I
 if 90 - 90: II111iiii
 if 93 - 93: i11iIiiIii / Ii1I * Oo0Ooo . iII111i % iII111i / IiII
 if 15 - 15: OoOoOO00 % I1Ii111 - iIii1I11I1II1
 if 52 - 52: i11iIiiIii * ooOoO0o
 if 15 - 15: OoooooooOO . oO0o . i11iIiiIii / o0oOOo0O0Ooo
 if 91 - 91: ooOoO0o
 if 47 - 47: II111iiii + I11i + ooOoO0o % Oo0Ooo / iII111i
 if 9 - 9: O0 + IiII
 if 69 - 69: I1IiiI
 if 11 - 11: I11i % I1Ii111 + O0 . Ii1I . I1ii11iIi11i % I1Ii111
 if 28 - 28: IiII . o0oOOo0O0Ooo + iII111i - OoOoOO00 / OOooOOo
 if 86 - 86: ooOoO0o * OoOoOO00 + oO0o / II111iiii % OOooOOo
 if 89 - 89: O0 * Ii1I / OoO0O00 / OoOoOO00 % iII111i * iIii1I11I1II1
 if 72 - 72: iIii1I11I1II1 / iIii1I11I1II1 * I11i
 if 19 - 19: I1ii11iIi11i
 if 42 - 42: OoOoOO00 / IiII
 if 65 - 65: ooOoO0o - ooOoO0o * OoO0O00
 if 99 - 99: I11i % ooOoO0o . I1Ii111
 if 34 - 34: ooOoO0o + oO0o + II111iiii . I1Ii111 . i1IIi
 if 14 - 14: OoO0O00 . ooOoO0o - i1IIi * I1IiiI
 if 24 - 24: iIii1I11I1II1 / I1Ii111
 if 16 - 16: OoOoOO00 * I1Ii111 - I1IiiI / I1Ii111
 if 64 - 64: I1ii11iIi11i . i1IIi % II111iiii % Oo0Ooo + oO0o - I1IiiI
 if 24 - 24: IiII . II111iiii . II111iiii . OoOoOO00 . i11iIiiIii
 if 11 - 11: Ii1I
 if 82 - 82: I11i - i1IIi . Oo0Ooo * I1Ii111
 if 44 - 44: iII111i
 if 56 - 56: II111iiii / Oo0Ooo % IiII * II111iiii - iIii1I11I1II1 + ooOoO0o
 if 33 - 33: o0oOOo0O0Ooo . I11i / I1IiiI
 if 29 - 29: o0oOOo0O0Ooo - ooOoO0o
 if 59 - 59: I11i / IiII * OoO0O00 / IiII . I1Ii111
 if 82 - 82: OOooOOo . iIii1I11I1II1 + I1Ii111
 if 14 - 14: IiII . i11iIiiIii
 if 17 - 17: ooOoO0o % ooOoO0o * oO0o
 if 8 - 8: ooOoO0o + OoO0O00 . II111iiii / iIii1I11I1II1 - OOooOOo
 if 87 - 87: iIii1I11I1II1 . IiII % I1IiiI . OoO0O00 - I1Ii111
 if 53 - 53: I1Ii111 % i11iIiiIii
 if 99 - 99: I1IiiI - i1IIi * i11iIiiIii + OoO0O00
 if 80 - 80: o0oOOo0O0Ooo . I11i % iIii1I11I1II1 + OoOoOO00
def lisp_program_vxlan_hardware ( mc ) :
 if 87 - 87: I1Ii111 + II111iiii / I1ii11iIi11i + OoOoOO00
 if 71 - 71: I1IiiI + iIii1I11I1II1 + O0 * iII111i % IiII
 if 42 - 42: OOooOOo - I1ii11iIi11i
 if 93 - 93: I1Ii111 + OOooOOo % ooOoO0o / I1Ii111 % OOooOOo . IiII
 if 37 - 37: iII111i * oO0o / oO0o / Ii1I % I11i
 if 12 - 12: i11iIiiIii
 if ( os . path . exists ( "/persist/local/lispers.net" ) == False ) : return
 if 62 - 62: oO0o + OOooOOo + oO0o + I1IiiI
 if 10 - 10: IiII - Oo0Ooo % ooOoO0o
 if 38 - 38: oO0o * o0oOOo0O0Ooo . I11i % II111iiii / I11i % Ii1I
 if 19 - 19: II111iiii / i11iIiiIii * II111iiii + OoOoOO00 - OoOoOO00
 if ( len ( mc . best_rloc_set ) == 0 ) : return
 if 7 - 7: OoOoOO00 - OoO0O00 % OoOoOO00 . I1ii11iIi11i % Oo0Ooo * iII111i
 if 90 - 90: IiII - OOooOOo + iIii1I11I1II1
 if 88 - 88: ooOoO0o . o0oOOo0O0Ooo . OOooOOo - I11i
 if 76 - 76: IiII % I1IiiI . iII111i
 IiI1Iiii = mc . eid . print_prefix_no_iid ( )
 I1II = mc . best_rloc_set [ 0 ] . rloc . print_address_no_iid ( )
 if 5 - 5: ooOoO0o . oO0o - OoOoOO00 - OoooooooOO
 if 2 - 2: OOooOOo
 if 37 - 37: IiII - iIii1I11I1II1 * i11iIiiIii . ooOoO0o
 if 78 - 78: OOooOOo - I1ii11iIi11i + iII111i % OoOoOO00
 I1ii1iO0OOO = commands . getoutput ( "ip route get {} | egrep vlan4094" . format ( IiI1Iiii ) )
 if 69 - 69: IiII * iIii1I11I1II1
 if ( I1ii1iO0OOO != "" ) :
  lprint ( "Route {} already in hardware: '{}'" . format ( green ( IiI1Iiii , False ) , I1ii1iO0OOO ) )
  if 71 - 71: O0 * oO0o % I1Ii111
  return
  if 53 - 53: I11i - iIii1I11I1II1 - Ii1I / iII111i % I1Ii111
  if 59 - 59: OoooooooOO
  if 89 - 89: i1IIi / OoooooooOO . I1IiiI
  if 70 - 70: OOooOOo . I1Ii111
  if 20 - 20: i1IIi * IiII % II111iiii + IiII
  if 4 - 4: Ii1I + I1ii11iIi11i
  if 40 - 40: OOooOOo % iII111i
 IiiiI1I = commands . getoutput ( "ifconfig | egrep 'vxlan|vlan4094'" )
 if ( IiiiI1I . find ( "vxlan" ) == - 1 ) :
  lprint ( "No VXLAN interface found, cannot program hardware" )
  return
  if 51 - 51: OOooOOo . I1IiiI % OoO0O00 . I1IiiI
 if ( IiiiI1I . find ( "vlan4094" ) == - 1 ) :
  lprint ( "No vlan4094 interface found, cannot program hardware" )
  return
  if 88 - 88: O0 . iIii1I11I1II1 . iIii1I11I1II1 - ooOoO0o * iIii1I11I1II1 . Oo0Ooo
 i1I1i1II11I = commands . getoutput ( "ip addr | egrep vlan4094 | egrep inet" )
 if ( i1I1i1II11I == "" ) :
  lprint ( "No IP address found on vlan4094, cannot program hardware" )
  return
  if 70 - 70: i11iIiiIii - OoO0O00 / i11iIiiIii
 i1I1i1II11I = i1I1i1II11I . split ( "inet " ) [ 1 ]
 i1I1i1II11I = i1I1i1II11I . split ( "/" ) [ 0 ]
 if 46 - 46: II111iiii + O0 * OoooooooOO
 if 39 - 39: OoooooooOO % II111iiii . o0oOOo0O0Ooo
 if 29 - 29: I11i . o0oOOo0O0Ooo . i1IIi . o0oOOo0O0Ooo
 if 77 - 77: iIii1I11I1II1 + iIii1I11I1II1
 if 52 - 52: I1ii11iIi11i - IiII % I1IiiI % i1IIi
 if 98 - 98: I1Ii111 + II111iiii % OoO0O00 % iII111i
 if 54 - 54: II111iiii . ooOoO0o . iII111i - I1IiiI
 OOoo0oOo0 = [ ]
 OO00oOOO0o0oo = commands . getoutput ( "arp -i vlan4094" ) . split ( "\n" )
 for oOOo0ooO0 in OO00oOOO0o0oo :
  if ( oOOo0ooO0 . find ( "vlan4094" ) == - 1 ) : continue
  if ( oOOo0ooO0 . find ( "(incomplete)" ) == - 1 ) : continue
  o0OoiIiIIi = oOOo0ooO0 . split ( " " ) [ 0 ]
  OOoo0oOo0 . append ( o0OoiIiIIi )
  if 13 - 13: I1IiiI - Ii1I - iII111i - iIii1I11I1II1 . II111iiii
  if 40 - 40: I1ii11iIi11i * o0oOOo0O0Ooo + oO0o - OoOoOO00
 o0OoiIiIIi = None
 OoOo0 = i1I1i1II11I
 i1I1i1II11I = i1I1i1II11I . split ( "." )
 for iIi1I1 in range ( 1 , 255 ) :
  i1I1i1II11I [ 3 ] = str ( iIi1I1 )
  o0o00O0oOooO0 = "." . join ( i1I1i1II11I )
  if ( o0o00O0oOooO0 in OOoo0oOo0 ) : continue
  if ( o0o00O0oOooO0 == OoOo0 ) : continue
  o0OoiIiIIi = o0o00O0oOooO0
  break
  if 80 - 80: I1ii11iIi11i . OoooooooOO / ooOoO0o
 if ( o0OoiIiIIi == None ) :
  lprint ( "Address allocation failed for vlan4094, cannot program " + "hardware" )
  if 19 - 19: oO0o
  return
  if 97 - 97: IiII
  if 36 - 36: II111iiii
  if 83 - 83: I11i . ooOoO0o
  if 57 - 57: IiII
  if 34 - 34: I1ii11iIi11i + i11iIiiIii - I1ii11iIi11i / OoOoOO00 + i1IIi . i11iIiiIii
  if 48 - 48: I1ii11iIi11i % OoOoOO00 * OoOoOO00 % o0oOOo0O0Ooo * II111iiii / OoOoOO00
  if 73 - 73: OoOoOO00 + OOooOOo * II111iiii . OOooOOo % I1Ii111 % oO0o
 oO00O0oO0O = I1II . split ( "." )
 IiIiII1iI = lisp_hex_string ( oO00O0oO0O [ 1 ] ) . zfill ( 2 )
 O0o0O0O0O = lisp_hex_string ( oO00O0oO0O [ 2 ] ) . zfill ( 2 )
 iiI11I = lisp_hex_string ( oO00O0oO0O [ 3 ] ) . zfill ( 2 )
 i1III1iI = "00:00:00:{}:{}:{}" . format ( IiIiII1iI , O0o0O0O0O , iiI11I )
 IIiiiII = "0000.00{}.{}{}" . format ( IiIiII1iI , O0o0O0O0O , iiI11I )
 Oo0OoO00ooo0 = "arp -i vlan4094 -s {} {}" . format ( o0OoiIiIIi , i1III1iI )
 os . system ( Oo0OoO00ooo0 )
 if 50 - 50: iIii1I11I1II1 + iIii1I11I1II1
 if 46 - 46: II111iiii
 if 24 - 24: OOooOOo % OOooOOo * iII111i . Oo0Ooo * OOooOOo
 if 52 - 52: I11i
 IIIIII1IIi = ( "mac address-table static {} vlan 4094 " + "interface vxlan 1 vtep {}" ) . format ( IIiiiII , I1II )
 if 47 - 47: I1IiiI * O0 + I1ii11iIi11i - OOooOOo
 lisp_send_to_arista ( IIIIII1IIi , None )
 if 24 - 24: i1IIi / i1IIi + I11i * II111iiii / IiII
 if 8 - 8: I11i . I11i + I11i % OoooooooOO / ooOoO0o
 if 25 - 25: I1IiiI / OoO0O00
 if 92 - 92: oO0o % I1IiiI / OoO0O00 - I11i
 if 36 - 36: i1IIi * iIii1I11I1II1 + I1ii11iIi11i + iII111i - II111iiii
 IIIIiI = "ip route add {} via {}" . format ( IiI1Iiii , o0OoiIiIIi )
 os . system ( IIIIiI )
 if 98 - 98: i11iIiiIii . OoooooooOO
 lprint ( "Hardware programmed with commands:" )
 IIIIiI = IIIIiI . replace ( IiI1Iiii , green ( IiI1Iiii , False ) )
 lprint ( "  " + IIIIiI )
 lprint ( "  " + Oo0OoO00ooo0 )
 IIIIII1IIi = IIIIII1IIi . replace ( I1II , red ( I1II , False ) )
 lprint ( "  " + IIIIII1IIi )
 return
 if 37 - 37: OoooooooOO + O0 . I11i % OoOoOO00
 if 57 - 57: I1Ii111 . OOooOOo + I1Ii111 . iIii1I11I1II1 / oO0o / O0
 if 88 - 88: I1Ii111
 if 16 - 16: Oo0Ooo . ooOoO0o / OoO0O00 / o0oOOo0O0Ooo . OoooooooOO * OoO0O00
 if 50 - 50: II111iiii + I11i . OoooooooOO . I1Ii111 - OOooOOo
 if 83 - 83: oO0o
 if 100 - 100: I1Ii111 + o0oOOo0O0Ooo * oO0o / oO0o . oO0o + iII111i
def lisp_clear_hardware_walk ( mc , parms ) :
 I11i11IIIII = mc . eid . print_prefix_no_iid ( )
 os . system ( "ip route delete {}" . format ( I11i11IIIII ) )
 return ( [ True , None ] )
 if 71 - 71: II111iiii + iII111i + O0 % Oo0Ooo / I1IiiI
 if 52 - 52: Oo0Ooo . I1Ii111 * i1IIi / Oo0Ooo / OoO0O00
 if 29 - 29: iII111i
 if 91 - 91: Oo0Ooo - IiII
 if 47 - 47: iII111i / OOooOOo + iII111i
 if 69 - 69: I1IiiI . I1ii11iIi11i
 if 18 - 18: I11i * I1IiiI
 if 42 - 42: i1IIi . I1Ii111 - ooOoO0o + I11i / oO0o
def lisp_clear_map_cache ( ) :
 global lisp_map_cache , lisp_rloc_probe_list
 global lisp_crypto_keys_by_rloc_encap , lisp_crypto_keys_by_rloc_decap
 global lisp_rtr_list , lisp_gleaned_groups
 global lisp_no_map_request_rate_limit
 if 60 - 60: i1IIi + OoooooooOO % i11iIiiIii / IiII % Oo0Ooo + I1IiiI
 O00o000oO0 = bold ( "User cleared" , False )
 I1I1 = lisp_map_cache . cache_count
 lprint ( "{} map-cache with {} entries" . format ( O00o000oO0 , I1I1 ) )
 if 7 - 7: IiII - iIii1I11I1II1 . o0oOOo0O0Ooo . ooOoO0o % Ii1I
 if ( lisp_program_hardware ) :
  lisp_map_cache . walk_cache ( lisp_clear_hardware_walk , None )
  if 61 - 61: oO0o . OoOoOO00 - Oo0Ooo / IiII - Oo0Ooo
 lisp_map_cache = lisp_cache ( )
 if 71 - 71: I11i * I1ii11iIi11i * OOooOOo * o0oOOo0O0Ooo
 if 53 - 53: I1IiiI % I1IiiI
 if 80 - 80: OoO0O00 - i11iIiiIii / iII111i * I1ii11iIi11i / I1IiiI - I1Ii111
 if 85 - 85: IiII
 lisp_no_map_request_rate_limit = lisp_get_timestamp ( )
 if 72 - 72: iII111i * OoOoOO00
 if 65 - 65: iIii1I11I1II1 / iIii1I11I1II1 % O0 / II111iiii . OOooOOo . O0
 if 65 - 65: I11i
 if 35 - 35: o0oOOo0O0Ooo - i11iIiiIii
 if 78 - 78: ooOoO0o - II111iiii - i1IIi
 lisp_rloc_probe_list = { }
 if 18 - 18: OoooooooOO % OoOoOO00 - IiII / oO0o . OOooOOo . I1IiiI
 if 77 - 77: I1ii11iIi11i . OoO0O00 / OoOoOO00 / O0
 if 67 - 67: ooOoO0o % I11i % oO0o
 if 74 - 74: II111iiii
 lisp_crypto_keys_by_rloc_encap = { }
 lisp_crypto_keys_by_rloc_decap = { }
 if 44 - 44: Oo0Ooo + OoO0O00 + OoOoOO00 - I1IiiI
 if 68 - 68: i11iIiiIii / OOooOOo . i1IIi . i11iIiiIii . I11i
 if 56 - 56: iIii1I11I1II1 - II111iiii * i1IIi / Ii1I
 if 65 - 65: OOooOOo / I1IiiI . OoooooooOO + I1IiiI + OoooooooOO + i11iIiiIii
 if 20 - 20: I1IiiI + iII111i + O0 * O0
 lisp_rtr_list = { }
 if 18 - 18: I11i - I11i . OoOoOO00 . ooOoO0o
 if 31 - 31: ooOoO0o
 if 87 - 87: OoooooooOO + OOooOOo - I1ii11iIi11i / I1IiiI + ooOoO0o - Oo0Ooo
 if 19 - 19: ooOoO0o + I1ii11iIi11i - ooOoO0o
 lisp_gleaned_groups = { }
 if 17 - 17: I11i * i1IIi + iIii1I11I1II1 % I1IiiI
 if 44 - 44: IiII + I1IiiI . Ii1I % Oo0Ooo
 if 97 - 97: O0
 if 95 - 95: OoO0O00 % iII111i / I1IiiI * OoooooooOO
 lisp_process_data_plane_restart ( True )
 return
 if 31 - 31: iIii1I11I1II1
 if 62 - 62: o0oOOo0O0Ooo - iII111i / II111iiii . o0oOOo0O0Ooo
 if 20 - 20: iIii1I11I1II1 % OOooOOo
 if 91 - 91: ooOoO0o
 if 96 - 96: I1IiiI . OOooOOo
 if 94 - 94: OoooooooOO + II111iiii % ooOoO0o - II111iiii / O0
 if 34 - 34: IiII % oO0o
 if 54 - 54: I1IiiI
 if 80 - 80: OoOoOO00 . I1IiiI / I1ii11iIi11i . iII111i
 if 31 - 31: I11i * o0oOOo0O0Ooo
 if 17 - 17: Ii1I * iIii1I11I1II1
def lisp_encapsulate_rloc_probe ( lisp_sockets , rloc , nat_info , packet ) :
 if ( len ( lisp_sockets ) != 4 ) : return
 if 9 - 9: o0oOOo0O0Ooo - IiII
 ooO = lisp_myrlocs [ 0 ]
 if 72 - 72: Oo0Ooo % II111iiii + O0 * OoOoOO00 - OOooOOo + I1Ii111
 if 23 - 23: I1IiiI - O0 - iII111i . II111iiii / oO0o
 if 1 - 1: I11i . OOooOOo / oO0o % I11i * Oo0Ooo + Oo0Ooo
 if 23 - 23: Ii1I % i1IIi - I1Ii111
 if 95 - 95: OoOoOO00 - ooOoO0o . i1IIi . OoooooooOO
 oOOoO0O = len ( packet ) + 28
 ooooo0Oo0 = struct . pack ( "BBHIBBHII" , 0x45 , 0 , socket . htons ( oOOoO0O ) , 0 , 64 ,
 17 , 0 , socket . htonl ( ooO . address ) , socket . htonl ( rloc . address ) )
 ooooo0Oo0 = lisp_ip_checksum ( ooooo0Oo0 )
 if 38 - 38: I1IiiI + I1ii11iIi11i - Oo0Ooo . i11iIiiIii - i1IIi
 oOoO0OOO00O = struct . pack ( "HHHH" , 0 , socket . htons ( LISP_CTRL_PORT ) ,
 socket . htons ( oOOoO0O - 20 ) , 0 )
 if 11 - 11: IiII / I1IiiI . I1IiiI
 if 87 - 87: OoooooooOO * OoO0O00 * iIii1I11I1II1
 if 16 - 16: o0oOOo0O0Ooo * I11i + OoooooooOO + O0 / iIii1I11I1II1
 if 60 - 60: Ii1I % IiII * OoooooooOO * ooOoO0o * Ii1I
 packet = lisp_packet ( ooooo0Oo0 + oOoO0OOO00O + packet )
 if 8 - 8: I1Ii111 - o0oOOo0O0Ooo
 if 52 - 52: OoOoOO00 % O0 + I1ii11iIi11i . i11iIiiIii
 if 59 - 59: Ii1I - I1Ii111 . ooOoO0o - OoOoOO00 + oO0o . OoO0O00
 if 88 - 88: OOooOOo - ooOoO0o * o0oOOo0O0Ooo . OoooooooOO
 packet . inner_dest . copy_address ( rloc )
 packet . inner_dest . instance_id = 0xffffff
 packet . inner_source . copy_address ( ooO )
 packet . inner_ttl = 64
 packet . outer_dest . copy_address ( rloc )
 packet . outer_source . copy_address ( ooO )
 packet . outer_version = packet . outer_dest . afi_to_version ( )
 packet . outer_ttl = 64
 packet . encap_port = nat_info . port if nat_info else LISP_DATA_PORT
 if 3 - 3: I1Ii111
 O0ooo0Ooo = red ( rloc . print_address_no_iid ( ) , False )
 if ( nat_info ) :
  IIIi = " {}" . format ( blue ( nat_info . hostname , False ) )
  oO0oo000O = bold ( "RLOC-probe request" , False )
 else :
  IIIi = ""
  oO0oo000O = bold ( "RLOC-probe reply" , False )
  if 24 - 24: Ii1I + i11iIiiIii * I1Ii111 - OoOoOO00 / Ii1I - OoOoOO00
  if 69 - 69: I11i - I1IiiI . oO0o - OoooooooOO
 lprint ( ( "Data encapsulate {} to {}{} port {} for " + "NAT-traversal" ) . format ( oO0oo000O , O0ooo0Ooo , IIIi , packet . encap_port ) )
 if 33 - 33: o0oOOo0O0Ooo - o0oOOo0O0Ooo
 if 55 - 55: OoooooooOO / IiII + i1IIi
 if 54 - 54: ooOoO0o * Ii1I / Ii1I
 if 15 - 15: oO0o * I1Ii111
 if 11 - 11: Ii1I + o0oOOo0O0Ooo * OoooooooOO % iIii1I11I1II1
 if ( packet . encode ( None ) == None ) : return
 packet . print_packet ( "Send" , True )
 if 87 - 87: OoO0O00 + o0oOOo0O0Ooo
 iIIiIi = lisp_sockets [ 3 ]
 packet . send_packet ( iIIiIi , packet . outer_dest )
 del ( packet )
 return
 if 78 - 78: OOooOOo + OOooOOo - i11iIiiIii - O0
 if 75 - 75: o0oOOo0O0Ooo / OoooooooOO . I1ii11iIi11i * oO0o * I11i / OoooooooOO
 if 17 - 17: Ii1I % I1ii11iIi11i + I11i
 if 80 - 80: i1IIi . OoooooooOO % OoooooooOO . oO0o / OOooOOo
 if 85 - 85: OOooOOo
 if 80 - 80: ooOoO0o % O0 % I1ii11iIi11i + Oo0Ooo
 if 82 - 82: oO0o / iIii1I11I1II1 % ooOoO0o . Ii1I / i1IIi - I1Ii111
 if 15 - 15: I11i - OOooOOo . II111iiii . iIii1I11I1II1
def lisp_get_default_route_next_hops ( ) :
 if 93 - 93: I11i + o0oOOo0O0Ooo / OOooOOo + Ii1I % Oo0Ooo % I1ii11iIi11i
 if 72 - 72: IiII / II111iiii
 if 25 - 25: i1IIi + OoOoOO00 + oO0o + OoooooooOO
 if 21 - 21: I1ii11iIi11i
 if ( lisp_is_macos ( ) ) :
  ooO0ooooO = "route -n get default"
  oooO0 = commands . getoutput ( ooO0ooooO ) . split ( "\n" )
  Ii1III1 = II1i = None
  for I1ii1ii in oooO0 :
   if ( I1ii1ii . find ( "gateway: " ) != - 1 ) : Ii1III1 = I1ii1ii . split ( ": " ) [ 1 ]
   if ( I1ii1ii . find ( "interface: " ) != - 1 ) : II1i = I1ii1ii . split ( ": " ) [ 1 ]
   if 56 - 56: I1Ii111 % II111iiii
  return ( [ [ II1i , Ii1III1 ] ] )
  if 11 - 11: i11iIiiIii / OoO0O00 * OoO0O00 . I1Ii111 - OOooOOo
  if 12 - 12: OOooOOo . OoOoOO00 % ooOoO0o
  if 100 - 100: OoOoOO00 . iII111i
  if 50 - 50: iIii1I11I1II1 * OOooOOo . I1IiiI . OoOoOO00 - O0 + Oo0Ooo
  if 89 - 89: IiII - iII111i + IiII
 ooO0ooooO = "ip route | egrep 'default via'"
 i1I1iiii111 = commands . getoutput ( ooO0ooooO ) . split ( "\n" )
 if 39 - 39: oO0o % I11i . oO0o * I11i
 II1Oo0o00ooOooo = [ ]
 for I1ii1iO0OOO in i1I1iiii111 :
  if ( I1ii1iO0OOO . find ( " metric " ) != - 1 ) : continue
  I1I111iIiI = I1ii1iO0OOO . split ( " " )
  try :
   ii1Ii = I1I111iIiI . index ( "via" ) + 1
   if ( ii1Ii >= len ( I1I111iIiI ) ) : continue
   i111I = I1I111iIiI . index ( "dev" ) + 1
   if ( i111I >= len ( I1I111iIiI ) ) : continue
  except :
   continue
   if 96 - 96: I1Ii111
   if 31 - 31: II111iiii
  II1Oo0o00ooOooo . append ( [ I1I111iIiI [ i111I ] , I1I111iIiI [ ii1Ii ] ] )
  if 37 - 37: IiII * iII111i
 return ( II1Oo0o00ooOooo )
 if 49 - 49: Oo0Ooo % I1ii11iIi11i / I1Ii111
 if 16 - 16: I1ii11iIi11i + OoO0O00 + iIii1I11I1II1 + ooOoO0o - i1IIi + i11iIiiIii
 if 33 - 33: i1IIi * OoO0O00
 if 76 - 76: OoOoOO00 - Ii1I * i11iIiiIii + IiII - I1Ii111 % ooOoO0o
 if 43 - 43: Ii1I / I11i % I1ii11iIi11i / OoO0O00
 if 49 - 49: iII111i + iII111i % ooOoO0o * i11iIiiIii / Ii1I
 if 72 - 72: OOooOOo * Ii1I % OoO0O00
def lisp_get_host_route_next_hop ( rloc ) :
 ooO0ooooO = "ip route | egrep '{} via'" . format ( rloc )
 I1ii1iO0OOO = commands . getoutput ( ooO0ooooO ) . split ( " " )
 if 72 - 72: OoOoOO00 + o0oOOo0O0Ooo - i1IIi - OoO0O00 % OoOoOO00
 try : ooo = I1ii1iO0OOO . index ( "via" ) + 1
 except : return ( None )
 if 42 - 42: oO0o / i1IIi . IiII
 if ( ooo >= len ( I1ii1iO0OOO ) ) : return ( None )
 return ( I1ii1iO0OOO [ ooo ] )
 if 12 - 12: i11iIiiIii . ooOoO0o
 if 80 - 80: O0 / iIii1I11I1II1 % iII111i * ooOoO0o / i11iIiiIii . OoOoOO00
 if 88 - 88: OoooooooOO . I1IiiI
 if 6 - 6: I1Ii111 - i11iIiiIii - oO0o
 if 7 - 7: i1IIi
 if 6 - 6: OoooooooOO - Oo0Ooo - I1ii11iIi11i
 if 34 - 34: iII111i + i11iIiiIii . IiII
def lisp_install_host_route ( dest , nh , install ) :
 install = "add" if install else "delete"
 oO0O0oooo = "none" if nh == None else nh
 if 54 - 54: Oo0Ooo + I11i - iII111i * ooOoO0o % i11iIiiIii . IiII
 lprint ( "{} host-route {}, nh {}" . format ( install . title ( ) , dest , oO0O0oooo ) )
 if 29 - 29: II111iiii % i11iIiiIii % O0
 if ( nh == None ) :
  iiIIiI11I = "ip route {} {}/32" . format ( install , dest )
 else :
  iiIIiI11I = "ip route {} {}/32 via {}" . format ( install , dest , nh )
  if 38 - 38: o0oOOo0O0Ooo * IiII
 os . system ( iiIIiI11I )
 return
 if 51 - 51: OoooooooOO . Ii1I % OoooooooOO - I1IiiI + I1Ii111 % oO0o
 if 28 - 28: i11iIiiIii - I1IiiI * OoO0O00
 if 19 - 19: OoooooooOO
 if 34 - 34: OoOoOO00 . oO0o
 if 53 - 53: oO0o + OoooooooOO * ooOoO0o
 if 85 - 85: I1ii11iIi11i - o0oOOo0O0Ooo % o0oOOo0O0Ooo % iII111i * OoOoOO00
 if 50 - 50: I1Ii111 + I1Ii111 + I11i - OoOoOO00
 if 65 - 65: oO0o / I11i + iII111i - I1ii11iIi11i
def lisp_checkpoint ( checkpoint_list ) :
 if ( lisp_checkpoint_map_cache == False ) : return
 if 80 - 80: II111iiii . i11iIiiIii
 I1ii1ii = open ( lisp_checkpoint_filename , "w" )
 for i1ii1i1Ii11 in checkpoint_list :
  I1ii1ii . write ( i1ii1i1Ii11 + "\n" )
  if 66 - 66: ooOoO0o * iII111i * OOooOOo % OoO0O00 / I1ii11iIi11i
 I1ii1ii . close ( )
 lprint ( "{} {} entries to file '{}'" . format ( bold ( "Checkpoint" , False ) ,
 len ( checkpoint_list ) , lisp_checkpoint_filename ) )
 return
 if 33 - 33: iIii1I11I1II1
 if 52 - 52: iIii1I11I1II1 + O0
 if 84 - 84: OOooOOo / iII111i . I1IiiI / O0 % OOooOOo . iII111i
 if 32 - 32: OoO0O00 + OoO0O00 % o0oOOo0O0Ooo / O0
 if 29 - 29: iII111i % I1Ii111
 if 95 - 95: OOooOOo - ooOoO0o % i1IIi / O0 % I11i . IiII
 if 63 - 63: ooOoO0o
 if 22 - 22: OOooOOo . i11iIiiIii + II111iiii - Oo0Ooo % i1IIi / o0oOOo0O0Ooo
def lisp_load_checkpoint ( ) :
 if ( lisp_checkpoint_map_cache == False ) : return
 if ( os . path . exists ( lisp_checkpoint_filename ) == False ) : return
 if 90 - 90: IiII
 I1ii1ii = open ( lisp_checkpoint_filename , "r" )
 if 38 - 38: i1IIi / ooOoO0o / I11i * I1ii11iIi11i / II111iiii . iIii1I11I1II1
 I1I1 = 0
 for i1ii1i1Ii11 in I1ii1ii :
  I1I1 += 1
  iIIi1iI1I1IIi = i1ii1i1Ii11 . split ( " rloc " )
  ooOOo = [ ] if ( iIIi1iI1I1IIi [ 1 ] in [ "native-forward\n" , "\n" ] ) else iIIi1iI1I1IIi [ 1 ] . split ( ", " )
  if 52 - 52: I1ii11iIi11i % ooOoO0o * Ii1I * IiII + IiII / i11iIiiIii
  if 51 - 51: iIii1I11I1II1 * o0oOOo0O0Ooo % o0oOOo0O0Ooo . Ii1I / OoooooooOO
  OoO0oOOooOO = [ ]
  for I1II in ooOOo :
   oOO0O = lisp_rloc ( False )
   I1I111iIiI = I1II . split ( " " )
   oOO0O . rloc . store_address ( I1I111iIiI [ 0 ] )
   oOO0O . priority = int ( I1I111iIiI [ 1 ] )
   oOO0O . weight = int ( I1I111iIiI [ 2 ] )
   OoO0oOOooOO . append ( oOO0O )
   if 23 - 23: oO0o * I1IiiI - oO0o - ooOoO0o . IiII / i11iIiiIii
   if 53 - 53: Ii1I * Ii1I . OoOoOO00 . OOooOOo / I1ii11iIi11i % O0
  o0Oo0 = lisp_mapping ( "" , "" , OoO0oOOooOO )
  if ( o0Oo0 != None ) :
   o0Oo0 . eid . store_prefix ( iIIi1iI1I1IIi [ 0 ] )
   o0Oo0 . checkpoint_entry = True
   o0Oo0 . map_cache_ttl = LISP_NMR_TTL * 60
   if ( OoO0oOOooOO == [ ] ) : o0Oo0 . action = LISP_NATIVE_FORWARD_ACTION
   o0Oo0 . add_cache ( )
   continue
   if 98 - 98: OOooOOo
   if 11 - 11: OOooOOo * iIii1I11I1II1 % IiII - I1IiiI . I11i
  I1I1 -= 1
  if 29 - 29: OOooOOo % I11i - OOooOOo - OOooOOo * I11i . oO0o
  if 75 - 75: II111iiii . O0 . I1Ii111 * O0 / OoooooooOO
 I1ii1ii . close ( )
 lprint ( "{} {} map-cache entries from file '{}'" . format (
 bold ( "Loaded" , False ) , I1I1 , lisp_checkpoint_filename ) )
 return
 if 60 - 60: OOooOOo - Oo0Ooo * OOooOOo / OoO0O00
 if 55 - 55: I1ii11iIi11i * II111iiii * iIii1I11I1II1
 if 38 - 38: iIii1I11I1II1 % I1ii11iIi11i . Ii1I + I1IiiI % i11iIiiIii - i11iIiiIii
 if 62 - 62: I1Ii111 + I1IiiI
 if 9 - 9: iIii1I11I1II1 / iIii1I11I1II1
 if 24 - 24: OOooOOo . I1IiiI % i11iIiiIii
 if 43 - 43: OoooooooOO . o0oOOo0O0Ooo - I1ii11iIi11i + OoO0O00 . I1Ii111 . iII111i
 if 1 - 1: iII111i / OoO0O00 / OoOoOO00 * Oo0Ooo * OoooooooOO
 if 59 - 59: iII111i
 if 14 - 14: oO0o . IiII + iIii1I11I1II1 - i1IIi
 if 46 - 46: i11iIiiIii * II111iiii / i11iIiiIii % i11iIiiIii * II111iiii + i11iIiiIii
 if 87 - 87: Oo0Ooo + OoO0O00 / II111iiii * OoooooooOO
 if 95 - 95: I1Ii111 * o0oOOo0O0Ooo + OoO0O00 % OoOoOO00 - ooOoO0o / OoOoOO00
 if 45 - 45: OoooooooOO / oO0o / o0oOOo0O0Ooo + Ii1I + O0 . iII111i
def lisp_write_checkpoint_entry ( checkpoint_list , mc ) :
 if ( lisp_checkpoint_map_cache == False ) : return
 if 34 - 34: iIii1I11I1II1 . o0oOOo0O0Ooo + ooOoO0o
 i1ii1i1Ii11 = "{} rloc " . format ( mc . eid . print_prefix ( ) )
 if 96 - 96: O0 / ooOoO0o
 for oOO0O in mc . rloc_set :
  if ( oOO0O . rloc . is_null ( ) ) : continue
  i1ii1i1Ii11 += "{} {} {}, " . format ( oOO0O . rloc . print_address_no_iid ( ) ,
 oOO0O . priority , oOO0O . weight )
  if 82 - 82: OoO0O00 * OOooOOo * I11i * I1Ii111 % iIii1I11I1II1
  if 50 - 50: Ii1I * Ii1I % I11i / iIii1I11I1II1 / ooOoO0o / iII111i
 if ( mc . rloc_set != [ ] ) :
  i1ii1i1Ii11 = i1ii1i1Ii11 [ 0 : - 2 ]
 elif ( mc . action == LISP_NATIVE_FORWARD_ACTION ) :
  i1ii1i1Ii11 += "native-forward"
  if 91 - 91: Ii1I - O0 . I11i - OoooooooOO * IiII . II111iiii
  if 38 - 38: I1IiiI + OoO0O00
 checkpoint_list . append ( i1ii1i1Ii11 )
 return
 if 11 - 11: iIii1I11I1II1 + i1IIi * IiII - Oo0Ooo
 if 66 - 66: I1Ii111 . Ii1I / I1ii11iIi11i / iIii1I11I1II1 + O0 / i1IIi
 if 72 - 72: ooOoO0o . II111iiii
 if 32 - 32: I1Ii111 - oO0o + OoooooooOO . OoOoOO00 + i11iIiiIii / i1IIi
 if 26 - 26: I1IiiI + OoooooooOO % OoOoOO00 . IiII - II111iiii . OoOoOO00
 if 37 - 37: OoO0O00 % O0 + OoOoOO00 * I11i . Ii1I * OoO0O00
 if 18 - 18: o0oOOo0O0Ooo / OOooOOo
def lisp_check_dp_socket ( ) :
 IiI11OooO0ooo0 = lisp_ipc_dp_socket_name
 if ( os . path . exists ( IiI11OooO0ooo0 ) == False ) :
  OoOO0oOo00Oo = bold ( "does not exist" , False )
  lprint ( "Socket '{}' {}" . format ( IiI11OooO0ooo0 , OoOO0oOo00Oo ) )
  return ( False )
  if 10 - 10: iIii1I11I1II1
 return ( True )
 if 59 - 59: II111iiii + iII111i - iIii1I11I1II1 / iIii1I11I1II1 + Ii1I
 if 20 - 20: iIii1I11I1II1 + Oo0Ooo - Ii1I / i11iIiiIii . OoO0O00
 if 66 - 66: OoooooooOO - Ii1I / iII111i . I1IiiI + I1ii11iIi11i - I1Ii111
 if 36 - 36: I1Ii111 - OoO0O00 . I1ii11iIi11i * I1ii11iIi11i
 if 9 - 9: OOooOOo - oO0o - iIii1I11I1II1 * i11iIiiIii / I11i
 if 2 - 2: i1IIi % iII111i * ooOoO0o / OoOoOO00 + Oo0Ooo
 if 59 - 59: i11iIiiIii / I1IiiI * iII111i
def lisp_write_to_dp_socket ( entry ) :
 try :
  iiIi111IiIiI = json . dumps ( entry )
  OO000o0o0O00 = bold ( "Write IPC" , False )
  lprint ( "{} record to named socket: '{}'" . format ( OO000o0o0O00 , iiIi111IiIiI ) )
  lisp_ipc_dp_socket . sendto ( iiIi111IiIiI , lisp_ipc_dp_socket_name )
 except :
  lprint ( "Failed to write IPC record to named socket: '{}'" . format ( iiIi111IiIiI ) )
  if 60 - 60: Oo0Ooo / Oo0Ooo * Oo0Ooo + oO0o + I1ii11iIi11i / o0oOOo0O0Ooo
 return
 if 78 - 78: i11iIiiIii
 if 21 - 21: iII111i / ooOoO0o - i11iIiiIii % iII111i
 if 94 - 94: OoooooooOO / iII111i * ooOoO0o / i1IIi * i11iIiiIii * II111iiii
 if 98 - 98: Ii1I * Ii1I / IiII
 if 1 - 1: OOooOOo
 if 47 - 47: i11iIiiIii - I11i
 if 38 - 38: Oo0Ooo % OoooooooOO + iII111i
 if 31 - 31: OoO0O00 + I1Ii111 / iIii1I11I1II1
 if 11 - 11: ooOoO0o - OoOoOO00
def lisp_write_ipc_keys ( rloc ) :
 oo0o00OO = rloc . rloc . print_address_no_iid ( )
 Oo0o = rloc . translated_port
 if ( Oo0o != 0 ) : oo0o00OO += ":" + str ( Oo0o )
 if ( lisp_rloc_probe_list . has_key ( oo0o00OO ) == False ) : return
 if 19 - 19: O0 . OoOoOO00 - i1IIi . oO0o
 for I1I111iIiI , iIIi1iI1I1IIi , i11ii in lisp_rloc_probe_list [ oo0o00OO ] :
  o0Oo0 = lisp_map_cache . lookup_cache ( iIIi1iI1I1IIi , True )
  if ( o0Oo0 == None ) : continue
  lisp_write_ipc_map_cache ( True , o0Oo0 )
  if 96 - 96: o0oOOo0O0Ooo % o0oOOo0O0Ooo - OoO0O00 * iIii1I11I1II1 + ooOoO0o - ooOoO0o
 return
 if 4 - 4: OoO0O00 - OOooOOo
 if 21 - 21: I1Ii111 * i11iIiiIii
 if 63 - 63: oO0o + OoOoOO00
 if 50 - 50: o0oOOo0O0Ooo / Oo0Ooo * ooOoO0o * Ii1I
 if 97 - 97: I1IiiI / oO0o + I1Ii111 + I1Ii111
 if 86 - 86: o0oOOo0O0Ooo % ooOoO0o + OoOoOO00 * ooOoO0o
 if 20 - 20: Ii1I * iII111i / ooOoO0o
def lisp_write_ipc_map_cache ( add_or_delete , mc , dont_send = False ) :
 if ( lisp_i_am_etr ) : return
 if ( lisp_ipc_dp_socket == None ) : return
 if ( lisp_check_dp_socket ( ) == False ) : return
 if 18 - 18: Oo0Ooo * Ii1I / i11iIiiIii . OoO0O00 + OoooooooOO
 if 23 - 23: I1IiiI - I1ii11iIi11i . O0 . OoOoOO00 . OoO0O00
 if 81 - 81: IiII * I11i - iIii1I11I1II1
 if 41 - 41: oO0o * I11i + I1IiiI - OoO0O00
 OOOOO0o0OOo = "add" if add_or_delete else "delete"
 i1ii1i1Ii11 = { "type" : "map-cache" , "opcode" : OOOOO0o0OOo }
 if 63 - 63: Oo0Ooo * Ii1I - Ii1I
 o000OO0oO0O = ( mc . group . is_null ( ) == False )
 if ( o000OO0oO0O ) :
  i1ii1i1Ii11 [ "eid-prefix" ] = mc . group . print_prefix_no_iid ( )
  i1ii1i1Ii11 [ "rles" ] = [ ]
 else :
  i1ii1i1Ii11 [ "eid-prefix" ] = mc . eid . print_prefix_no_iid ( )
  i1ii1i1Ii11 [ "rlocs" ] = [ ]
  if 76 - 76: OoO0O00 . IiII % iIii1I11I1II1 / I1IiiI + iIii1I11I1II1 . I1IiiI
 i1ii1i1Ii11 [ "instance-id" ] = str ( mc . eid . instance_id )
 if 57 - 57: IiII - i1IIi * ooOoO0o
 if ( o000OO0oO0O ) :
  if ( len ( mc . rloc_set ) >= 1 and mc . rloc_set [ 0 ] . rle ) :
   for IiioOoo in mc . rloc_set [ 0 ] . rle . rle_forwarding_list :
    o0o00O0oOooO0 = IiioOoo . address . print_address_no_iid ( )
    Oo0o = str ( 4341 ) if IiioOoo . translated_port == 0 else str ( IiioOoo . translated_port )
    if 5 - 5: oO0o . O0 * IiII / Ii1I + OoO0O00
    I1I111iIiI = { "rle" : o0o00O0oOooO0 , "port" : Oo0o }
    II11iI11i1 , oOO0o00oOoOo = IiioOoo . get_encap_keys ( )
    I1I111iIiI = lisp_build_json_keys ( I1I111iIiI , II11iI11i1 , oOO0o00oOoOo , "encrypt-key" )
    i1ii1i1Ii11 [ "rles" ] . append ( I1I111iIiI )
    if 87 - 87: OOooOOo % iIii1I11I1II1 * I11i
    if 69 - 69: I11i + Ii1I + Oo0Ooo - IiII - OoO0O00
 else :
  for I1II in mc . rloc_set :
   if ( I1II . rloc . is_ipv4 ( ) == False and I1II . rloc . is_ipv6 ( ) == False ) :
    continue
    if 25 - 25: iIii1I11I1II1 % iIii1I11I1II1 / iII111i + iIii1I11I1II1
   if ( I1II . up_state ( ) == False ) : continue
   if 48 - 48: OoooooooOO + OoO0O00 % i11iIiiIii * OoooooooOO
   Oo0o = str ( 4341 ) if I1II . translated_port == 0 else str ( I1II . translated_port )
   if 64 - 64: I1ii11iIi11i . I1Ii111
   I1I111iIiI = { "rloc" : I1II . rloc . print_address_no_iid ( ) , "priority" :
 str ( I1II . priority ) , "weight" : str ( I1II . weight ) , "port" :
 Oo0o }
   II11iI11i1 , oOO0o00oOoOo = I1II . get_encap_keys ( )
   I1I111iIiI = lisp_build_json_keys ( I1I111iIiI , II11iI11i1 , oOO0o00oOoOo , "encrypt-key" )
   i1ii1i1Ii11 [ "rlocs" ] . append ( I1I111iIiI )
   if 81 - 81: IiII . ooOoO0o + O0 . ooOoO0o + iIii1I11I1II1
   if 68 - 68: i11iIiiIii . iII111i + OoooooooOO + II111iiii + iIii1I11I1II1 % I11i
   if 7 - 7: i1IIi - o0oOOo0O0Ooo - I1IiiI
 if ( dont_send == False ) : lisp_write_to_dp_socket ( i1ii1i1Ii11 )
 return ( i1ii1i1Ii11 )
 if 62 - 62: OoOoOO00 * oO0o - I1IiiI / Ii1I
 if 48 - 48: o0oOOo0O0Ooo % o0oOOo0O0Ooo - OoOoOO00
 if 13 - 13: OoO0O00 - Ii1I . ooOoO0o / O0 * OoOoOO00
 if 57 - 57: O0 + OoooooooOO % o0oOOo0O0Ooo / I1Ii111 / OOooOOo - OoOoOO00
 if 48 - 48: o0oOOo0O0Ooo - II111iiii + OoOoOO00
 if 54 - 54: II111iiii - OoO0O00 - o0oOOo0O0Ooo - O0 % I1Ii111
 if 9 - 9: i1IIi % iII111i / Ii1I
def lisp_write_ipc_decap_key ( rloc_addr , keys ) :
 if ( lisp_i_am_itr ) : return
 if ( lisp_ipc_dp_socket == None ) : return
 if ( lisp_check_dp_socket ( ) == False ) : return
 if 83 - 83: oO0o
 if 1 - 1: oO0o * iIii1I11I1II1 % iIii1I11I1II1 % iIii1I11I1II1 / oO0o + IiII
 if 29 - 29: OoooooooOO
 if 55 - 55: O0 - o0oOOo0O0Ooo % I1ii11iIi11i * I11i * oO0o
 if ( keys == None or len ( keys ) == 0 or keys [ 1 ] == None ) : return
 if 83 - 83: iIii1I11I1II1
 II11iI11i1 = keys [ 1 ] . encrypt_key
 oOO0o00oOoOo = keys [ 1 ] . icv_key
 if 92 - 92: OoO0O00 - iII111i
 if 97 - 97: ooOoO0o / I11i . IiII + I1Ii111 . iIii1I11I1II1
 if 24 - 24: ooOoO0o - oO0o % OoOoOO00 * Oo0Ooo
 if 54 - 54: Ii1I - OoooooooOO % I1IiiI + oO0o
 o0o0O0oOoO = rloc_addr . split ( ":" )
 if ( len ( o0o0O0oOoO ) == 1 ) :
  i1ii1i1Ii11 = { "type" : "decap-keys" , "rloc" : o0o0O0oOoO [ 0 ] }
 else :
  i1ii1i1Ii11 = { "type" : "decap-keys" , "rloc" : o0o0O0oOoO [ 0 ] , "port" : o0o0O0oOoO [ 1 ] }
  if 94 - 94: OoO0O00 * I1IiiI / O0 + I1Ii111 / i11iIiiIii
 i1ii1i1Ii11 = lisp_build_json_keys ( i1ii1i1Ii11 , II11iI11i1 , oOO0o00oOoOo , "decrypt-key" )
 if 34 - 34: Oo0Ooo . i1IIi
 lisp_write_to_dp_socket ( i1ii1i1Ii11 )
 return
 if 97 - 97: I11i
 if 89 - 89: iII111i % OoOoOO00 . Oo0Ooo
 if 20 - 20: oO0o % OoOoOO00
 if 93 - 93: I1ii11iIi11i - Ii1I % i1IIi / i1IIi
 if 82 - 82: OOooOOo
 if 27 - 27: I1Ii111 / IiII - i1IIi * Ii1I
 if 90 - 90: ooOoO0o
 if 100 - 100: iII111i * i1IIi . iII111i / O0 / OoO0O00 - oO0o
def lisp_build_json_keys ( entry , ekey , ikey , key_type ) :
 if ( ekey == None ) : return ( entry )
 if 65 - 65: OoOoOO00 + ooOoO0o * OoO0O00 % OoooooooOO + OoooooooOO * OoooooooOO
 entry [ "keys" ] = [ ]
 o0Oo = { "key-id" : "1" , key_type : ekey , "icv-key" : ikey }
 entry [ "keys" ] . append ( o0Oo )
 return ( entry )
 if 49 - 49: o0oOOo0O0Ooo + i1IIi / iII111i
 if 43 - 43: i1IIi . OoO0O00 + I1ii11iIi11i
 if 88 - 88: OoooooooOO / I11i % II111iiii % OOooOOo - I11i
 if 55 - 55: Oo0Ooo - OOooOOo - O0
 if 40 - 40: OoOoOO00 - OOooOOo
 if 3 - 3: IiII % I11i * I1Ii111 + iIii1I11I1II1 . oO0o
 if 35 - 35: II111iiii
def lisp_write_ipc_database_mappings ( ephem_port ) :
 if ( lisp_i_am_etr == False ) : return
 if ( lisp_ipc_dp_socket == None ) : return
 if ( lisp_check_dp_socket ( ) == False ) : return
 if 15 - 15: I11i * iIii1I11I1II1 + OOooOOo % IiII . o0oOOo0O0Ooo % Oo0Ooo
 if 96 - 96: O0
 if 15 - 15: i1IIi . iIii1I11I1II1
 if 3 - 3: II111iiii * i11iIiiIii * i1IIi - i1IIi
 i1ii1i1Ii11 = { "type" : "database-mappings" , "database-mappings" : [ ] }
 if 11 - 11: I1IiiI % Ii1I * i11iIiiIii % OOooOOo + II111iiii
 if 61 - 61: I1Ii111 + I11i + I1IiiI
 if 48 - 48: I11i
 if 67 - 67: o0oOOo0O0Ooo
 for ii1iii in lisp_db_list :
  if ( ii1iii . eid . is_ipv4 ( ) == False and ii1iii . eid . is_ipv6 ( ) == False ) : continue
  I1I1i11I = { "instance-id" : str ( ii1iii . eid . instance_id ) ,
 "eid-prefix" : ii1iii . eid . print_prefix_no_iid ( ) }
  i1ii1i1Ii11 [ "database-mappings" ] . append ( I1I1i11I )
  if 100 - 100: oO0o . II111iiii - i11iIiiIii
 lisp_write_to_dp_socket ( i1ii1i1Ii11 )
 if 56 - 56: OOooOOo . IiII - OOooOOo / i11iIiiIii * I1ii11iIi11i
 if 66 - 66: oO0o + ooOoO0o
 if 1 - 1: ooOoO0o
 if 61 - 61: o0oOOo0O0Ooo / OoooooooOO . I1ii11iIi11i + Oo0Ooo
 if 75 - 75: Ii1I
 i1ii1i1Ii11 = { "type" : "etr-nat-port" , "port" : ephem_port }
 lisp_write_to_dp_socket ( i1ii1i1Ii11 )
 return
 if 79 - 79: i1IIi . I1ii11iIi11i * o0oOOo0O0Ooo / I11i . I11i / ooOoO0o
 if 99 - 99: oO0o + I11i % i1IIi . iII111i
 if 58 - 58: Oo0Ooo % i11iIiiIii . Oo0Ooo / Oo0Ooo - I1IiiI . Ii1I
 if 65 - 65: OoO0O00
 if 16 - 16: IiII % I1IiiI % iIii1I11I1II1 . I1IiiI . I1ii11iIi11i - IiII
 if 6 - 6: I1Ii111 + OoO0O00 + O0 * OoOoOO00 . iIii1I11I1II1 . I1Ii111
 if 93 - 93: ooOoO0o % iIii1I11I1II1 + I1ii11iIi11i
def lisp_write_ipc_interfaces ( ) :
 if ( lisp_i_am_etr ) : return
 if ( lisp_ipc_dp_socket == None ) : return
 if ( lisp_check_dp_socket ( ) == False ) : return
 if 74 - 74: OoOoOO00 + I1ii11iIi11i
 if 82 - 82: II111iiii
 if 55 - 55: I11i . iIii1I11I1II1 / Ii1I - OoO0O00 * I1ii11iIi11i % iIii1I11I1II1
 if 48 - 48: ooOoO0o + Oo0Ooo / Oo0Ooo
 i1ii1i1Ii11 = { "type" : "interfaces" , "interfaces" : [ ] }
 if 15 - 15: iIii1I11I1II1 . I1Ii111 * OoooooooOO * O0 % OOooOOo
 for II1i in lisp_myinterfaces . values ( ) :
  if ( II1i . instance_id == None ) : continue
  I1I1i11I = { "interface" : II1i . device ,
 "instance-id" : str ( II1i . instance_id ) }
  i1ii1i1Ii11 [ "interfaces" ] . append ( I1I1i11I )
  if 53 - 53: Ii1I
  if 63 - 63: I11i % OoOoOO00
 lisp_write_to_dp_socket ( i1ii1i1Ii11 )
 return
 if 46 - 46: iIii1I11I1II1 . II111iiii / OoooooooOO - ooOoO0o * iII111i
 if 52 - 52: I11i + iII111i
 if 9 - 9: OoOoOO00 % II111iiii . I11i * Oo0Ooo
 if 53 - 53: II111iiii / i1IIi + OoooooooOO * O0
 if 62 - 62: IiII . O0
 if 87 - 87: I1ii11iIi11i / oO0o / IiII . OOooOOo
 if 91 - 91: OOooOOo % oO0o . OoOoOO00 . I1IiiI - OoOoOO00
 if 18 - 18: O0 - I1IiiI + i1IIi % i11iIiiIii
 if 97 - 97: iII111i * OoooooooOO + I1Ii111 + ooOoO0o - ooOoO0o
 if 63 - 63: o0oOOo0O0Ooo * OOooOOo + iIii1I11I1II1 + Oo0Ooo
 if 25 - 25: oO0o + IiII % o0oOOo0O0Ooo
 if 24 - 24: OoOoOO00
 if 87 - 87: I1ii11iIi11i / ooOoO0o * i1IIi
 if 71 - 71: OoOoOO00 - I11i
def lisp_parse_auth_key ( value ) :
 iIIiIIII11iii = value . split ( "[" )
 OOOOoOO = { }
 if ( len ( iIIiIIII11iii ) == 1 ) :
  OOOOoOO [ 0 ] = value
  return ( OOOOoOO )
  if 38 - 38: iII111i
  if 66 - 66: iII111i + Oo0Ooo + i1IIi * Oo0Ooo
 for OOOOOO0O00O00 in iIIiIIII11iii :
  if ( OOOOOO0O00O00 == "" ) : continue
  ooo = OOOOOO0O00O00 . find ( "]" )
  o00oO = OOOOOO0O00O00 [ 0 : ooo ]
  try : o00oO = int ( o00oO )
  except : return
  if 18 - 18: O0 - IiII
  OOOOoOO [ o00oO ] = OOOOOO0O00O00 [ ooo + 1 : : ]
  if 5 - 5: I1ii11iIi11i * iII111i + II111iiii * Oo0Ooo * O0 - I1IiiI
 return ( OOOOoOO )
 if 71 - 71: i11iIiiIii % I1IiiI + I1ii11iIi11i + II111iiii + OoooooooOO + oO0o
 if 12 - 12: I1IiiI + I1Ii111
 if 66 - 66: I1Ii111 + OOooOOo + I1Ii111 . OoooooooOO * oO0o / OoO0O00
 if 74 - 74: O0 % OOooOOo * OoOoOO00 / oO0o - Oo0Ooo
 if 79 - 79: Ii1I + IiII
 if 21 - 21: o0oOOo0O0Ooo * iII111i * o0oOOo0O0Ooo * o0oOOo0O0Ooo . Oo0Ooo
 if 98 - 98: I1ii11iIi11i
 if 58 - 58: IiII / i11iIiiIii % I11i
 if 74 - 74: OoooooooOO - I1ii11iIi11i + OOooOOo % IiII . o0oOOo0O0Ooo
 if 21 - 21: Ii1I
 if 72 - 72: I1Ii111 . OoooooooOO / I1Ii111 - Ii1I / I1ii11iIi11i * I1ii11iIi11i
 if 72 - 72: IiII . Ii1I + OoooooooOO * OoOoOO00 + Oo0Ooo . iII111i
 if 92 - 92: O0 * Ii1I - I1ii11iIi11i - IiII . OoO0O00 + I1IiiI
 if 59 - 59: i1IIi * OOooOOo % Oo0Ooo
 if 44 - 44: iIii1I11I1II1 . OOooOOo
 if 57 - 57: II111iiii + I1Ii111
def lisp_reassemble ( packet ) :
 Ooi1IIii1i = socket . ntohs ( struct . unpack ( "H" , packet [ 6 : 8 ] ) [ 0 ] )
 if 42 - 42: OoOoOO00 % O0
 if 70 - 70: iIii1I11I1II1 * Oo0Ooo - I1IiiI / OoO0O00 + OoOoOO00
 if 94 - 94: OoooooooOO + O0 * iIii1I11I1II1 * II111iiii
 if 90 - 90: I11i + O0 / I1IiiI . oO0o / O0
 if ( Ooi1IIii1i == 0 or Ooi1IIii1i == 0x4000 ) : return ( packet )
 if 46 - 46: O0 . O0 - oO0o . II111iiii * I1IiiI * Ii1I
 if 10 - 10: i1IIi + i1IIi . i1IIi - I1IiiI - I1IiiI
 if 26 - 26: Ii1I * I11i / I11i
 if 79 - 79: ooOoO0o / oO0o - oO0o / OoooooooOO
 iIiIi1i1Iiii = socket . ntohs ( struct . unpack ( "H" , packet [ 4 : 6 ] ) [ 0 ] )
 Ooo0oo0 = socket . ntohs ( struct . unpack ( "H" , packet [ 2 : 4 ] ) [ 0 ] )
 if 91 - 91: iIii1I11I1II1 - O0 * o0oOOo0O0Ooo * o0oOOo0O0Ooo . II111iiii
 OoOOooOoO = ( Ooi1IIii1i & 0x2000 == 0 and ( Ooi1IIii1i & 0x1fff ) != 0 )
 i1ii1i1Ii11 = [ ( Ooi1IIii1i & 0x1fff ) * 8 , Ooo0oo0 - 20 , packet , OoOOooOoO ]
 if 20 - 20: OoooooooOO - OoO0O00 * ooOoO0o * OoOoOO00 / OOooOOo
 if 64 - 64: O0 + iII111i / I11i * OoOoOO00 + o0oOOo0O0Ooo + I1Ii111
 if 16 - 16: I11i
 if 9 - 9: Ii1I / IiII * I11i - i11iIiiIii * I1ii11iIi11i / iII111i
 if 61 - 61: O0 % iII111i
 if 41 - 41: I1Ii111 * OoooooooOO
 if 76 - 76: OoooooooOO * II111iiii . II111iiii / o0oOOo0O0Ooo - iII111i
 if 49 - 49: O0 . I1ii11iIi11i . OoOoOO00 . I1Ii111 % O0 . iIii1I11I1II1
 if ( Ooi1IIii1i == 0x2000 ) :
  oo0O , O0o0o0ooO0ooo = struct . unpack ( "HH" , packet [ 20 : 24 ] )
  oo0O = socket . ntohs ( oo0O )
  O0o0o0ooO0ooo = socket . ntohs ( O0o0o0ooO0ooo )
  if ( O0o0o0ooO0ooo not in [ 4341 , 8472 , 4789 ] and oo0O != 4341 ) :
   lisp_reassembly_queue [ iIiIi1i1Iiii ] = [ ]
   i1ii1i1Ii11 [ 2 ] = None
   if 19 - 19: iIii1I11I1II1
   if 97 - 97: Ii1I . I11i / ooOoO0o + Oo0Ooo
   if 100 - 100: iII111i / I1Ii111 % OoOoOO00 . O0 / OoOoOO00
   if 81 - 81: OoO0O00 % i11iIiiIii / OoO0O00 + ooOoO0o
   if 100 - 100: O0 . Oo0Ooo % Oo0Ooo % O0 / i11iIiiIii
   if 56 - 56: IiII - OOooOOo - OoOoOO00 - I11i
 if ( lisp_reassembly_queue . has_key ( iIiIi1i1Iiii ) == False ) :
  lisp_reassembly_queue [ iIiIi1i1Iiii ] = [ ]
  if 57 - 57: i1IIi
  if 41 - 41: I11i / Ii1I
  if 1 - 1: II111iiii / iII111i
  if 83 - 83: OoO0O00 / iII111i
  if 59 - 59: I1Ii111 % OOooOOo . I1IiiI + I1ii11iIi11i % oO0o
 oOoOOOO = lisp_reassembly_queue [ iIiIi1i1Iiii ]
 if 27 - 27: OoOoOO00 . I11i - Ii1I
 if 82 - 82: I1IiiI + OoOoOO00 . II111iiii / OoOoOO00 % OoOoOO00 . I1ii11iIi11i
 if 19 - 19: iIii1I11I1II1 . iIii1I11I1II1 + OOooOOo - I1ii11iIi11i
 if 59 - 59: i11iIiiIii / oO0o * IiII . o0oOOo0O0Ooo % Ii1I
 if 95 - 95: OoooooooOO - I1IiiI * I1ii11iIi11i
 if ( len ( oOoOOOO ) == 1 and oOoOOOO [ 0 ] [ 2 ] == None ) :
  dprint ( "Drop non-LISP encapsulated fragment 0x{}" . format ( lisp_hex_string ( iIiIi1i1Iiii ) . zfill ( 4 ) ) )
  if 52 - 52: oO0o % iII111i - I1IiiI - o0oOOo0O0Ooo
  return ( None )
  if 66 - 66: o0oOOo0O0Ooo - Oo0Ooo - OoooooooOO * o0oOOo0O0Ooo + I1Ii111
  if 82 - 82: I11i * i1IIi / Ii1I + O0
  if 85 - 85: O0 + oO0o / I1Ii111
  if 65 - 65: o0oOOo0O0Ooo . Oo0Ooo . i1IIi / IiII . I11i . O0
  if 69 - 69: Oo0Ooo - i11iIiiIii
 oOoOOOO . append ( i1ii1i1Ii11 )
 oOoOOOO = sorted ( oOoOOOO )
 if 87 - 87: Oo0Ooo % OOooOOo - Ii1I
 if 34 - 34: iII111i / Ii1I / I1IiiI * i11iIiiIii
 if 41 - 41: Ii1I / Oo0Ooo . OoO0O00 . iIii1I11I1II1 % IiII . I11i
 if 59 - 59: O0 + II111iiii + IiII % Oo0Ooo
 o0o00O0oOooO0 = lisp_address ( LISP_AFI_IPV4 , "" , 32 , 0 )
 o0o00O0oOooO0 . address = socket . ntohl ( struct . unpack ( "I" , packet [ 12 : 16 ] ) [ 0 ] )
 o0O0OOOoo = o0o00O0oOooO0 . print_address_no_iid ( )
 o0o00O0oOooO0 . address = socket . ntohl ( struct . unpack ( "I" , packet [ 16 : 20 ] ) [ 0 ] )
 I11I111iII11i = o0o00O0oOooO0 . print_address_no_iid ( )
 o0o00O0oOooO0 = red ( "{} -> {}" . format ( o0O0OOOoo , I11I111iII11i ) , False )
 if 82 - 82: I1ii11iIi11i * I1Ii111 . O0
 dprint ( "{}{} fragment, RLOCs: {}, packet 0x{}, frag-offset: 0x{}" . format ( bold ( "Received" , False ) , " non-LISP encapsulated" if i1ii1i1Ii11 [ 2 ] == None else "" , o0o00O0oOooO0 , lisp_hex_string ( iIiIi1i1Iiii ) . zfill ( 4 ) ,
 # iII111i . i11iIiiIii
 # iII111i
 lisp_hex_string ( Ooi1IIii1i ) . zfill ( 4 ) ) )
 if 75 - 75: I1IiiI * IiII % OoO0O00 - ooOoO0o * iII111i
 if 32 - 32: iII111i
 if 59 - 59: OoOoOO00 - I1Ii111
 if 34 - 34: ooOoO0o . OoooooooOO / ooOoO0o + OoooooooOO
 if 24 - 24: OoooooooOO * I1ii11iIi11i / O0 / Oo0Ooo * I1IiiI / ooOoO0o
 if ( oOoOOOO [ 0 ] [ 0 ] != 0 or oOoOOOO [ - 1 ] [ 3 ] == False ) : return ( None )
 iiiI111i1Ii = oOoOOOO [ 0 ]
 for o0o00OoOo0 in oOoOOOO [ 1 : : ] :
  Ooi1IIii1i = o0o00OoOo0 [ 0 ]
  ii1I1Ii , IiO00 = iiiI111i1Ii [ 0 ] , iiiI111i1Ii [ 1 ]
  if ( ii1I1Ii + IiO00 != Ooi1IIii1i ) : return ( None )
  iiiI111i1Ii = o0o00OoOo0
  if 62 - 62: Oo0Ooo * I1IiiI % Ii1I
 lisp_reassembly_queue . pop ( iIiIi1i1Iiii )
 if 37 - 37: iII111i - OoOoOO00 + oO0o / OoooooooOO
 if 18 - 18: II111iiii . o0oOOo0O0Ooo
 if 34 - 34: ooOoO0o
 if 9 - 9: o0oOOo0O0Ooo
 if 52 - 52: IiII . oO0o + i11iIiiIii % IiII
 packet = oOoOOOO [ 0 ] [ 2 ]
 for o0o00OoOo0 in oOoOOOO [ 1 : : ] : packet += o0o00OoOo0 [ 2 ] [ 20 : : ]
 if 45 - 45: i1IIi - I1IiiI / IiII - I1IiiI
 dprint ( "{} fragments arrived for packet 0x{}, length {}" . format ( bold ( "All" , False ) , lisp_hex_string ( iIiIi1i1Iiii ) . zfill ( 4 ) , len ( packet ) ) )
 if 21 - 21: IiII
 if 43 - 43: IiII
 if 9 - 9: OOooOOo * ooOoO0o + ooOoO0o . I1Ii111
 if 8 - 8: IiII * iIii1I11I1II1
 if 7 - 7: I1Ii111 / OoooooooOO % O0 - I1ii11iIi11i
 oOOoO0O = socket . htons ( len ( packet ) )
 O00O0OO = packet [ 0 : 2 ] + struct . pack ( "H" , oOOoO0O ) + packet [ 4 : 6 ] + struct . pack ( "H" , 0 ) + packet [ 8 : 10 ] + struct . pack ( "H" , 0 ) + packet [ 12 : 20 ]
 if 49 - 49: OoooooooOO . I1ii11iIi11i / OoooooooOO * oO0o
 if 81 - 81: I1ii11iIi11i . ooOoO0o + I1ii11iIi11i
 O00O0OO = lisp_ip_checksum ( O00O0OO )
 return ( O00O0OO + packet [ 20 : : ] )
 if 84 - 84: OoooooooOO
 if 95 - 95: o0oOOo0O0Ooo
 if 22 - 22: ooOoO0o / o0oOOo0O0Ooo - OoooooooOO / Oo0Ooo - I1Ii111 / OOooOOo
 if 41 - 41: oO0o . II111iiii
 if 47 - 47: I1ii11iIi11i
 if 5 - 5: Oo0Ooo
 if 23 - 23: i11iIiiIii / I11i + i1IIi % I1Ii111
 if 100 - 100: Oo0Ooo
def lisp_get_crypto_decap_lookup_key ( addr , port ) :
 oo0o00OO = addr . print_address_no_iid ( ) + ":" + str ( port )
 if ( lisp_crypto_keys_by_rloc_decap . has_key ( oo0o00OO ) ) : return ( oo0o00OO )
 if 13 - 13: I1IiiI + ooOoO0o * II111iiii
 oo0o00OO = addr . print_address_no_iid ( )
 if ( lisp_crypto_keys_by_rloc_decap . has_key ( oo0o00OO ) ) : return ( oo0o00OO )
 if 32 - 32: iIii1I11I1II1 + O0 + i1IIi
 if 28 - 28: IiII + I11i
 if 1 - 1: OoooooooOO - i11iIiiIii . OoooooooOO - o0oOOo0O0Ooo - OOooOOo * I1Ii111
 if 56 - 56: Ii1I . OoO0O00
 if 43 - 43: iII111i * iII111i
 for Iiiii1I1 in lisp_crypto_keys_by_rloc_decap :
  oO0OO = Iiiii1I1 . split ( ":" )
  if ( len ( oO0OO ) == 1 ) : continue
  oO0OO = oO0OO [ 0 ] if len ( oO0OO ) == 2 else ":" . join ( oO0OO [ 0 : - 1 ] )
  if ( oO0OO == oo0o00OO ) :
   iIi11III = lisp_crypto_keys_by_rloc_decap [ Iiiii1I1 ]
   lisp_crypto_keys_by_rloc_decap [ oo0o00OO ] = iIi11III
   return ( oo0o00OO )
   if 35 - 35: IiII / Oo0Ooo . Ii1I % OoO0O00 / i11iIiiIii % I11i
   if 96 - 96: O0 % I1Ii111 * II111iiii - iII111i / IiII . I11i
 return ( None )
 if 8 - 8: I1ii11iIi11i / i11iIiiIii
 if 98 - 98: OoooooooOO
 if 13 - 13: II111iiii / Ii1I - iII111i
 if 67 - 67: I1IiiI + OOooOOo * oO0o
 if 41 - 41: OoooooooOO * I1IiiI
 if 3 - 3: IiII
 if 96 - 96: I11i - OOooOOo + I11i
 if 71 - 71: Oo0Ooo
 if 48 - 48: o0oOOo0O0Ooo / II111iiii / OoOoOO00 * o0oOOo0O0Ooo + I1IiiI . OoOoOO00
 if 52 - 52: Ii1I / OoOoOO00 . OOooOOo * IiII . OoooooooOO
 if 6 - 6: i1IIi . oO0o % IiII . Oo0Ooo % I11i
def lisp_build_crypto_decap_lookup_key ( addr , port ) :
 addr = addr . print_address_no_iid ( )
 Oo00oO = addr + ":" + str ( port )
 if 1 - 1: i1IIi * I1ii11iIi11i
 if ( lisp_i_am_rtr ) :
  if ( lisp_rloc_probe_list . has_key ( addr ) ) : return ( addr )
  if 92 - 92: I1ii11iIi11i + I11i - I11i - IiII . I11i
  if 34 - 34: iIii1I11I1II1 - oO0o * i11iIiiIii * o0oOOo0O0Ooo
  if 15 - 15: I1Ii111
  if 25 - 25: I1ii11iIi11i * O0
  if 8 - 8: i11iIiiIii
  if 95 - 95: ooOoO0o + i1IIi / OOooOOo . i11iIiiIii
  for i1II1iiI in lisp_nat_state_info . values ( ) :
   for i1iII1Iiii1ii in i1II1iiI :
    if ( addr == i1iII1Iiii1ii . address ) : return ( Oo00oO )
    if 31 - 31: iII111i - iII111i - oO0o
    if 62 - 62: Oo0Ooo % Oo0Ooo / OoooooooOO * o0oOOo0O0Ooo . Ii1I
  return ( addr )
  if 1 - 1: I1ii11iIi11i / II111iiii / II111iiii + o0oOOo0O0Ooo + OoooooooOO
 return ( Oo00oO )
 if 34 - 34: i11iIiiIii + iIii1I11I1II1 - i11iIiiIii * o0oOOo0O0Ooo - iII111i
 if 87 - 87: OOooOOo * OoO0O00
 if 61 - 61: iII111i - II111iiii . I1Ii111 % II111iiii / I11i
 if 86 - 86: II111iiii
 if 94 - 94: o0oOOo0O0Ooo % Ii1I * Ii1I % Oo0Ooo / I1ii11iIi11i
 if 40 - 40: Oo0Ooo . II111iiii / II111iiii - i1IIi
 if 91 - 91: Ii1I
def lisp_set_ttl ( lisp_socket , ttl ) :
 try :
  lisp_socket . setsockopt ( socket . SOL_IP , socket . IP_TTL , ttl )
  lisp_socket . setsockopt ( socket . SOL_IP , socket . IP_MULTICAST_TTL , ttl )
 except :
  lprint ( "socket.setsockopt(IP_TTL) not supported" )
  pass
  if 45 - 45: I1ii11iIi11i + Oo0Ooo
 return
 if 72 - 72: I1ii11iIi11i
 if 5 - 5: i1IIi
 if 31 - 31: iII111i - OoooooooOO + oO0o / OoooooooOO + I1ii11iIi11i
 if 93 - 93: o0oOOo0O0Ooo * I1ii11iIi11i % I1IiiI * ooOoO0o
 if 37 - 37: OoO0O00 * OoooooooOO / oO0o * I11i * I1ii11iIi11i
 if 42 - 42: OoooooooOO - ooOoO0o . OOooOOo + OoOoOO00
 if 53 - 53: o0oOOo0O0Ooo
def lisp_is_rloc_probe_request ( lisp_type ) :
 lisp_type = struct . unpack ( "B" , lisp_type ) [ 0 ]
 return ( lisp_type == 0x12 )
 if 55 - 55: ooOoO0o . i1IIi - ooOoO0o + O0 + I1IiiI
 if 31 - 31: OoO0O00 % I1Ii111
 if 62 - 62: oO0o / O0 - I1Ii111 . IiII
 if 81 - 81: i11iIiiIii
 if 57 - 57: O0
 if 85 - 85: i11iIiiIii - i11iIiiIii - OoOoOO00 / II111iiii - II111iiii
 if 4 - 4: I1ii11iIi11i * O0 / OoO0O00 * II111iiii . iIii1I11I1II1 / OOooOOo
def lisp_is_rloc_probe_reply ( lisp_type ) :
 lisp_type = struct . unpack ( "B" , lisp_type ) [ 0 ]
 return ( lisp_type == 0x28 )
 if 97 - 97: i1IIi - OoOoOO00 . OoooooooOO
 if 24 - 24: iIii1I11I1II1 + OOooOOo * iII111i % IiII % OOooOOo
 if 64 - 64: IiII . I1ii11iIi11i - o0oOOo0O0Ooo - ooOoO0o + OoooooooOO
 if 95 - 95: iII111i . I1ii11iIi11i + ooOoO0o + o0oOOo0O0Ooo % OoO0O00
 if 50 - 50: iII111i * O0 % II111iiii
 if 80 - 80: OOooOOo - II111iiii - OoO0O00
 if 62 - 62: Ii1I . i11iIiiIii % OOooOOo
 if 44 - 44: i1IIi * I1ii11iIi11i % Ii1I . Ii1I * I11i + II111iiii
 if 15 - 15: i1IIi - I11i - I1Ii111 / OoO0O00 + Oo0Ooo + I1IiiI
 if 81 - 81: IiII
 if 54 - 54: I1IiiI % OoO0O00 % OoOoOO00
 if 12 - 12: II111iiii . O0 * i11iIiiIii . I11i
 if 98 - 98: II111iiii + i1IIi * oO0o % I1IiiI
 if 53 - 53: i11iIiiIii . I1ii11iIi11i - OOooOOo - OOooOOo
 if 97 - 97: I1IiiI % iII111i % OoooooooOO / ooOoO0o / i11iIiiIii
 if 7 - 7: O0 % IiII / o0oOOo0O0Ooo
 if 79 - 79: IiII + I1Ii111
 if 59 - 59: iII111i - oO0o . ooOoO0o / IiII * i11iIiiIii
 if 61 - 61: I11i - Oo0Ooo * II111iiii + iIii1I11I1II1
def lisp_is_rloc_probe ( packet , rr ) :
 oOoO0OOO00O = ( struct . unpack ( "B" , packet [ 9 ] ) [ 0 ] == 17 )
 if ( oOoO0OOO00O == False ) : return ( [ packet , None , None , None ] )
 if 37 - 37: OoooooooOO % II111iiii / o0oOOo0O0Ooo . OOooOOo * I1ii11iIi11i . iIii1I11I1II1
 oo0O = struct . unpack ( "H" , packet [ 20 : 22 ] ) [ 0 ]
 O0o0o0ooO0ooo = struct . unpack ( "H" , packet [ 22 : 24 ] ) [ 0 ]
 oOooOOo = ( socket . htons ( LISP_CTRL_PORT ) in [ oo0O , O0o0o0ooO0ooo ] )
 if ( oOooOOo == False ) : return ( [ packet , None , None , None ] )
 if 88 - 88: Oo0Ooo / ooOoO0o + II111iiii + OoooooooOO * iIii1I11I1II1
 if ( rr == 0 ) :
  oO0oo000O = lisp_is_rloc_probe_request ( packet [ 28 ] )
  if ( oO0oo000O == False ) : return ( [ packet , None , None , None ] )
 elif ( rr == 1 ) :
  oO0oo000O = lisp_is_rloc_probe_reply ( packet [ 28 ] )
  if ( oO0oo000O == False ) : return ( [ packet , None , None , None ] )
 elif ( rr == - 1 ) :
  oO0oo000O = lisp_is_rloc_probe_request ( packet [ 28 ] )
  if ( oO0oo000O == False ) :
   oO0oo000O = lisp_is_rloc_probe_reply ( packet [ 28 ] )
   if ( oO0oo000O == False ) : return ( [ packet , None , None , None ] )
   if 82 - 82: i1IIi - I11i % ooOoO0o . OoOoOO00 * o0oOOo0O0Ooo
   if 20 - 20: i11iIiiIii - O0 / i11iIiiIii
   if 51 - 51: iII111i . ooOoO0o
   if 70 - 70: I11i / O0 - I11i + o0oOOo0O0Ooo . ooOoO0o . o0oOOo0O0Ooo
   if 6 - 6: I11i + II111iiii - I1Ii111
   if 45 - 45: i1IIi / iII111i + i11iIiiIii * I11i + ooOoO0o / OoooooooOO
 iI1Iii1i1 = lisp_address ( LISP_AFI_IPV4 , "" , 32 , 0 )
 iI1Iii1i1 . address = socket . ntohl ( struct . unpack ( "I" , packet [ 12 : 16 ] ) [ 0 ] )
 if 56 - 56: I11i + I1Ii111
 if 80 - 80: II111iiii . Ii1I + o0oOOo0O0Ooo / II111iiii / OoO0O00 + iIii1I11I1II1
 if 29 - 29: o0oOOo0O0Ooo + OoOoOO00 + ooOoO0o - I1ii11iIi11i
 if 64 - 64: O0 / OoooooooOO
 if ( iI1Iii1i1 . is_local ( ) ) : return ( [ None , None , None , None ] )
 if 28 - 28: I1ii11iIi11i + oO0o . Oo0Ooo % iIii1I11I1II1 / I1Ii111
 if 8 - 8: O0 . I1IiiI * o0oOOo0O0Ooo + I1IiiI
 if 44 - 44: i1IIi % iII111i . i11iIiiIii / I11i + OoooooooOO
 if 21 - 21: OoOoOO00 . OoO0O00 . OoOoOO00 + OoOoOO00
 iI1Iii1i1 = iI1Iii1i1 . print_address_no_iid ( )
 Oo0o = socket . ntohs ( struct . unpack ( "H" , packet [ 20 : 22 ] ) [ 0 ] )
 Oo0o0 = struct . unpack ( "B" , packet [ 8 ] ) [ 0 ] - 1
 packet = packet [ 28 : : ]
 if 30 - 30: I1IiiI - iII111i - OOooOOo + oO0o
 I1I111iIiI = bold ( "Receive(pcap)" , False )
 I1ii1ii = bold ( "from " + iI1Iii1i1 , False )
 IiI1i1i1 = lisp_format_packet ( packet )
 lprint ( "{} {} bytes {} {}, packet: {}" . format ( I1I111iIiI , len ( packet ) , I1ii1ii , Oo0o , IiI1i1i1 ) )
 if 51 - 51: Ii1I % O0 / II111iiii . Oo0Ooo
 return ( [ packet , iI1Iii1i1 , Oo0o , Oo0o0 ] )
 if 90 - 90: i11iIiiIii * II111iiii % iIii1I11I1II1 . I1ii11iIi11i / Oo0Ooo . OOooOOo
 if 77 - 77: OoO0O00
 if 95 - 95: II111iiii
 if 59 - 59: iIii1I11I1II1 % OOooOOo / OoOoOO00 * I1Ii111 * OoooooooOO * O0
 if 43 - 43: OoO0O00 * I1IiiI * OOooOOo * O0 - O0 / o0oOOo0O0Ooo
 if 77 - 77: I11i % I1Ii111 . IiII % OoooooooOO * o0oOOo0O0Ooo
 if 87 - 87: iII111i + IiII / ooOoO0o * ooOoO0o * OOooOOo
 if 97 - 97: I1Ii111
 if 47 - 47: iII111i / I1ii11iIi11i - Ii1I . II111iiii
 if 56 - 56: O0 - i1IIi % o0oOOo0O0Ooo + IiII
 if 42 - 42: o0oOOo0O0Ooo . OOooOOo % I11i - OoOoOO00
def lisp_ipc_write_xtr_parameters ( cp , dp ) :
 if ( lisp_ipc_dp_socket == None ) : return
 if 38 - 38: OoooooooOO
 oOOO0oo0 = { "type" : "xtr-parameters" , "control-plane-logging" : cp ,
 "data-plane-logging" : dp , "rtr" : lisp_i_am_rtr }
 if 27 - 27: O0 + I1ii11iIi11i % Ii1I . i1IIi + OoO0O00 + OoOoOO00
 lisp_write_to_dp_socket ( oOOO0oo0 )
 return
 if 22 - 22: II111iiii / I1IiiI + o0oOOo0O0Ooo * I1IiiI . OoooooooOO * OOooOOo
 if 49 - 49: I1ii11iIi11i * I1IiiI + OOooOOo + i11iIiiIii * I1ii11iIi11i . o0oOOo0O0Ooo
 if 36 - 36: o0oOOo0O0Ooo - i11iIiiIii
 if 37 - 37: O0 + IiII + I1IiiI
 if 50 - 50: OoooooooOO . I1Ii111
 if 100 - 100: ooOoO0o * ooOoO0o - Ii1I
 if 13 - 13: iII111i . I11i * OoO0O00 . i1IIi . iIii1I11I1II1 - o0oOOo0O0Ooo
 if 68 - 68: Ii1I % o0oOOo0O0Ooo / OoooooooOO + Ii1I - Ii1I
def lisp_external_data_plane ( ) :
 ooO0ooooO = 'egrep "ipc-data-plane = yes" ./lisp.config'
 if ( commands . getoutput ( ooO0ooooO ) != "" ) : return ( True )
 if 79 - 79: II111iiii / IiII
 if ( os . getenv ( "LISP_RUN_LISP_XTR" ) != None ) : return ( True )
 return ( False )
 if 4 - 4: O0 - i11iIiiIii % ooOoO0o * O0 - ooOoO0o
 if 96 - 96: oO0o % II111iiii . Ii1I % OoO0O00 . iIii1I11I1II1 / IiII
 if 96 - 96: o0oOOo0O0Ooo / O0 . iIii1I11I1II1 . Ii1I % OOooOOo % II111iiii
 if 5 - 5: OoooooooOO / I1Ii111 % I1Ii111 / I1IiiI
 if 19 - 19: I1IiiI - ooOoO0o % IiII - o0oOOo0O0Ooo * OOooOOo + I1ii11iIi11i
 if 44 - 44: i1IIi
 if 85 - 85: I1ii11iIi11i / IiII + oO0o
 if 95 - 95: IiII . OoO0O00
 if 36 - 36: IiII % Ii1I - OoOoOO00 + OoO0O00 + IiII * Ii1I
 if 15 - 15: I1IiiI / O0 % I1ii11iIi11i % OoOoOO00 . OoOoOO00 + iII111i
 if 79 - 79: OOooOOo + Ii1I . I1Ii111 / Oo0Ooo / i11iIiiIii / O0
 if 28 - 28: i1IIi % OoO0O00 / i1IIi - o0oOOo0O0Ooo
 if 97 - 97: II111iiii + O0 . Ii1I + OoooooooOO
 if 39 - 39: i11iIiiIii + OoO0O00 + I11i * oO0o + iIii1I11I1II1 % o0oOOo0O0Ooo
def lisp_process_data_plane_restart ( do_clear = False ) :
 os . system ( "touch ./lisp.config" )
 if 25 - 25: OoooooooOO
 OO0oiI1ii1i1i1I = { "type" : "entire-map-cache" , "entries" : [ ] }
 if 86 - 86: I11i * IiII . ooOoO0o
 if ( do_clear == False ) :
  iIII1I = OO0oiI1ii1i1i1I [ "entries" ]
  lisp_map_cache . walk_cache ( lisp_ipc_walk_map_cache , iIII1I )
  if 21 - 21: i1IIi
  if 11 - 11: Oo0Ooo % o0oOOo0O0Ooo % Oo0Ooo + Oo0Ooo + iIii1I11I1II1 / OOooOOo
 lisp_write_to_dp_socket ( OO0oiI1ii1i1i1I )
 return
 if 64 - 64: OoOoOO00
 if 37 - 37: ooOoO0o - oO0o - i1IIi
 if 55 - 55: IiII % IiII * i1IIi . II111iiii + II111iiii
 if 33 - 33: OoO0O00 % OoooooooOO * ooOoO0o * O0 % IiII % O0
 if 76 - 76: I1ii11iIi11i - OOooOOo + o0oOOo0O0Ooo % Ii1I * Oo0Ooo + Ii1I
 if 1 - 1: Oo0Ooo * I1Ii111
 if 95 - 95: iIii1I11I1II1 - O0 - IiII * OoO0O00
 if 9 - 9: Ii1I
 if 58 - 58: OoooooooOO + OoO0O00 . I1IiiI % OoOoOO00 / Ii1I
 if 32 - 32: IiII
 if 52 - 52: O0
 if 60 - 60: OoooooooOO % OoooooooOO . II111iiii / iIii1I11I1II1
 if 82 - 82: o0oOOo0O0Ooo / ooOoO0o . I1IiiI + ooOoO0o
 if 71 - 71: oO0o + ooOoO0o
def lisp_process_data_plane_stats ( msg , lisp_sockets , lisp_port ) :
 if ( msg . has_key ( "entries" ) == False ) :
  lprint ( "No 'entries' in stats IPC message" )
  return
  if 87 - 87: ooOoO0o % oO0o
 if ( type ( msg [ "entries" ] ) != list ) :
  lprint ( "'entries' in stats IPC message must be an array" )
  return
  if 45 - 45: oO0o
  if 95 - 95: iII111i * iIii1I11I1II1 . i1IIi
 for msg in msg [ "entries" ] :
  if ( msg . has_key ( "eid-prefix" ) == False ) :
   lprint ( "No 'eid-prefix' in stats IPC message" )
   continue
   if 43 - 43: oO0o * ooOoO0o - I11i
  Ii1i1 = msg [ "eid-prefix" ]
  if 70 - 70: oO0o / Ii1I
  if ( msg . has_key ( "instance-id" ) == False ) :
   lprint ( "No 'instance-id' in stats IPC message" )
   continue
   if 15 - 15: iIii1I11I1II1 % ooOoO0o % i11iIiiIii
  IiIIi11i111 = int ( msg [ "instance-id" ] )
  if 16 - 16: iII111i
  if 50 - 50: iIii1I11I1II1 - II111iiii % i1IIi
  if 48 - 48: O0
  if 60 - 60: ooOoO0o - IiII % i1IIi
  iiI1I1IIi = lisp_address ( LISP_AFI_NONE , "" , 0 , IiIIi11i111 )
  iiI1I1IIi . store_prefix ( Ii1i1 )
  o0Oo0 = lisp_map_cache_lookup ( None , iiI1I1IIi )
  if ( o0Oo0 == None ) :
   lprint ( "Map-cache entry for {} not found for stats update" . format ( Ii1i1 ) )
   if 5 - 5: oO0o
   continue
   if 29 - 29: i1IIi . OoOoOO00 . i1IIi + oO0o . I1Ii111 + O0
   if 62 - 62: I1ii11iIi11i . IiII + OoO0O00 - OoOoOO00 * O0 + I1Ii111
  if ( msg . has_key ( "rlocs" ) == False ) :
   lprint ( "No 'rlocs' in stats IPC message for {}" . format ( Ii1i1 ) )
   if 58 - 58: oO0o . OoO0O00 / ooOoO0o
   continue
   if 61 - 61: I11i + I1Ii111
  if ( type ( msg [ "rlocs" ] ) != list ) :
   lprint ( "'rlocs' in stats IPC message must be an array" )
   continue
   if 27 - 27: ooOoO0o / i1IIi . oO0o - OoooooooOO
  I1i1Ii1iII = msg [ "rlocs" ]
  if 98 - 98: iIii1I11I1II1 / iII111i % OoOoOO00 + IiII * OoOoOO00
  if 40 - 40: i11iIiiIii % IiII * ooOoO0o % Oo0Ooo * I1Ii111 % I1ii11iIi11i
  if 64 - 64: I1ii11iIi11i / O0 % II111iiii * I1Ii111
  if 76 - 76: I1ii11iIi11i + o0oOOo0O0Ooo
  for Ooo0O00 in I1i1Ii1iII :
   if ( Ooo0O00 . has_key ( "rloc" ) == False ) : continue
   if 96 - 96: Ii1I * i11iIiiIii - OOooOOo - O0 * OoooooooOO - ooOoO0o
   O0ooo0Ooo = Ooo0O00 [ "rloc" ]
   if ( O0ooo0Ooo == "no-address" ) : continue
   if 35 - 35: iII111i . i11iIiiIii - OOooOOo % Oo0Ooo + Ii1I . iIii1I11I1II1
   I1II = lisp_address ( LISP_AFI_NONE , "" , 0 , 0 )
   I1II . store_address ( O0ooo0Ooo )
   if 91 - 91: o0oOOo0O0Ooo / OoO0O00 + I1IiiI % i11iIiiIii % i1IIi
   oOO0O = o0Oo0 . get_rloc ( I1II )
   if ( oOO0O == None ) : continue
   if 22 - 22: I1Ii111 * O0 % OoO0O00 * I1ii11iIi11i
   if 47 - 47: OoO0O00 / OOooOOo / OoOoOO00 % i11iIiiIii / OoOoOO00
   if 52 - 52: ooOoO0o / I11i % i11iIiiIii - I1Ii111 % ooOoO0o - o0oOOo0O0Ooo
   if 67 - 67: OoOoOO00 / I1Ii111 + i11iIiiIii - IiII
   o0O0O0OoO = 0 if Ooo0O00 . has_key ( "packet-count" ) == False else Ooo0O00 [ "packet-count" ]
   if 92 - 92: O0
   o0O00o0OOoo0 = 0 if Ooo0O00 . has_key ( "byte-count" ) == False else Ooo0O00 [ "byte-count" ]
   if 52 - 52: iII111i - i11iIiiIii + o0oOOo0O0Ooo + i1IIi
   i1 = 0 if Ooo0O00 . has_key ( "seconds-last-packet" ) == False else Ooo0O00 [ "seconds-last-packet" ]
   if 58 - 58: OOooOOo - Ii1I * I1Ii111 - O0 . oO0o
   if 72 - 72: i1IIi * iII111i * Ii1I / o0oOOo0O0Ooo . I1Ii111 + i11iIiiIii
   oOO0O . stats . packet_count += o0O0O0OoO
   oOO0O . stats . byte_count += o0O00o0OOoo0
   oOO0O . stats . last_increment = lisp_get_timestamp ( ) - i1
   if 33 - 33: I11i / OoO0O00 * ooOoO0o + iIii1I11I1II1
   lprint ( "Update stats {}/{}/{}s for {} RLOC {}" . format ( o0O0O0OoO , o0O00o0OOoo0 ,
 i1 , Ii1i1 , O0ooo0Ooo ) )
   if 54 - 54: Oo0Ooo / IiII + i11iIiiIii . O0
   if 94 - 94: OoooooooOO + iII111i * OoooooooOO / o0oOOo0O0Ooo
   if 12 - 12: iIii1I11I1II1 / iIii1I11I1II1 / II111iiii
   if 93 - 93: oO0o
   if 53 - 53: OoO0O00 * i1IIi / Oo0Ooo / OoO0O00 * ooOoO0o
  if ( o0Oo0 . group . is_null ( ) and o0Oo0 . has_ttl_elapsed ( ) ) :
   Ii1i1 = green ( o0Oo0 . print_eid_tuple ( ) , False )
   lprint ( "Refresh map-cache entry {}" . format ( Ii1i1 ) )
   lisp_send_map_request ( lisp_sockets , lisp_port , None , o0Oo0 . eid , None )
   if 77 - 77: iIii1I11I1II1 % I1IiiI + o0oOOo0O0Ooo + I1Ii111 * Oo0Ooo * i1IIi
   if 14 - 14: iIii1I11I1II1 * iIii1I11I1II1 - OOooOOo . iII111i / ooOoO0o
 return
 if 54 - 54: OoOoOO00 - I1IiiI - iII111i
 if 49 - 49: i11iIiiIii * Oo0Ooo
 if 100 - 100: Oo0Ooo * oO0o
 if 85 - 85: OoooooooOO . IiII / IiII . ooOoO0o . IiII % II111iiii
 if 65 - 65: oO0o - OoO0O00 / iII111i + ooOoO0o
 if 80 - 80: o0oOOo0O0Ooo + II111iiii * Ii1I % OoOoOO00 % I1IiiI + I1ii11iIi11i
 if 46 - 46: Oo0Ooo / Oo0Ooo % iII111i % I1IiiI
 if 85 - 85: OoO0O00 - Ii1I / O0
 if 45 - 45: IiII + I1Ii111 / I11i
 if 84 - 84: iII111i % II111iiii
 if 86 - 86: IiII % II111iiii / i1IIi * I1ii11iIi11i - O0 * OOooOOo
 if 53 - 53: OOooOOo * oO0o + i1IIi % Oo0Ooo + II111iiii
 if 34 - 34: oO0o % iII111i / IiII . IiII + i11iIiiIii
 if 68 - 68: O0 % oO0o * IiII % O0
 if 55 - 55: O0 % I1IiiI % O0
 if 27 - 27: I1IiiI + I1ii11iIi11i * I1Ii111 % Ii1I - Oo0Ooo
 if 87 - 87: i11iIiiIii % OOooOOo - OoOoOO00 * ooOoO0o / Oo0Ooo
 if 74 - 74: OoooooooOO * ooOoO0o - I11i / I1ii11iIi11i % iIii1I11I1II1
 if 94 - 94: Ii1I * I1Ii111 + OoOoOO00 . iIii1I11I1II1
 if 44 - 44: Oo0Ooo . Oo0Ooo * Oo0Ooo
 if 23 - 23: I1Ii111 / iII111i . O0 % II111iiii
 if 67 - 67: I11i / iIii1I11I1II1 / ooOoO0o
 if 90 - 90: II111iiii % I1Ii111 - IiII . Oo0Ooo % OOooOOo - OoOoOO00
def lisp_process_data_plane_decap_stats ( msg , lisp_ipc_socket ) :
 if 89 - 89: Oo0Ooo - I1ii11iIi11i . I1Ii111
 if 65 - 65: ooOoO0o % OOooOOo + OOooOOo % I1Ii111 . I1IiiI % O0
 if 46 - 46: OoO0O00 * I1Ii111 + iII111i . oO0o % OOooOOo / i11iIiiIii
 if 1 - 1: I1ii11iIi11i % O0 - I1ii11iIi11i / OoooooooOO / OoO0O00
 if 82 - 82: i1IIi % Ii1I
 if ( lisp_i_am_itr ) :
  lprint ( "Send decap-stats IPC message to lisp-etr process" )
  oOOO0oo0 = "stats%{}" . format ( json . dumps ( msg ) )
  oOOO0oo0 = lisp_command_ipc ( oOOO0oo0 , "lisp-itr" )
  lisp_ipc ( oOOO0oo0 , lisp_ipc_socket , "lisp-etr" )
  return
  if 85 - 85: I1Ii111 * i11iIiiIii * iIii1I11I1II1 % iIii1I11I1II1
  if 64 - 64: OoO0O00 / Ii1I
  if 79 - 79: Ii1I % OOooOOo
  if 39 - 39: I1ii11iIi11i / Ii1I - II111iiii . i1IIi
  if 59 - 59: II111iiii
  if 36 - 36: ooOoO0o . II111iiii - OoOoOO00 % I1ii11iIi11i * O0
  if 91 - 91: iII111i + Oo0Ooo / OoooooooOO * iIii1I11I1II1 - OoO0O00
  if 73 - 73: iIii1I11I1II1 % I1Ii111 % II111iiii * Oo0Ooo * OoO0O00
 oOOO0oo0 = bold ( "IPC" , False )
 lprint ( "Process decap-stats {} message: '{}'" . format ( oOOO0oo0 , msg ) )
 if 48 - 48: OOooOOo * i11iIiiIii - i11iIiiIii + iIii1I11I1II1 + I1IiiI % OoooooooOO
 if ( lisp_i_am_etr ) : msg = json . loads ( msg )
 if 61 - 61: i1IIi
 Oo00 = [ "good-packets" , "ICV-error" , "checksum-error" ,
 "lisp-header-error" , "no-decrypt-key" , "bad-inner-version" ,
 "outer-header-error" ]
 if 98 - 98: I11i * OoO0O00 / I1ii11iIi11i * Ii1I - o0oOOo0O0Ooo - I11i
 for Ii1I1Ii1 in Oo00 :
  o0O0O0OoO = 0 if msg . has_key ( Ii1I1Ii1 ) == False else msg [ Ii1I1Ii1 ] [ "packet-count" ]
  if 17 - 17: II111iiii
  lisp_decap_stats [ Ii1I1Ii1 ] . packet_count += o0O0O0OoO
  if 37 - 37: I1ii11iIi11i % i11iIiiIii
  o0O00o0OOoo0 = 0 if msg . has_key ( Ii1I1Ii1 ) == False else msg [ Ii1I1Ii1 ] [ "byte-count" ]
  if 16 - 16: II111iiii . iII111i
  lisp_decap_stats [ Ii1I1Ii1 ] . byte_count += o0O00o0OOoo0
  if 67 - 67: ooOoO0o * Ii1I - I11i
  i1 = 0 if msg . has_key ( Ii1I1Ii1 ) == False else msg [ Ii1I1Ii1 ] [ "seconds-last-packet" ]
  if 45 - 45: i1IIi % iII111i / OoO0O00 * OoO0O00
  lisp_decap_stats [ Ii1I1Ii1 ] . last_increment = lisp_get_timestamp ( ) - i1
  if 6 - 6: OOooOOo % i1IIi * o0oOOo0O0Ooo / OoO0O00 / o0oOOo0O0Ooo - Oo0Ooo
 return
 if 70 - 70: O0 - OoO0O00 + II111iiii
 if 97 - 97: I1Ii111 % IiII
 if 34 - 34: II111iiii . oO0o * Oo0Ooo - O0 + I1Ii111
 if 99 - 99: OoO0O00 * o0oOOo0O0Ooo + OoOoOO00 * iIii1I11I1II1
 if 38 - 38: I1ii11iIi11i - OOooOOo * O0 - I1ii11iIi11i
 if 95 - 95: OoO0O00 . oO0o . OoooooooOO - iIii1I11I1II1
 if 35 - 35: o0oOOo0O0Ooo / OoooooooOO - i1IIi * iIii1I11I1II1 + ooOoO0o
 if 66 - 66: Oo0Ooo - OoOoOO00 . I1Ii111 + O0 + o0oOOo0O0Ooo
 if 36 - 36: II111iiii % IiII . i11iIiiIii
 if 88 - 88: Oo0Ooo . IiII * Oo0Ooo
 if 92 - 92: I1IiiI % IiII
 if 95 - 95: OoooooooOO / OoO0O00 % O0 / I1Ii111 * Ii1I + I1ii11iIi11i
 if 7 - 7: ooOoO0o
 if 83 - 83: oO0o / I1Ii111 + I1Ii111 * I1ii11iIi11i
 if 8 - 8: I11i . I1ii11iIi11i % i1IIi + Ii1I
 if 63 - 63: I1IiiI / OoooooooOO
 if 16 - 16: OoOoOO00
def lisp_process_punt ( punt_socket , lisp_send_sockets , lisp_ephem_port ) :
 oo0II1I11ii1iI , iI1Iii1i1 = punt_socket . recvfrom ( 4000 )
 if 90 - 90: oO0o * Oo0Ooo * oO0o . Ii1I * i1IIi
 iii1iI1I1i11 = json . loads ( oo0II1I11ii1iI )
 if ( type ( iii1iI1I1i11 ) != dict ) :
  lprint ( "Invalid punt message from {}, not in JSON format" . format ( iI1Iii1i1 ) )
  if 47 - 47: OOooOOo
  return
  if 38 - 38: I11i
 IIi1I = bold ( "Punt" , False )
 lprint ( "{} message from '{}': '{}'" . format ( IIi1I , iI1Iii1i1 , iii1iI1I1i11 ) )
 if 41 - 41: o0oOOo0O0Ooo . OoO0O00 / OoO0O00
 if ( iii1iI1I1i11 . has_key ( "type" ) == False ) :
  lprint ( "Punt IPC message has no 'type' key" )
  return
  if 80 - 80: O0
  if 3 - 3: o0oOOo0O0Ooo . I1ii11iIi11i - I11i / OoOoOO00 % I1ii11iIi11i
  if 17 - 17: i11iIiiIii * oO0o . Oo0Ooo / OoooooooOO
  if 58 - 58: OoO0O00 * OoO0O00 % I1Ii111
  if 83 - 83: Ii1I
 if ( iii1iI1I1i11 [ "type" ] == "statistics" ) :
  lisp_process_data_plane_stats ( iii1iI1I1i11 , lisp_send_sockets , lisp_ephem_port )
  return
  if 85 - 85: ooOoO0o * I1IiiI * IiII % O0
 if ( iii1iI1I1i11 [ "type" ] == "decap-statistics" ) :
  lisp_process_data_plane_decap_stats ( iii1iI1I1i11 , punt_socket )
  return
  if 12 - 12: Oo0Ooo + iII111i - I1IiiI / OoOoOO00 * O0 - OOooOOo
  if 32 - 32: O0
  if 2 - 2: Oo0Ooo / I11i / Oo0Ooo + OoO0O00 * i11iIiiIii
  if 56 - 56: II111iiii - I11i
  if 83 - 83: I11i - i1IIi - iII111i . ooOoO0o * OoOoOO00
 if ( iii1iI1I1i11 [ "type" ] == "restart" ) :
  lisp_process_data_plane_restart ( )
  return
  if 71 - 71: I11i + IiII * II111iiii + OoooooooOO . iII111i
  if 65 - 65: i11iIiiIii * ooOoO0o * I1ii11iIi11i
  if 15 - 15: OoO0O00
  if 75 - 75: IiII - OOooOOo + OOooOOo / Oo0Ooo - iII111i + O0
  if 1 - 1: o0oOOo0O0Ooo . II111iiii % OoooooooOO - oO0o - I1Ii111 * o0oOOo0O0Ooo
 if ( iii1iI1I1i11 [ "type" ] != "discovery" ) :
  lprint ( "Punt IPC message has wrong format" )
  return
  if 70 - 70: o0oOOo0O0Ooo * I1IiiI * OoOoOO00 / I11i * O0 / IiII
 if ( iii1iI1I1i11 . has_key ( "interface" ) == False ) :
  lprint ( "Invalid punt message from {}, required keys missing" . format ( iI1Iii1i1 ) )
  if 99 - 99: II111iiii
  return
  if 34 - 34: OOooOOo + OoOoOO00 * o0oOOo0O0Ooo + I1ii11iIi11i + IiII * i1IIi
  if 73 - 73: I1ii11iIi11i - IiII - O0 . oO0o + Oo0Ooo % iII111i
  if 68 - 68: I1ii11iIi11i - OoooooooOO
  if 5 - 5: I1ii11iIi11i * I1IiiI + OoooooooOO / Oo0Ooo
  if 18 - 18: OoO0O00 * iII111i % I1IiiI . OOooOOo * o0oOOo0O0Ooo
 OoO0o0OOOO = iii1iI1I1i11 [ "interface" ]
 if ( OoO0o0OOOO == "" ) :
  IiIIi11i111 = int ( iii1iI1I1i11 [ "instance-id" ] )
  if ( IiIIi11i111 == - 1 ) : return
 else :
  IiIIi11i111 = lisp_get_interface_instance_id ( OoO0o0OOOO , None )
  if 58 - 58: iII111i . IiII + iIii1I11I1II1
  if 13 - 13: oO0o * I1Ii111 / I1Ii111 . I1IiiI
  if 93 - 93: I11i % OoOoOO00 - OOooOOo + iIii1I11I1II1 / OoooooooOO % i11iIiiIii
  if 90 - 90: oO0o % iIii1I11I1II1 + o0oOOo0O0Ooo - I11i / i11iIiiIii
  if 57 - 57: I1IiiI . Oo0Ooo / I1IiiI / II111iiii - I1Ii111
 i1IiIiii = None
 if ( iii1iI1I1i11 . has_key ( "source-eid" ) ) :
  i1i1Ii1iiII1I = iii1iI1I1i11 [ "source-eid" ]
  i1IiIiii = lisp_address ( LISP_AFI_NONE , i1i1Ii1iiII1I , 0 , IiIIi11i111 )
  if ( i1IiIiii . is_null ( ) ) :
   lprint ( "Invalid source-EID format '{}'" . format ( i1i1Ii1iiII1I ) )
   return
   if 68 - 68: I1IiiI
   if 97 - 97: Ii1I + o0oOOo0O0Ooo / OoO0O00
 OOoo0OOo = None
 if ( iii1iI1I1i11 . has_key ( "dest-eid" ) ) :
  ooOoo0ooOo = iii1iI1I1i11 [ "dest-eid" ]
  OOoo0OOo = lisp_address ( LISP_AFI_NONE , ooOoo0ooOo , 0 , IiIIi11i111 )
  if ( OOoo0OOo . is_null ( ) ) :
   lprint ( "Invalid dest-EID format '{}'" . format ( ooOoo0ooOo ) )
   return
   if 28 - 28: OoooooooOO + i1IIi
   if 29 - 29: Oo0Ooo
   if 98 - 98: OOooOOo / Oo0Ooo % Ii1I * OoooooooOO - oO0o
   if 64 - 64: I1IiiI - I1IiiI
   if 90 - 90: iII111i - I1IiiI - II111iiii / OOooOOo + Ii1I
   if 34 - 34: i11iIiiIii + I1Ii111 / O0 / iIii1I11I1II1 * OoooooooOO % Ii1I
   if 32 - 32: i11iIiiIii - OoOoOO00 / iIii1I11I1II1 * o0oOOo0O0Ooo % I1IiiI + O0
   if 36 - 36: I1ii11iIi11i + I1ii11iIi11i % I1Ii111 * ooOoO0o * OoOoOO00
 if ( i1IiIiii ) :
  iIIi1iI1I1IIi = green ( i1IiIiii . print_address ( ) , False )
  ii1iii = lisp_db_for_lookups . lookup_cache ( i1IiIiii , False )
  if ( ii1iii != None ) :
   if 54 - 54: Oo0Ooo - I1IiiI % OOooOOo . I1ii11iIi11i / I1IiiI
   if 75 - 75: OOooOOo - O0 % iII111i . Ii1I % I1ii11iIi11i + I1ii11iIi11i
   if 32 - 32: Ii1I + II111iiii * IiII
   if 9 - 9: I1Ii111
   if 96 - 96: I1Ii111 / iIii1I11I1II1
   if ( ii1iii . dynamic_eid_configured ( ) ) :
    II1i = lisp_allow_dynamic_eid ( OoO0o0OOOO , i1IiIiii )
    if ( II1i != None and lisp_i_am_itr ) :
     lisp_itr_discover_eid ( ii1iii , i1IiIiii , OoO0o0OOOO , II1i )
    else :
     lprint ( ( "Disallow dynamic source-EID {} " + "on interface {}" ) . format ( iIIi1iI1I1IIi , OoO0o0OOOO ) )
     if 48 - 48: iII111i * IiII + OoooooooOO
     if 63 - 63: I1IiiI / Ii1I
     if 31 - 31: i1IIi - oO0o
  else :
   lprint ( "Punt from non-EID source {}" . format ( iIIi1iI1I1IIi ) )
   if 99 - 99: iII111i - i11iIiiIii + oO0o
   if 66 - 66: Oo0Ooo * I11i . iIii1I11I1II1 - OoO0O00
   if 11 - 11: I1Ii111 + iIii1I11I1II1 * O0 * Oo0Ooo
   if 66 - 66: OoooooooOO % OoO0O00 + i11iIiiIii + I1Ii111 % OoO0O00
   if 80 - 80: Oo0Ooo - Ii1I
   if 54 - 54: O0 - iIii1I11I1II1 . OoO0O00 . IiII % OoO0O00
 if ( OOoo0OOo ) :
  o0Oo0 = lisp_map_cache_lookup ( i1IiIiii , OOoo0OOo )
  if ( o0Oo0 == None or lisp_mr_or_pubsub ( o0Oo0 . action ) ) :
   if 28 - 28: O0 % i1IIi % OoO0O00 / o0oOOo0O0Ooo . iIii1I11I1II1 - iII111i
   if 50 - 50: o0oOOo0O0Ooo + iII111i / i1IIi % II111iiii
   if 61 - 61: IiII
   if 5 - 5: OOooOOo % iIii1I11I1II1 % O0 * i11iIiiIii / I1Ii111
   if 48 - 48: IiII * oO0o
   if ( lisp_rate_limit_map_request ( OOoo0OOo ) ) : return
   if 53 - 53: i1IIi * iIii1I11I1II1 . OOooOOo
   I1IIiI = ( o0Oo0 . action == LISP_SEND_PUBSUB_ACTION )
   lisp_send_map_request ( lisp_send_sockets , lisp_ephem_port ,
 i1IiIiii , OOoo0OOo , None , I1IIiI )
  else :
   iIIi1iI1I1IIi = green ( OOoo0OOo . print_address ( ) , False )
   lprint ( "Map-cache entry for {} already exists" . format ( iIIi1iI1I1IIi ) )
   if 68 - 68: IiII % IiII - iII111i . IiII + OoooooooOO
   if 82 - 82: Ii1I . II111iiii / i1IIi * OoO0O00
 return
 if 80 - 80: I11i
 if 96 - 96: i1IIi - I1ii11iIi11i * iII111i . OOooOOo . OoO0O00
 if 93 - 93: oO0o * Oo0Ooo * IiII
 if 26 - 26: o0oOOo0O0Ooo + O0 % i11iIiiIii . ooOoO0o . I1IiiI + Oo0Ooo
 if 90 - 90: IiII * OoooooooOO + II111iiii / iII111i + i11iIiiIii / ooOoO0o
 if 20 - 20: II111iiii % I1ii11iIi11i - OoooooooOO * Ii1I / I11i - OoooooooOO
 if 11 - 11: I1IiiI + Ii1I + i11iIiiIii * I1ii11iIi11i - oO0o
def lisp_ipc_map_cache_entry ( mc , jdata ) :
 i1ii1i1Ii11 = lisp_write_ipc_map_cache ( True , mc , dont_send = True )
 jdata . append ( i1ii1i1Ii11 )
 return ( [ True , jdata ] )
 if 46 - 46: OoooooooOO - Oo0Ooo
 if 4 - 4: II111iiii . OOooOOo - Ii1I - i11iIiiIii
 if 27 - 27: iII111i * iII111i - OoO0O00 % o0oOOo0O0Ooo . o0oOOo0O0Ooo
 if 64 - 64: I1ii11iIi11i * ooOoO0o - OoooooooOO - I1IiiI
 if 59 - 59: I1ii11iIi11i . I1Ii111 - OOooOOo / Oo0Ooo + OOooOOo . I1ii11iIi11i
 if 69 - 69: Oo0Ooo
 if 34 - 34: I1Ii111 - ooOoO0o . o0oOOo0O0Ooo
 if 52 - 52: o0oOOo0O0Ooo % I11i * I11i / iIii1I11I1II1
def lisp_ipc_walk_map_cache ( mc , jdata ) :
 if 77 - 77: OoOoOO00
 if 67 - 67: OoooooooOO / OoooooooOO + IiII - ooOoO0o
 if 72 - 72: Ii1I
 if 21 - 21: ooOoO0o + iII111i
 if ( mc . group . is_null ( ) ) : return ( lisp_ipc_map_cache_entry ( mc , jdata ) )
 if 39 - 39: o0oOOo0O0Ooo % I1Ii111 - o0oOOo0O0Ooo % Oo0Ooo
 if ( mc . source_cache == None ) : return ( [ True , jdata ] )
 if 78 - 78: OoO0O00 / o0oOOo0O0Ooo / O0 % OOooOOo % i1IIi
 if 78 - 78: o0oOOo0O0Ooo - oO0o . II111iiii
 if 67 - 67: iII111i + I11i - OoO0O00 . OOooOOo * iIii1I11I1II1
 if 44 - 44: OoooooooOO * i1IIi % i1IIi - i11iIiiIii % OOooOOo - OoO0O00
 if 62 - 62: OOooOOo + OoooooooOO / I1Ii111 % iIii1I11I1II1
 jdata = mc . source_cache . walk_cache ( lisp_ipc_map_cache_entry , jdata )
 return ( [ True , jdata ] )
 if 59 - 59: i11iIiiIii . IiII
 if 91 - 91: Oo0Ooo / iII111i + I1Ii111
 if 32 - 32: i1IIi - iII111i + o0oOOo0O0Ooo * I1Ii111 % I1ii11iIi11i / i11iIiiIii
 if 91 - 91: IiII / OoooooooOO . OoooooooOO + OoooooooOO * I1ii11iIi11i . OoOoOO00
 if 22 - 22: iIii1I11I1II1 - OoO0O00
 if 77 - 77: I1IiiI + IiII - oO0o - I1ii11iIi11i * II111iiii + i1IIi
 if 79 - 79: I1ii11iIi11i + O0 * OoooooooOO
def lisp_itr_discover_eid ( db , eid , input_interface , routed_interface ,
 lisp_ipc_listen_socket ) :
 Ii1i1 = eid . print_address ( )
 if ( db . dynamic_eids . has_key ( Ii1i1 ) ) :
  db . dynamic_eids [ Ii1i1 ] . last_packet = lisp_get_timestamp ( )
  return
  if 43 - 43: I11i
  if 29 - 29: o0oOOo0O0Ooo / I11i
  if 88 - 88: OoOoOO00 - Ii1I . O0 % I1Ii111 % I1ii11iIi11i
  if 56 - 56: OoOoOO00 - iIii1I11I1II1 / I1IiiI - i1IIi / o0oOOo0O0Ooo * I11i
  if 70 - 70: OOooOOo
 OO0oOo = lisp_dynamic_eid ( )
 OO0oOo . dynamic_eid . copy_address ( eid )
 OO0oOo . interface = routed_interface
 OO0oOo . last_packet = lisp_get_timestamp ( )
 OO0oOo . get_timeout ( routed_interface )
 db . dynamic_eids [ Ii1i1 ] = OO0oOo
 if 11 - 11: I11i * II111iiii * Oo0Ooo + OOooOOo % i1IIi
 OOooo00 = ""
 if ( input_interface != routed_interface ) :
  OOooo00 = ", routed-interface " + routed_interface
  if 18 - 18: i1IIi . OOooOOo * o0oOOo0O0Ooo . iII111i / o0oOOo0O0Ooo + I11i
  if 56 - 56: I1Ii111 - OoOoOO00 / I11i
 OOooOOO = green ( Ii1i1 , False ) + bold ( " discovered" , False )
 lprint ( "Dynamic-EID {} on interface {}{}, timeout {}" . format ( OOooOOO , input_interface , OOooo00 , OO0oOo . timeout ) )
 if 5 - 5: I1IiiI / oO0o + OoOoOO00
 if 32 - 32: o0oOOo0O0Ooo % oO0o % I1IiiI * OoooooooOO
 if 4 - 4: OOooOOo % oO0o
 if 18 - 18: Ii1I * I11i
 if 14 - 14: ooOoO0o . ooOoO0o * OoOoOO00 * o0oOOo0O0Ooo - iII111i - I1Ii111
 oOOO0oo0 = "learn%{}%{}" . format ( Ii1i1 , routed_interface )
 oOOO0oo0 = lisp_command_ipc ( oOOO0oo0 , "lisp-itr" )
 lisp_ipc ( oOOO0oo0 , lisp_ipc_listen_socket , "lisp-etr" )
 return
 if 53 - 53: Oo0Ooo * OoOoOO00 * II111iiii % IiII - I1ii11iIi11i
 if 56 - 56: Oo0Ooo . I1ii11iIi11i - i11iIiiIii / iIii1I11I1II1 . ooOoO0o
 if 28 - 28: OoooooooOO + I1IiiI / oO0o . iIii1I11I1II1 - oO0o
 if 64 - 64: I1Ii111 + Oo0Ooo / iII111i
 if 61 - 61: Ii1I * Ii1I . OoOoOO00 + OoO0O00 * i11iIiiIii * OoO0O00
 if 4 - 4: OoooooooOO % iII111i % Oo0Ooo * IiII % o0oOOo0O0Ooo . o0oOOo0O0Ooo
 if 66 - 66: I1IiiI . Oo0Ooo - oO0o
 if 53 - 53: oO0o / Ii1I + oO0o + II111iiii
 if 70 - 70: OoooooooOO - I1Ii111 + OoOoOO00
 if 61 - 61: I1IiiI * I1Ii111 * i11iIiiIii
 if 68 - 68: OoOoOO00 - iII111i - I1IiiI
 if 37 - 37: iII111i - I1Ii111 + i1IIi / o0oOOo0O0Ooo % iII111i / iII111i
 if 8 - 8: i1IIi % I11i
def lisp_retry_decap_keys ( addr_str , packet , iv , packet_icv ) :
 if ( lisp_search_decap_keys == False ) : return
 if 12 - 12: ooOoO0o / II111iiii + ooOoO0o * I1ii11iIi11i / i1IIi - iIii1I11I1II1
 if 71 - 71: IiII - i11iIiiIii
 if 3 - 3: i11iIiiIii - o0oOOo0O0Ooo / oO0o . OoO0O00 * I11i + o0oOOo0O0Ooo
 if 18 - 18: OoooooooOO % oO0o / IiII - ooOoO0o
 if ( addr_str . find ( ":" ) != - 1 ) : return
 if 80 - 80: I11i
 O0Ii1IiiiI = lisp_crypto_keys_by_rloc_decap [ addr_str ]
 if 98 - 98: iII111i / I1ii11iIi11i
 for o0Oo in lisp_crypto_keys_by_rloc_decap :
  if 87 - 87: iII111i - O0 * ooOoO0o / II111iiii % OoooooooOO . o0oOOo0O0Ooo
  if 55 - 55: OOooOOo - o0oOOo0O0Ooo * I1IiiI / o0oOOo0O0Ooo + I1Ii111 + iIii1I11I1II1
  if 3 - 3: II111iiii % iII111i / IiII * ooOoO0o . OoooooooOO
  if 56 - 56: IiII * II111iiii + Oo0Ooo - O0 - OoO0O00 . I1Ii111
  if ( o0Oo . find ( addr_str ) == - 1 ) : continue
  if 53 - 53: i1IIi + IiII
  if 90 - 90: II111iiii / oO0o / oO0o . OoOoOO00 / OoO0O00 / iIii1I11I1II1
  if 96 - 96: iIii1I11I1II1 % I1ii11iIi11i
  if 35 - 35: i1IIi - OoooooooOO * Ii1I / OOooOOo % I11i
  if ( o0Oo == addr_str ) : continue
  if 72 - 72: I1Ii111 / OoO0O00 + II111iiii
  if 40 - 40: Ii1I + O0 . i11iIiiIii % I11i / Oo0Ooo
  if 25 - 25: IiII * IiII
  if 54 - 54: I1Ii111
  i1ii1i1Ii11 = lisp_crypto_keys_by_rloc_decap [ o0Oo ]
  if ( i1ii1i1Ii11 == O0Ii1IiiiI ) : continue
  if 90 - 90: Oo0Ooo / Ii1I
  if 66 - 66: i11iIiiIii - I11i + oO0o . OoooooooOO
  if 77 - 77: OoO0O00 / OOooOOo
  if 97 - 97: OoOoOO00 / Ii1I * I1IiiI - Oo0Ooo % O0
  Oo0Ooo0 = i1ii1i1Ii11 [ 1 ]
  if ( packet_icv != Oo0Ooo0 . do_icv ( packet , iv ) ) :
   lprint ( "Test ICV with key {} failed" . format ( red ( o0Oo , False ) ) )
   continue
   if 23 - 23: i1IIi / I11i * O0 + iII111i
   if 20 - 20: Ii1I * I1ii11iIi11i - I1Ii111 + I1IiiI - ooOoO0o
  lprint ( "Changing decap crypto key to {}" . format ( red ( o0Oo , False ) ) )
  lisp_crypto_keys_by_rloc_decap [ addr_str ] = i1ii1i1Ii11
  if 63 - 63: Ii1I + o0oOOo0O0Ooo - iII111i
 return
 if 1 - 1: O0 . I1IiiI . OoooooooOO . I1ii11iIi11i + I11i - i11iIiiIii
 if 16 - 16: I1ii11iIi11i
 if 69 - 69: IiII + I1ii11iIi11i - ooOoO0o . II111iiii
 if 41 - 41: iII111i - OoO0O00
 if 74 - 74: I1ii11iIi11i . OoO0O00 % Oo0Ooo / oO0o
 if 43 - 43: iIii1I11I1II1
 if 79 - 79: O0 % ooOoO0o - OoOoOO00 / I1Ii111
 if 85 - 85: iII111i % OOooOOo . OoooooooOO % O0 % O0
def lisp_decent_pull_xtr_configured ( ) :
 return ( lisp_decent_modulus != 0 and lisp_decent_dns_suffix != None )
 if 72 - 72: o0oOOo0O0Ooo * IiII / II111iiii / iIii1I11I1II1
 if 41 - 41: iII111i / Ii1I
 if 11 - 11: Oo0Ooo % OOooOOo . ooOoO0o
 if 24 - 24: IiII / Oo0Ooo
 if 90 - 90: ooOoO0o . OOooOOo - Ii1I
 if 60 - 60: i11iIiiIii % iII111i . I1IiiI * I1ii11iIi11i
 if 30 - 30: Ii1I + i11iIiiIii . I11i + o0oOOo0O0Ooo - OoO0O00
 if 55 - 55: ooOoO0o - II111iiii . ooOoO0o . iII111i / OoooooooOO
def lisp_is_decent_dns_suffix ( dns_name ) :
 if ( lisp_decent_dns_suffix == None ) : return ( False )
 II1 = dns_name . split ( "." )
 II1 = "." . join ( II1 [ 1 : : ] )
 return ( II1 == lisp_decent_dns_suffix )
 if 51 - 51: I1IiiI * I1Ii111 - ooOoO0o + IiII
 if 22 - 22: OoOoOO00 % Ii1I + iII111i
 if 64 - 64: ooOoO0o
 if 87 - 87: IiII - Ii1I / Oo0Ooo / I1ii11iIi11i . iII111i
 if 49 - 49: IiII * OoooooooOO * iIii1I11I1II1 * Oo0Ooo / iII111i % oO0o
 if 88 - 88: I1Ii111 * OOooOOo
 if 38 - 38: Oo0Ooo - OoooooooOO - OoooooooOO / II111iiii
 if 10 - 10: II111iiii - OoO0O00 / II111iiii % Ii1I - OoOoOO00
 if 90 - 90: I11i + II111iiii - oO0o - ooOoO0o / ooOoO0o / i11iIiiIii
 if 80 - 80: I1ii11iIi11i % O0 / II111iiii + iII111i
 if 22 - 22: Oo0Ooo + ooOoO0o . OOooOOo % Oo0Ooo . IiII
def lisp_get_decent_index ( eid ) :
 Ii1i1 = eid . print_prefix ( )
 I1IIIIi1IIiIi = hmac . new ( "lisp-decent" , Ii1i1 , hashlib . sha256 ) . hexdigest ( )
 if 42 - 42: Ii1I - OoOoOO00 . OoOoOO00
 if 88 - 88: o0oOOo0O0Ooo . Ii1I . iII111i * iII111i + i11iIiiIii
 if 68 - 68: OoooooooOO
 if 5 - 5: OoOoOO00 . i11iIiiIii . OOooOOo / I11i * Oo0Ooo % Oo0Ooo
 II1IIi = os . getenv ( "LISP_DECENT_HASH_WIDTH" )
 if ( II1IIi in [ "" , None ] ) :
  II1IIi = 12
 else :
  II1IIi = int ( II1IIi )
  if ( II1IIi > 32 ) :
   II1IIi = 12
  else :
   II1IIi *= 2
   if 16 - 16: II111iiii + I1ii11iIi11i * I1Ii111
   if 6 - 6: i11iIiiIii . o0oOOo0O0Ooo * iIii1I11I1II1 . OoOoOO00 . II111iiii
   if 67 - 67: OoO0O00 - Oo0Ooo + OOooOOo / OoOoOO00 + OOooOOo
 iI1IiIi1Iii = I1IIIIi1IIiIi [ 0 : II1IIi ]
 ooo = int ( iI1IiIi1Iii , 16 ) % lisp_decent_modulus
 if 52 - 52: Oo0Ooo . iII111i / oO0o * II111iiii
 lprint ( "LISP-Decent modulus {}, hash-width {}, mod-value {}, index {}" . format ( lisp_decent_modulus , II1IIi / 2 , iI1IiIi1Iii , ooo ) )
 if 21 - 21: o0oOOo0O0Ooo / I1ii11iIi11i
 if 48 - 48: i11iIiiIii % I1ii11iIi11i
 return ( ooo )
 if 73 - 73: OoOoOO00 + O0 + I1IiiI . iIii1I11I1II1 / I1ii11iIi11i
 if 98 - 98: Oo0Ooo
 if 72 - 72: oO0o + OoooooooOO . O0 + IiII
 if 49 - 49: i1IIi - i11iIiiIii + II111iiii + Ii1I / OoO0O00
 if 34 - 34: I1ii11iIi11i * i11iIiiIii
 if 6 - 6: I1ii11iIi11i + I1IiiI / OoooooooOO % I11i * Oo0Ooo
 if 20 - 20: Oo0Ooo
def lisp_get_decent_dns_name ( eid ) :
 ooo = lisp_get_decent_index ( eid )
 return ( str ( ooo ) + "." + lisp_decent_dns_suffix )
 if 85 - 85: I1Ii111
 if 98 - 98: OoO0O00 - IiII % iIii1I11I1II1 . OoOoOO00 + i1IIi + OoooooooOO
 if 29 - 29: I1ii11iIi11i * I1Ii111 - i1IIi * i11iIiiIii * iIii1I11I1II1 % I11i
 if 73 - 73: OoO0O00 . I1IiiI / o0oOOo0O0Ooo
 if 12 - 12: I11i * i11iIiiIii - O0 * o0oOOo0O0Ooo - IiII + I1IiiI
 if 7 - 7: oO0o + I1Ii111 . o0oOOo0O0Ooo / IiII + iIii1I11I1II1 % I1Ii111
 if 24 - 24: i11iIiiIii + iIii1I11I1II1
 if 22 - 22: i11iIiiIii . II111iiii / o0oOOo0O0Ooo / Ii1I . O0 . OoOoOO00
def lisp_get_decent_dns_name_from_str ( iid , eid_str ) :
 iiI1I1IIi = lisp_address ( LISP_AFI_NONE , eid_str , 0 , iid )
 ooo = lisp_get_decent_index ( iiI1I1IIi )
 return ( str ( ooo ) + "." + lisp_decent_dns_suffix )
 if 89 - 89: O0 * Oo0Ooo + I1Ii111 + ooOoO0o * OoOoOO00
 if 20 - 20: OoO0O00 - OoOoOO00
 if 84 - 84: iIii1I11I1II1 + ooOoO0o . o0oOOo0O0Ooo % iII111i
 if 35 - 35: I11i - oO0o * oO0o / OoooooooOO + iII111i + OoOoOO00
 if 48 - 48: I1Ii111 / o0oOOo0O0Ooo - OOooOOo / o0oOOo0O0Ooo % O0
 if 38 - 38: OoO0O00 + o0oOOo0O0Ooo / OoO0O00
 if 74 - 74: oO0o - i1IIi . Oo0Ooo / I1IiiI + o0oOOo0O0Ooo . OoOoOO00
 if 35 - 35: iII111i / Ii1I
 if 57 - 57: ooOoO0o . I1IiiI * OOooOOo
 if 87 - 87: I11i - I11i % iII111i - Ii1I
def lisp_trace_append ( packet , reason = None , ed = "encap" , lisp_socket = None ,
 rloc_entry = None ) :
 if 29 - 29: oO0o - ooOoO0o * iIii1I11I1II1 / OoOoOO00
 oO0ooOoO = 28 if packet . inner_version == 4 else 48
 iiiI11ii1IIii = packet . packet [ oO0ooOoO : : ]
 OO0oO0 = lisp_trace ( )
 if ( OO0oO0 . decode ( iiiI11ii1IIii ) == False ) :
  lprint ( "Could not decode JSON portion of a LISP-Trace packet" )
  return ( False )
  if 27 - 27: I11i . I1ii11iIi11i + I11i * o0oOOo0O0Ooo
  if 93 - 93: O0 . I1IiiI % I1IiiI * oO0o % I1Ii111 * Ii1I
 o0O000OOo0 = "?" if packet . outer_dest . is_null ( ) else packet . outer_dest . print_address_no_iid ( )
 if 90 - 90: o0oOOo0O0Ooo
 if 5 - 5: i1IIi
 if 55 - 55: Ii1I
 if 46 - 46: OOooOOo / iII111i . i1IIi . i11iIiiIii . iIii1I11I1II1 % I11i
 if 62 - 62: I11i % II111iiii % OoooooooOO * ooOoO0o / oO0o
 if 29 - 29: o0oOOo0O0Ooo / O0 / OoO0O00
 if ( o0O000OOo0 != "?" and packet . encap_port != LISP_DATA_PORT ) :
  if ( ed == "encap" ) : o0O000OOo0 += ":{}" . format ( packet . encap_port )
  if 23 - 23: Ii1I + i11iIiiIii % IiII
  if 64 - 64: i11iIiiIii + OoooooooOO . oO0o * Ii1I
  if 49 - 49: O0
  if 72 - 72: I1Ii111
  if 96 - 96: II111iiii / OOooOOo % i1IIi / Oo0Ooo
 i1ii1i1Ii11 = { }
 i1ii1i1Ii11 [ "node" ] = "ITR" if lisp_i_am_itr else "ETR" if lisp_i_am_etr else "RTR" if lisp_i_am_rtr else "?"
 if 22 - 22: I1IiiI % iIii1I11I1II1 % I1ii11iIi11i
 o00OooO = packet . outer_source
 if ( o00OooO . is_null ( ) ) : o00OooO = lisp_myrlocs [ 0 ]
 i1ii1i1Ii11 [ "srloc" ] = o00OooO . print_address_no_iid ( )
 if 95 - 95: O0 % o0oOOo0O0Ooo . Ii1I % OoOoOO00 % IiII
 if 27 - 27: OoOoOO00 + OOooOOo - oO0o % Oo0Ooo . iII111i
 if 95 - 95: o0oOOo0O0Ooo * ooOoO0o * I1Ii111 + iII111i . i1IIi / OoooooooOO
 if 8 - 8: o0oOOo0O0Ooo * I1ii11iIi11i % OOooOOo
 if 8 - 8: OoOoOO00 * oO0o % I1Ii111 . oO0o
 if ( i1ii1i1Ii11 [ "node" ] == "ITR" and packet . inner_sport != LISP_TRACE_PORT ) :
  i1ii1i1Ii11 [ "srloc" ] += ":{}" . format ( packet . inner_sport )
  if 94 - 94: Ii1I + II111iiii / OOooOOo * OoOoOO00 / I11i
  if 92 - 92: iII111i
 i1ii1i1Ii11 [ "hn" ] = lisp_hostname
 o0Oo = ed + "-ts"
 i1ii1i1Ii11 [ o0Oo ] = lisp_get_timestamp ( )
 if 93 - 93: Ii1I / Oo0Ooo . OoO0O00 . oO0o % OOooOOo
 if 63 - 63: II111iiii
 if 43 - 43: I11i . iII111i + I1IiiI . OOooOOo * Ii1I / ooOoO0o
 if 70 - 70: i11iIiiIii * oO0o . I11i - OoooooooOO / I1ii11iIi11i
 if 10 - 10: IiII * OoOoOO00 . II111iiii . II111iiii * Oo0Ooo
 if 23 - 23: I1ii11iIi11i + I11i
 if ( o0O000OOo0 == "?" and i1ii1i1Ii11 [ "node" ] == "ETR" ) :
  ii1iii = lisp_db_for_lookups . lookup_cache ( packet . inner_dest , False )
  if ( ii1iii != None and len ( ii1iii . rloc_set ) >= 1 ) :
   o0O000OOo0 = ii1iii . rloc_set [ 0 ] . rloc . print_address_no_iid ( )
   if 74 - 74: i1IIi % I1IiiI
   if 44 - 44: Oo0Ooo - OoooooooOO % ooOoO0o + II111iiii
 i1ii1i1Ii11 [ "drloc" ] = o0O000OOo0
 if 60 - 60: o0oOOo0O0Ooo - ooOoO0o + i11iIiiIii % I1ii11iIi11i % II111iiii
 if 62 - 62: Ii1I
 if 30 - 30: iII111i % O0 + II111iiii * I1IiiI
 if 91 - 91: i11iIiiIii
 if ( o0O000OOo0 == "?" and reason != None ) :
  i1ii1i1Ii11 [ "drloc" ] += " ({})" . format ( reason )
  if 35 - 35: OoOoOO00 * I1Ii111 / Oo0Ooo - i1IIi - IiII + OOooOOo
  if 96 - 96: Oo0Ooo + I1ii11iIi11i . O0
  if 62 - 62: i1IIi % OoooooooOO % OoooooooOO
  if 53 - 53: O0 * oO0o
  if 22 - 22: OOooOOo % Oo0Ooo % ooOoO0o - O0 + i1IIi
 if ( rloc_entry != None ) :
  i1ii1i1Ii11 [ "rtts" ] = rloc_entry . recent_rloc_probe_rtts
  i1ii1i1Ii11 [ "hops" ] = rloc_entry . recent_rloc_probe_hops
  i1ii1i1Ii11 [ "latencies" ] = rloc_entry . recent_rloc_probe_latencies
  if 67 - 67: OoO0O00 / I1IiiI - IiII + iII111i - iII111i
  if 4 - 4: IiII . Ii1I . IiII % OoO0O00
  if 12 - 12: OoOoOO00 + O0 / O0 . i1IIi
  if 58 - 58: IiII . iII111i % O0 . Ii1I * Oo0Ooo
  if 54 - 54: OoO0O00 % OOooOOo - OoO0O00 . Oo0Ooo % i1IIi
  if 95 - 95: iII111i . OoooooooOO . o0oOOo0O0Ooo / II111iiii - OoooooooOO / I1Ii111
 i1IiIiii = packet . inner_source . print_address ( )
 OOoo0OOo = packet . inner_dest . print_address ( )
 if ( OO0oO0 . packet_json == [ ] ) :
  iiIi111IiIiI = { }
  iiIi111IiIiI [ "seid" ] = i1IiIiii
  iiIi111IiIiI [ "deid" ] = OOoo0OOo
  iiIi111IiIiI [ "paths" ] = [ ]
  OO0oO0 . packet_json . append ( iiIi111IiIiI )
  if 11 - 11: II111iiii / iII111i . oO0o / ooOoO0o / OOooOOo + OoO0O00
  if 37 - 37: iIii1I11I1II1 * O0
  if 64 - 64: I1Ii111 - II111iiii + oO0o % ooOoO0o * oO0o
  if 27 - 27: iIii1I11I1II1 - Ii1I . i11iIiiIii / IiII . I1Ii111 / i11iIiiIii
  if 27 - 27: OoOoOO00 . I11i / OoOoOO00
  if 96 - 96: OoO0O00 - I1IiiI
 for iiIi111IiIiI in OO0oO0 . packet_json :
  if ( iiIi111IiIiI [ "deid" ] != OOoo0OOo ) : continue
  iiIi111IiIiI [ "paths" ] . append ( i1ii1i1Ii11 )
  break
  if 73 - 73: I1IiiI - o0oOOo0O0Ooo - I1Ii111
  if 34 - 34: iIii1I11I1II1 - i1IIi + OoO0O00 % Oo0Ooo + i1IIi
  if 46 - 46: I1IiiI
  if 82 - 82: iII111i . i1IIi
  if 38 - 38: Ii1I . I1IiiI . I1ii11iIi11i
  if 26 - 26: O0 - II111iiii * I1Ii111 - OoOoOO00
  if 96 - 96: I11i * Oo0Ooo / OOooOOo - IiII
  if 75 - 75: OoooooooOO - O0
 iii11 = False
 if ( len ( OO0oO0 . packet_json ) == 1 and i1ii1i1Ii11 [ "node" ] == "ETR" and
 OO0oO0 . myeid ( packet . inner_dest ) ) :
  iiIi111IiIiI = { }
  iiIi111IiIiI [ "seid" ] = OOoo0OOo
  iiIi111IiIiI [ "deid" ] = i1IiIiii
  iiIi111IiIiI [ "paths" ] = [ ]
  OO0oO0 . packet_json . append ( iiIi111IiIiI )
  iii11 = True
  if 93 - 93: o0oOOo0O0Ooo - Oo0Ooo / oO0o / OoOoOO00
  if 75 - 75: o0oOOo0O0Ooo * ooOoO0o % Ii1I
  if 94 - 94: OoooooooOO + II111iiii / iIii1I11I1II1 * ooOoO0o
  if 85 - 85: ooOoO0o / IiII
  if 28 - 28: i11iIiiIii - OoOoOO00
  if 13 - 13: O0
 OO0oO0 . print_trace ( )
 iiiI11ii1IIii = OO0oO0 . encode ( )
 if 82 - 82: OoooooooOO
 if 59 - 59: I1Ii111 + I1ii11iIi11i + OoO0O00 % oO0o . i1IIi % O0
 if 22 - 22: i1IIi * OoOoOO00 + Ii1I
 if 48 - 48: Ii1I % IiII + OoO0O00 . IiII
 if 42 - 42: Ii1I
 if 70 - 70: I11i
 if 82 - 82: O0
 if 58 - 58: II111iiii . O0 - OoO0O00 - IiII
 iiiiiII = OO0oO0 . packet_json [ 0 ] [ "paths" ] [ 0 ] [ "srloc" ]
 if ( o0O000OOo0 == "?" ) :
  lprint ( "LISP-Trace return to sender RLOC {}" . format ( iiiiiII ) )
  OO0oO0 . return_to_sender ( lisp_socket , iiiiiII , iiiI11ii1IIii )
  return ( False )
  if 68 - 68: ooOoO0o - i1IIi % i1IIi + O0 . i11iIiiIii
  if 6 - 6: o0oOOo0O0Ooo % I1ii11iIi11i
  if 23 - 23: iIii1I11I1II1
  if 84 - 84: I1ii11iIi11i + I1Ii111
  if 23 - 23: OoooooooOO % OoO0O00 . i11iIiiIii * i11iIiiIii * OoOoOO00
  if 84 - 84: OOooOOo % I1Ii111 + I11i / I1IiiI . iII111i
 iIIIIi = OO0oO0 . packet_length ( )
 if 78 - 78: oO0o . Oo0Ooo
 if 18 - 18: IiII
 if 35 - 35: OoooooooOO / i1IIi - OoO0O00 + Oo0Ooo - o0oOOo0O0Ooo
 if 100 - 100: II111iiii % i11iIiiIii % oO0o + O0
 if 46 - 46: OoO0O00 / I1IiiI - Oo0Ooo . o0oOOo0O0Ooo . Oo0Ooo % I11i
 if 43 - 43: IiII - O0 + I1Ii111 % OoooooooOO % OoO0O00 / I1Ii111
 IIoo00OO0O0 = packet . packet [ 0 : oO0ooOoO ]
 IiI1i1i1 = struct . pack ( "HH" , socket . htons ( iIIIIi ) , 0 )
 IIoo00OO0O0 = IIoo00OO0O0 [ 0 : oO0ooOoO - 4 ] + IiI1i1i1
 if ( packet . inner_version == 6 and i1ii1i1Ii11 [ "node" ] == "ETR" and
 len ( OO0oO0 . packet_json ) == 2 ) :
  oOoO0OOO00O = IIoo00OO0O0 [ oO0ooOoO - 8 : : ] + iiiI11ii1IIii
  oOoO0OOO00O = lisp_udp_checksum ( i1IiIiii , OOoo0OOo , oOoO0OOO00O )
  IIoo00OO0O0 = IIoo00OO0O0 [ 0 : oO0ooOoO - 8 ] + oOoO0OOO00O [ 0 : 8 ]
  if 1 - 1: II111iiii + II111iiii
  if 34 - 34: I1Ii111
  if 51 - 51: OoooooooOO - OOooOOo / ooOoO0o
  if 65 - 65: iIii1I11I1II1 * i1IIi
  if 48 - 48: O0 / I11i
  if 8 - 8: OOooOOo + iIii1I11I1II1 / OoooooooOO
 if ( iii11 ) :
  if ( packet . inner_version == 4 ) :
   IIoo00OO0O0 = IIoo00OO0O0 [ 0 : 12 ] + IIoo00OO0O0 [ 16 : 20 ] + IIoo00OO0O0 [ 12 : 16 ] + IIoo00OO0O0 [ 22 : 24 ] + IIoo00OO0O0 [ 20 : 22 ] + IIoo00OO0O0 [ 24 : : ]
   if 11 - 11: i11iIiiIii / iIii1I11I1II1 % ooOoO0o + OOooOOo
  else :
   IIoo00OO0O0 = IIoo00OO0O0 [ 0 : 8 ] + IIoo00OO0O0 [ 24 : 40 ] + IIoo00OO0O0 [ 8 : 24 ] + IIoo00OO0O0 [ 42 : 44 ] + IIoo00OO0O0 [ 40 : 42 ] + IIoo00OO0O0 [ 44 : : ]
   if 73 - 73: OoOoOO00 + OoooooooOO + iIii1I11I1II1 + II111iiii * iIii1I11I1II1 - OoOoOO00
   if 71 - 71: O0 * OOooOOo . I1IiiI . I1Ii111 * I11i
  o0 = packet . inner_dest
  packet . inner_dest = packet . inner_source
  packet . inner_source = o0
  if 45 - 45: O0 . O0 . II111iiii * ooOoO0o
  if 2 - 2: OoO0O00 . o0oOOo0O0Ooo
  if 48 - 48: Ii1I
  if 45 - 45: I1ii11iIi11i - I11i + Ii1I
  if 82 - 82: iII111i
 oO0ooOoO = 2 if packet . inner_version == 4 else 4
 OoOOOOOooo = 20 + iIIIIi if packet . inner_version == 4 else iIIIIi
 iIIi1Iii1Ii = struct . pack ( "H" , socket . htons ( OoOOOOOooo ) )
 IIoo00OO0O0 = IIoo00OO0O0 [ 0 : oO0ooOoO ] + iIIi1Iii1Ii + IIoo00OO0O0 [ oO0ooOoO + 2 : : ]
 if 97 - 97: OoO0O00 + i11iIiiIii % I1IiiI * Ii1I
 if 89 - 89: IiII % i11iIiiIii + OoO0O00 . oO0o / I1IiiI . Ii1I
 if 11 - 11: ooOoO0o - I1Ii111 - I11i + OoOoOO00
 if 20 - 20: I11i + O0
 if ( packet . inner_version == 4 ) :
  IiiI11iIi = struct . pack ( "H" , 0 )
  IIoo00OO0O0 = IIoo00OO0O0 [ 0 : 10 ] + IiiI11iIi + IIoo00OO0O0 [ 12 : : ]
  iIIi1Iii1Ii = lisp_ip_checksum ( IIoo00OO0O0 [ 0 : 20 ] )
  IIoo00OO0O0 = iIIi1Iii1Ii + IIoo00OO0O0 [ 20 : : ]
  if 27 - 27: Oo0Ooo
  if 12 - 12: I1ii11iIi11i . iII111i - iII111i - OOooOOo - iIii1I11I1II1
  if 50 - 50: I1IiiI - iIii1I11I1II1 . iII111i - Ii1I / I1Ii111 + iII111i
  if 46 - 46: OOooOOo + iII111i % Oo0Ooo * iII111i % OoooooooOO * IiII
  if 27 - 27: I1IiiI + I1IiiI + I1ii11iIi11i - oO0o * OOooOOo
 packet . packet = IIoo00OO0O0 + iiiI11ii1IIii
 return ( True )
 if 53 - 53: I1ii11iIi11i / OoooooooOO * iIii1I11I1II1
 if 4 - 4: I1IiiI . iIii1I11I1II1 + OOooOOo / IiII . o0oOOo0O0Ooo . I11i
 if 52 - 52: ooOoO0o % i11iIiiIii . IiII + OoO0O00
 if 66 - 66: II111iiii . Ii1I
 if 42 - 42: iIii1I11I1II1 * iII111i * I1IiiI
 if 66 - 66: Oo0Ooo * i1IIi / I1ii11iIi11i / OoO0O00
 if 12 - 12: OOooOOo + iIii1I11I1II1 % I1Ii111 + OOooOOo
 if 19 - 19: OoO0O00 / I1IiiI - o0oOOo0O0Ooo - i1IIi + I1ii11iIi11i * OoooooooOO
 if 74 - 74: I1Ii111 . I11i / Oo0Ooo
 if 88 - 88: oO0o % OoO0O00 - i11iIiiIii % I1Ii111 / O0 * IiII
def lisp_allow_gleaning ( eid , group , rloc ) :
 if ( lisp_glean_mappings == [ ] ) : return ( False , False , False )
 if 99 - 99: o0oOOo0O0Ooo . ooOoO0o / i11iIiiIii
 for i1ii1i1Ii11 in lisp_glean_mappings :
  if ( i1ii1i1Ii11 . has_key ( "instance-id" ) ) :
   IiIIi11i111 = eid . instance_id
   I11II1i1i , OOoOooO0 = i1ii1i1Ii11 [ "instance-id" ]
   if ( IiIIi11i111 < I11II1i1i or IiIIi11i111 > OOoOooO0 ) : continue
   if 44 - 44: IiII + OOooOOo % OoO0O00 . OoooooooOO * O0
  if ( i1ii1i1Ii11 . has_key ( "eid-prefix" ) ) :
   iIIi1iI1I1IIi = copy . deepcopy ( i1ii1i1Ii11 [ "eid-prefix" ] )
   iIIi1iI1I1IIi . instance_id = eid . instance_id
   if ( eid . is_more_specific ( iIIi1iI1I1IIi ) == False ) : continue
   if 72 - 72: i1IIi - iII111i * I1IiiI % O0 - I11i * O0
  if ( i1ii1i1Ii11 . has_key ( "group-prefix" ) ) :
   if ( group == None ) : continue
   i11ii = copy . deepcopy ( i1ii1i1Ii11 [ "group-prefix" ] )
   i11ii . instance_id = group . instance_id
   if ( group . is_more_specific ( i11ii ) == False ) : continue
   if 78 - 78: I1IiiI - OoO0O00 / Ii1I . i1IIi
  if ( i1ii1i1Ii11 . has_key ( "rloc-prefix" ) ) :
   if ( rloc != None and rloc . is_more_specific ( i1ii1i1Ii11 [ "rloc-prefix" ] )
 == False ) : continue
   if 30 - 30: IiII
  return ( True , i1ii1i1Ii11 [ "rloc-probe" ] , i1ii1i1Ii11 [ "igmp-query" ] )
  if 21 - 21: i1IIi . iII111i - I1IiiI
 return ( False , False , False )
 if 28 - 28: IiII / Ii1I - i1IIi - OoOoOO00
 if 65 - 65: o0oOOo0O0Ooo * OoO0O00 / o0oOOo0O0Ooo
 if 77 - 77: OoooooooOO - Oo0Ooo - OoOoOO00 / I11i / O0 . i11iIiiIii
 if 27 - 27: I1Ii111 * O0
 if 9 - 9: i1IIi - Oo0Ooo - i11iIiiIii / iIii1I11I1II1 . i1IIi
 if 2 - 2: I11i + II111iiii - I11i / oO0o / I11i
 if 73 - 73: IiII % I1Ii111 . OoOoOO00
def lisp_build_gleaned_multicast ( seid , geid , rloc , port , igmp ) :
 oo0oo = geid . print_address ( )
 ooo0Ii11 = seid . print_address_no_iid ( )
 OO0o0OO0 = green ( "{}" . format ( ooo0Ii11 ) , False )
 iIIi1iI1I1IIi = green ( "(*, {})" . format ( oo0oo ) , False )
 I1I111iIiI = red ( rloc . print_address_no_iid ( ) + ":" + str ( port ) , False )
 if 87 - 87: Oo0Ooo / IiII * OOooOOo + I1ii11iIi11i . I11i
 if 56 - 56: oO0o + oO0o % o0oOOo0O0Ooo + OOooOOo . II111iiii + i11iIiiIii
 if 45 - 45: iIii1I11I1II1 / o0oOOo0O0Ooo * OoooooooOO - Oo0Ooo
 if 77 - 77: II111iiii
 o0Oo0 = lisp_map_cache_lookup ( seid , geid )
 if ( o0Oo0 == None ) :
  o0Oo0 = lisp_mapping ( "" , "" , [ ] )
  o0Oo0 . group . copy_address ( geid )
  o0Oo0 . eid . copy_address ( geid )
  o0Oo0 . eid . address = 0
  o0Oo0 . eid . mask_len = 0
  o0Oo0 . mapping_source . copy_address ( rloc )
  o0Oo0 . map_cache_ttl = LISP_IGMP_TTL
  o0Oo0 . gleaned = True
  o0Oo0 . add_cache ( )
  lprint ( "Add gleaned EID {} to map-cache" . format ( iIIi1iI1I1IIi ) )
  if 8 - 8: I1IiiI * II111iiii % I1ii11iIi11i
  if 88 - 88: Oo0Ooo . oO0o + OoOoOO00 % OoooooooOO
  if 81 - 81: OoooooooOO . I1Ii111 + OoO0O00 % I1Ii111
  if 49 - 49: oO0o . oO0o % oO0o / Oo0Ooo
  if 62 - 62: ooOoO0o . i1IIi % OoO0O00 - I1ii11iIi11i - IiII
  if 57 - 57: i1IIi - II111iiii - O0 . iII111i + OoO0O00
 oOO0O = O0o0ooOoO0o0O = IiioOoo = None
 if ( o0Oo0 . rloc_set != [ ] ) :
  oOO0O = o0Oo0 . rloc_set [ 0 ]
  if ( oOO0O . rle ) :
   O0o0ooOoO0o0O = oOO0O . rle
   for i1I1iIiI111i in O0o0ooOoO0o0O . rle_nodes :
    if ( i1I1iIiI111i . rloc_name != ooo0Ii11 ) : continue
    IiioOoo = i1I1iIiI111i
    break
    if 54 - 54: I1Ii111
    if 88 - 88: Oo0Ooo % Ii1I
    if 3 - 3: o0oOOo0O0Ooo % II111iiii
    if 77 - 77: I11i / ooOoO0o + I1Ii111 + Ii1I * I1IiiI
    if 63 - 63: OOooOOo - Oo0Ooo / I1IiiI / Oo0Ooo + i11iIiiIii
    if 17 - 17: OOooOOo . iIii1I11I1II1 * OoO0O00 . o0oOOo0O0Ooo * II111iiii
    if 23 - 23: I1IiiI + ooOoO0o % iII111i - o0oOOo0O0Ooo % OoooooooOO . OoO0O00
 if ( oOO0O == None ) :
  oOO0O = lisp_rloc ( )
  o0Oo0 . rloc_set = [ oOO0O ]
  oOO0O . priority = 253
  oOO0O . mpriority = 255
  o0Oo0 . build_best_rloc_set ( )
  if 24 - 24: oO0o / O0 + I1Ii111 % i11iIiiIii
 if ( O0o0ooOoO0o0O == None ) :
  O0o0ooOoO0o0O = lisp_rle ( geid . print_address ( ) )
  oOO0O . rle = O0o0ooOoO0o0O
  if 5 - 5: II111iiii + oO0o / o0oOOo0O0Ooo / i11iIiiIii
 if ( IiioOoo == None ) :
  IiioOoo = lisp_rle_node ( )
  IiioOoo . rloc_name = ooo0Ii11
  O0o0ooOoO0o0O . rle_nodes . append ( IiioOoo )
  O0o0ooOoO0o0O . build_forwarding_list ( )
  lprint ( "Add RLE {} from {} for gleaned EID {}" . format ( I1I111iIiI , OO0o0OO0 , iIIi1iI1I1IIi ) )
 elif ( rloc . is_exact_match ( IiioOoo . address ) == False or
 port != IiioOoo . translated_port ) :
  lprint ( "Changed RLE {} from {} for gleaned EID {}" . format ( I1I111iIiI , OO0o0OO0 , iIIi1iI1I1IIi ) )
  if 55 - 55: ooOoO0o . I1IiiI + OoOoOO00 % OoooooooOO % i11iIiiIii / I1Ii111
  if 99 - 99: OoO0O00 - oO0o + iII111i . o0oOOo0O0Ooo + I1IiiI
  if 65 - 65: O0 / OoOoOO00
  if 77 - 77: OoO0O00
  if 17 - 17: i1IIi
 IiioOoo . store_translated_rloc ( rloc , port )
 if 35 - 35: OoOoOO00
 if 61 - 61: I1Ii111
 if 78 - 78: I1Ii111 * Ii1I % Ii1I + I1IiiI
 if 83 - 83: iIii1I11I1II1 + O0 / IiII . iIii1I11I1II1
 if 74 - 74: Oo0Ooo
 if ( igmp ) :
  I1IIiiiI1I1iiIii = seid . print_address ( )
  if ( lisp_gleaned_groups . has_key ( I1IIiiiI1I1iiIii ) == False ) :
   lisp_gleaned_groups [ I1IIiiiI1I1iiIii ] = { }
   if 60 - 60: OoooooooOO
  lisp_gleaned_groups [ I1IIiiiI1I1iiIii ] [ oo0oo ] = lisp_get_timestamp ( )
  if 16 - 16: iIii1I11I1II1 - OoOoOO00 / I1ii11iIi11i % O0 % o0oOOo0O0Ooo
  if 99 - 99: ooOoO0o . o0oOOo0O0Ooo - O0 * I1Ii111 . i11iIiiIii / iIii1I11I1II1
  if 40 - 40: iIii1I11I1II1 + oO0o / iIii1I11I1II1 - i1IIi % OoO0O00
  if 22 - 22: OOooOOo
  if 65 - 65: i1IIi - oO0o . I1Ii111 . ooOoO0o % I1ii11iIi11i % I1ii11iIi11i
  if 1 - 1: I1Ii111 + I1Ii111
  if 96 - 96: iII111i + OoOoOO00 - o0oOOo0O0Ooo + Ii1I
  if 6 - 6: O0 . I11i
def lisp_remove_gleaned_multicast ( seid , geid ) :
 if 22 - 22: Oo0Ooo . O0 / i1IIi - OoOoOO00
 if 41 - 41: II111iiii - I1ii11iIi11i - I1Ii111
 if 82 - 82: I1IiiI * I1IiiI / iIii1I11I1II1
 if 14 - 14: I11i + Ii1I - OOooOOo % Ii1I / Ii1I
 o0Oo0 = lisp_map_cache_lookup ( seid , geid )
 if ( o0Oo0 == None ) : return
 if 86 - 86: I1Ii111 - i11iIiiIii + Ii1I + I11i
 iI1Ii11 = o0Oo0 . rloc_set [ 0 ] . rle
 if ( iI1Ii11 == None ) : return
 if 96 - 96: Ii1I
 IIiiI11iI = seid . print_address_no_iid ( )
 ooOoOO0o = False
 for IiioOoo in iI1Ii11 . rle_nodes :
  if ( IiioOoo . rloc_name == IIiiI11iI ) :
   ooOoOO0o = True
   break
   if 28 - 28: i1IIi . oO0o . IiII + Oo0Ooo . Oo0Ooo . i1IIi
   if 34 - 34: Oo0Ooo + IiII / i1IIi
 if ( ooOoOO0o == False ) : return
 if 33 - 33: i1IIi
 if 26 - 26: ooOoO0o - Oo0Ooo * II111iiii - Oo0Ooo
 if 15 - 15: OoO0O00 - oO0o . OoOoOO00 / O0 * oO0o
 if 45 - 45: O0
 iI1Ii11 . rle_nodes . remove ( IiioOoo )
 iI1Ii11 . build_forwarding_list ( )
 if 89 - 89: IiII - IiII % o0oOOo0O0Ooo * Oo0Ooo % ooOoO0o
 oo0oo = geid . print_address ( )
 I1IIiiiI1I1iiIii = seid . print_address ( )
 OO0o0OO0 = green ( "{}" . format ( I1IIiiiI1I1iiIii ) , False )
 iIIi1iI1I1IIi = green ( "(*, {})" . format ( oo0oo ) , False )
 lprint ( "Gleaned EID {} RLE removed for {}" . format ( iIIi1iI1I1IIi , OO0o0OO0 ) )
 if 4 - 4: OoO0O00 % II111iiii / I11i
 if 95 - 95: I1Ii111 - I1Ii111 - iII111i + IiII . OoO0O00
 if 5 - 5: i11iIiiIii - O0 % ooOoO0o
 if 55 - 55: II111iiii
 if ( lisp_gleaned_groups . has_key ( I1IIiiiI1I1iiIii ) ) :
  if ( lisp_gleaned_groups [ I1IIiiiI1I1iiIii ] . has_key ( oo0oo ) ) :
   lisp_gleaned_groups [ I1IIiiiI1I1iiIii ] . pop ( oo0oo )
   if 7 - 7: I1Ii111 % o0oOOo0O0Ooo . oO0o . ooOoO0o % i1IIi / I1IiiI
   if 88 - 88: i11iIiiIii / oO0o - i1IIi / I1IiiI
   if 57 - 57: oO0o + O0 * I11i
   if 87 - 87: o0oOOo0O0Ooo % Oo0Ooo * I1ii11iIi11i / OoooooooOO / o0oOOo0O0Ooo
   if 78 - 78: Ii1I
   if 5 - 5: i1IIi * ooOoO0o / OoOoOO00 % i11iIiiIii
 if ( iI1Ii11 . rle_nodes == [ ] ) :
  o0Oo0 . delete_cache ( )
  lprint ( "Gleaned EID {} remove, no more RLEs" . format ( iIIi1iI1I1IIi ) )
  if 57 - 57: IiII
  if 89 - 89: I1ii11iIi11i - I1Ii111 + o0oOOo0O0Ooo
  if 62 - 62: I1ii11iIi11i + OoooooooOO * OOooOOo
  if 49 - 49: i1IIi - I11i * II111iiii
  if 4 - 4: o0oOOo0O0Ooo + o0oOOo0O0Ooo
  if 57 - 57: I1IiiI * OOooOOo . i11iIiiIii * oO0o - OoOoOO00
  if 35 - 35: O0
  if 65 - 65: Oo0Ooo
def lisp_change_gleaned_multicast ( seid , rloc , port ) :
 I1IIiiiI1I1iiIii = seid . print_address ( )
 if ( lisp_gleaned_groups . has_key ( I1IIiiiI1I1iiIii ) == False ) : return
 if 100 - 100: I1Ii111 . o0oOOo0O0Ooo * OoooooooOO . o0oOOo0O0Ooo
 for OOo0oOOO0 in lisp_gleaned_groups [ I1IIiiiI1I1iiIii ] :
  lisp_geid . store_address ( OOo0oOOO0 )
  lisp_build_gleaned_multicast ( seid , lisp_geid , rloc , port , False )
  if 90 - 90: i11iIiiIii . I1IiiI + ooOoO0o * OoooooooOO * OoooooooOO + oO0o
  if 77 - 77: OOooOOo * OoOoOO00
  if 75 - 75: Oo0Ooo * Oo0Ooo - IiII - OoOoOO00 / i11iIiiIii + I1Ii111
  if 57 - 57: i11iIiiIii / oO0o
  if 37 - 37: o0oOOo0O0Ooo + OoOoOO00 - i1IIi . Oo0Ooo
  if 3 - 3: ooOoO0o % OoooooooOO / I1Ii111 + oO0o - O0
  if 72 - 72: oO0o * OoO0O00
  if 89 - 89: OoooooooOO . OOooOOo
  if 96 - 96: o0oOOo0O0Ooo + OoOoOO00 / i11iIiiIii - o0oOOo0O0Ooo * i11iIiiIii + OOooOOo
  if 16 - 16: IiII / I1Ii111 . II111iiii * I11i
  if 33 - 33: I1ii11iIi11i / Oo0Ooo % i11iIiiIii
  if 37 - 37: Oo0Ooo - I1Ii111 - IiII / oO0o % I1IiiI / I1Ii111
  if 80 - 80: iII111i - oO0o % i1IIi * iIii1I11I1II1 . oO0o
  if 86 - 86: Ii1I
  if 36 - 36: i11iIiiIii % i11iIiiIii
  if 91 - 91: Oo0Ooo + I1Ii111 % iII111i
  if 7 - 7: I1Ii111 + II111iiii
  if 63 - 63: OoO0O00 - o0oOOo0O0Ooo / iII111i % II111iiii * IiII
  if 71 - 71: IiII
  if 34 - 34: II111iiii
  if 7 - 7: IiII / I1ii11iIi11i
  if 88 - 88: iIii1I11I1II1 / o0oOOo0O0Ooo
  if 68 - 68: OoooooooOO % Ii1I + ooOoO0o / oO0o
  if 60 - 60: i11iIiiIii / O0 / I1IiiI
  if 99 - 99: I1IiiI / oO0o . OoO0O00 / ooOoO0o + IiII
  if 3 - 3: II111iiii . OOooOOo * i11iIiiIii / I11i
  if 16 - 16: I1ii11iIi11i - ooOoO0o + OoO0O00 . I11i / O0
  if 56 - 56: I1IiiI + Oo0Ooo * II111iiii + iIii1I11I1II1
  if 56 - 56: o0oOOo0O0Ooo * I1IiiI - I11i * I1Ii111 - I11i
  if 92 - 92: oO0o % iIii1I11I1II1 * o0oOOo0O0Ooo * OoooooooOO - iIii1I11I1II1
  if 51 - 51: Ii1I - OoO0O00 + i1IIi
  if 11 - 11: II111iiii - iII111i + oO0o % Oo0Ooo
  if 56 - 56: IiII
  if 72 - 72: Oo0Ooo
  if 37 - 37: i11iIiiIii * I1IiiI % ooOoO0o
  if 23 - 23: OoO0O00 + o0oOOo0O0Ooo * I1IiiI
  if 76 - 76: i1IIi . OOooOOo
  if 78 - 78: OoooooooOO % OoOoOO00 * oO0o . I1ii11iIi11i
  if 79 - 79: OoooooooOO
  if 6 - 6: i11iIiiIii / II111iiii + II111iiii + I1ii11iIi11i % IiII - I1ii11iIi11i
  if 92 - 92: IiII
  if 49 - 49: O0 . OoOoOO00
  if 7 - 7: i1IIi + II111iiii
  if 96 - 96: I1Ii111 / OoO0O00
  if 27 - 27: Ii1I
  if 90 - 90: I1ii11iIi11i
  if 43 - 43: OoO0O00 . I1IiiI . oO0o + Ii1I
  if 7 - 7: iII111i / Oo0Ooo - OoO0O00 + I1Ii111 * II111iiii * ooOoO0o
  if 80 - 80: oO0o - i1IIi / I11i . II111iiii % O0 % I11i
  if 70 - 70: iIii1I11I1II1 * i1IIi * OOooOOo - Oo0Ooo % i1IIi
  if 60 - 60: o0oOOo0O0Ooo . OOooOOo % II111iiii - I1ii11iIi11i
  if 4 - 4: OOooOOo % ooOoO0o
  if 39 - 39: Ii1I
  if 67 - 67: iIii1I11I1II1 - OOooOOo
  if 47 - 47: OOooOOo - OOooOOo * I1Ii111
  if 24 - 24: I1ii11iIi11i
  if 37 - 37: II111iiii - iIii1I11I1II1 / o0oOOo0O0Ooo . O0 + II111iiii
  if 9 - 9: o0oOOo0O0Ooo
  if 47 - 47: Ii1I * I1Ii111 / II111iiii
  if 73 - 73: ooOoO0o
  if 53 - 53: IiII . Oo0Ooo
  if 54 - 54: i11iIiiIii % ooOoO0o % I1Ii111 + o0oOOo0O0Ooo
  if 2 - 2: IiII
  if 25 - 25: OoOoOO00 . OoO0O00 * o0oOOo0O0Ooo . OoooooooOO - Oo0Ooo + I1IiiI
  if 82 - 82: OoO0O00 - Ii1I * I11i * o0oOOo0O0Ooo
  if 17 - 17: OoooooooOO + I1Ii111
  if 91 - 91: iIii1I11I1II1 % i11iIiiIii - o0oOOo0O0Ooo
  if 98 - 98: o0oOOo0O0Ooo % II111iiii * IiII - i11iIiiIii * oO0o
  if 15 - 15: O0 - II111iiii - Oo0Ooo . I1ii11iIi11i % OoO0O00
  if 63 - 63: o0oOOo0O0Ooo / OoOoOO00 % I1ii11iIi11i % I11i
  if 58 - 58: O0 + iII111i
  if 66 - 66: i1IIi . O0 . i1IIi - iIii1I11I1II1 - ooOoO0o % I1ii11iIi11i
  if 96 - 96: i1IIi + oO0o - OoOoOO00 - OoOoOO00
  if 13 - 13: I11i
  if 52 - 52: iII111i . OoOoOO00 * iIii1I11I1II1 . iII111i * IiII
  if 52 - 52: iII111i + iII111i
  if 35 - 35: I1Ii111 * oO0o + Ii1I / I1IiiI + O0 - I11i
  if 42 - 42: o0oOOo0O0Ooo
  if 89 - 89: o0oOOo0O0Ooo
  if 99 - 99: I1ii11iIi11i + Oo0Ooo
  if 20 - 20: OoO0O00 / iII111i
  if 62 - 62: i1IIi % iIii1I11I1II1 + OoOoOO00 - I1IiiI . I1ii11iIi11i
  if 92 - 92: i11iIiiIii * o0oOOo0O0Ooo . Oo0Ooo
  if 15 - 15: o0oOOo0O0Ooo * IiII . iII111i % O0 . iIii1I11I1II1
  if 34 - 34: OOooOOo / iII111i * iIii1I11I1II1 + i11iIiiIii
  if 37 - 37: I11i + o0oOOo0O0Ooo . o0oOOo0O0Ooo
  if 8 - 8: Oo0Ooo * Ii1I % I11i - OoooooooOO
  if 11 - 11: OoO0O00 - oO0o
  if 50 - 50: II111iiii * IiII
  if 26 - 26: OoO0O00 . II111iiii
  if 19 - 19: iII111i / i11iIiiIii
  if 31 - 31: I1Ii111 / I1Ii111 % IiII
igmp_types = { 17 : "IGMP-query" , 18 : "IGMPv1-report" , 19 : "DVMRP" ,
 20 : "PIMv1" , 22 : "IGMPv2-report" , 23 : "IGMPv2-leave" ,
 30 : "mtrace-response" , 31 : "mtrace-request" , 34 : "IGMPv3-report" }
if 68 - 68: O0 / OOooOOo % OoOoOO00
lisp_igmp_record_types = { 1 : "include-mode" , 2 : "exclude-mode" ,
 3 : "change-to-include" , 4 : "change-to-exclude" , 5 : "allow-new-source" ,
 6 : "block-old-sources" }
if 68 - 68: OoooooooOO - IiII + I1IiiI * IiII / I11i - OoO0O00
def lisp_process_igmp_packet ( packet ) :
 iI1Iii1i1 = lisp_address ( LISP_AFI_IPV4 , "" , 32 , 0 )
 iI1Iii1i1 . address = socket . ntohl ( struct . unpack ( "I" , packet [ 12 : 16 ] ) [ 0 ] )
 iI1Iii1i1 = bold ( "from {}" . format ( iI1Iii1i1 . print_address_no_iid ( ) ) , False )
 if 69 - 69: oO0o / II111iiii
 I1I111iIiI = bold ( "Receive" , False )
 lprint ( "{} {}-byte {}, IGMP packet: {}" . format ( I1I111iIiI , len ( packet ) , iI1Iii1i1 ,
 lisp_format_packet ( packet ) ) )
 if 56 - 56: i1IIi + II111iiii + Ii1I . OoooooooOO
 if 26 - 26: OoooooooOO % Ii1I % I11i * oO0o - i1IIi - i1IIi
 if 76 - 76: i11iIiiIii + OoO0O00 - iII111i . OoOoOO00 * Oo0Ooo
 if 15 - 15: II111iiii + iIii1I11I1II1
 oOOOOO0O0 = ( struct . unpack ( "B" , packet [ 0 ] ) [ 0 ] & 0x0f ) * 4
 if 2 - 2: O0 / I11i . OOooOOo % o0oOOo0O0Ooo + Oo0Ooo
 if 13 - 13: iIii1I11I1II1 - I11i
 if 57 - 57: I1IiiI - i11iIiiIii - I1ii11iIi11i
 if 49 - 49: i1IIi . O0 % Ii1I * i1IIi
 i1I1i1IiI = packet [ oOOOOO0O0 : : ]
 IIi1IiI = struct . unpack ( "B" , i1I1i1IiI [ 0 ] ) [ 0 ]
 if 27 - 27: Ii1I . iII111i . I11i . I11i / i1IIi - Ii1I
 if 51 - 51: O0 * I1IiiI - O0
 if 81 - 81: I1ii11iIi11i / iIii1I11I1II1
 if 83 - 83: I1IiiI % I1ii11iIi11i - I1Ii111 / I11i / OoOoOO00
 if 36 - 36: I1Ii111 % IiII
 OOo0oOOO0 = lisp_address ( LISP_AFI_IPV4 , "" , 32 , 0 )
 OOo0oOOO0 . address = socket . ntohl ( struct . unpack ( "II" , i1I1i1IiI [ : 8 ] ) [ 1 ] )
 oo0oo = OOo0oOOO0 . print_address_no_iid ( )
 if 35 - 35: I1IiiI * I1Ii111 % iIii1I11I1II1
 if ( IIi1IiI == 17 ) :
  lprint ( "IGMP Query for group {}" . format ( oo0oo ) )
  return ( True )
  if 15 - 15: II111iiii % OoO0O00 % Oo0Ooo + I1Ii111
  if 54 - 54: I1Ii111 + OOooOOo
 iiiI1i1iiIi = ( IIi1IiI in ( 0x12 , 0x16 , 0x17 , 0x22 ) )
 if ( iiiI1i1iiIi == False ) :
  Ii1iI = "{} ({})" . format ( IIi1IiI , igmp_types [ IIi1IiI ] ) if igmp_types . has_key ( IIi1IiI ) else IIi1IiI
  if 72 - 72: I1ii11iIi11i * i11iIiiIii . I1IiiI * Oo0Ooo + II111iiii
  lprint ( "IGMP type {} not supported" . format ( Ii1iI ) )
  return ( [ ] )
  if 85 - 85: Oo0Ooo
  if 41 - 41: OoooooooOO % I1Ii111
 if ( len ( i1I1i1IiI ) < 8 ) :
  lprint ( "IGMP message too small" )
  return ( [ ] )
  if 42 - 42: iIii1I11I1II1 * OoooooooOO * IiII . OoooooooOO + o0oOOo0O0Ooo * OoooooooOO
  if 56 - 56: Ii1I + IiII * I1IiiI % OoOoOO00
  if 99 - 99: I1ii11iIi11i * OoO0O00 * oO0o - ooOoO0o
  if 28 - 28: OoO0O00 % OoO0O00 / Ii1I / Oo0Ooo
  if 93 - 93: O0 + oO0o . OOooOOo * IiII
 if ( IIi1IiI == 0x17 ) :
  lprint ( "IGMPv2 leave (*, {})" . format ( bold ( oo0oo , False ) ) )
  return ( [ [ None , oo0oo , False ] ] )
  if 12 - 12: iIii1I11I1II1
 if ( IIi1IiI in ( 0x12 , 0x16 ) ) :
  lprint ( "IGMPv{} join (*, {})" . format ( 1 if ( IIi1IiI == 0x12 ) else 2 , bold ( oo0oo , False ) ) )
  if 64 - 64: OoOoOO00 + iII111i % I1Ii111 - OOooOOo + O0
  if 83 - 83: I1Ii111 + I1Ii111
  if 43 - 43: oO0o * i1IIi * Ii1I . iIii1I11I1II1 % o0oOOo0O0Ooo
  if 97 - 97: I1IiiI . i1IIi * OoOoOO00 / OOooOOo
  if 50 - 50: II111iiii . OoO0O00
  if ( oo0oo . find ( "224.0.0." ) != - 1 ) :
   lprint ( "Suppress registration for link-local groups" )
  else :
   return ( [ [ None , oo0oo , True ] ] )
   if 60 - 60: I11i . iIii1I11I1II1
   if 41 - 41: II111iiii / I1IiiI
   if 2 - 2: IiII / OoOoOO00 + I11i
   if 3 - 3: OoooooooOO + Oo0Ooo + OOooOOo
   if 20 - 20: Ii1I - oO0o - OoO0O00 + I1ii11iIi11i % OoO0O00 . i1IIi
  return ( [ ] )
  if 2 - 2: ooOoO0o * IiII . Ii1I
  if 69 - 69: IiII % i1IIi
  if 17 - 17: o0oOOo0O0Ooo . OoO0O00 * ooOoO0o * II111iiii - OoooooooOO % iII111i
  if 47 - 47: I1IiiI * iIii1I11I1II1 - I11i - o0oOOo0O0Ooo
  if 47 - 47: IiII + OoO0O00 % ooOoO0o - iII111i - IiII - oO0o
 O000oOooO0oo = OOo0oOOO0 . address
 i1I1i1IiI = i1I1i1IiI [ 8 : : ]
 if 63 - 63: OoooooooOO / I1Ii111
 O0Oi1I = "BBHI"
 OOOo0oo0o0oo = struct . calcsize ( O0Oi1I )
 oooOOoo00 = "I"
 Ii1ii1Ii1IIiII = struct . calcsize ( oooOOoo00 )
 iI1Iii1i1 = lisp_address ( LISP_AFI_IPV4 , "" , 32 , 0 )
 if 31 - 31: IiII % O0
 if 46 - 46: iIii1I11I1II1 - OoooooooOO . oO0o % iIii1I11I1II1 / i1IIi + Ii1I
 if 5 - 5: I1ii11iIi11i % II111iiii
 if 17 - 17: i11iIiiIii - II111iiii / O0 % OoO0O00 . Oo0Ooo + IiII
 o0O0OoO000 = [ ]
 for iIi1I1 in range ( O000oOooO0oo ) :
  if ( len ( i1I1i1IiI ) < OOOo0oo0o0oo ) : return
  OO0OOooOO0o0O , oOo0oo , i1Ii11iII , ii1i1II11II1i = struct . unpack ( O0Oi1I ,
 i1I1i1IiI [ : OOOo0oo0o0oo ] )
  if 77 - 77: i11iIiiIii . II111iiii . OoOoOO00 + OoO0O00 * II111iiii
  i1I1i1IiI = i1I1i1IiI [ OOOo0oo0o0oo : : ]
  if 23 - 23: iIii1I11I1II1 % OoO0O00
  if ( lisp_igmp_record_types . has_key ( OO0OOooOO0o0O ) == False ) :
   lprint ( "Invalid record type {}" . format ( OO0OOooOO0o0O ) )
   continue
   if 14 - 14: I1ii11iIi11i
   if 56 - 56: I1ii11iIi11i * I1Ii111 - I11i - OoooooooOO * Ii1I % O0
  ooOo0 = lisp_igmp_record_types [ OO0OOooOO0o0O ]
  i1Ii11iII = socket . ntohs ( i1Ii11iII )
  OOo0oOOO0 . address = socket . ntohl ( ii1i1II11II1i )
  oo0oo = OOo0oOOO0 . print_address_no_iid ( )
  if 14 - 14: O0
  lprint ( "Record type: {}, group: {}, source-count: {}" . format ( ooOo0 , oo0oo , i1Ii11iII ) )
  if 59 - 59: I11i % II111iiii . iIii1I11I1II1 * oO0o % Ii1I
  if 79 - 79: OoooooooOO . II111iiii
  if 55 - 55: II111iiii
  if 2 - 2: I1ii11iIi11i * i1IIi + OOooOOo / OoO0O00 % OoOoOO00 / O0
  if 47 - 47: OoooooooOO - i11iIiiIii - IiII * O0 * iII111i * Ii1I
  if 36 - 36: I1Ii111
  if 85 - 85: Oo0Ooo % OOooOOo
  IiII11 = False
  if ( OO0OOooOO0o0O in ( 1 , 5 ) ) : IiII11 = True
  if ( OO0OOooOO0o0O in ( 2 , 4 ) and i1Ii11iII == 0 ) : IiII11 = True
  OoOO00o = "join" if ( IiII11 ) else "leave"
  if 41 - 41: I11i % o0oOOo0O0Ooo
  if 75 - 75: Ii1I / O0 . ooOoO0o . II111iiii . i11iIiiIii % I1Ii111
  if 96 - 96: I1Ii111 % OoooooooOO + O0 % o0oOOo0O0Ooo + OOooOOo - iIii1I11I1II1
  if 29 - 29: II111iiii - I1Ii111 + o0oOOo0O0Ooo
  if ( oo0oo . find ( "224.0.0." ) != - 1 ) :
   lprint ( "Suppress registration for link-local groups" )
   continue
   if 23 - 23: OOooOOo * OOooOOo * I1Ii111 . II111iiii
   if 34 - 34: IiII * Oo0Ooo % II111iiii . Ii1I . I1ii11iIi11i
   if 28 - 28: iII111i
   if 74 - 74: Ii1I + I1IiiI * iII111i / i11iIiiIii - ooOoO0o * OoooooooOO
   if 98 - 98: I1IiiI
   if 85 - 85: OoooooooOO * i1IIi * O0 * OoooooooOO . IiII
   if 22 - 22: ooOoO0o
   if 44 - 44: I1ii11iIi11i + IiII + IiII * I1ii11iIi11i - OoooooooOO / I1Ii111
  if ( i1Ii11iII == 0 ) :
   o0O0OoO000 . append ( [ None , oo0oo , IiII11 ] )
   lprint ( "IGMPv3 {} (*, {})" . format ( bold ( OoOO00o , False ) ,
 bold ( oo0oo , False ) ) )
   if 3 - 3: I1ii11iIi11i + o0oOOo0O0Ooo * I11i / Oo0Ooo
   if 31 - 31: i11iIiiIii % OoO0O00 - oO0o / o0oOOo0O0Ooo % O0
   if 53 - 53: iIii1I11I1II1 * I1ii11iIi11i
   if 46 - 46: OOooOOo % OoOoOO00 * iII111i
   if 55 - 55: I1IiiI * iIii1I11I1II1 . OoOoOO00
  for I1iII in range ( i1Ii11iII ) :
   if ( len ( i1I1i1IiI ) < Ii1ii1Ii1IIiII ) : return
   ii1i1II11II1i = struct . unpack ( oooOOoo00 , i1I1i1IiI [ : Ii1ii1Ii1IIiII ] ) [ 0 ]
   iI1Iii1i1 . address = socket . ntohl ( ii1i1II11II1i )
   Oo00OO0O = iI1Iii1i1 . print_address_no_iid ( )
   o0O0OoO000 . append ( [ Oo00OO0O , oo0oo , IiII11 ] )
   lprint ( "{} ({}, {})" . format ( OoOO00o ,
 green ( Oo00OO0O , False ) , bold ( oo0oo , False ) ) )
   i1I1i1IiI = i1I1i1IiI [ Ii1ii1Ii1IIiII : : ]
   if 78 - 78: oO0o . I1IiiI
   if 36 - 36: o0oOOo0O0Ooo + iIii1I11I1II1
   if 54 - 54: ooOoO0o - I1Ii111 + I11i * Oo0Ooo - oO0o + I1ii11iIi11i
   if 34 - 34: O0 % iIii1I11I1II1 - OoOoOO00
   if 16 - 16: I11i . I1IiiI / IiII + OoOoOO00 . OoooooooOO
   if 91 - 91: ooOoO0o * OOooOOo - iII111i . I1IiiI * oO0o . IiII
   if 46 - 46: O0 / I1Ii111 . OOooOOo * OOooOOo % OoOoOO00 . O0
   if 31 - 31: O0 % OoO0O00 % O0 + iII111i - iIii1I11I1II1
 return ( o0O0OoO000 )
 if 71 - 71: I1IiiI / Ii1I + IiII * OoooooooOO
 if 39 - 39: OoO0O00
 if 60 - 60: iII111i . iII111i - ooOoO0o / i1IIi
 if 68 - 68: oO0o + I11i + Oo0Ooo / OOooOOo . II111iiii - iIii1I11I1II1
 if 81 - 81: I1ii11iIi11i
 if 39 - 39: II111iiii
 if 60 - 60: OoOoOO00 % Oo0Ooo
 if 19 - 19: iIii1I11I1II1 + I1IiiI + O0 * Ii1I
lisp_geid = lisp_address ( LISP_AFI_IPV4 , "" , 32 , 0 )
if 15 - 15: IiII
def lisp_glean_map_cache ( seid , rloc , encap_port , igmp ) :
 if 6 - 6: I1ii11iIi11i
 if 27 - 27: iII111i . iII111i . i1IIi
 if 10 - 10: iII111i
 if 27 - 27: OoooooooOO . i1IIi + OoO0O00 + IiII % ooOoO0o
 if 88 - 88: OoooooooOO
 if 22 - 22: OoOoOO00 / i1IIi - i1IIi - Oo0Ooo - O0 / IiII
 IIiIi11 = True
 o0Oo0 = lisp_map_cache . lookup_cache ( seid , True )
 if ( o0Oo0 and len ( o0Oo0 . rloc_set ) != 0 ) :
  o0Oo0 . last_refresh_time = lisp_get_timestamp ( )
  if 18 - 18: I1IiiI / o0oOOo0O0Ooo % I1Ii111 * I1Ii111
  Oo0OO = o0Oo0 . rloc_set [ 0 ]
  O0oOOooO = Oo0OO . rloc
  Oo0Oooii11iiI = Oo0OO . translated_port
  IIiIi11 = ( O0oOOooO . is_exact_match ( rloc ) == False or
 Oo0Oooii11iiI != encap_port )
  if 12 - 12: iIii1I11I1II1
  if ( IIiIi11 ) :
   iIIi1iI1I1IIi = green ( seid . print_address ( ) , False )
   I1I111iIiI = red ( rloc . print_address_no_iid ( ) + ":" + str ( encap_port ) , False )
   lprint ( "Change gleaned EID {} to RLOC {}" . format ( iIIi1iI1I1IIi , I1I111iIiI ) )
   Oo0OO . delete_from_rloc_probe_list ( o0Oo0 . eid , o0Oo0 . group )
   lisp_change_gleaned_multicast ( seid , rloc , encap_port )
   if 97 - 97: iII111i * I1IiiI - II111iiii
 else :
  o0Oo0 = lisp_mapping ( "" , "" , [ ] )
  o0Oo0 . eid . copy_address ( seid )
  o0Oo0 . mapping_source . copy_address ( rloc )
  o0Oo0 . map_cache_ttl = LISP_GLEAN_TTL
  o0Oo0 . gleaned = True
  iIIi1iI1I1IIi = green ( seid . print_address ( ) , False )
  I1I111iIiI = red ( rloc . print_address_no_iid ( ) + ":" + str ( encap_port ) , False )
  lprint ( "Add gleaned EID {} to map-cache with RLOC {}" . format ( iIIi1iI1I1IIi , I1I111iIiI ) )
  o0Oo0 . add_cache ( )
  if 56 - 56: oO0o + i11iIiiIii / ooOoO0o - Oo0Ooo
  if 11 - 11: OoO0O00 - i1IIi / OoO0O00
  if 91 - 91: OoO0O00 % iII111i + OoO0O00 % i11iIiiIii + ooOoO0o * OoOoOO00
  if 89 - 89: O0 . OoooooooOO + Ii1I % iIii1I11I1II1 / I11i
  if 74 - 74: i11iIiiIii . OoOoOO00 % I1Ii111
 if ( IIiIi11 ) :
  oOO0O = lisp_rloc ( )
  oOO0O . store_translated_rloc ( rloc , encap_port )
  oOO0O . add_to_rloc_probe_list ( o0Oo0 . eid , o0Oo0 . group )
  oOO0O . priority = 253
  oOO0O . mpriority = 255
  OoO0oOOooOO = [ oOO0O ]
  o0Oo0 . rloc_set = OoO0oOOooOO
  o0Oo0 . build_best_rloc_set ( )
  if 37 - 37: I11i % IiII - OoOoOO00 / I1Ii111 % iII111i
  if 65 - 65: OoooooooOO / OoO0O00 - Ii1I % IiII % OoOoOO00
  if 61 - 61: iII111i * I1IiiI + i11iIiiIii % Oo0Ooo . Oo0Ooo * IiII
  if 39 - 39: O0 . oO0o * iIii1I11I1II1 / OOooOOo
  if 60 - 60: iII111i - I11i
 if ( igmp == None ) : return
 if 12 - 12: o0oOOo0O0Ooo % i1IIi
 if 29 - 29: OOooOOo . OoooooooOO . iII111i % i1IIi + i11iIiiIii
 if 9 - 9: IiII
 if 29 - 29: I11i * II111iiii / I1ii11iIi11i
 if 49 - 49: iIii1I11I1II1 + I11i + IiII . I1IiiI
 lisp_geid . instance_id = seid . instance_id
 if 32 - 32: I1Ii111 - o0oOOo0O0Ooo / i1IIi
 if 12 - 12: II111iiii % Oo0Ooo / Oo0Ooo . i1IIi % Ii1I
 if 21 - 21: II111iiii - o0oOOo0O0Ooo * OoO0O00 . OOooOOo
 if 65 - 65: o0oOOo0O0Ooo + I1IiiI
 if 21 - 21: I1Ii111
 iIII1I = lisp_process_igmp_packet ( igmp )
 if ( type ( iIII1I ) == bool ) : return
 if 74 - 74: iII111i
 for iI1Iii1i1 , OOo0oOOO0 , IiII11 in iIII1I :
  if ( iI1Iii1i1 != None ) : continue
  if 51 - 51: O0 . II111iiii - OoooooooOO + ooOoO0o - o0oOOo0O0Ooo
  if 86 - 86: OOooOOo % i11iIiiIii / OoOoOO00
  if 72 - 72: I1IiiI . oO0o
  if 76 - 76: Ii1I - Oo0Ooo * II111iiii
  lisp_geid . store_address ( OOo0oOOO0 )
  IiO0ooOoO , oOo0oo , IIIi1i1iIIIi = lisp_allow_gleaning ( seid , lisp_geid , rloc )
  if ( IiO0ooOoO == False ) : continue
  if 17 - 17: I1Ii111 * O0
  if ( IiII11 ) :
   lisp_build_gleaned_multicast ( seid , lisp_geid , rloc , encap_port ,
 True )
  else :
   lisp_remove_gleaned_multicast ( seid , lisp_geid )
   if 8 - 8: i11iIiiIii / OoO0O00 / OOooOOo
   if 26 - 26: I1ii11iIi11i . Ii1I - iIii1I11I1II1 . Ii1I / Ii1I % I11i
   if 56 - 56: OOooOOo . I11i + O0 * oO0o - i11iIiiIii / i11iIiiIii
   if 73 - 73: I1ii11iIi11i
   if 59 - 59: iII111i % iIii1I11I1II1 * OoOoOO00
   if 41 - 41: i1IIi * IiII - i11iIiiIii / O0 + Oo0Ooo + ooOoO0o
   if 94 - 94: OoO0O00 . O0 + iIii1I11I1II1 . oO0o % oO0o
   if 7 - 7: I1ii11iIi11i * oO0o / OoOoOO00
   if 89 - 89: OoO0O00 / oO0o % I11i - I1ii11iIi11i . o0oOOo0O0Ooo
   if 46 - 46: i11iIiiIii
   if 99 - 99: i11iIiiIii / oO0o / OoOoOO00 / O0 * I1ii11iIi11i
   if 72 - 72: ooOoO0o - I1Ii111 - iIii1I11I1II1 . I1IiiI
def lisp_is_json_telemetry ( json_string ) :
 try :
  I1i1Iii1i1iI = json . loads ( json_string )
  if ( type ( I1i1Iii1i1iI ) != dict ) : return ( None )
 except :
  lprint ( "Could not decode telemetry json: {}" . format ( json_string ) )
  return ( None )
  if 77 - 77: Oo0Ooo * OoO0O00
  if 67 - 67: OoOoOO00 . I1Ii111 / I1IiiI * II111iiii
 if ( I1i1Iii1i1iI . has_key ( "type" ) == False ) : return ( None )
 if ( I1i1Iii1i1iI . has_key ( "sub-type" ) == False ) : return ( None )
 if ( I1i1Iii1i1iI [ "type" ] != "telemetry" ) : return ( None )
 if ( I1i1Iii1i1iI [ "sub-type" ] != "timestamps" ) : return ( None )
 return ( I1i1Iii1i1iI )
 if 45 - 45: I1ii11iIi11i * o0oOOo0O0Ooo . iIii1I11I1II1 * Oo0Ooo
 if 58 - 58: OOooOOo + O0
 if 19 - 19: o0oOOo0O0Ooo
 if 8 - 8: OOooOOo * OOooOOo - Ii1I * OoOoOO00 % OoO0O00 * O0
 if 70 - 70: I1IiiI
 if 17 - 17: I11i % OOooOOo - i11iIiiIii . OoooooooOO % OoO0O00 + OoO0O00
 if 24 - 24: Ii1I . OOooOOo . IiII / Oo0Ooo . Oo0Ooo . II111iiii
 if 63 - 63: ooOoO0o . I11i
 if 39 - 39: II111iiii % oO0o % I1IiiI - iIii1I11I1II1 / I1IiiI
 if 94 - 94: iII111i + oO0o
 if 43 - 43: iIii1I11I1II1 + iIii1I11I1II1
 if 8 - 8: iIii1I11I1II1
def lisp_encode_telemetry ( json_string , ii = "?" , io = "?" , ei = "?" , eo = "?" ) :
 I1i1Iii1i1iI = lisp_is_json_telemetry ( json_string )
 if ( I1i1Iii1i1iI == None ) : return ( json_string )
 if 30 - 30: OOooOOo - I1ii11iIi11i * iIii1I11I1II1 + Oo0Ooo
 if ( I1i1Iii1i1iI [ "itr-in" ] == "?" ) : I1i1Iii1i1iI [ "itr-in" ] = ii
 if ( I1i1Iii1i1iI [ "itr-out" ] == "?" ) : I1i1Iii1i1iI [ "itr-out" ] = io
 if ( I1i1Iii1i1iI [ "etr-in" ] == "?" ) : I1i1Iii1i1iI [ "etr-in" ] = ei
 if ( I1i1Iii1i1iI [ "etr-out" ] == "?" ) : I1i1Iii1i1iI [ "etr-out" ] = eo
 json_string = json . dumps ( I1i1Iii1i1iI )
 return ( json_string )
 if 25 - 25: IiII
 if 78 - 78: OoOoOO00 * iIii1I11I1II1 * ooOoO0o - OoooooooOO - IiII
 if 40 - 40: OoO0O00 . i11iIiiIii + ooOoO0o
 if 30 - 30: OOooOOo . OoO0O00 % iII111i - OoO0O00 % i11iIiiIii
 if 28 - 28: Ii1I + Oo0Ooo / iIii1I11I1II1
 if 57 - 57: o0oOOo0O0Ooo
 if 23 - 23: II111iiii
 if 88 - 88: I1IiiI / II111iiii * i11iIiiIii - oO0o - OOooOOo
 if 41 - 41: iIii1I11I1II1
 if 7 - 7: Oo0Ooo + iII111i . ooOoO0o
 if 31 - 31: iIii1I11I1II1 - OoOoOO00 - II111iiii / I1ii11iIi11i
 if 70 - 70: iIii1I11I1II1 / I1ii11iIi11i . I1Ii111 % I1ii11iIi11i
def lisp_decode_telemetry ( json_string ) :
 I1i1Iii1i1iI = lisp_is_json_telemetry ( json_string )
 if ( I1i1Iii1i1iI == None ) : return ( { } )
 return ( I1i1Iii1i1iI )
 if 40 - 40: I1Ii111 + o0oOOo0O0Ooo - I11i + OoO0O00
 if 49 - 49: i11iIiiIii % OoO0O00 - Ii1I + I1Ii111
 if 7 - 7: ooOoO0o * I1ii11iIi11i - Ii1I % i1IIi + I11i
 if 22 - 22: I1IiiI - OOooOOo - II111iiii * I1IiiI
 if 93 - 93: OOooOOo + I11i
 if 93 - 93: I1IiiI . I1ii11iIi11i * iII111i
 if 25 - 25: Oo0Ooo + o0oOOo0O0Ooo + OoOoOO00
 if 76 - 76: Oo0Ooo * Oo0Ooo + o0oOOo0O0Ooo % I11i + Oo0Ooo / o0oOOo0O0Ooo
 if 76 - 76: OOooOOo . ooOoO0o * iII111i . oO0o
def lisp_telemetry_configured ( ) :
 if ( lisp_json_list . has_key ( "telemetry" ) == False ) : return ( None )
 if 80 - 80: i1IIi . Ii1I
 o0Ooo = lisp_json_list [ "telemetry" ] . json_string
 if ( lisp_is_json_telemetry ( o0Ooo ) == None ) : return ( None )
 if 59 - 59: OOooOOo . I11i
 return ( o0Ooo )
 if 88 - 88: i11iIiiIii / I1ii11iIi11i . I11i % OOooOOo
 if 75 - 75: ooOoO0o - OOooOOo
 if 97 - 97: i11iIiiIii / I11i % II111iiii
 if 20 - 20: I1Ii111 + OoooooooOO . o0oOOo0O0Ooo - ooOoO0o
 if 61 - 61: i11iIiiIii + OoooooooOO
 if 7 - 7: I1IiiI * OoO0O00 * I1IiiI
 if 50 - 50: I1ii11iIi11i
def lisp_mr_or_pubsub ( action ) :
 return ( action in [ LISP_SEND_MAP_REQUEST_ACTION , LISP_SEND_PUBSUB_ACTION ] )
 if 88 - 88: IiII
 if 55 - 55: Oo0Ooo + OOooOOo + IiII
 if 55 - 55: O0 . I1Ii111 * I1ii11iIi11i * o0oOOo0O0Ooo - ooOoO0o
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
