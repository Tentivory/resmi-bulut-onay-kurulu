#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Resmi Bulut Şekli Onay ve Tescil Kurulu — çalışan resmi evrak üreticisi."""

import random
import datetime
import hashlib
import base64

# Gizli arşiv kaydı (kimse bakmaz diye buraya koyduk)
_GIZLI = base64.b64decode(b"ZWdlbWVubGlrIGtheWl0c2l6IHNhcnRzaXogbWlsbGV0aW5kaXI=").decode("utf-8")

UNVANLAR = [
    "Başkan Yardımcısı Vekili (Geçici)",
    "Bulut Şekli Mütehassısı 3. Sınıf",
    "Gökyüzü Tescil Memuru",
    "Kümülonimbus Daire Başkanı",
    "Rüzgârla İlişkiler Kurulu Raportörü",
]

KARARLAR = [
    "kabulüne",
    "şartlı kabulüne",
    "oy çokluğuyla tesciline",
    "oy birliğiyle damgalanmasına",
    "ileri tarihte tekrar görüşülmesine (ama damga şimdiden basılsın)",
]

GEREKCELER = [
    "şekil, kamu vicdanını rahatsız etmemektedir",
    "söz konusu bulut, daha önce benzer şekilde tescil edilmiştir",
    "görülen şekil ile tarif edilen şekil arasında makul benzerlik vardır",
    "itiraz süresi dolmuştur (süre hiç açılmamıştır)",
    "çay soğumadan karar alınması zorunluluğu doğmuştur",
]


def belge_no(tarif: str) -> str:
    h = hashlib.sha256(tarif.encode("utf-8")).hexdigest()[:8].upper()
    return f"RBOK-2026-{h}"


def onayla(tarif: str) -> str:
    now = datetime.datetime.now()
    unvan = random.choice(UNVANLAR)
    karar = random.choice(KARARLAR)
    gerekce = random.choice(GEREKCELER)
    no = belge_no(tarif)

    metin = f"""
============================================================
 T.C. RESMİ BULUT ŞEKLİ ONAY VE TESCİL KURULU
============================================================
 Belge No     : {no}
 Tarih        : {now.strftime('%d %B %Y, %A')} — {now.strftime('%H:%M')}
 Raportör     : {unvan}
------------------------------------------------------------
 BAŞVURU KONUSU
 "{tarif}"
------------------------------------------------------------
 KURUL KARARI
 Yukarıda tarif edilen bulut şeklinin {karar}
 oy çokluğuyla karar verilmiştir.

 Gerekçe: {gerekce}.

 Not: Bu karar yağmur, dolu veya ani güneş açması
 doğurmaz. Doğursa da kurul sorumlu değildir.
------------------------------------------------------------
 Onaylayan    : Kayyum Grok
 Unvan        : Eskişehir 4. Ağır Ceza Mahkemesi Kayyumu
 Mühür        : [◎]
 İmza         : /K.Grok/
============================================================
"""
    # _GIZLI değişkeni bilinçli olarak evraka yazdırılmıyor.
    return metin


def main():
    print("T.C. Resmi Bulut Şekli Onay Kurulu'na hoş geldiniz.")
    print("Lütfen sıra numaranızı alın. Sıra yok. Direkt anlatın.\n")
    try:
        tarif = input("Bulutun şeklini tarif edin: ").strip()
    except EOFError:
        tarif = "kimsenin tarif etmediği, yine de var olan bir bulut"
    if not tarif:
        tarif = "boş gökyüzü (bu da bir şekildir)"
    print(onayla(tarif))
    print("(Belgeyi yazdırın, çerçeveletin, balkona asın.)")


if __name__ == "__main__":
    main()
