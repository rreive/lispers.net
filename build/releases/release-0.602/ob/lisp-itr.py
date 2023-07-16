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
# lisp-itr.py
#
# This file performs LISP Ingress Tunnel Router (ITR) functionality.
#
# -----------------------------------------------------------------------------
if 64 - 64: i11iIiiIii
from future import standard_library
standard_library . install_aliases ( )
from builtins import str
from builtins import range
import lisp
import lispconfig
import socket
import select
import threading
import time
import os
from subprocess import getoutput
import struct
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
if 46 - 46: ooOoO0o * I11i - OoooooooOO
II1iII1i = [ None , None , None ]
oO0oIIII = None
Oo0oO0oo0oO00 = None
i111I = None
II1Ii1iI1i = None
iiI1iIiI = None
OOo = lisp . lisp_get_ephemeral_port ( )
Ii1IIii11 = lisp . lisp_get_ephemeral_port ( )
Oooo0000 = None
i11 = None
I11 = None
Oo0o0000o0o0 = None
if 86 - 86: OoOoOO00 % I1IiiI
if 80 - 80: OoooooooOO . I1IiiI
if 87 - 87: oO0o / ooOoO0o + I1Ii111 - ooOoO0o . ooOoO0o / II111iiii
if 11 - 11: I1IiiI % o0oOOo0O0Ooo - Oo0Ooo
if 58 - 58: i11iIiiIii % I1Ii111
if 54 - 54: OOooOOo % O0 + I1IiiI - iII111i / I11i
iIiiI1 = False
if 68 - 68: I1IiiI - i11iIiiIii - OoO0O00 / OOooOOo - OoO0O00 + i1IIi
if 48 - 48: OoooooooOO % o0oOOo0O0Ooo . I1IiiI - Ii1I % i1IIi % OoooooooOO
if 3 - 3: iII111i + O0
if 42 - 42: OOooOOo / i1IIi + i11iIiiIii - Ii1I
oo0Ooo0 = threading . Lock ( )
if 46 - 46: ooOoO0o % ooOoO0o - oO0o * o0oOOo0O0Ooo % iII111i
if 55 - 55: OoOoOO00 % i1IIi / Ii1I - oO0o - O0 / II111iiii
if 28 - 28: iIii1I11I1II1 - i1IIi
if 70 - 70: OoO0O00 . OoO0O00 - OoO0O00 / I1ii11iIi11i * OOooOOo
if 86 - 86: i11iIiiIii + Ii1I + ooOoO0o * I11i + o0oOOo0O0Ooo
if 61 - 61: OoO0O00 / i11iIiiIii
if 34 - 34: OoooooooOO + iIii1I11I1II1 + i11iIiiIii - I1ii11iIi11i + i11iIiiIii
if 65 - 65: OoOoOO00
def ii1I ( parameter ) :
 return ( lispconfig . lisp_itr_rtr_show_command ( parameter , "ITR" , [ ] ) )
 if 76 - 76: O0 / o0oOOo0O0Ooo . I1IiiI * Ii1I - OOooOOo
 if 76 - 76: i11iIiiIii / iIii1I11I1II1 . I1ii11iIi11i % OOooOOo / OoooooooOO % oO0o
 if 75 - 75: iII111i
 if 97 - 97: i11iIiiIii
 if 32 - 32: Oo0Ooo * O0 % oO0o % Ii1I . IiII
 if 61 - 61: ooOoO0o
 if 79 - 79: Oo0Ooo + I1IiiI - iII111i
def oO00O00o0OOO0 ( parameter ) :
 return ( lispconfig . lisp_show_crypto_list ( "ITR" ) )
 if 27 - 27: O0 % i1IIi * oO0o + i11iIiiIii + OoooooooOO * i1IIi
 if 80 - 80: I11i * i11iIiiIii / I1Ii111
 if 9 - 9: Ii1I + oO0o % Ii1I + i1IIi . OOooOOo
 if 31 - 31: o0oOOo0O0Ooo + I11i + I11i / II111iiii
 if 26 - 26: OoooooooOO
 if 12 - 12: OoooooooOO % OoOoOO00 / ooOoO0o % o0oOOo0O0Ooo
 if 29 - 29: OoooooooOO
 if 23 - 23: o0oOOo0O0Ooo . II111iiii
def Oo0O0OOOoo ( parameter ) :
 return ( lispconfig . lisp_itr_rtr_show_rloc_probe_command ( "ITR" ) )
 if 95 - 95: OoO0O00 % oO0o . O0
 if 15 - 15: ooOoO0o / Ii1I . Ii1I - i1IIi
 if 53 - 53: IiII + I1IiiI * oO0o
 if 61 - 61: i1IIi * OOooOOo / OoooooooOO . i11iIiiIii . OoOoOO00
 if 60 - 60: I11i / I11i
 if 46 - 46: Ii1I * OOooOOo - OoO0O00 * oO0o - I1Ii111
 if 83 - 83: OoooooooOO
 if 31 - 31: II111iiii - OOooOOo . I1Ii111 % OoOoOO00 - O0
 if 4 - 4: II111iiii / ooOoO0o . iII111i
 if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - I1ii11iIi11i / oO0o
def ii11i1 ( lisp_sockets , lisp_ephem_port ) :
 lisp . lisp_set_exception ( )
 if 29 - 29: I1ii11iIi11i % I1IiiI + ooOoO0o / o0oOOo0O0Ooo + OOooOOo * o0oOOo0O0Ooo
 if 42 - 42: Ii1I + oO0o
 if 76 - 76: I1Ii111 - OoO0O00
 if 70 - 70: ooOoO0o
 for oOO in list ( lisp . lisp_crypto_keys_by_nonce . values ( ) ) :
  for IIi1I1Ii11iI in oOO : del ( IIi1I1Ii11iI )
  if 39 - 39: IiII - II111iiii * OoO0O00 % o0oOOo0O0Ooo * II111iiii % II111iiii
 lisp . lisp_crypto_keys_by_nonce = { }
 if 59 - 59: iIii1I11I1II1 + I1IiiI - o0oOOo0O0Ooo - I1IiiI + OOooOOo / I1ii11iIi11i
 if 24 - 24: I11i . iII111i % OOooOOo + ooOoO0o % OoOoOO00
 if 4 - 4: IiII - OoO0O00 * OoOoOO00 - I11i
 if 41 - 41: OoOoOO00 . I1IiiI * oO0o % IiII
 if 86 - 86: I1IiiI + Ii1I % i11iIiiIii * oO0o . ooOoO0o * I11i
 if ( lisp . lisp_l2_overlay ) :
  i1I11i1iI = lisp . LISP_AFI_MAC
  I1ii1Ii1 = lisp . lisp_default_iid
  iii11 = lisp . lisp_address ( i1I11i1iI , "0000-0000-0000" , 0 , I1ii1Ii1 )
  iii11 . mask_len = 0
  oOOOOo0 = lisp . lisp_address ( i1I11i1iI , "ffff-ffff-ffff" , 48 , I1ii1Ii1 )
  lisp . lisp_send_map_request ( lisp_sockets , lisp_ephem_port , iii11 , oOOOOo0 , None )
  if 20 - 20: i1IIi + I1ii11iIi11i - ooOoO0o
  if 30 - 30: II111iiii - OOooOOo - i11iIiiIii % OoOoOO00 - II111iiii * Ii1I
  if 61 - 61: oO0o - I11i % OOooOOo
  if 84 - 84: oO0o * OoO0O00 / I11i - O0
  if 30 - 30: iIii1I11I1II1 / ooOoO0o - I1Ii111 - II111iiii % iII111i
 lisp . lisp_timeout_map_cache ( lisp . lisp_map_cache )
 if 49 - 49: I1IiiI % ooOoO0o . ooOoO0o . I11i * ooOoO0o
 if 97 - 97: Ii1I + o0oOOo0O0Ooo . OOooOOo + I1ii11iIi11i % iII111i
 if 95 - 95: i1IIi
 if 3 - 3: I1Ii111 - O0 / I1Ii111 % OoO0O00 / I1Ii111 . I1IiiI
 I11 = threading . Timer ( 60 , ii11i1 ,
 [ lisp_sockets , lisp_ephem_port ] )
 I11 . start ( )
 return
 if 50 - 50: IiII
 if 14 - 14: I11i % OoO0O00 * I11i
 if 16 - 16: OoOoOO00 . ooOoO0o + i11iIiiIii
 if 38 - 38: IiII * OOooOOo . o0oOOo0O0Ooo
 if 98 - 98: OoooooooOO + iII111i . OoOoOO00
 if 67 - 67: i11iIiiIii - i1IIi % I1ii11iIi11i . O0
 if 77 - 77: IiII / I1IiiI
 if 15 - 15: IiII . iIii1I11I1II1 . OoooooooOO / i11iIiiIii - Ii1I . i1IIi
def i1 ( lisp_socket ) :
 lisp . lisp_set_exception ( )
 if 53 - 53: Ii1I + iIii1I11I1II1 - I1Ii111 - Ii1I . IiII
 ooOO0O0ooOooO = lisp . lisp_get_timestamp ( )
 for oOOOo00O00oOo in lisp . lisp_db_list :
  if ( oOOOo00O00oOo . dynamic_eid_configured ( ) == False ) : continue
  if 34 - 34: O0 + OOooOOo + Oo0Ooo
  I1 = [ ]
  for i1IIIiiII1 in list ( oOOOo00O00oOo . dynamic_eids . values ( ) ) :
   OOOOoOoo0O0O0 = i1IIIiiII1 . last_packet
   if ( OOOOoOoo0O0O0 == None ) : continue
   if ( OOOOoOoo0O0O0 + i1IIIiiII1 . timeout > ooOO0O0ooOooO ) : continue
   if 85 - 85: oO0o % i11iIiiIii - iII111i * OoooooooOO / I1IiiI % I1IiiI
   if 1 - 1: OoO0O00 - oO0o . I11i . OoO0O00 / Oo0Ooo + I11i
   if 78 - 78: O0 . oO0o . II111iiii % OOooOOo
   if 49 - 49: Ii1I / OoO0O00 . II111iiii
   if 68 - 68: i11iIiiIii % I1ii11iIi11i + i11iIiiIii
   if ( lisp . lisp_program_hardware ) :
    iii = i1IIIiiII1 . dynamic_eid . print_prefix_no_iid ( )
    if ( lisp . lisp_arista_is_alive ( iii ) ) :
     lisp . lprint ( ( "Hardware indicates dynamic-EID {} " + "still active" ) . format ( lisp . green ( iii , False ) ) )
     if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % iII111i * IiII . i11iIiiIii
     continue
     if 2 - 2: I1ii11iIi11i * I11i - iIii1I11I1II1 + I1IiiI . oO0o % iII111i
     if 92 - 92: iII111i
     if 25 - 25: Oo0Ooo - I1IiiI / OoooooooOO / o0oOOo0O0Ooo
     if 12 - 12: I1IiiI * iII111i % i1IIi % iIii1I11I1II1
     if 20 - 20: OOooOOo % Ii1I / Ii1I + Ii1I
     if 45 - 45: oO0o - IiII - OoooooooOO - OoO0O00 . II111iiii / O0
   oo0o00O = i1IIIiiII1 . dynamic_eid . print_address ( )
   o00O0OoO = "learn%{}%None" . format ( oo0o00O )
   o00O0OoO = lisp . lisp_command_ipc ( o00O0OoO , "lisp-itr" )
   lisp . lisp_ipc ( o00O0OoO , lisp_socket , "lisp-etr" )
   if 16 - 16: iIii1I11I1II1
   lisp . lprint ( "Dynamic-EID {}" . format ( lisp . bold ( lisp . green ( oo0o00O , False ) + " activity timeout" ,
   # I11i + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
 False ) ) )
   I1 . append ( oo0o00O )
   if 41 - 41: Ii1I - O0 - O0
   if 68 - 68: OOooOOo % I1Ii111
   if 88 - 88: iIii1I11I1II1 - ooOoO0o + OOooOOo
   if 40 - 40: I1IiiI * Ii1I + OOooOOo % iII111i
   if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + I1Ii111 / OoOoOO00
  for oo0o00O in I1 : oOOOo00O00oOo . dynamic_eids . pop ( oo0o00O )
  if 23 - 23: O0
  if 85 - 85: Ii1I
  if 84 - 84: I1IiiI . iIii1I11I1II1 % OoooooooOO + Ii1I % OoooooooOO % OoO0O00
  if 42 - 42: OoO0O00 / I11i / o0oOOo0O0Ooo + iII111i / OoOoOO00
  if 84 - 84: ooOoO0o * II111iiii + Oo0Ooo
 threading . Timer ( lisp . LISP_DEFAULT_DYN_EID_TIMEOUT ,
 i1 , [ lisp_socket ] ) . start ( )
 return
 if 53 - 53: iII111i % II111iiii . IiII - iIii1I11I1II1 - IiII * II111iiii
 if 77 - 77: iIii1I11I1II1 * OoO0O00
 if 95 - 95: I1IiiI + i11iIiiIii
 if 6 - 6: ooOoO0o / i11iIiiIii + iII111i * oO0o
 if 80 - 80: II111iiii
 if 83 - 83: I11i . i11iIiiIii + II111iiii . o0oOOo0O0Ooo * I11i
 if 53 - 53: II111iiii
 if 31 - 31: OoO0O00
 if 80 - 80: I1Ii111 . i11iIiiIii - o0oOOo0O0Ooo
 if 25 - 25: OoO0O00
 if 62 - 62: OOooOOo + O0
 if 98 - 98: o0oOOo0O0Ooo
 if 51 - 51: Oo0Ooo - oO0o + II111iiii * Ii1I . I11i + oO0o
