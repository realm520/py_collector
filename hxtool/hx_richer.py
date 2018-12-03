#!/usr/bin/env python
# encoding=utf-8

from hxrpc import http_request

def get_account_balances():
    i = 42
    asset_hc = {}
    asset_hx = {}
    asset_ltc = {}
    while i <= 550:
        print("process 1.2.%d" % i)
        asset = http_request('get_account_balances', ['1.2.'+str(i)])
        if asset is None:
            break
        else:
            for t in asset:
                if t['asset_id'] == '1.3.3':
                    asset_hc['1.2.'+str(i)] = t['amount']
                elif t['asset_id'] == '1.3.0':
                    asset_hx['1.2.'+str(i)] = t['amount']
                elif t['asset_id'] == '1.3.2':
                    asset_ltc['1.2.'+str(i)] = t['amount']
        i += 1
    hc_richer = sorted(asset_hc.items(), key=lambda s: s[1], reverse=True)
    hx_richer = sorted(asset_hx.items(), key=lambda s: s[1], reverse=True)
    ltc_richer = sorted(asset_ltc.items(), key=lambda s: s[1], reverse=True)
    print("HC richer:")
    for i in hc_richer:
        if i[1] > 0:
            print(i)
    print("HX richer:")
    for i in hx_richer:
        if i[1] > 0:
            print(i)
    print("LTC richer:")
    for i in ltc_richer:
        if i[1] > 0:
            print(i)

def get_account_mortagage():
    citizens = http_request('list_citizens', [0, 1000])
    asset_hc = {}
    asset_hx = {}
    asset_ltc = {}
    for c in citizens:
        print("get locked info of " + str(c))
        lockedAssets = http_request('get_citizen_lockbalance_info', [c[0]])
        for a in lockedAssets:
            for item in a[1]:
                if int(item['amount']) > 0 and item['asset_id'] == '1.3.3':
                    if a[0] in asset_hc:
                        asset_hc[a[0]] += int(item['amount'])
                    else:
                        asset_hc[a[0]] = int(item['amount'])
                elif int(item['amount']) > 0 and item['asset_id'] == '1.3.0':
                    if a[0] in asset_hx:
                        asset_hx[a[0]] += int(item['amount'])
                    else:
                        asset_hx[a[0]] = int(item['amount'])
                elif int(item['amount']) > 0 and item['asset_id'] == '1.3.2':
                    if a[0] in asset_ltc:
                        asset_ltc[a[0]] += int(item['amount'])
                    else:
                        asset_ltc[a[0]] = int(item['amount'])
        #break
    hc_richer = sorted(asset_hc.items(), key=lambda s: s[1], reverse=True)
    hx_richer = sorted(asset_hx.items(), key=lambda s: s[1], reverse=True)
    ltc_richer = sorted(asset_ltc.items(), key=lambda s: s[1], reverse=True)
    print("HC richer:")
    for i in hc_richer:
        if i[1] > 0:
            print("User: %s,\tHC: %d" % (i[0], i[1]/100000000))
    print("HX richer:")
    for i in hx_richer:
        if i[1] > 0:
            print("User: %s,\tHX: %d" % (i[0], i[1]/100000))
    print("LTC richer:")
    for i in ltc_richer:
        if i[1] > 0:
            print(i)


if __name__ == '__main__':
    get_account_mortagage()