import requests
from lxml import html
import json

cookies = {
    'at': 'ZXlKcmFXUWlPaUl5SWl3aWRIbHdJam9pU2xkVUlpd2lZV3huSWpvaVVsTXlOVFlpZlEuZXlKemRXSWlPaUptT0RrNU56aGlaQzQwTlRoaUxqUTVPREF1T1RJMlppNDBNemt6TW1RNU1UQXpPR05tZWtsSVRXZElPV0UwSWl3aVlYQndUbUZ0WlNJNkltMTViblJ5WVNJc0ltbHpjeUk2SWtsRVJVRWlMQ0owYjJ0bGJsOTBlWEJsSWpvaVlYUWlMQ0p6ZEc5eVpVbGtJam9pTWpJNU55SXNJbXh6YVdRaU9pSTRPV1kwTTJZek15MWhOelEwTFRSaE1qVXRPR0U1TmkwNU5qbGtNV1ZoTjJNd01XVXRNVGMxT1RJd016a3dOREl5TUNJc0luQWlPaUl5TWprM0lpd2lZWFZrSWpvaWJYbHVkSEpoTFRBeVpEZGtaV00xTFRoaE1EQXROR00zTkMwNVkyWTNMVGxrTmpKa1ltVmhOV1UyTVNJc0luQndjeUk2TVRBc0ltTnBaSGdpT2lKdGVXNTBjbUV0TURKa04yUmxZelV0T0dFd01DMDBZemMwTFRsalpqY3RPV1EyTW1SaVpXRTFaVFl4SWl3aWMzVmlYM1I1Y0dVaU9qQXNJbk5qYjNCbElqb2lRa0ZUU1VNZ1VFOVNWRUZNSWl3aVpYaHdJam94TnpZMk5EQXlNalE0TENKdWFXUjRJam9pWTJGak0yUTJObU10T1dSaFppMHhNV1l3TFRoa1pqSXRaRFl4TnpJMk1EUXlNakExSWl3aWFXRjBJam94TnpZMk16azROalE0TENKMWFXUjRJam9pWmpnNU9UYzRZbVF1TkRVNFlpNDBPVGd3TGpreU5tWXVORE01TXpKa09URXdNemhqWm5wSlNFMW5TRGxoTkNKOS5mZEZUenFlSzdoMU5SQUpjUGtxbGREOVAwX1VicjFGOXFMNU5KOHhMd3BGeEZzY3djZEZ1d0pYZlhQZ0lDUVFMemxrNkQ3cXZIRjFkNlhRdERZYm9LaVhrMlpkeHVhdUtIcG5oYS1SUW5GYmZYc3lCN3pHYktGM0dSM2FHd1VfdU5OcXdjUllRYjV2RlRIV1JNQ1ZoT1ViZ3ZqOE1ZZmdZX09NVWJ5TEtVUTA=',
    'utrid': 'GV94HENADwUdD35iSh5AMCMyNjM5NDU1OTE4JDI%3D.9859f6159f92b76b0181420897b7a386',
    '_d_id': '27c92c95-0bb9-48cf-8e2a-7ad37bc4394a',
    '_abck': 'A77CCFB646B8F131DE4B5299B537AF46~0~YAAQtULHF+Xa9iibAQAAiWOQRQ8+9xb1HN1BK6zOSvpagi2UQQ87oaIlSpG9O1EnAVYcQWbXc13utnWZRzSzTpzU6lcQj8aMaKRvnWUF/N8UnEHAP65uQkaJin4glnS3c99s0EmBHf294BXG83tGujpBJ7K/Gj0TDX1mLdy2jH5CIKHDlmRzA3sIoUuZbdldssRG9CNtBa+xMNcccpKpqzqe8Pz212v/siutl3HKuCsRTYgMp1ZtX1SmuKNwhQeBXC82t2FKbZovzA8f/ZFbZ5D7dHtGSCF2/Bn78l3eqLu/AZYBHaflNIzBWuCOOaBcDxDpKDvkreIMdFJr0pdA4hyFIUvORHP9URKbYvksNvPG7veV015HhOt9U4mbX+zNd2IEmcxUoeWNZ7Djfy0fcivlv8Zh7G+2yBF/qzYb4Truw/z+1EiFj81DmLNLobQGr7XvGj8SKanYHK5TqHxD3dT6c1OZ7Tn54fUKbYsL0zcnv/UXYMtABqIM9enbcYd3ovZf63ox5+vD+u9XZHWcsvcv/YIU+zkDFWbYM1c0qpQnLrdoS9HeiYLGlEfj5YJ94jV7s4EUCleClPlYNRA3i9UBZ6G78XB+5VO6jTdA2Em2RVrGjn0PXrcaBM4CnZVieNou4rVnO2h6b91HjE6CWZnOJE4kV8y4gq/7FV4JfIf1E0SqDaXRQF/4eERB9FYWiFrqCrn1m2FTBpniCV6+qO0OJsyEED7Mb2+y9KYdcbS6ogzH7vg+39+Yg65z61aBmeMSUDTmDp/Gsy5biqHufYF+eY23jd5PLCkglEnadSiQR64tbLNfphBg~-1~-1~-1~AAQAAAAE%2f%2f%2f%2f%2fwtdk8Jo2ZSI19QDqQTtTV%2fFxmk69GwKirFebtJfhb+ZTjVG%2ffPnTRXkQrrHv2u0cFwe0l09NThd5ws%2fCoffVqIuUf6YNr4sZxiI~-1',
    'mynt-eupv': '1',
    '_xsrf': 'zcqDemZfoicf4iJMOJOZb5OKlShruR3C',
    'x-mynt-pca': 'J6KcjyQSXRxQrVSQ0XQ_ME6tvwBptMrylyBH58VGtlnNfrIhXHC0NawaQct4N8Vw5G8XbahSFDllzxKrj9mQlJafvCB0Vwcyj-nsX1ccIsBrbhv3owQJjqRxObVlYuFd1yD2i7QYQ8K6o4ZorIfVKI4dOjOMKqfDKpiF-z7PCn96DmlN3XYkUzsVxGwsNzMUlbWEtWLPyCb9n9CZMOSj5KDTrJl_8aAu',
    '_gcl_au': '1.1.993586219.1759203880.1706144040.1763575528.1763575527',
    'tvc_VID': '1',
    '_cs_c': '1',
    '_fbp': 'fb.1.1759203880751.106061031811714387',
    '_scid': 'oBIlkospsJ9CSYsx9vnhNK4n4RMgH_MU',
    '_sctr': '1%7C1766341800000',
    'G_ENABLED_IDPS': 'google',
    '__insp_wid': '617845923',
    '__insp_slim': '1759203886421',
    '__insp_nv': 'true',
    '__insp_targlpu': 'aHR0cHM6Ly93d3cubXludHJhLmNvbS9sb2dpbj9yZWZlcmVyPWh0dHBzJTNBJTJGJTJGd3d3Lm15bnRyYS5jb20lMkY%3D',
    '__insp_targlpt': 'TXludHJh',
    '__insp_norec_sess': 'true',
    'rt': 'ZXlKcmFXUWlPaUl5SWl3aWRIbHdJam9pU2xkVUlpd2lZV3huSWpvaVVsTXlOVFlpZlEuZXlKemRXSWlPaUptT0RrNU56aGlaQzQwTlRoaUxqUTVPREF1T1RJMlppNDBNemt6TW1RNU1UQXpPR05tZWtsSVRXZElPV0UwSWl3aWNuUnBkeUk2TWpNek1qZ3dNREFzSW1Gd2NFNWhiV1VpT2lKdGVXNTBjbUVpTENKcGMzTWlPaUpKUkVWQklpd2lkRzlyWlc1ZmRIbHdaU0k2SW5KMElpd2ljM1J2Y21WSlpDSTZJakl5T1RjaUxDSnNjMmxrSWpvaU9EbG1ORE5tTXpNdFlUYzBOQzAwWVRJMUxUaGhPVFl0T1RZNVpERmxZVGRqTURGbExURTNOVGt5TURNNU1EUXlNakFpTENKd0lqb2lNakk1TnlJc0ltRjFaQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKMGIyNGlPakUzTmpZek9UZzJORGdzSW5Cd2N5STZNVEFzSW5KMGRDSTZNU3dpWTJsa2VDSTZJbTE1Ym5SeVlTMHdNbVEzWkdWak5TMDRZVEF3TFRSak56UXRPV05tTnkwNVpEWXlaR0psWVRWbE5qRWlMQ0p6ZFdKZmRIbHdaU0k2TUN3aWMyTnZjR1VpT2lKQ1FWTkpReUJRVDFKVVFVd2lMQ0psZUhBaU9qRTNPRGszTWpZMk5EZ3NJbTVwWkhnaU9pSmpZV016WkRZMll5MDVaR0ZtTFRFeFpqQXRPR1JtTWkxa05qRTNNall3TkRJeU1EVWlMQ0pwWVhRaU9qRTNOall6T1RnMk5EZ3NJblZwWkhnaU9pSm1PRGs1TnpoaVpDNDBOVGhpTGpRNU9EQXVPVEkyWmk0ME16a3pNbVE1TVRBek9HTm1la2xJVFdkSU9XRTBJbjAuR2d3dnNibHFuRGJITnNTS2RTRmRlVkpWSFRmWE1sbjUxOG5fc3lQa09JQk9rUWhhd20zeVR5VkpOS2NMNWMtems2MFcwVG5MblhIMHZjUDBrN21YNUJHTjN0MHNaenRpd1dCemNBOWhrUXduYm04eVUyM09BQUxjU245Nmp1d2l3dHJlOWp3MHM2aWNxUGtYdE5NZ1ZyMDRQM1ZQLWVqNUU2ckRTQk1xR2dR',
    'ilgim': 'true',
    'ru': 'TlB0HEZIXlkEAn5oGgUdGFcCaR8fU1JVcHFbRlYPbGBzVXApKBBqPnQiFgIyWEAwIzI2Mzk0NTU5MTgkMg%3D%3D.8a1e6c3fdbd74edf5fc49828e75e6385',
    'user_uuid': 'f89978bd.458b.4980.926f.43932d91038cfzIHMgH9a4',
    'uidx': 'f89978bd.458b.4980.926f.43932d91038cfzIHMgH9a4',
    '_cs_ex': '1',
    '_ga': 'GA1.2.2065834106.1762789985',
    'user_transaction_ids': '1314748-9244066-3790403,1315453-8773259-8558001',
    '_gcl_aw': 'GCL.1765814119.EAIaIQobChMI8NeKq_m_kQMVOgl7Bx3klxsgEAQYBiABEgKjA_D_BwE',
    '_gcl_gs': '2.1.k1$i1765814118$u83349770',
    'mws': 'false',
    'oeeAnimationScreen': '%7B%22itemId%22%3A10721846901%7D',
    '__cab': 'cart.fsexp%3D',
    'ftc': 'false',
    'mynt-ulc-api': 'pincode%3A500028',
    'mynt-loc-src': 'expiry%3A1766400177651%7Csource%3AIP',
    'mynt-ulc': 'pincode:535001|addressId:177081639|lat:|long:|hexagonId:',
    'ak_RT': '"z=1&dm=myntra.com&si=31656015-dafa-44f4-940e-8a95c82227e9&ss=mjh05c9r&sl=8&tt=ai6&obo=2&rl=1&ld=sntl&r=kwaajgbe&ul=sntl"',
    'oai': '177081639',
    'oaui': '177081639:260303307',
    '_gid': 'GA1.2.1054245083.1766323083',
    '_mxab_': 'config.bucket%3Dregular%3Bpdp.desktop.savedAddress%3Denabled%3Bcoupon.cart.channelAware%3DchannelAware_Enabled%3Breturns.obd%3Denabled%3Brefund.tracker.myorders%3DTest%3Bcart.cartfiller.personalised%3Denabled%3Bpayments.mcotp.disable%3Denabled',
    'x-mynt-userConsent': '%7B%22blockingType%22%3Anull%7D',
    'lt_timeout': '1',
    'lt_session': '1',
    'ak_bmsc': 'FE8B5FCCE363B2F9E919A6EBCB86BE27~000000000000000000000000000000~YAAQtULHF9Pb9iibAQAAZmaQRR49bU/FPOrGl8ayZTc/5bRhMxkHQGbBFPwtuF/RWlW8p11DKN/Nr7wHyin3ZDWTsCyf59Ke2hvdpq685uabQE5JGRwrj039tXOKWu2VIAgD1WK8f1MONVWc/zbrTwbO2qhl/x65/ItWJFcwr98iLabdUtXm/3YScf+sP2QxM0ndXybAebR+6hPD4ajeQsvEf0KqgHrWYXkp1aKWGge3OBdvPfDh8f1HlVQ7HZQFIjzWtFGhHbjdAtT1Muh1bE1GNQnysmcxUUeNG9sm9BV63ZK5VgOlxPpIuWofByUqJPCsPPAmTYJMsNkFL0im8DfSqs3piRK+zaB7RhxMu/LDOJjqg4bI3m1C6IKWX9yr6wrnVxB5ZytQKoqf5a0Eq0LlvPEWTtpBvM4i/ZvzgDiHWSq8JJWF5AYtdHOTA6l+MWJ3chtdPnsglIW13A==',
    'bm_sz': 'A2A2950A476F601F72F7570D665EFB06~YAAQtULHF7E/9yibAQAAYbyRRR7MSqtOvWPbKTlppQWJFqouXDL1ZX0Qykjw9ev/PfPc+VkDeh9QRXvM/vesSaidK7PFeo7FeOAPKi5NwwFxOmvZ33HG2CALuwioeDMmFWl8PSymAw/0rIkeOUhAdrnnZt7PxBb6cJHPZRoBB2eRlA09+68Gj0zAWYxs4Fmv7lpdqiRXVConTH5yLPHfv+6uVRziCzUUUWFvZGL8CS6L+mg8rNnhzagYkbuw41nmXVAa/+TKvsWYBfJHzjcGmHK/0dqEmjtqb0MymglHObkJAAw+QNUI98iPRUjkv5S0kKgUv3MrU/cAF04dRJT/Tt8VsMS+4fEbDJYracwHGaIsu/sRjobwkQDi4FEgDGC+V+yWPKyaDWRqJoOrceN2t2LLFOx0MUp88GyeRRaq1hoCDfJFYpqLRqHxT03NxMGa3uRbuP237ks6109Cg8JnAQ==~4276546~3748161',
    '_ma_session': '%7B%22id%22%3A%22d7b7191b-fb93-4d35-8116-e8db6bce4a09-27c92c95-0bb9-48cf-8e2a-7ad37bc4394a%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D',
    'microsessid': '326',
    'bm_sv': '4D5B68D6C259E7A144583B3B2A49AEF5~YAAQtULHF9NA9yibAQAAg7+RRR5dl8oFAMMXrO1tbEHUHzic8S1GSpCR3faOp+aa7fqJglvfJ6kp9ldpw9+ExumVWRu2zUXC0rn99/atY4NVdzqPtknsvjjdlUdubmPcyRZGqnKoED5sthbU3189GXZY+we+aoU4cyu1wb4cajt9hwH2DOY6+//NF0CcSIrqM+GySqgYcqBB/JzpLRF+JwjK+OuIEbygpOrliuHlVJsEfev9wn56rbZFleBd7Ii3iA==~1',
    '_cf': 'default',
    '_scid_r': 'y5IlkospsJ9CSYsx9vnhNK4n4RMgH_MUseH-7g',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:145.0) Gecko/20100101 Firefox/145.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://www.myntra.com/checkout/cart',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    'Priority': 'u=0, i',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

url = 'https://www.myntra.com/casual-shoes/nike/nike-killshot-2-leather-mens-shoes/36555048/buy'
# url = "https://www.myntra.com/x/x/x/37890914/buy"

response = requests.get(
    url,
    cookies=cookies,
    headers=headers,
)


tree = html.fromstring(response.content)

script = tree.xpath("//script[2]/text()")

product_json = json.loads(script[0].strip())

print(json.dumps(product_json, indent=4))