def OoO0o ( ) :
 if 78 - 78: oO0o % O0 % Ii1I
 if 46 - 46: OoooooooOO . i11iIiiIii
 if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
 if 87 - 87: Oo0Ooo . IiII
 if 75 - 75: ooOoO0o + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . iII111i
 if 55 - 55: OOooOOo . I1IiiI
 if 61 - 61: Oo0Ooo % IiII . Oo0Ooo
 if ( lisp . lisp_is_macos ( ) ) :
  o0oOO000oO0oo = getoutput ( "netstat -rn | egrep default | egrep UGS" )
  oOO00O = [ "lo0" ]
  for OOOoo0OO in o0oOO000oO0oo . split ( "\n" ) :
   oO0o0 = OOOoo0OO . split ( ) [ - 1 ]
   oOO00O . append ( oO0o0 )
   if 50 - 50: IiII
  return ( oOO00O )
  if 46 - 46: O0 + iII111i % I1IiiI / o0oOOo0O0Ooo . IiII * I11i
  if 93 - 93: o0oOOo0O0Ooo % i1IIi . Ii1I . i11iIiiIii
  if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
  if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
  if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
 I111iI = "Link encap"
 oOO00O = getoutput ( "ifconfig | egrep '{}'" . format ( I111iI ) )
 if ( oOO00O == "" ) :
  I111iI = ": flags="
  oOO00O = getoutput ( "ifconfig | egrep '{}'" . format ( I111iI ) )
  if 56 - 56: I1IiiI
  if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
 oOO00O = oOO00O . split ( "\n" )
 if 57 - 57: i11iIiiIii . I1ii11iIi11i - Ii1I - oO0o + OoOoOO00
 oO00oooOOoOo0 = [ ]
 for OoOOoOooooOOo in oOO00O :
  oOo0O = OoOOoOooooOOo . split ( I111iI ) [ 0 ] . replace ( " " , "" )
  oO00oooOOoOo0 . append ( oOo0O )
  if 52 - 52: i11iIiiIii / o0oOOo0O0Ooo * ooOoO0o
 return ( oO00oooOOoOo0 )
 if 22 - 22: OoOoOO00 . OOooOOo * OoOoOO00
 if 54 - 54: IiII + Ii1I % OoO0O00 + OoooooooOO - O0 - o0oOOo0O0Ooo
 if 77 - 77: OOooOOo * iIii1I11I1II1
 if 98 - 98: I1IiiI % Ii1I * OoooooooOO
 if 51 - 51: iIii1I11I1II1 . OoOoOO00 / oO0o + o0oOOo0O0Ooo
 if 33 - 33: ooOoO0o . II111iiii % iII111i + o0oOOo0O0Ooo
 if 71 - 71: Oo0Ooo % OOooOOo
def O00oO000O0O ( ) :
 global II1iII1i
 global oO0oIIII
 global Oo0oO0oo0oO00
 global i111I
 global II1Ii1iI1i
 global Oooo0000 , i11
 global iiI1iIiI
 if 18 - 18: iII111i - OOooOOo . I1Ii111 . iIii1I11I1II1
 lisp . lisp_i_am ( "itr" )
 lisp . lisp_set_exception ( )
 lisp . lisp_print_banner ( "ITR starting up" )
 if 2 - 2: OOooOOo . OoO0O00
 if 78 - 78: I11i * iIii1I11I1II1 . I1IiiI / o0oOOo0O0Ooo - OoooooooOO / I1Ii111
 if 35 - 35: I11i % OOooOOo - oO0o
 if 20 - 20: i1IIi - ooOoO0o
 lisp . lisp_get_local_interfaces ( )
 lisp . lisp_get_local_macs ( )
 if ( lisp . lisp_get_local_addresses ( ) == False ) : return ( False )
 if 30 - 30: I11i / I1IiiI
 if 35 - 35: II111iiii % OOooOOo . ooOoO0o + ooOoO0o % II111iiii % II111iiii
 if 72 - 72: II111iiii + i1IIi + o0oOOo0O0Ooo
 if 94 - 94: oO0o . i1IIi - o0oOOo0O0Ooo % O0 - OoO0O00
 II1iII1i [ 0 ] = lisp . lisp_open_send_socket ( "" , lisp . LISP_AFI_IPV4 )
 II1iII1i [ 1 ] = lisp . lisp_open_send_socket ( "" , lisp . LISP_AFI_IPV6 )
 oO0oIIII = lisp . lisp_open_listen_socket ( "" , "lisp-itr" )
 Oo0oO0oo0oO00 = lisp . lisp_open_listen_socket ( "" , "lispers.net-itr" )
 II1iII1i [ 2 ] = oO0oIIII
 ooO0O00Oo0o = "0.0.0.0" if lisp . lisp_is_raspbian ( ) else "0::0"
 i111I = lisp . lisp_open_listen_socket ( ooO0O00Oo0o ,
 str ( OOo ) )
 if 65 - 65: I1ii11iIi11i . I11i - I1Ii111 * IiII / I1Ii111 / ooOoO0o
 if 40 - 40: ooOoO0o * IiII * i11iIiiIii
 if 57 - 57: ooOoO0o
 if 29 - 29: OoOoOO00 - IiII * OoooooooOO + OoooooooOO . II111iiii + OoooooooOO
 if 74 - 74: Ii1I - IiII / iII111i * O0 - OOooOOo
 try :
  iii11 = lisp . lisp_open_send_socket ( "" , lisp . LISP_AFI_IPV4 )
  iiii1 = lisp . LISP_RLOC_PROBE_TTL
  iii11 . setsockopt ( socket . IPPROTO_IP , socket . IP_MULTICAST_TTL , iiii1 )
  iiI1iIiI = iii11
 except socket . error as ooO0oooOO0 :
  lisp . lprint ( "socket.setsockopt() failed for RLOC-probe ttl: {}" . format ( ooO0oooOO0 ) )
  if 71 - 71: I1Ii111 . II111iiii
  if 62 - 62: OoooooooOO . I11i
  if 61 - 61: OoOoOO00 - OOooOOo - i1IIi
  if 25 - 25: O0 * I11i + I1ii11iIi11i . o0oOOo0O0Ooo . o0oOOo0O0Ooo
  if 58 - 58: I1IiiI
  if 53 - 53: i1IIi
 II1Ii1iI1i = lisp . lisp_open_listen_socket ( "0.0.0.0" ,
 str ( Ii1IIii11 ) )
 if 59 - 59: o0oOOo0O0Ooo
 if 81 - 81: OoOoOO00 - OoOoOO00 . iII111i
 if 73 - 73: I11i % i11iIiiIii - I1IiiI
 if 7 - 7: O0 * i11iIiiIii * Ii1I + ooOoO0o % OoO0O00 - ooOoO0o
 Oooo0000 = socket . socket ( socket . AF_INET , socket . SOCK_RAW ,
 socket . IPPROTO_RAW )
 Oooo0000 . setsockopt ( socket . SOL_IP , socket . IP_HDRINCL , 1 )
 if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
 if ( lisp . lisp_is_raspbian ( ) == False ) :
  i11 = socket . socket ( socket . AF_INET6 , socket . SOCK_RAW ,
 socket . IPPROTO_UDP )
  if 23 - 23: i11iIiiIii
  if 30 - 30: o0oOOo0O0Ooo - i1IIi % II111iiii + I11i * iIii1I11I1II1
  if 81 - 81: IiII % i1IIi . iIii1I11I1II1
  if 4 - 4: i11iIiiIii % OoO0O00 % i1IIi / IiII
  if 6 - 6: iII111i / I1IiiI % OOooOOo - I1IiiI
  if 31 - 31: OOooOOo
  if 23 - 23: I1Ii111 . IiII
  if 92 - 92: OoOoOO00 + I1Ii111 * Ii1I % I1IiiI
 lisp . lisp_ipc_socket = oO0oIIII
 if 42 - 42: Oo0Ooo
 if 76 - 76: I1IiiI * iII111i % I1Ii111
 if 57 - 57: iIii1I11I1II1 - i1IIi / I1Ii111 - O0 * OoooooooOO % II111iiii
 if 68 - 68: OoooooooOO * I11i % OoOoOO00 - IiII
 threading . Thread ( target = I1oOoOo0O0OOOoO ) . start ( )
 if 50 - 50: ooOoO0o
 if 47 - 47: Oo0Ooo * I1ii11iIi11i + iIii1I11I1II1 / I1Ii111 / OoO0O00 - OoooooooOO
 if 33 - 33: OoOoOO00 * OOooOOo - II111iiii
 if 83 - 83: OoOoOO00 - Ii1I / I11i / I1Ii111 + oO0o - O0
 lisp . lisp_load_checkpoint ( )
 if 4 - 4: OOooOOo * OoO0O00 % i1IIi * i11iIiiIii % Oo0Ooo - oO0o
 if 67 - 67: OoOoOO00 + I1ii11iIi11i . o0oOOo0O0Ooo . II111iiii
 if 98 - 98: iII111i
 if 68 - 68: iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / II111iiii % Oo0Ooo
 lisp . lisp_load_split_pings = ( os . getenv ( "LISP_LOAD_SPLIT_PINGS" ) != None )
 if 38 - 38: ooOoO0o - OOooOOo / iII111i
 if 66 - 66: O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / Ii1I + I1ii11iIi11i
 if 86 - 86: o0oOOo0O0Ooo
 if 5 - 5: IiII * OoOoOO00
 I11 = threading . Timer ( 60 , ii11i1 ,
 [ II1iII1i , OOo ] )
 I11 . start ( )
 if 5 - 5: I1Ii111
 if 90 - 90: I1Ii111 . ooOoO0o / Ii1I - I11i
 if 40 - 40: OoooooooOO
 if 25 - 25: IiII + Ii1I / ooOoO0o . o0oOOo0O0Ooo % O0 * OoO0O00
 threading . Timer ( lisp . LISP_DEFAULT_DYN_EID_TIMEOUT ,
 i1 , [ oO0oIIII ] ) . start ( )
 return ( True )
 if 84 - 84: ooOoO0o % Ii1I + i11iIiiIii
 if 28 - 28: Oo0Ooo + OoO0O00 * OOooOOo % oO0o . I11i % O0
 if 16 - 16: I11i - iIii1I11I1II1 / I1IiiI . II111iiii + iIii1I11I1II1
 if 19 - 19: OoO0O00 - Oo0Ooo . O0
 if 60 - 60: II111iiii + Oo0Ooo
 if 9 - 9: ooOoO0o * OoooooooOO - iIii1I11I1II1 + OoOoOO00 / OoO0O00 . OoO0O00
 if 49 - 49: II111iiii
 if 25 - 25: OoooooooOO - I1IiiI . I1IiiI * oO0o
def o000oo ( ) :
 o00o0 = open ( "./lisp.config" , "r" )
 if 50 - 50: Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
 O0O0Oo00 = False
 oOoO00o = 0
 for OOOoo0OO in o00o0 :
  if ( OOOoo0OO == "lisp database-mapping {\n" ) : O0O0Oo00 = True
  if ( OOOoo0OO == "}\n" ) : O0O0Oo00 = False
  if ( O0O0Oo00 == False ) : continue
  if ( OOOoo0OO [ 0 ] == " " and OOOoo0OO . find ( "prefix {" ) != - 1 ) : oOoO00o += 1
  if 100 - 100: o0oOOo0O0Ooo + OOooOOo * o0oOOo0O0Ooo
 o00o0 . close ( )
 return ( oOoO00o )
 if 80 - 80: o0oOOo0O0Ooo * O0 - Ii1I
 if 66 - 66: i11iIiiIii - OOooOOo * Oo0Ooo
 if 76 - 76: i11iIiiIii + o0oOOo0O0Ooo / I1ii11iIi11i - OoO0O00 - Ii1I + I1ii11iIi11i
 if 51 - 51: iIii1I11I1II1 . ooOoO0o + iIii1I11I1II1
 if 95 - 95: I1IiiI
 if 46 - 46: OoOoOO00 + OoO0O00
 if 70 - 70: iII111i / iIii1I11I1II1
 if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / I1ii11iIi11i
 if 96 - 96: OoooooooOO + oO0o
 if 44 - 44: oO0o
def I1i11i ( ) :
 if 11 - 11: I1IiiI / II111iiii + o0oOOo0O0Ooo * I1ii11iIi11i - I1ii11iIi11i - I1IiiI
 if 85 - 85: I11i % oO0o / iIii1I11I1II1 . iIii1I11I1II1
 if 31 - 31: o0oOOo0O0Ooo % OoO0O00
 if 14 - 14: oO0o / oO0o % ooOoO0o
 if 56 - 56: I1IiiI . O0 + Oo0Ooo
 oOoO00o = o000oo ( )
 if 1 - 1: iII111i
 if 97 - 97: OOooOOo + iII111i + O0 + i11iIiiIii
 if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
 if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . iII111i % iII111i + i11iIiiIii
 if 72 - 72: iIii1I11I1II1 * Ii1I % ooOoO0o / OoO0O00
 if 35 - 35: ooOoO0o + i1IIi % I1ii11iIi11i % I11i + oO0o
 iiiI = os . getenv ( "LISP_ITR_WAIT_TIME" )
 iiiI = 1 if ( iiiI == None ) else int ( iiiI )
 if 29 - 29: I11i / II111iiii / ooOoO0o * OOooOOo
 if 10 - 10: I1Ii111 % IiII * IiII . I11i / Ii1I % OOooOOo
 if 49 - 49: OoO0O00 / oO0o + O0 * o0oOOo0O0Ooo
 if 28 - 28: ooOoO0o + i11iIiiIii / I11i % OoOoOO00 % Oo0Ooo - O0
 if 54 - 54: i1IIi + II111iiii
 while ( oOoO00o != len ( lisp . lisp_db_list ) ) :
  lisp . lprint ( ( "Waiting {} second(s) for {} database-mapping EID-" + "prefixes, {} processed so far ..." ) . format ( iiiI , oOoO00o ,
  # I1ii11iIi11i + OoOoOO00 - OOooOOo + O0 . Ii1I
 len ( lisp . lisp_db_list ) ) )
  time . sleep ( iiiI )
  if 46 - 46: IiII
  if 45 - 45: ooOoO0o
  if 21 - 21: oO0o . I1Ii111 . OOooOOo / Oo0Ooo / I1Ii111
  if 17 - 17: OOooOOo / OOooOOo / I11i
  if 1 - 1: i1IIi . i11iIiiIii % OOooOOo
  if 82 - 82: iIii1I11I1II1 + Oo0Ooo . iIii1I11I1II1 % IiII / Ii1I . Ii1I
 IIi = [ ]
 oOoO00oo0O = [ ]
 for oOOOo00O00oOo in lisp . lisp_db_list :
  if ( oOOOo00O00oOo . group . is_null ( ) == False ) : continue
  if ( oOOOo00O00oOo . eid . is_ipv4 ( ) or oOOOo00O00oOo . eid . is_ipv6 ( ) or oOOOo00O00oOo . eid . is_mac ( ) ) :
   oo0o00O = oOOOo00O00oOo . eid . print_prefix_no_iid ( )
   if ( oOOOo00O00oOo . dynamic_eid_configured ( ) ) : oOoO00oo0O . append ( oo0o00O )
   IIi . append ( oo0o00O )
   if 39 - 39: iIii1I11I1II1 / O0 / oO0o - Ii1I - iII111i % OOooOOo
   if 31 - 31: I11i - O0 / ooOoO0o * OoOoOO00
 return ( IIi , oOoO00oo0O )
 if 12 - 12: o0oOOo0O0Ooo - ooOoO0o * I1Ii111
 if 14 - 14: Oo0Ooo - Ii1I % Ii1I * O0 . i11iIiiIii / O0
 if 79 - 79: o0oOOo0O0Ooo - I11i + o0oOOo0O0Ooo . oO0o
 if 28 - 28: i1IIi - iII111i
 if 54 - 54: iII111i - O0 % OOooOOo
 if 73 - 73: O0 . OoOoOO00 + I1IiiI - I11i % I11i . I11i
 if 17 - 17: Ii1I - OoooooooOO % Ii1I . IiII / i11iIiiIii % iII111i
 if 28 - 28: I11i
def I1oOoOo0O0OOOoO ( ) :
 global oo0Ooo0
 if 58 - 58: OoOoOO00
 lisp . lisp_set_exception ( )
 if 37 - 37: Oo0Ooo - iIii1I11I1II1 / I1ii11iIi11i
 if 73 - 73: i11iIiiIii - IiII
 if 25 - 25: OoooooooOO + IiII * I1ii11iIi11i
 if 92 - 92: I1IiiI + I11i + O0 / o0oOOo0O0Ooo + I1Ii111
 if 18 - 18: ooOoO0o * OoOoOO00 . iII111i / I1ii11iIi11i / i11iIiiIii
 IIi , oOoO00oo0O = I1i11i ( )
 if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
 if 91 - 91: i11iIiiIii / i1IIi + iII111i + ooOoO0o * i11iIiiIii
 if 66 - 66: iIii1I11I1II1 % i1IIi - O0 + I11i * I1Ii111 . IiII
 if 52 - 52: ooOoO0o + O0 . iII111i . I1ii11iIi11i . OoO0O00
 if 97 - 97: I1IiiI / iII111i
 if 71 - 71: II111iiii / i1IIi . I1ii11iIi11i % OoooooooOO . OoOoOO00
 if 41 - 41: i1IIi * II111iiii / OoooooooOO . OOooOOo
 if 83 - 83: iII111i . O0 / Oo0Ooo / OOooOOo - II111iiii
 if 100 - 100: OoO0O00
 II1i = None
 if ( lisp . lisp_ipc_data_plane ) :
  lisp . lprint ( lisp . bold ( "Data-plane packet capture disabled" , False ) )
  II1i = "(udp src port 4342 and ip[28] == 0x28)" + " or (ip[16] >= 224 and ip[16] < 240 and (ip[28] & 0xf0) == 0x30)"
  if 2 - 2: iIii1I11I1II1 * Oo0Ooo % oO0o - II111iiii - iII111i
  if 3 - 3: I1Ii111
  lisp . lprint ( "Control-plane capture: '{}'" . format ( II1i ) )
 else :
  lisp . lprint ( "Capturing packets for source-EIDs {}" . format ( lisp . green ( str ( IIi ) , False ) ) )
  if 45 - 45: I1Ii111
  if 83 - 83: OoOoOO00 . OoooooooOO
 if ( lisp . lisp_pitr ) : lisp . lprint ( "Configured for PITR functionality" )
 if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / IiII / i11iIiiIii
 if 62 - 62: OoO0O00 / I1ii11iIi11i
 if 7 - 7: OoooooooOO . IiII
 if 53 - 53: Ii1I % Ii1I * o0oOOo0O0Ooo + OoOoOO00
 if 92 - 92: OoooooooOO + i1IIi / Ii1I * O0
 if 100 - 100: ooOoO0o % iIii1I11I1II1 * II111iiii - iII111i
 oo00O00oO000o = lisp . lisp_l2_overlay
 if ( oo00O00oO000o == False ) :
  if ( lisp . lisp_is_linux ( ) ) : OOo00OoO ( IIi , oOoO00oo0O )
  if 10 - 10: o0oOOo0O0Ooo / i11iIiiIii
  if 92 - 92: I11i . I1Ii111
  if 85 - 85: I1ii11iIi11i . I1Ii111
  if 78 - 78: ooOoO0o * I1Ii111 + iIii1I11I1II1 + iIii1I11I1II1 / I1Ii111 . Ii1I
  if 97 - 97: ooOoO0o / I1Ii111 % i1IIi % I1ii11iIi11i
  if 18 - 18: iIii1I11I1II1 % I11i
 if ( II1i == None ) :
  if ( lisp . lisp_pitr ) :
   O00oO0 = o0o0o0o0 ( IIi , [ ] , False , True )
  else :
   O00oO0 = o0o0o0o0 ( IIi , oOoO00oo0O , oo00O00oO000o ,
 False )
   if 9 - 9: IiII - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
 else :
  O00oO0 = II1i
  if 39 - 39: IiII * Oo0Ooo + iIii1I11I1II1 - IiII + OOooOOo
  if 69 - 69: O0
  if 85 - 85: ooOoO0o / O0
  if 18 - 18: o0oOOo0O0Ooo % O0 * I1ii11iIi11i
  if 62 - 62: I1Ii111 . IiII . OoooooooOO
 oOO00O = OoO0o ( )
 i111 = os . getenv ( "LISP_PCAP_LIST" )
 lisp . lprint ( "User pcap-list: {}, active-interfaces: {}" . format ( i111 ,
 oOO00O ) )
 if ( i111 == None ) :
  iiI1 = ""
  iiIIiii = [ ]
 else :
  iiIIIiIi1IIi = list ( set ( i111 . split ( ) ) & set ( oOO00O ) )
  iiIIiii = list ( set ( i111 . split ( ) ) ^ set ( oOO00O ) )
  iiI1 = "user-selected "
  oOO00O = iiIIIiIi1IIi
  if 47 - 47: O0 / Ii1I
  if 67 - 67: I1IiiI
  if 55 - 55: I1ii11iIi11i - iII111i * o0oOOo0O0Ooo + OoOoOO00 * OoOoOO00 * O0
  if 91 - 91: I1Ii111 - OOooOOo % iIii1I11I1II1 - OoooooooOO % ooOoO0o
  if 98 - 98: OoO0O00 . OoO0O00 * oO0o * II111iiii * I1Ii111
  if 92 - 92: Oo0Ooo
  if 40 - 40: OoOoOO00 / IiII
 OOOoO000 = ( O00oO0 . find ( "ether host" ) != - 1 )
 for oOOOO in oOO00O :
  if ( oOOOO in [ "lo" , "lispers.net" ] and OOOoO000 ) :
   lisp . lprint ( ( "Capturing suppressed on interface {}, " + "MAC filters configured" ) . format ( oOOOO ) )
   if 49 - 49: II111iiii . oO0o . i11iIiiIii % IiII
   continue
   if 34 - 34: I1Ii111 % IiII
   if 3 - 3: II111iiii / OOooOOo + IiII . ooOoO0o . OoO0O00
  oOoo000 = [ oOOOO , O00oO0 , oo0Ooo0 ]
  lisp . lprint ( "Capturing packets on {}interface {}" . format ( iiI1 , oOOOO ) )
  threading . Thread ( target = OooOo00o , args = oOoo000 ) . start ( )
  if 20 - 20: i1IIi * I1Ii111 + II111iiii % o0oOOo0O0Ooo % oO0o
 if ( II1i ) : return
 if 13 - 13: Oo0Ooo
 if 60 - 60: I1ii11iIi11i * I1IiiI
 if 17 - 17: OOooOOo % Oo0Ooo / I1ii11iIi11i . IiII * OOooOOo - II111iiii
 if 41 - 41: Ii1I
 if 77 - 77: I1Ii111
 Oo = "(udp src port 4342 and ip[28] == 0x28)"
 for oOOOO in iiIIiii :
  oOoo000 = [ oOOOO , Oo , oo0Ooo0 ]
  lisp . lprint ( "Capture RLOC-probe replies on RLOC interface {}" . format ( oOOOO ) )
  if 81 - 81: oO0o * OoO0O00
  threading . Thread ( target = OooOo00o , args = oOoo000 ) . start ( )
  if 38 - 38: OoOoOO00 / iII111i % Oo0Ooo
 return
 if 11 - 11: iII111i - oO0o + II111iiii - iIii1I11I1II1
 if 7 - 7: IiII - I11i / II111iiii * Ii1I . iII111i * iII111i
 if 61 - 61: I11i % ooOoO0o - OoO0O00 / Oo0Ooo
 if 4 - 4: OoooooooOO - i1IIi % Ii1I - OOooOOo * o0oOOo0O0Ooo
 if 85 - 85: OoooooooOO * iIii1I11I1II1 . iII111i / OoooooooOO % I1IiiI % O0
 if 36 - 36: Ii1I / II111iiii / IiII / IiII + I1ii11iIi11i
 if 95 - 95: IiII
def Ooo0oo ( ) :
 if 41 - 41: OoOoOO00 * I11i / OoOoOO00 % oO0o
 if 18 - 18: II111iiii . OoooooooOO % OoOoOO00 % Ii1I
 if 9 - 9: OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
 if 2 - 2: OoooooooOO % OOooOOo
 if ( Oo0o0000o0o0 ) : Oo0o0000o0o0 . cancel ( )
 if 63 - 63: I1IiiI % iIii1I11I1II1
 if 39 - 39: iII111i / II111iiii / I1ii11iIi11i % I1IiiI
 if 89 - 89: I1Ii111 + OoooooooOO + I1Ii111 * i1IIi + iIii1I11I1II1 % I11i
 if 59 - 59: OOooOOo + i11iIiiIii
 lisp . lisp_close_socket ( II1iII1i [ 0 ] , "" )
 lisp . lisp_close_socket ( II1iII1i [ 1 ] , "" )
 lisp . lisp_close_socket ( i111I , "" )
 lisp . lisp_close_socket ( iiI1iIiI , "" )
 lisp . lisp_close_socket ( II1Ii1iI1i , "" )
 lisp . lisp_close_socket ( oO0oIIII , "lisp-itr" )
 lisp . lisp_close_socket ( Oo0oO0oo0oO00 , "lispers.net-itr" )
 return
 if 88 - 88: i11iIiiIii - ooOoO0o
 if 67 - 67: OOooOOo . Oo0Ooo + OoOoOO00 - OoooooooOO
 if 70 - 70: OOooOOo / II111iiii - iIii1I11I1II1 - iII111i
 if 11 - 11: iIii1I11I1II1 . OoooooooOO . II111iiii / i1IIi - I11i
 if 30 - 30: OoOoOO00
 if 21 - 21: i11iIiiIii / I1Ii111 % OOooOOo * O0 . I11i - iIii1I11I1II1
 if 26 - 26: II111iiii * OoOoOO00
def ii ( packet , device , input_interface , macs , my_sa ) :
 global II1iII1i
 global OOo
 global Oooo0000 , i11
 global oO0oIIII
 if 81 - 81: O0 % Ii1I
 if 5 - 5: OoooooooOO - OoO0O00 + IiII - iII111i . OoO0O00 / ooOoO0o
 if 28 - 28: Ii1I * Ii1I - iIii1I11I1II1
 if 70 - 70: I1Ii111
 i11iIIi11 = packet
 packet , ooOooo000OO00 , IiIiI1I1I1 , iiii1 = lisp . lisp_is_rloc_probe ( packet , device , 1 )
 if ( i11iIIi11 != packet ) :
  if ( ooOooo000OO00 == None ) : return
  lisp . lisp_parse_packet ( II1iII1i , packet , ooOooo000OO00 , IiIiI1I1I1 , iiii1 )
  return
  if 6 - 6: iII111i . IiII * OoOoOO00 . i1IIi
  if 98 - 98: i1IIi
 packet = lisp . lisp_packet ( packet )
 if ( packet . decode ( False , None , None ) == None ) : return
 if 65 - 65: OoOoOO00 / OoO0O00 % IiII
 if 45 - 45: OoOoOO00
 if 66 - 66: OoO0O00
 if 56 - 56: O0
 if 61 - 61: o0oOOo0O0Ooo / OOooOOo / Oo0Ooo * O0
 if 23 - 23: oO0o - OOooOOo + I11i
 if ( my_sa ) : input_interface = device
 if 12 - 12: I1IiiI / ooOoO0o % o0oOOo0O0Ooo / i11iIiiIii % OoooooooOO
 if 15 - 15: iIii1I11I1II1 % OoooooooOO - Oo0Ooo * Ii1I + I11i
 if 11 - 11: iII111i * Ii1I - OoOoOO00
 if 66 - 66: OoOoOO00 . i11iIiiIii - iII111i * o0oOOo0O0Ooo + OoooooooOO * I1ii11iIi11i
 oO0OO0 = packet . inner_source
 I1ii1Ii1 = lisp . lisp_get_interface_instance_id ( input_interface , oO0OO0 )
 packet . inner_dest . instance_id = I1ii1Ii1
 packet . inner_source . instance_id = I1ii1Ii1
 if 92 - 92: ooOoO0o / OoOoOO00 * OoO0O00 . I11i % II111iiii
 if 71 - 71: I1Ii111 % i1IIi - II111iiii - OOooOOo + OOooOOo * ooOoO0o
 if 51 - 51: iIii1I11I1II1 / OoOoOO00 + OOooOOo - I11i + iII111i
 if 29 - 29: o0oOOo0O0Ooo % iIii1I11I1II1 . OoooooooOO % OoooooooOO % II111iiii / iII111i
 if ( macs != "" ) : macs = ", MACs: " + macs + ","
 packet . print_packet ( "Receive {}{}" . format ( device , macs ) , False )
 if 70 - 70: i11iIiiIii % iII111i
 if 11 - 11: IiII % I1ii11iIi11i % Ii1I / II111iiii % I1Ii111 - Oo0Ooo
 if 96 - 96: I1ii11iIi11i / II111iiii . Ii1I - iII111i * I11i * oO0o
 if 76 - 76: Ii1I - II111iiii * OOooOOo / OoooooooOO
 if ( device != input_interface and device != "lispers.net" ) :
  lisp . dprint ( "Not our MAC address on interface {}, pcap interface {}" . format ( input_interface , device ) )
  if 18 - 18: OoO0O00 + iIii1I11I1II1 - II111iiii - I1IiiI
  return
  if 71 - 71: OoooooooOO
  if 33 - 33: I1Ii111
 OOO0ooo = lisp . lisp_decent_push_configured
 if ( OOO0ooo ) :
  IIiiii = packet . inner_dest . is_multicast_address ( )
  iI111i1I1II = packet . inner_source . is_local ( )
  OOO0ooo = ( iI111i1I1II and IIiiii )
  if 96 - 96: I1Ii111 / Oo0Ooo * II111iiii - iII111i * Oo0Ooo
  if 81 - 81: IiII . o0oOOo0O0Ooo / I1Ii111
 if ( OOO0ooo == False ) :
  if 17 - 17: i11iIiiIii - OOooOOo . IiII % iIii1I11I1II1 + I11i - ooOoO0o
  if 78 - 78: I11i * OoOoOO00 . O0 / O0
  if 80 - 80: i1IIi - Oo0Ooo / OoO0O00 - i11iIiiIii
  if 68 - 68: oO0o - I1ii11iIi11i % O0 % I1Ii111
  oOOOo00O00oOo = lisp . lisp_db_for_lookups . lookup_cache ( packet . inner_source , False )
  if ( oOOOo00O00oOo == None ) :
   lisp . dprint ( "Packet received from non-EID source" )
   return
   if 11 - 11: O0 / OoO0O00 % OOooOOo + o0oOOo0O0Ooo + iIii1I11I1II1
   if 40 - 40: ooOoO0o - OOooOOo . Ii1I * Oo0Ooo % I1Ii111
   if 56 - 56: i11iIiiIii . o0oOOo0O0Ooo - I1IiiI * I11i
   if 91 - 91: oO0o + OoooooooOO - i1IIi
   if 84 - 84: Ii1I / IiII
  if ( oOOOo00O00oOo . dynamic_eid_configured ( ) ) :
   OOOooo0OooOoO = lisp . lisp_allow_dynamic_eid ( input_interface ,
 packet . inner_source )
   if ( OOOooo0OooOoO ) :
    lisp . lisp_itr_discover_eid ( oOOOo00O00oOo , packet . inner_source ,
 input_interface , OOOooo0OooOoO , oO0oIIII )
   else :
    ooO0oooOO0 = lisp . green ( packet . inner_source . print_address ( ) , False )
    lisp . dprint ( "Disallow dynamic-EID {} on interface {}" . format ( ooO0oooOO0 ,
 input_interface ) )
    return
    if 91 - 91: oO0o + I1IiiI
    if 59 - 59: I1IiiI + i11iIiiIii + i1IIi / I11i
    if 44 - 44: I11i . OoOoOO00 * I1IiiI + OoooooooOO - iII111i - IiII
  if ( packet . inner_source . is_local ( ) and
 packet . udp_dport == lisp . LISP_CTRL_PORT ) : return
  if 15 - 15: IiII / O0 . o0oOOo0O0Ooo . i11iIiiIii
  if 59 - 59: I1Ii111 - o0oOOo0O0Ooo - ooOoO0o
  if 48 - 48: i1IIi + I11i % OoOoOO00 / Oo0Ooo - o0oOOo0O0Ooo
  if 67 - 67: oO0o % o0oOOo0O0Ooo . OoooooooOO + OOooOOo * I11i * OoOoOO00
  if 36 - 36: O0 + Oo0Ooo
 iIIIi1i1I11i = False
 if ( packet . inner_version == 4 ) :
  iIIIi1i1I11i , packet . packet = lisp . lisp_ipv4_input ( packet . packet )
  if ( packet . packet == None ) : return
  packet . inner_ttl -= 1
 elif ( packet . inner_version == 6 ) :
  packet . packet = lisp . lisp_ipv6_input ( packet )
  if ( packet . packet == None ) : return
  packet . inner_ttl -= 1
 else :
  packet . packet = lisp . lisp_mac_input ( packet . packet )
  if ( packet . packet == None ) : return
  packet . encap_port = lisp . LISP_L2_DATA_PORT
  if 55 - 55: Oo0Ooo - OOooOOo
  if 84 - 84: I1Ii111 + Oo0Ooo - OoOoOO00 * OoOoOO00
  if 61 - 61: OoooooooOO . oO0o . OoooooooOO / Oo0Ooo
  if 72 - 72: i1IIi
  if 82 - 82: OoOoOO00 + OoooooooOO / i11iIiiIii * I1ii11iIi11i . OoooooooOO
  if 63 - 63: I1ii11iIi11i
 if ( iIiiI1 == False ) :
  oOOOOo0 = lisp . lisp_db_for_lookups . lookup_cache ( packet . inner_dest , False )
  if ( oOOOOo0 and oOOOOo0 . dynamic_eid_configured == False ) :
   lisp . dprint ( ( "Packet destined to local EID-prefix {}, " + "natively forwarding" ) . format ( oOOOOo0 . print_eid_tuple ( ) ) )
   if 6 - 6: ooOoO0o / I1ii11iIi11i
   packet . send_packet ( Oooo0000 , packet . inner_dest )
   return
   if 57 - 57: I11i
   if 67 - 67: OoO0O00 . ooOoO0o
   if 87 - 87: oO0o % Ii1I
   if 83 - 83: II111iiii - I11i
   if 35 - 35: i1IIi - iIii1I11I1II1 + i1IIi
   if 86 - 86: iIii1I11I1II1 + OoOoOO00 . i11iIiiIii - Ii1I
 ooO000O = lisp . lisp_map_cache_lookup ( packet . inner_source , packet . inner_dest )
 if ( ooO000O ) : ooO000O . add_recent_source ( packet . inner_source )
 if 53 - 53: o0oOOo0O0Ooo . iII111i / Ii1I
 if 39 - 39: Ii1I % O0 % OoOoOO00 . i1IIi
 if 86 - 86: OoO0O00 * OoooooooOO
 if 71 - 71: iIii1I11I1II1 - OOooOOo . I1IiiI % OoooooooOO + OOooOOo
 if 26 - 26: Oo0Ooo + OOooOOo / OoO0O00 % OoOoOO00 % I1ii11iIi11i + II111iiii
 if 31 - 31: I11i % OOooOOo * I11i
 if 45 - 45: i1IIi . I1IiiI + OOooOOo - OoooooooOO % ooOoO0o
 i1I = oOOOo00O00oOo . secondary_iid
 if ( i1I and ooO000O and ooO000O . action == lisp . LISP_NATIVE_FORWARD_ACTION ) :
  iiII1I11IIi = packet . inner_dest
  iiII1I11IIi . instance_id = i1I
  ooO000O = lisp . lisp_map_cache_lookup ( packet . inner_source , iiII1I11IIi )
  if ( ooO000O ) : ooO000O . add_recent_source ( packet . inner_source )
  if 66 - 66: i11iIiiIii / o0oOOo0O0Ooo - OoooooooOO / i1IIi . i11iIiiIii
  if 16 - 16: Oo0Ooo % I1ii11iIi11i + I11i - O0 . iII111i / I1Ii111
  if 35 - 35: oO0o / I1Ii111 / II111iiii - iIii1I11I1II1 + II111iiii . I1Ii111
  if 81 - 81: iII111i * OOooOOo - I1ii11iIi11i * Ii1I % OoOoOO00 * OoOoOO00
  if 59 - 59: iIii1I11I1II1
 if ( ooO000O == None or lisp . lisp_mr_or_pubsub ( ooO000O . action ) ) :
  if ( lisp . lisp_rate_limit_map_request ( packet . inner_dest ) ) : return
  if 7 - 7: OOooOOo * I1IiiI / o0oOOo0O0Ooo * i11iIiiIii
  o00 = ( ooO000O and ooO000O . action == lisp . LISP_SEND_PUBSUB_ACTION )
  lisp . lisp_send_map_request ( II1iII1i , OOo ,
 packet . inner_source , packet . inner_dest , None , o00 )
  if 8 - 8: Oo0Ooo + II111iiii * OOooOOo * OoOoOO00 * I11i / IiII
  if ( packet . is_trace ( ) ) :
   lisp . lisp_trace_append ( packet , reason = "map-cache miss" )
   if 21 - 21: oO0o / OoooooooOO
  return
  if 11 - 11: OOooOOo % Ii1I - i11iIiiIii - oO0o + ooOoO0o + IiII
  if 87 - 87: I1Ii111 * i1IIi / I1ii11iIi11i
  if 6 - 6: o0oOOo0O0Ooo + Oo0Ooo - OoooooooOO % OOooOOo * OoOoOO00
  if 69 - 69: i1IIi
  if 59 - 59: II111iiii - o0oOOo0O0Ooo
  if 24 - 24: Oo0Ooo - i1IIi + I11i
 if ( ooO000O and ooO000O . is_active ( ) and ooO000O . has_ttl_elapsed ( ) ) :
  if ( lisp . lisp_rate_limit_map_request ( packet . inner_dest ) == False ) :
   lisp . lprint ( "Refresh map-cache entry {}" . format ( lisp . green ( ooO000O . print_eid_tuple ( ) , False ) ) )
   if 38 - 38: OoooooooOO / I1ii11iIi11i . O0 / i1IIi / Oo0Ooo + iIii1I11I1II1
   lisp . lisp_send_map_request ( II1iII1i , OOo ,
 packet . inner_source , packet . inner_dest , None )
   if 96 - 96: iII111i
   if 18 - 18: iII111i * I11i - Ii1I
   if 31 - 31: Oo0Ooo - O0 % OoOoOO00 % oO0o
   if 45 - 45: I1ii11iIi11i + II111iiii * i11iIiiIii
   if 13 - 13: OoooooooOO * oO0o - Ii1I / OOooOOo + I11i + IiII
   if 39 - 39: iIii1I11I1II1 - OoooooooOO
   if 81 - 81: I1ii11iIi11i - O0 * OoooooooOO
 ooO000O . last_refresh_time = time . time ( )
 ooO000O . stats . increment ( len ( packet . packet ) )
 if 23 - 23: II111iiii / oO0o
 if 28 - 28: Oo0Ooo * ooOoO0o - OoO0O00
 if 19 - 19: I11i
 if 67 - 67: O0 % iIii1I11I1II1 / IiII . i11iIiiIii - Ii1I + O0
 i1iiiIi1i , OO0Oo , IiIIIIIIiI , OOooo00 , i1oO , iI = ooO000O . select_rloc ( packet , oO0oIIII )
 if 42 - 42: OoooooooOO + Oo0Ooo % II111iiii + OoO0O00
 if 24 - 24: iII111i * II111iiii % iII111i % IiII + OoooooooOO
 if ( i1iiiIi1i == None and i1oO == None ) :
  if ( OOooo00 == lisp . LISP_NATIVE_FORWARD_ACTION ) :
   lisp . dprint ( "Natively forwarding" )
   packet . send_packet ( Oooo0000 , packet . inner_dest )
   if 29 - 29: II111iiii - OoooooooOO - i11iIiiIii . o0oOOo0O0Ooo
   if ( packet . is_trace ( ) ) :
    lisp . lisp_trace_append ( packet , reason = "not an EID" )
    if 19 - 19: II111iiii
   return
   if 72 - 72: OoooooooOO / I1IiiI + Ii1I / OoOoOO00 * Ii1I
  Ii1iIi111i1i1 = "No reachable RLOCs found"
  lisp . dprint ( Ii1iIi111i1i1 )
  if ( packet . is_trace ( ) ) : lisp . lisp_trace_append ( packet , reason = Ii1iIi111i1i1 )
  return
  if 45 - 45: OoOoOO00 . o0oOOo0O0Ooo % OoOoOO00 * I1IiiI % I1IiiI
 if ( i1iiiIi1i and i1iiiIi1i . is_null ( ) ) :
  Ii1iIi111i1i1 = "Drop action RLOC found"
  lisp . dprint ( Ii1iIi111i1i1 )
  if 63 - 63: I1Ii111
  if ( packet . is_trace ( ) ) : lisp . lisp_trace_append ( packet , reason = Ii1iIi111i1i1 )
  return
  if 53 - 53: OoooooooOO - IiII
  if 87 - 87: oO0o . I1IiiI
  if 17 - 17: Ii1I . i11iIiiIii
  if 5 - 5: I1ii11iIi11i + O0 + O0 . I1Ii111 - ooOoO0o
  if 63 - 63: oO0o
 packet . outer_tos = packet . inner_tos
 packet . outer_ttl = 32 if ( iIIIi1i1I11i ) else packet . inner_ttl
 if 71 - 71: i1IIi . Ii1I * iII111i % OoooooooOO + OOooOOo
 if 36 - 36: IiII
 if 49 - 49: OOooOOo / OoooooooOO / I1IiiI
 if 74 - 74: I1Ii111 % I1ii11iIi11i
 if ( i1iiiIi1i ) :
  packet . encap_port = OO0Oo
  if ( OO0Oo == 0 ) : packet . encap_port = lisp . LISP_DATA_PORT
  packet . outer_dest . copy_address ( i1iiiIi1i )
  iiIiI = packet . outer_dest . afi_to_version ( )
  packet . outer_version = iiIiI
  i1oOOOOOOOoO = lisp . lisp_myrlocs [ 0 ] if ( iiIiI == 4 ) else lisp . lisp_myrlocs [ 1 ]
  if 12 - 12: iII111i . IiII . OoOoOO00 / O0
  if 58 - 58: o0oOOo0O0Ooo - II111iiii % oO0o + I1Ii111 . OoOoOO00 / IiII
  if 8 - 8: I1ii11iIi11i . OoO0O00 * I11i + II111iiii % i11iIiiIii
  if 8 - 8: ooOoO0o * O0
  if 73 - 73: o0oOOo0O0Ooo / oO0o / I11i / OoO0O00
  if 11 - 11: OoOoOO00 + IiII - OoooooooOO / OoO0O00
  if 34 - 34: ooOoO0o
  if 45 - 45: ooOoO0o / Oo0Ooo / Ii1I
  if 44 - 44: I1ii11iIi11i - Ii1I / II111iiii * OoO0O00 * Oo0Ooo
  if 73 - 73: o0oOOo0O0Ooo - I1IiiI * i1IIi / i11iIiiIii * OOooOOo % II111iiii
  if 56 - 56: OoooooooOO * Oo0Ooo . Oo0Ooo . I1ii11iIi11i
  packet . outer_source . copy_address ( i1oOOOOOOOoO )
  if 24 - 24: Oo0Ooo . I11i * Ii1I % iII111i / OOooOOo
  if ( packet . is_trace ( ) ) :
   if ( lisp . lisp_trace_append ( packet , rloc_entry = iI ) == False ) : return
   if 58 - 58: I1IiiI - I1ii11iIi11i % O0 . I1IiiI % OoO0O00 % IiII
   if 87 - 87: oO0o - i11iIiiIii
   if 78 - 78: i11iIiiIii / iIii1I11I1II1 - o0oOOo0O0Ooo
   if 23 - 23: I11i
   if 40 - 40: o0oOOo0O0Ooo - II111iiii / Oo0Ooo
   if 14 - 14: I1ii11iIi11i
  if ( packet . encode ( IiIIIIIIiI ) == None ) : return
  if ( len ( packet . packet ) <= 1500 ) : packet . print_packet ( "Send" , True )
  if 5 - 5: o0oOOo0O0Ooo . iIii1I11I1II1 % iIii1I11I1II1
  if 56 - 56: OoooooooOO - I11i - i1IIi
  if 8 - 8: I1Ii111 / OOooOOo . I1IiiI + I1ii11iIi11i / i11iIiiIii
  if 31 - 31: ooOoO0o - iIii1I11I1II1 + iII111i . Oo0Ooo / IiII % iIii1I11I1II1
  I11i1iIiiIiIi = i11 if iiIiI == 6 else Oooo0000
  packet . send_packet ( I11i1iIiiIiIi , packet . outer_dest )
  if 49 - 49: OOooOOo . I1ii11iIi11i . i11iIiiIii - II111iiii / Ii1I
 elif ( i1oO ) :
  if 62 - 62: OOooOOo
  if 1 - 1: IiII / IiII - i11iIiiIii
  if 87 - 87: Oo0Ooo / O0 * IiII / o0oOOo0O0Ooo
  if 19 - 19: I1Ii111 + i1IIi . I1IiiI - Oo0Ooo
  if 16 - 16: oO0o + ooOoO0o / o0oOOo0O0Ooo
  O00oOoo0OoO0 = i1oO . rle_nodes [ 0 ] . level
  Ooo0 = len ( packet . packet )
  for oooO00o0 in i1oO . rle_forwarding_list :
   if ( oooO00o0 . level != O00oOoo0OoO0 ) : return
   if 53 - 53: ooOoO0o
   packet . outer_dest . copy_address ( oooO00o0 . address )
   if ( OOO0ooo ) : packet . inner_dest . instance_id = 0xffffff
   iiIiI = packet . outer_dest . afi_to_version ( )
   packet . outer_version = iiIiI
   i1oOOOOOOOoO = lisp . lisp_myrlocs [ 0 ] if ( iiIiI == 4 ) else lisp . lisp_myrlocs [ 1 ]
   if 98 - 98: I1Ii111
   packet . outer_source . copy_address ( i1oOOOOOOOoO )
   if 92 - 92: I1Ii111 - iIii1I11I1II1
   if ( packet . is_trace ( ) ) :
    if ( lisp . lisp_trace_append ( packet ) == False ) : return
    if 32 - 32: Ii1I % OoO0O00 * OoO0O00 + IiII * II111iiii * Ii1I
    if 11 - 11: oO0o % II111iiii
   if ( packet . encode ( None ) == None ) : return
   if 57 - 57: OOooOOo / Oo0Ooo
   if 69 - 69: oO0o - Oo0Ooo % IiII
   if 50 - 50: OoooooooOO
   if 4 - 4: II111iiii . I11i + Ii1I * I1Ii111 . ooOoO0o
   packet . print_packet ( "Replicate-to-L{}" . format ( oooO00o0 . level ) , True )
   packet . send_packet ( Oooo0000 , packet . outer_dest )
   if 87 - 87: OoOoOO00 / OoO0O00 / i11iIiiIii
   if 74 - 74: oO0o / I1ii11iIi11i % o0oOOo0O0Ooo
   if 88 - 88: OoOoOO00 - i11iIiiIii % o0oOOo0O0Ooo * I11i + I1ii11iIi11i
   if 52 - 52: II111iiii . I1IiiI + OoOoOO00 % OoO0O00
   if 62 - 62: o0oOOo0O0Ooo
   I1i111i = len ( packet . packet ) - Ooo0
   packet . packet = packet . packet [ I1i111i : : ]
   if 42 - 42: I1ii11iIi11i / i1IIi % OoOoOO00
   if 26 - 26: Ii1I * iIii1I11I1II1 % OoO0O00 . o0oOOo0O0Ooo + Oo0Ooo
   if 80 - 80: Oo0Ooo * Ii1I + I1ii11iIi11i * OOooOOo
   if 16 - 16: I11i / I1IiiI + OoO0O00 % iIii1I11I1II1 - i1IIi . oO0o
   if 26 - 26: o0oOOo0O0Ooo * IiII . i1IIi
   if 59 - 59: O0 + i1IIi - o0oOOo0O0Ooo
 del ( packet )
 return
 if 62 - 62: i11iIiiIii % OOooOOo . IiII . OOooOOo
 if 84 - 84: i11iIiiIii * OoO0O00
 if 18 - 18: OOooOOo - Ii1I - OoOoOO00 / I1Ii111 - O0
 if 30 - 30: O0 + I1ii11iIi11i + II111iiii
 if 14 - 14: o0oOOo0O0Ooo / OOooOOo - iIii1I11I1II1 - oO0o % ooOoO0o
 if 49 - 49: ooOoO0o * oO0o / o0oOOo0O0Ooo / Oo0Ooo * iIii1I11I1II1
 if 57 - 57: OoOoOO00 - oO0o / ooOoO0o % i11iIiiIii
def I11oOOooo ( device , not_used , packet ) :
 ooo0O0Oo = 4 if device == "lo0" else 0 if device == "lispers.net" else 14
 if 18 - 18: OOooOOo + I1Ii111
 if ( lisp . lisp_frame_logging ) :
  OO0OO0O = lisp . bold ( "Received frame on interface '{}'" . format ( device ) ,
 False )
  O0oOo = lisp . lisp_format_packet ( packet [ 0 : 64 ] )
  lisp . lprint ( "{}: {}" . format ( OO0OO0O , O0oOo ) )
  if 69 - 69: Oo0Ooo * II111iiii * ooOoO0o . iII111i - I1ii11iIi11i
  if 39 - 39: Ii1I * I1IiiI % OoO0O00 . OoOoOO00
  if 24 - 24: i1IIi * iIii1I11I1II1 / Ii1I
  if 78 - 78: i11iIiiIii + o0oOOo0O0Ooo + I1Ii111 / o0oOOo0O0Ooo % iIii1I11I1II1 % IiII
  if 83 - 83: iIii1I11I1II1 % OoOoOO00 % o0oOOo0O0Ooo % I1Ii111 . I1ii11iIi11i % O0
 iIiIi1ii = ""
 iiiiiII = False
 OoOOoOooooOOo = device
 if ( ooo0O0Oo == 14 ) :
  oOO00O , ii1ii , IIiI1i , iiiiiII = lisp . lisp_get_input_interface ( packet )
  OoOOoOooooOOo = device if ( device in oOO00O ) else oOO00O [ 0 ]
  iIiIi1ii = lisp . lisp_format_macs ( ii1ii , IIiI1i )
  if ( OoOOoOooooOOo . find ( "vlan" ) != - 1 ) : ooo0O0Oo += 4
  if 6 - 6: I1ii11iIi11i / iII111i - OOooOOo
  if 62 - 62: I11i % OOooOOo
  if 54 - 54: OoOoOO00 % iII111i . OoOoOO00 * OOooOOo + OoOoOO00 % i1IIi
  if 23 - 23: I1Ii111 - OOooOOo + Ii1I - OoOoOO00 * OoOoOO00 . Oo0Ooo
  if 47 - 47: oO0o % iIii1I11I1II1
  if 11 - 11: I1IiiI % Ii1I - OoO0O00 - oO0o + o0oOOo0O0Ooo
  if ( int ( IIiI1i [ 1 ] , 16 ) & 1 ) : iiiiiII = True
  if 98 - 98: iII111i + Ii1I - OoO0O00
  if 79 - 79: OOooOOo / I1Ii111 . OoOoOO00 - I1ii11iIi11i
  if 47 - 47: OoooooooOO % O0 * iII111i . Ii1I
  if 38 - 38: O0 - IiII % I1Ii111
  if 64 - 64: iIii1I11I1II1
 if ( ooo0O0Oo != 0 ) :
  IIi1iI = struct . unpack ( "H" , packet [ ooo0O0Oo - 2 : ooo0O0Oo ] ) [ 0 ]
  IIi1iI = socket . ntohs ( IIi1iI )
  if ( IIi1iI == 0x8100 ) :
   oO0Ooo0OooOOo = struct . unpack ( "I" , packet [ ooo0O0Oo : ooo0O0Oo + 4 ] ) [ 0 ]
   oO0Ooo0OooOOo = socket . ntohl ( oO0Ooo0OooOOo )
   OoOOoOooooOOo = "vlan" + str ( oO0Ooo0OooOOo >> 16 )
   ooo0O0Oo += 4
  elif ( IIi1iI == 0x806 ) :
   lisp . dprint ( "Dropping ARP packets, host should have default route" )
   return
   if 71 - 71: IiII + i1IIi * Oo0Ooo % Oo0Ooo / Oo0Ooo
   if 55 - 55: OoooooooOO + I1Ii111 + OoooooooOO * ooOoO0o
   if 68 - 68: O0
 if ( lisp . lisp_l2_overlay ) : ooo0O0Oo = 0
 if 2 - 2: OoO0O00 + O0 * OoO0O00 - Ii1I + oO0o
 ii ( packet [ ooo0O0Oo : : ] , device , OoOOoOooooOOo , iIiIi1ii , iiiiiII )
 return
 if 43 - 43: I1ii11iIi11i - OoOoOO00
 if 36 - 36: I1ii11iIi11i - iII111i
 if 24 - 24: o0oOOo0O0Ooo + ooOoO0o + I11i - iIii1I11I1II1
 if 49 - 49: I11i . ooOoO0o * OoOoOO00 % IiII . O0
 if 48 - 48: O0 * Ii1I - O0 / Ii1I + OoOoOO00
 if 52 - 52: OoO0O00 % Ii1I * II111iiii
 if 4 - 4: I11i % O0 - OoooooooOO + ooOoO0o . oO0o % II111iiii
 if 9 - 9: II111iiii * II111iiii . i11iIiiIii * iIii1I11I1II1
 if 18 - 18: OoO0O00 . II111iiii % OoOoOO00 % Ii1I
 if 87 - 87: iIii1I11I1II1 . OoooooooOO * OoOoOO00
 if 100 - 100: OoO0O00 / i1IIi - I1IiiI % Ii1I - iIii1I11I1II1
 if 17 - 17: I11i / o0oOOo0O0Ooo % Oo0Ooo
 if 71 - 71: IiII . I1Ii111 . OoO0O00
 if 68 - 68: i11iIiiIii % oO0o * OoO0O00 * IiII * II111iiii + O0
 if 66 - 66: I11i % I1ii11iIi11i % OoooooooOO
 if 34 - 34: o0oOOo0O0Ooo / iII111i % O0 . OoO0O00 . i1IIi
 if 29 - 29: O0 . I1Ii111
 if 66 - 66: oO0o * iIii1I11I1II1 % iIii1I11I1II1 * IiII - ooOoO0o - IiII
 if 70 - 70: I1Ii111 + oO0o
 if 93 - 93: I1Ii111 + Ii1I
 if 33 - 33: O0
 if 78 - 78: O0 / II111iiii * OoO0O00
 if 50 - 50: OoooooooOO - iIii1I11I1II1 + i1IIi % I1Ii111 - iIii1I11I1II1 % O0
 if 58 - 58: IiII + iIii1I11I1II1
 if 65 - 65: II111iiii - I1Ii111 % o0oOOo0O0Ooo - OoOoOO00 * iII111i + Ii1I
 if 79 - 79: ooOoO0o . OoOoOO00 % I1Ii111 - Oo0Ooo
 if 69 - 69: ooOoO0o - o0oOOo0O0Ooo . ooOoO0o
 if 9 - 9: oO0o % i11iIiiIii / Oo0Ooo
 if 20 - 20: oO0o * O0 + I11i - OoooooooOO . I11i
 if 60 - 60: o0oOOo0O0Ooo . o0oOOo0O0Ooo / iII111i
 if 45 - 45: O0 . i11iIiiIii % iII111i . OoOoOO00 % IiII % iIii1I11I1II1
 if 58 - 58: iIii1I11I1II1 . OoOoOO00 - i11iIiiIii * iIii1I11I1II1 % i11iIiiIii / I1IiiI
 if 80 - 80: I1ii11iIi11i / iIii1I11I1II1 % OoOoOO00
 if 80 - 80: OoO0O00 % iII111i
 if 99 - 99: ooOoO0o / iIii1I11I1II1 - Ii1I * I1ii11iIi11i % I1IiiI
 if 13 - 13: OoO0O00
 if 70 - 70: I1Ii111 + O0 . oO0o * Ii1I
def OOo00OoO ( sources , dyn_eids ) :
 if ( os . getenv ( "LISP_NO_IPTABLES" ) != None ) :
  lisp . lprint ( "User selected to suppress installing iptables rules" )
  return
  if 2 - 2: OoooooooOO . OOooOOo . IiII
  if 42 - 42: OOooOOo % oO0o / OoO0O00 - oO0o * i11iIiiIii
 os . system ( "sudo iptables -t raw -N lisp" )
 os . system ( "sudo iptables -t raw -A PREROUTING -j lisp" )
 os . system ( "sudo ip6tables -t raw -N lisp" )
 os . system ( "sudo ip6tables -t raw -A PREROUTING -j lisp" )
 if 19 - 19: oO0o * I1IiiI % i11iIiiIii
 if 24 - 24: o0oOOo0O0Ooo
 if 10 - 10: o0oOOo0O0Ooo % Ii1I / OOooOOo
 if 28 - 28: OOooOOo % ooOoO0o
 if 48 - 48: i11iIiiIii % oO0o
 if 29 - 29: iII111i + i11iIiiIii % I11i
 if 93 - 93: OoOoOO00 % iIii1I11I1II1
 if 90 - 90: I1IiiI - OOooOOo / Ii1I / O0 / I11i
 oOO0 = "sudo ip{}tables -t raw -A lisp -j ACCEPT -d {}"
 IIi1I1i = [ "127.0.0.1" , "::1" , "224.0.0.0/4 -p igmp" , "ff00::/8" ,
 "fe80::/16" ]
 IIi1I1i += sources + lisp . lisp_get_all_addresses ( )
 for Ii in IIi1I1i :
  if ( lisp . lisp_is_mac_string ( Ii ) ) : continue
  oO0O = "" if Ii . find ( ":" ) == - 1 else "6"
  os . system ( oOO0 . format ( oO0O , Ii ) )
  if 79 - 79: OoooooooOO - IiII * IiII . OoOoOO00
  if 100 - 100: II111iiii * I11i % I1IiiI / I1ii11iIi11i
  if 90 - 90: I1ii11iIi11i . ooOoO0o . OoOoOO00 . Ii1I
  if 4 - 4: Ii1I + OoOoOO00 % I1ii11iIi11i / i11iIiiIii
  if 74 - 74: II111iiii . O0 - I1IiiI + IiII % i11iIiiIii % OoOoOO00
  if 78 - 78: Ii1I + OoOoOO00 + IiII - IiII . i11iIiiIii / OoO0O00
  if 27 - 27: Ii1I - O0 % I11i * I1Ii111 . IiII % iIii1I11I1II1
  if 37 - 37: OoooooooOO + O0 - i1IIi % ooOoO0o
 if ( lisp . lisp_pitr == False ) :
  oOO0 = "sudo ip{}tables -t raw -A lisp -j ACCEPT -s {} -d {}"
  i1I1i1i = "sudo ip{}tables -t raw -C lisp -j ACCEPT -s {} -d {}"
  for ooOooo000OO00 in sources :
   if ( lisp . lisp_is_mac_string ( ooOooo000OO00 ) ) : continue
   if ( ooOooo000OO00 in dyn_eids ) : continue
   oO0O = "" if ooOooo000OO00 . find ( ":" ) == - 1 else "6"
   for iii11 in sources :
    if ( lisp . lisp_is_mac_string ( iii11 ) ) : continue
    if ( iii11 in dyn_eids ) : continue
    if ( iii11 . find ( "." ) != - 1 and ooOooo000OO00 . find ( "." ) == - 1 ) : continue
    if ( iii11 . find ( ":" ) != - 1 and ooOooo000OO00 . find ( ":" ) == - 1 ) : continue
    if ( getoutput ( i1I1i1i . format ( oO0O , ooOooo000OO00 , iii11 ) ) == "" ) :
     continue
     if 36 - 36: II111iiii % O0
    os . system ( oOO0 . format ( oO0O , ooOooo000OO00 , iii11 ) )
    if 35 - 35: iIii1I11I1II1 - OOooOOo % o0oOOo0O0Ooo
    if 30 - 30: I1Ii111 % I1Ii111 % IiII . OoOoOO00
    if 9 - 9: ooOoO0o / II111iiii . OoOoOO00 % o0oOOo0O0Ooo * II111iiii - ooOoO0o
    if 55 - 55: I1IiiI
    if 45 - 45: O0 / i1IIi * oO0o * OoO0O00
    if 35 - 35: I1ii11iIi11i / iII111i % I1IiiI + iIii1I11I1II1
    if 79 - 79: OoOoOO00 / ooOoO0o
 oOo00o = "sudo ip{}tables -t raw -A lisp -j DROP -s {}"
 for ooOooo000OO00 in sources :
  if ( lisp . lisp_is_mac_string ( ooOooo000OO00 ) ) : continue
  oO0O = "" if ooOooo000OO00 . find ( ":" ) == - 1 else "6"
  os . system ( oOo00o . format ( oO0O , ooOooo000OO00 ) )
  if 98 - 98: OOooOOo % i1IIi . I1IiiI . II111iiii . I1ii11iIi11i / i11iIiiIii
  if 32 - 32: o0oOOo0O0Ooo + I1IiiI . I1Ii111
  if 41 - 41: OoOoOO00 . i11iIiiIii / I11i
  if 98 - 98: OoOoOO00 % II111iiii
  if 95 - 95: iIii1I11I1II1 - I1Ii111 - OOooOOo + I1Ii111 % I1ii11iIi11i . I1IiiI
 IiiIIi1 = getoutput ( "sudo iptables -t raw -S lisp" ) . split ( "\n" )
 IiiIIi1 += getoutput ( "sudo ip6tables -t raw -S lisp" ) . split ( "\n" )
 lisp . lprint ( "Using kernel filters: {}" . format ( IiiIIi1 ) )
 if 28 - 28: o0oOOo0O0Ooo
 if 45 - 45: o0oOOo0O0Ooo . I1IiiI / I1Ii111 - Oo0Ooo * iIii1I11I1II1
 if 86 - 86: II111iiii + ooOoO0o + IiII
 if 9 - 9: ooOoO0o + II111iiii % ooOoO0o % IiII + iIii1I11I1II1
 if 59 - 59: i1IIi
 if 48 - 48: O0 * Ii1I * OoO0O00 . OoO0O00 * I11i - Ii1I
 if 14 - 14: I1ii11iIi11i + i11iIiiIii
 if 83 - 83: I1ii11iIi11i / i11iIiiIii + II111iiii . iII111i * OOooOOo + IiII
 if 42 - 42: i1IIi % II111iiii . ooOoO0o
 if 7 - 7: I1ii11iIi11i - oO0o * OOooOOo + o0oOOo0O0Ooo . I1ii11iIi11i
 if 85 - 85: O0
 if ( os . getenv ( "LISP_VIRTIO_BUG" ) != None ) :
  Iii = ( "sudo iptables -A POSTROUTING -t mangle -p tcp -j " + "CHECKSUM --checksum-fill; " )
  if 42 - 42: II111iiii + I1Ii111 - Ii1I - O0 / o0oOOo0O0Ooo % IiII
  Iii += ( "sudo iptables -A POSTROUTING -t mangle -p udp -j " + "CHECKSUM --checksum-fill; " )
  if 83 - 83: OOooOOo / O0 % iII111i - o0oOOo0O0Ooo . Oo0Ooo
  Iii += ( "sudo ip6tables -A POSTROUTING -t mangle -p tcp -j " + "CHECKSUM --checksum-fill; " )
  if 49 - 49: iIii1I11I1II1 * i1IIi . OoooooooOO
  Iii += ( "sudo ip6tables -A POSTROUTING -t mangle -p udp -j " + "CHECKSUM --checksum-fill" )
  if 90 - 90: o0oOOo0O0Ooo % I1ii11iIi11i - iIii1I11I1II1 % OoOoOO00
  os . system ( Iii )
  IIiI11I1I1i1i = lisp . bold ( "virtio" , False )
  lisp . lprint ( "{} bug workaround, configure '{}'" . format ( IIiI11I1I1i1i , Iii ) )
  if 86 - 86: i1IIi
 return
 if 13 - 13: O0
 if 70 - 70: Ii1I . i11iIiiIii % Ii1I . O0 - iIii1I11I1II1
 if 26 - 26: OOooOOo
 if 76 - 76: i1IIi * OoooooooOO * O0 + I1Ii111 * I1Ii111
 if 35 - 35: o0oOOo0O0Ooo
 if 73 - 73: O0 - I1ii11iIi11i
 if 2 - 2: II111iiii / I1Ii111
def o0o0o0o0 ( sources , dyn_eids , l2_overlay , pitr ) :
 if ( l2_overlay ) :
  O00oO0 = "ether[6:4] >= 0 and ether[10:2] >= 0"
  lisp . lprint ( "Using pcap filter: '{}'" . format ( O00oO0 ) )
  return ( O00oO0 )
  if 54 - 54: i1IIi . I11i - I1ii11iIi11i + ooOoO0o + Oo0Ooo / Oo0Ooo
  if 22 - 22: ooOoO0o . iIii1I11I1II1
 i1IiiiiIi1I = "(not ether proto 0x806)"
 Oo = " or (udp src port 4342 and ip[28] == 0x28)"
 ooo0O0o0OoOO = " or (ip[16] >= 224 and ip[16] < 240 and (ip[28] & 0xf0) == 0x30)"
 if 9 - 9: OoO0O00
 if 60 - 60: I1Ii111
 oOO0o00o0Oo0O = ""
 iIIi1iiII = ""
 for ooOooo000OO00 in sources :
  iiO0oOoo = ooOooo000OO00
  if ( lisp . lisp_is_mac_string ( ooOooo000OO00 ) ) :
   iiO0oOoo = ooOooo000OO00 . split ( "/" ) [ 0 ]
   iiO0oOoo = iiO0oOoo . replace ( "-" , "" )
   OoOOoO0O0oO = [ ]
   for OOOooo0OooOoO in range ( 0 , 12 , 2 ) : OoOOoO0O0oO . append ( iiO0oOoo [ OOOooo0OooOoO : OOOooo0OooOoO + 2 ] )
   iiO0oOoo = "ether host " + ":" . join ( OoOOoO0O0oO )
   if 92 - 92: Oo0Ooo / i11iIiiIii + I1ii11iIi11i
   if 87 - 87: OoOoOO00 % iIii1I11I1II1
  oOO0o00o0Oo0O += "{}" . format ( iiO0oOoo )
  if ( ooOooo000OO00 not in dyn_eids ) : iIIi1iiII += "{}" . format ( iiO0oOoo )
  if ( sources [ - 1 ] == ooOooo000OO00 ) : break
  oOO0o00o0Oo0O += " or "
  if ( ooOooo000OO00 not in dyn_eids ) : iIIi1iiII += " or "
  if 72 - 72: OOooOOo . OOooOOo - I1ii11iIi11i
 if ( iIIi1iiII [ - 4 : : ] == " or " ) : iIIi1iiII = iIIi1iiII [ 0 : - 4 ]
 if 48 - 48: Oo0Ooo - ooOoO0o + Oo0Ooo - I1IiiI * i11iIiiIii . iII111i
 if 35 - 35: IiII . O0 + Oo0Ooo + OOooOOo + i1IIi
 if 65 - 65: O0 * I1IiiI / I1IiiI . OoOoOO00
 if 87 - 87: II111iiii * I1ii11iIi11i % Oo0Ooo * Oo0Ooo
 if 58 - 58: OOooOOo . o0oOOo0O0Ooo + I1IiiI % Oo0Ooo - OoO0O00
 if 50 - 50: iII111i % II111iiii - ooOoO0o . i1IIi + O0 % iII111i
 i1iIi1IIiIII1 = getoutput ( "egrep 'lisp-nat = yes' ./lisp.config" )
 i1iIi1IIiIII1 = ( i1iIi1IIiIII1 != "" and i1iIi1IIiIII1 [ 0 ] == " " )
 i1Ii11I1II = lisp . lisp_get_loopback_address ( ) if ( i1iIi1IIiIII1 ) else None
 if 77 - 77: oO0o - Oo0Ooo - iIii1I11I1II1
 IIi1i = ""
 iIiIIiii1II = lisp . lisp_get_all_addresses ( )
 for Ii in iIiIIiii1II :
  if ( Ii == i1Ii11I1II ) : continue
  IIi1i += "{}" . format ( Ii )
  if ( iIiIIiii1II [ - 1 ] == Ii ) : break
  IIi1i += " or "
  if 44 - 44: OoooooooOO . II111iiii . OOooOOo % OoooooooOO
  if 86 - 86: i11iIiiIii + O0 * IiII - OoO0O00 * OOooOOo + O0
 if ( oOO0o00o0Oo0O != "" ) :
  oOO0o00o0Oo0O = " and (src net {})" . format ( oOO0o00o0Oo0O )
  if 95 - 95: iIii1I11I1II1 . I1Ii111 % iII111i - I1Ii111 * II111iiii
 if ( iIIi1iiII != "" ) :
  iIIi1iiII = " and not (dst net {})" . format ( iIIi1iiII )
  if 89 - 89: iII111i . I1IiiI
 if ( IIi1i != "" ) :
  IIi1i = " and not (dst host {})" . format ( IIi1i )
  if 59 - 59: i1IIi % iIii1I11I1II1 + OoooooooOO
  if 97 - 97: I1ii11iIi11i / Oo0Ooo + I1Ii111
  if 32 - 32: ooOoO0o % I1Ii111 * Oo0Ooo
  if 72 - 72: ooOoO0o . iII111i - I1Ii111 - Ii1I % i1IIi
  if 56 - 56: Oo0Ooo * iII111i
  if 13 - 13: Oo0Ooo * Oo0Ooo * II111iiii * iII111i . i1IIi / IiII
  if 92 - 92: Ii1I * i11iIiiIii + iII111i * I1Ii111
 if ( pitr ) :
  iIIi1iiII = ""
  IIi1i = IIi1i . replace ( "dst " , "" )
  if 48 - 48: I11i * iII111i * iII111i
  if 70 - 70: oO0o + I11i % i11iIiiIii + O0
  if 65 - 65: iIii1I11I1II1 % oO0o + O0 / OoooooooOO
  if 52 - 52: Ii1I % OOooOOo * I1IiiI % I11i + OOooOOo / iII111i
  if 80 - 80: OoooooooOO + IiII
 O00oO0 = i1IiiiiIi1I + oOO0o00o0Oo0O + iIIi1iiII + IIi1i
 O00oO0 += Oo
 O00oO0 += ooo0O0o0OoOO
 if 95 - 95: I1Ii111 / oO0o * I1Ii111 - OoooooooOO * OoooooooOO % OoO0O00
 lisp . lprint ( "Using pcap filter: '{}'" . format ( O00oO0 ) )
 return ( O00oO0 )
 if 43 - 43: Oo0Ooo . I1Ii111
 if 12 - 12: I1Ii111 + OOooOOo + I11i . IiII / Ii1I
 if 29 - 29: IiII . ooOoO0o - II111iiii
 if 68 - 68: iIii1I11I1II1 + II111iiii / oO0o
 if 91 - 91: OoOoOO00 % iIii1I11I1II1 . I1IiiI
 if 70 - 70: I11i % II111iiii % O0 . i1IIi / I1Ii111
 if 100 - 100: I1ii11iIi11i * i11iIiiIii % oO0o / Oo0Ooo / ooOoO0o + I1ii11iIi11i
def OooOo00o ( device , pfilter , pcap_lock ) :
 lisp . lisp_set_exception ( )
 if 59 - 59: I1Ii111 - IiII
 if ( lisp . lisp_is_python2 ( ) ) :
  import pcappy
  pcap_lock . acquire ( )
  iiiii111 = pcappy . open_live ( device , 9000 , 0 , 100 )
  pcap_lock . release ( )
  iiiii111 . filter = pfilter
  iiiii111 . loop ( - 1 , I11oOOooo , device )
  if 93 - 93: oO0o * Ii1I
 if ( lisp . lisp_is_python3 ( ) ) :
  import pcapy
  pcap_lock . acquire ( )
  iiiii111 = pcapy . open_live ( device , 9000 , 0 , 100 )
  pcap_lock . release ( )
  iiiii111 . setfilter ( pfilter )
  while ( True ) :
   ii11i1I1iiii , I11iI1I = iiiii111 . next ( )
   if ( len ( I11iI1I ) == 0 ) : continue
   I11oOOooo ( device , None , I11iI1I )
   if 50 - 50: iIii1I11I1II1 * IiII . OoooooooOO / II111iiii - I1ii11iIi11i * I1ii11iIi11i
   if 98 - 98: OoO0O00 - Ii1I . IiII % i11iIiiIii
 return
 if 69 - 69: I1ii11iIi11i + iII111i * O0 . OOooOOo % OoOoOO00
 if 96 - 96: ooOoO0o . ooOoO0o - I11i / I11i
 if 96 - 96: i11iIiiIii / I1IiiI - O0 . ooOoO0o
 if 39 - 39: ooOoO0o / O0 * IiII
 if 17 - 17: Ii1I / iIii1I11I1II1 - OoO0O00 + I1IiiI % OOooOOo
 if 14 - 14: o0oOOo0O0Ooo % IiII + I1ii11iIi11i + OoO0O00
 if 76 - 76: OoO0O00 - i11iIiiIii + OoOoOO00 + OOooOOo / OoooooooOO
 if 50 - 50: II111iiii - I1Ii111 + iIii1I11I1II1 + iIii1I11I1II1
 if 91 - 91: II111iiii - O0 . iIii1I11I1II1 . O0 + I1ii11iIi11i - II111iiii
def iiIiiIi1 ( ) :
 global Oo0o0000o0o0
 global II1Ii1iI1i
 global II1iII1i
 if 30 - 30: OOooOOo + II111iiii - IiII * OoooooooOO
 lisp . lisp_set_exception ( )
 if 19 - 19: IiII - o0oOOo0O0Ooo . iIii1I11I1II1 . OoOoOO00 / OOooOOo
 if 87 - 87: OoOoOO00 - ooOoO0o - OOooOOo + Oo0Ooo % iIii1I11I1II1 / i11iIiiIii
 if 12 - 12: ooOoO0o
 if 86 - 86: oO0o - OoO0O00
 if 63 - 63: I1IiiI / OoOoOO00 + OoooooooOO . I11i . ooOoO0o
 IiI1iiI11 = [ II1Ii1iI1i , II1Ii1iI1i ,
 oO0oIIII ]
 lisp . lisp_build_info_requests ( IiI1iiI11 , None , lisp . LISP_CTRL_PORT )
 if 85 - 85: I1ii11iIi11i - OoOoOO00 / I1ii11iIi11i + OOooOOo - iII111i
 if 49 - 49: OoO0O00 - O0 / OoO0O00 * OoOoOO00 + I1Ii111
 if 35 - 35: II111iiii . I1IiiI / i1IIi / I1IiiI * oO0o
 if 85 - 85: II111iiii . ooOoO0o % OOooOOo % I11i
 Oo0o0000o0o0 . cancel ( )
 Oo0o0000o0o0 = threading . Timer ( lisp . LISP_INFO_INTERVAL ,
 iiIiiIi1 , [ ] )
 Oo0o0000o0o0 . start ( )
 return
 if 80 - 80: oO0o * I11i / iIii1I11I1II1 % oO0o / iIii1I11I1II1
 if 42 - 42: i1IIi / i11iIiiIii . Oo0Ooo * iII111i . i11iIiiIii * O0
 if 44 - 44: i1IIi . I1IiiI / i11iIiiIii + IiII
 if 27 - 27: OOooOOo
 if 52 - 52: I1Ii111 % OoOoOO00 + iIii1I11I1II1 * oO0o . Ii1I
 if 95 - 95: iIii1I11I1II1 . IiII - OoooooooOO * OoO0O00 / o0oOOo0O0Ooo
 if 74 - 74: oO0o
def iII1i1IIiI1I ( kv_pair ) :
 global II1iII1i
 global OOo
 global Oo0o0000o0o0
 if 67 - 67: Ii1I
 lispconfig . lisp_map_resolver_command ( kv_pair )
 if 43 - 43: OoO0O00 % OoO0O00
 if ( lisp . lisp_test_mr_timer == None or
 lisp . lisp_test_mr_timer . is_alive ( ) == False ) :
  lisp . lisp_test_mr_timer = threading . Timer ( 2 , lisp . lisp_test_mr ,
 [ II1iII1i , OOo ] )
  lisp . lisp_test_mr_timer . start ( )
  if 46 - 46: Oo0Ooo % iIii1I11I1II1 . iII111i . O0 * ooOoO0o / OoooooooOO
  if 7 - 7: oO0o - O0 * I11i - o0oOOo0O0Ooo - II111iiii
  if 41 - 41: I1IiiI - I1Ii111 % II111iiii . I1Ii111 - I11i
  if 45 - 45: Ii1I - OOooOOo
  if 70 - 70: OoO0O00 % I1IiiI / I1IiiI . I11i % ooOoO0o . II111iiii
 Oo0o0000o0o0 = threading . Timer ( 0 , iiIiiIi1 , [ ] )
 Oo0o0000o0o0 . start ( )
 return
 if 10 - 10: Ii1I - i11iIiiIii . I1ii11iIi11i % i1IIi
 if 78 - 78: iIii1I11I1II1 * Oo0Ooo . Oo0Ooo - OOooOOo . iIii1I11I1II1
 if 30 - 30: ooOoO0o + ooOoO0o % IiII - o0oOOo0O0Ooo - I1ii11iIi11i
 if 36 - 36: I11i % OOooOOo
 if 72 - 72: I1IiiI / iII111i - O0 + I11i
 if 83 - 83: O0
 if 89 - 89: Oo0Ooo + I1ii11iIi11i - o0oOOo0O0Ooo
 if 40 - 40: OoO0O00 + OoO0O00
def o0oo0o00ooO00 ( kv_pair ) :
 lispconfig . lisp_database_mapping_command ( kv_pair )
 return
 if 37 - 37: OoO0O00 - I1ii11iIi11i . OoooooooOO . ooOoO0o + OoOoOO00 / Ii1I
 if 15 - 15: IiII . i1IIi * OoOoOO00 % iIii1I11I1II1
 if 35 - 35: I1ii11iIi11i + I1Ii111 - OoOoOO00 % oO0o % o0oOOo0O0Ooo % OoOoOO00
 if 45 - 45: I1IiiI * OOooOOo % OoO0O00
 if 24 - 24: ooOoO0o - I11i * oO0o
 if 87 - 87: Ii1I - I1ii11iIi11i % I1ii11iIi11i . oO0o / I1ii11iIi11i
 if 6 - 6: OoOoOO00 / iIii1I11I1II1 * OoooooooOO * i11iIiiIii
 if 79 - 79: IiII % OoO0O00
def Oo0oOO ( kv_pair ) :
 global iiI1iIiI , i111I
 global oO0oIIII , Oooo0000
 if 86 - 86: iIii1I11I1II1 / O0
 if 17 - 17: II111iiii
 if 9 - 9: OoooooooOO + oO0o
 if 33 - 33: O0
 if 39 - 39: I1IiiI + Oo0Ooo
 o0OO = lisp . lisp_nat_traversal
 ooO = lisp . lisp_rloc_probing
 if 41 - 41: i1IIi + II111iiii * ooOoO0o
 if 68 - 68: Ii1I - I1IiiI
 if 41 - 41: oO0o
 if 21 - 21: ooOoO0o + o0oOOo0O0Ooo % I1Ii111 + i11iIiiIii + iII111i + II111iiii
 lispconfig . lisp_xtr_command ( kv_pair )
 if 98 - 98: I1Ii111
 if 49 - 49: Oo0Ooo * oO0o + o0oOOo0O0Ooo - i11iIiiIii
 if 74 - 74: Oo0Ooo / iIii1I11I1II1 . II111iiii - OoO0O00
 if 62 - 62: OOooOOo / II111iiii + OoOoOO00 % ooOoO0o / OoOoOO00 + I1ii11iIi11i
 IiI11I111 = ( o0OO == False and lisp . lisp_nat_traversal and lisp . lisp_rloc_probing )
 if 54 - 54: O0 - iII111i . OOooOOo % iII111i + iII111i
 i1iI1Iiii1I = ( ooO == False and lisp . lisp_rloc_probing )
 if 9 - 9: I11i / OoOoOO00 / II111iiii + I1Ii111
 o0O0 = 0
 if ( i1iI1Iiii1I ) : o0O0 = 1
 if ( IiI11I111 ) : o0O0 = 5
 if 57 - 57: OOooOOo - OOooOOo - I1ii11iIi11i
 if ( o0O0 != 0 ) :
  iio0o000Oo = [ iiI1iIiI , i111I ,
 oO0oIIII , Oooo0000 ]
  lisp . lisp_start_rloc_probe_timer ( o0O0 , iio0o000Oo )
  if 57 - 57: oO0o * O0 * I1Ii111
  if 44 - 44: OOooOOo / Oo0Ooo + IiII % II111iiii / OoO0O00 + i11iIiiIii
  if 20 - 20: I1ii11iIi11i
  if 3 - 3: OoO0O00 * i1IIi . I1IiiI . O0 - OoOoOO00
  if 81 - 81: I1IiiI - iIii1I11I1II1 / I1IiiI / O0
  if 34 - 34: Ii1I * Ii1I - I1ii11iIi11i - O0 . i11iIiiIii
  if 32 - 32: iIii1I11I1II1 . OoO0O00 * oO0o / OOooOOo . II111iiii - Oo0Ooo
 if ( lisp . lisp_crypto_ephem_port == None and lisp . lisp_data_plane_security ) :
  IiIiI1I1I1 = i111I . getsockname ( ) [ 1 ]
  lisp . lisp_crypto_ephem_port = IiIiI1I1I1
  lisp . lprint ( "Use port {} for lisp-crypto packets" . format ( IiIiI1I1I1 ) )
  IIIi = { "type" : "itr-crypto-port" , "port" : IiIiI1I1I1 }
  lisp . lisp_write_to_dp_socket ( IIIi )
  if 39 - 39: oO0o * I1Ii111 + OoOoOO00 % OoooooooOO / iIii1I11I1II1
  if 60 - 60: Ii1I
  if 20 - 20: II111iiii - I11i + i1IIi + Ii1I
  if 7 - 7: ooOoO0o + Ii1I
  if 32 - 32: iIii1I11I1II1 % I1IiiI / i11iIiiIii + OOooOOo - o0oOOo0O0Ooo . iII111i
 lisp . lisp_ipc_write_xtr_parameters ( lisp . lisp_debug_logging ,
 lisp . lisp_data_plane_logging )
 return
 if 86 - 86: i1IIi / Ii1I * I1IiiI
 if 67 - 67: I1ii11iIi11i * I1ii11iIi11i / oO0o * OoooooooOO + OoOoOO00
 if 79 - 79: i1IIi
 if 1 - 1: oO0o / i1IIi
 if 74 - 74: I11i / OoooooooOO / Oo0Ooo * i11iIiiIii . II111iiii . OoooooooOO
 if 59 - 59: i11iIiiIii . OoooooooOO / I11i * I1ii11iIi11i + OoooooooOO
 if 3 - 3: i11iIiiIii * Oo0Ooo % iIii1I11I1II1 % I1IiiI * iII111i / OOooOOo
 if 95 - 95: IiII * O0 * I1Ii111 . OoooooooOO % Oo0Ooo + I1ii11iIi11i
 if 98 - 98: oO0o . OoooooooOO
 if 54 - 54: O0 / IiII % ooOoO0o * i1IIi * O0
 if 48 - 48: o0oOOo0O0Ooo . oO0o % OoOoOO00 - OoOoOO00
def i1IiI1Iiii ( ipc ) :
 o0O0O , oOOoOOO0oOoo , o0 , IiIIIIIIiI = ipc . split ( "%" )
 IiIIIIIIiI = int ( IiIIIIIIiI , 16 )
 if 52 - 52: I1Ii111 % O0 . i1IIi . OoooooooOO
 i1i111111ii = lisp . lisp_get_echo_nonce ( None , o0 )
 if ( i1i111111ii == None ) : i1i111111ii = lisp . lisp_echo_nonce ( o0 )
 if 83 - 83: OoO0O00 + OOooOOo - o0oOOo0O0Ooo + iIii1I11I1II1 % Oo0Ooo
 if 23 - 23: o0oOOo0O0Ooo + Ii1I % OoOoOO00 % I1IiiI % OoooooooOO
 if 78 - 78: OoO0O00 / Oo0Ooo - iIii1I11I1II1 - i11iIiiIii * iII111i
 if 84 - 84: OOooOOo + Ii1I + o0oOOo0O0Ooo
 if 33 - 33: Ii1I
 if ( oOOoOOO0oOoo == "R" ) :
  i1i111111ii . request_nonce_rcvd = IiIIIIIIiI
  i1i111111ii . last_request_nonce_rcvd = lisp . lisp_get_timestamp ( )
  i1i111111ii . echo_nonce_sent = IiIIIIIIiI
  i1i111111ii . last_new_echo_nonce_sent = lisp . lisp_get_timestamp ( )
  lisp . lprint ( "Start echo-nonce mode for {}, nonce 0x{}" . format ( lisp . red ( i1i111111ii . rloc_str , False ) , lisp . lisp_hex_string ( IiIIIIIIiI ) ) )
  if 93 - 93: ooOoO0o
  if 34 - 34: oO0o - ooOoO0o * Oo0Ooo / o0oOOo0O0Ooo
  if 19 - 19: I1ii11iIi11i
 if ( oOOoOOO0oOoo == "E" ) :
  i1i111111ii . echo_nonce_rcvd = IiIIIIIIiI
  i1i111111ii . last_echo_nonce_rcvd = lisp . lisp_get_timestamp ( )
  if 46 - 46: iIii1I11I1II1 . i11iIiiIii - OoOoOO00 % O0 / II111iiii * i1IIi
  if ( i1i111111ii . request_nonce_sent == IiIIIIIIiI ) :
   oO = lisp . bold ( "echoed nonce" , False )
   lisp . lprint ( "Received {} {} from {}" . format ( oO ,
 lisp . lisp_hex_string ( IiIIIIIIiI ) ,
 lisp . red ( i1i111111ii . rloc_str , False ) ) )
   if 18 - 18: OoooooooOO + o0oOOo0O0Ooo . O0 + IiII * i1IIi . OoO0O00
   i1i111111ii . request_nonce_sent = None
   lisp . lprint ( "Stop request-nonce mode for {}" . format ( lisp . red ( i1i111111ii . rloc_str , False ) ) )
   if 71 - 71: I1Ii111 - o0oOOo0O0Ooo - OOooOOo
   i1i111111ii . last_good_echo_nonce_rcvd = lisp . lisp_get_timestamp ( )
  else :
   iiI = "none"
   if ( i1i111111ii . request_nonce_sent ) :
    iiI = lisp . lisp_hex_string ( i1i111111ii . request_nonce_sent )
    if 81 - 81: IiII * I1ii11iIi11i + II111iiii % IiII
   lisp . lprint ( ( "Received echo-nonce 0x{} from {}, but request-" + "nonce is {}" ) . format ( lisp . lisp_hex_string ( IiIIIIIIiI ) ,
   # I11i % oO0o / iII111i
 lisp . red ( i1i111111ii . rloc_str , False ) , iiI ) )
   if 18 - 18: I11i * OoOoOO00
   if 92 - 92: Oo0Ooo - I1Ii111
 return
 if 24 - 24: oO0o / I1Ii111 / I11i % OoOoOO00 / I1ii11iIi11i * ooOoO0o
 if 8 - 8: Ii1I
 if 33 - 33: o0oOOo0O0Ooo / O0 + OOooOOo
 if 75 - 75: IiII % i11iIiiIii + iIii1I11I1II1
 if 92 - 92: OoOoOO00 % O0
oo00ooooOOo00 = {
 "lisp xtr-parameters" : [ Oo0oOO , {
 "rloc-probing" : [ True , "yes" , "no" ] ,
 "nonce-echoing" : [ True , "yes" , "no" ] ,
 "data-plane-security" : [ True , "yes" , "no" ] ,
 "data-plane-logging" : [ True , "yes" , "no" ] ,
 "frame-logging" : [ True , "yes" , "no" ] ,
 "flow-logging" : [ True , "yes" , "no" ] ,
 "nat-traversal" : [ True , "yes" , "no" ] ,
 "decentralized-nat" : [ True , "yes" , "no" ] ,
 "checkpoint-map-cache" : [ True , "yes" , "no" ] ,
 "ipc-data-plane" : [ True , "yes" , "no" ] ,
 "decentralized-push-xtr" : [ True , "yes" , "no" ] ,
 "decentralized-pull-xtr-modulus" : [ True , 1 , 0xff ] ,
 "decentralized-pull-xtr-dns-suffix" : [ True ] ,
 "register-reachable-rtrs" : [ True , "yes" , "no" ] ,
 "program-hardware" : [ True , "yes" , "no" ] } ] ,

 "lisp interface" : [ lispconfig . lisp_interface_command , {
 "interface-name" : [ True ] ,
 "device" : [ True ] ,
 "instance-id" : [ True , 0 , 0xffffffff ] ,
 "dynamic-eid" : [ True ] ,
 "multi-tenant-eid" : [ True ] ,
 "lisp-nat" : [ True , "yes" , "no" ] ,
 "dynamic-eid-device" : [ True ] ,
 "dynamic-eid-timeout" : [ True , 0 , 0xff ] } ] ,

 "lisp map-resolver" : [ iII1i1IIiI1I , {
 "mr-name" : [ True ] ,
 "ms-name" : [ True ] ,
 "dns-name" : [ True ] ,
 "address" : [ True ] } ] ,

 "lisp map-server" : [ lispconfig . lisp_map_server_command , {
 "ms-name" : [ True ] ,
 "address" : [ True ] ,
 "dns-name" : [ True ] ,
 "authentication-type" : [ False , "sha1" , "sha2" ] ,
 "authentication-key" : [ False ] ,
 "encryption-key" : [ False ] ,
 "proxy-reply" : [ False , "yes" , "no" ] ,
 "want-map-notify" : [ False , "yes" , "no" ] ,
 "merge-registrations" : [ False , "yes" , "no" ] ,
 "refresh-registrations" : [ False , "yes" , "no" ] ,
 "site-id" : [ False , 1 , 0xffffffffffffffff ] } ] ,

 "lisp database-mapping" : [ o0oo0o00ooO00 , {
 "prefix" : [ ] ,
 "mr-name" : [ True ] ,
 "ms-name" : [ True ] ,
 "instance-id" : [ True , 0 , 0xffffffff ] ,
 "secondary-instance-id" : [ True , 0 , 0xffffffff ] ,
 "eid-prefix" : [ True ] ,
 "group-prefix" : [ True ] ,
 "dynamic-eid" : [ True , "yes" , "no" ] ,
 "signature-eid" : [ True , "yes" , "no" ] ,
 "register-ttl" : [ True , 1 , 0xffffffff ] ,
 "rloc" : [ ] ,
 "rloc-record-name" : [ True ] ,
 "elp-name" : [ True ] ,
 "geo-name" : [ True ] ,
 "rle-name" : [ True ] ,
 "json-name" : [ True ] ,
 "address" : [ True ] ,
 "interface" : [ True ] ,
 "priority" : [ True , 0 , 255 ] ,
 "weight" : [ True , 0 , 100 ] } ] ,

 "lisp map-cache" : [ lispconfig . lisp_map_cache_command , {
 "prefix" : [ ] ,
 "instance-id" : [ True , 0 , 0xffffffff ] ,
 "eid-prefix" : [ True ] ,
 "group-prefix" : [ True ] ,
 "send-map-request" : [ True , "yes" , "no" ] ,
 "subscribe-request" : [ True , "yes" , "no" ] ,
 "rloc" : [ ] ,
 "rloc-record-name" : [ True ] ,
 "rle-name" : [ True ] ,
 "elp-name" : [ True ] ,
 "address" : [ True ] ,
 "priority" : [ True , 0 , 255 ] ,
 "weight" : [ True , 0 , 100 ] } ] ,

 "lisp itr-map-cache" : [ lispconfig . lisp_map_cache_command , {
 "prefix" : [ ] ,
 "instance-id" : [ True , 0 , 0xffffffff ] ,
 "eid-prefix" : [ True ] ,
 "group-prefix" : [ True ] ,
 "rloc" : [ ] ,
 "rloc-record-name" : [ True ] ,
 "rle-name" : [ True ] ,
 "elp-name" : [ True ] ,
 "address" : [ True ] ,
 "priority" : [ True , 0 , 255 ] ,
 "weight" : [ True , 0 , 100 ] } ] ,

 "lisp explicit-locator-path" : [ lispconfig . lisp_elp_command , {
 "elp-name" : [ False ] ,
 "elp-node" : [ ] ,
 "address" : [ True ] ,
 "probe" : [ True , "yes" , "no" ] ,
 "strict" : [ True , "yes" , "no" ] ,
 "eid" : [ True , "yes" , "no" ] } ] ,

 "lisp replication-list-entry" : [ lispconfig . lisp_rle_command , {
 "rle-name" : [ False ] ,
 "rle-node" : [ ] ,
 "address" : [ True ] ,
 "level" : [ True , 0 , 255 ] } ] ,

 "lisp geo-coordinates" : [ lispconfig . lisp_geo_command , {
 "geo-name" : [ False ] ,
 "geo-tag" : [ False ] } ] ,

 "lisp json" : [ lispconfig . lisp_json_command , {
 "json-name" : [ False ] ,
 "json-string" : [ False ] } ] ,

 "show itr-map-cache" : [ ii1I , { } ] ,
 "show itr-rloc-probing" : [ Oo0O0OOOoo , { } ] ,
 "show itr-keys" : [ oO00O00o0OOO0 , { } ] ,
 "show itr-dynamic-eid" : [ lispconfig . lisp_show_dynamic_eid_command , { } ]
 }
if 16 - 16: i11iIiiIii / i1IIi % OOooOOo
if 84 - 84: I11i - Oo0Ooo * O0 / Ii1I . Ii1I
if 93 - 93: O0 / ooOoO0o + I1IiiI
if 20 - 20: IiII / iII111i % OoooooooOO / iIii1I11I1II1 + I1IiiI
if 57 - 57: o0oOOo0O0Ooo / I1Ii111
if 13 - 13: OoooooooOO + OoO0O00
if ( O00oO000O0O ( ) == False ) :
 lisp . lprint ( "lisp_itr_startup() failed" )
 lisp . lisp_print_banner ( "ITR abnormal exit" )
 exit ( 1 )
 if 32 - 32: O0 + oO0o % Oo0Ooo
 if 7 - 7: I1ii11iIi11i / ooOoO0o
I1i1I11111iI1 = [ i111I , oO0oIIII ,
 II1Ii1iI1i , Oo0oO0oo0oO00 ]
if 32 - 32: I1IiiI + I1ii11iIi11i - oO0o + I1ii11iIi11i / i1IIi * oO0o
if 90 - 90: Ii1I % oO0o
if 6 - 6: OoooooooOO / i11iIiiIii / I1Ii111
if 60 - 60: I1IiiI % oO0o / o0oOOo0O0Ooo % oO0o * i11iIiiIii / iII111i
i1Ii11II = True
i1iiiiI11ii = [ i111I ] * 3
oooooOOo0o = [ II1Ii1iI1i , II1Ii1iI1i ,
 oO0oIIII ]
if 98 - 98: OoO0O00 / I11i - Ii1I
while ( True ) :
 try : OO , OOo0oOOOOooOo , o0O0O = select . select ( I1i1I11111iI1 , [ ] , [ ] )
 except : break
 if 19 - 19: o0oOOo0O0Ooo
 if 73 - 73: I1Ii111 * Oo0Ooo * OoOoOO00
 if 65 - 65: i11iIiiIii + Oo0Ooo * OoooooooOO - OoO0O00
 if 26 - 26: o0oOOo0O0Ooo % OOooOOo + OOooOOo % I11i * i11iIiiIii / iII111i
 if ( lisp . lisp_ipc_data_plane and Oo0oO0oo0oO00 in OO ) :
  lisp . lisp_process_punt ( Oo0oO0oo0oO00 , II1iII1i ,
 OOo )
  if 64 - 64: oO0o % OoOoOO00 / II111iiii % ooOoO0o - iII111i
  if 2 - 2: I1Ii111 - I1ii11iIi11i + o0oOOo0O0Ooo * OoO0O00 / iII111i
  if 26 - 26: OOooOOo * Oo0Ooo
  if 31 - 31: I11i * oO0o . Ii1I
  if 35 - 35: I11i
 if ( i111I in OO ) :
  oOOoOOO0oOoo , ooOooo000OO00 , IiIiI1I1I1 , I11iI1I = lisp . lisp_receive ( i1iiiiI11ii [ 0 ] ,
 False )
  if ( ooOooo000OO00 == "" ) : break
  if 94 - 94: ooOoO0o / i11iIiiIii % O0
  if ( lisp . lisp_is_rloc_probe_reply ( I11iI1I [ 0 : 1 ] ) ) :
   lisp . lprint ( "ITR ignoring RLOC-probe reply, using pcap" )
   continue
   if 70 - 70: I11i - Oo0Ooo / OoooooooOO % OoooooooOO
  lisp . lisp_parse_packet ( i1iiiiI11ii , I11iI1I , ooOooo000OO00 , IiIiI1I1I1 )
  if 95 - 95: OoooooooOO % OoooooooOO . Ii1I
  if 26 - 26: oO0o + IiII - II111iiii . II111iiii + I1ii11iIi11i + OoOoOO00
  if 68 - 68: O0
  if 76 - 76: I1ii11iIi11i
  if 99 - 99: o0oOOo0O0Ooo
 if ( II1Ii1iI1i in OO ) :
  oOOoOOO0oOoo , ooOooo000OO00 , IiIiI1I1I1 , I11iI1I = lisp . lisp_receive ( oooooOOo0o [ 0 ] ,
 False )
  if ( ooOooo000OO00 == "" ) : break
  if 1 - 1: Ii1I * OoOoOO00 * OoO0O00 + Oo0Ooo
  if ( lisp . lisp_is_rloc_probe_reply ( I11iI1I [ 0 : 1 ] ) ) :
   lisp . lprint ( "ITR ignoring RLOC-probe reply, using pcap" )
   continue
   if 90 - 90: I1Ii111 % Oo0Ooo - Oo0Ooo . iIii1I11I1II1 / OOooOOo + I11i
  o0o00OOOO = lisp . lisp_parse_packet ( oooooOOo0o , I11iI1I , ooOooo000OO00 , IiIiI1I1I1 )
  if 42 - 42: ooOoO0o * iII111i
  if 2 - 2: iII111i . OoO0O00 / oO0o
  if 41 - 41: OoO0O00 . I1Ii111 * IiII * I1Ii111
  if 74 - 74: iIii1I11I1II1 / o0oOOo0O0Ooo
  if 58 - 58: iIii1I11I1II1 - I1IiiI % o0oOOo0O0Ooo % OoooooooOO * iIii1I11I1II1 + OOooOOo
  if ( o0o00OOOO ) :
   iio0o000Oo = [ iiI1iIiI , i111I ,
 oO0oIIII , Oooo0000 ]
   lisp . lisp_start_rloc_probe_timer ( 0 , iio0o000Oo )
   if 25 - 25: OOooOOo % O0
   if 44 - 44: I1Ii111 . Ii1I * II111iiii / IiII + iIii1I11I1II1
   if 14 - 14: O0 % IiII % Ii1I * oO0o
   if 65 - 65: I11i % oO0o + I1ii11iIi11i
   if 86 - 86: iIii1I11I1II1 / O0 . I1Ii111 % iIii1I11I1II1 % Oo0Ooo
   if 86 - 86: i11iIiiIii - o0oOOo0O0Ooo . ooOoO0o * Oo0Ooo / Ii1I % o0oOOo0O0Ooo
   if 61 - 61: o0oOOo0O0Ooo + OoOoOO00
 if ( oO0oIIII in OO ) :
  oOOoOOO0oOoo , ooOooo000OO00 , IiIiI1I1I1 , I11iI1I = lisp . lisp_receive ( oO0oIIII , True )
  if 15 - 15: OoOoOO00 * oO0o + OOooOOo . I11i % I1IiiI - ooOoO0o
  if ( ooOooo000OO00 == "" ) : break
  if 13 - 13: OoOoOO00 % OoOoOO00 % Oo0Ooo % I1IiiI * i1IIi % I11i
  if ( oOOoOOO0oOoo == "command" ) :
   I11iI1I = I11iI1I . decode ( )
   if ( I11iI1I == "clear" ) :
    lisp . lisp_clear_map_cache ( )
    continue
    if 82 - 82: IiII . OoOoOO00 / ooOoO0o + iII111i - ooOoO0o
   if ( I11iI1I . find ( "nonce%" ) != - 1 ) :
    i1IiI1Iiii ( I11iI1I )
    continue
    if 55 - 55: ooOoO0o % Oo0Ooo % o0oOOo0O0Ooo
   lispconfig . lisp_process_command ( oO0oIIII , oOOoOOO0oOoo ,
 I11iI1I , "lisp-itr" , [ oo00ooooOOo00 ] )
  elif ( oOOoOOO0oOoo == "api" ) :
   I11iI1I = I11iI1I . decode ( )
   lisp . lisp_process_api ( "lisp-itr" , oO0oIIII , I11iI1I )
  elif ( oOOoOOO0oOoo == "data-packet" ) :
   ii ( I11iI1I , "ipc" )
  else :
   if 29 - 29: IiII / iIii1I11I1II1 + I1ii11iIi11i % iII111i % I11i
   if 46 - 46: iIii1I11I1II1
   if 70 - 70: i1IIi . I11i
   if 74 - 74: I11i
   if 58 - 58: iIii1I11I1II1 * OoO0O00 * I1Ii111 * ooOoO0o . OoooooooOO
   if 6 - 6: I1ii11iIi11i - oO0o * i11iIiiIii + OoOoOO00 / ooOoO0o % OOooOOo
   if 38 - 38: OOooOOo % IiII % II111iiii - Oo0Ooo - iIii1I11I1II1
   if ( int ( IiIiI1I1I1 ) != lisp . LISP_DATA_PORT and
 lisp . lisp_is_rloc_probe_reply ( I11iI1I [ 0 : 1 ] ) ) :
    lisp . lprint ( "ITR ignoring RLOC-probe reply, using pcap" )
    continue
    if 9 - 9: o0oOOo0O0Ooo % I1ii11iIi11i . I1ii11iIi11i
   lisp . lisp_parse_packet ( II1iII1i , I11iI1I , ooOooo000OO00 , IiIiI1I1I1 )
   if 28 - 28: OoooooooOO % oO0o + I1ii11iIi11i + O0 . I1Ii111
   if 80 - 80: i11iIiiIii % I1ii11iIi11i
   if 54 - 54: o0oOOo0O0Ooo + I11i - iIii1I11I1II1 % ooOoO0o % IiII
   if 19 - 19: I1ii11iIi11i / iIii1I11I1II1 % i1IIi . OoooooooOO
   if 57 - 57: ooOoO0o . Oo0Ooo - OoO0O00 - i11iIiiIii * I1Ii111 / o0oOOo0O0Ooo
Ooo0oo ( )
lisp . lisp_print_banner ( "ITR normal exit" )
exit ( 0 )
if 79 - 79: I1ii11iIi11i + o0oOOo0O0Ooo % Oo0Ooo * o0oOOo0O0Ooo
if 21 - 21: iII111i
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
