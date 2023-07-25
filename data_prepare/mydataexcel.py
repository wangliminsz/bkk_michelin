import pandas as pd
# from mycoordinates.py import *

coordinates_data = [

    {
    'Location': 'Bangkok Patana School',
    'Latitude': '13.663052',
    'Longitude': '100.6219206',
    'Website': 'http://www.patana.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcKJjr3ndneLYV5WSMC0_89jk2HC2P5kXPgJBUOGpr5IqcL3sHl_fw_ZK4YaJeXtqHDYuhOl5_hrXTurrpq4uMputsMmdBqa2rdAlbtFZSqPXxO2ii6mIuCOU1g2ug8_9DzP7pNx5haHr9nnprpsAj_HCsD2Lhw3_DMlaHJQsPDlbgYl&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'NIST International School Bangkok',
    'Latitude': '13.7467838',
    'Longitude': '100.5592757',
    'Website': 'https://www.nist.ac.th/?utm_source=google&utm_medium=businesspage&utm_campaign=searchanalytics',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcKlzelYOTERSE04WDBk-YovavJiCJLb_2WB7ZNdQj9iVoQLlpe2NOsFbRjAREPs-tefTxlY4VnhTO8Frj2XPeWaIRaiTptSYQepKJ23BKARpHuZE4pTvmvQq3naYqMR2q-WgS8NtOyWyTqtywmU6TlkJpQsy11254Ol903scE3fR54&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'International School Bangkok',
    'Latitude': '13.8928748',
    'Longitude': '100.525754',
    'Website': 'https://www.isb.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcI27ahXKKHVbyZfqo0TJeYrXH6ysEm3YGUNua51QSptiKmnMEWif-3jnvjNu0l88ihVJjM-N3qDW5SFGX2RTCs4_OiGcf8lU13rua8EtpV3cdv0OWsdnvPOYXOsd7-Mdwm_5ZGmOifjLTcKdFvGKfqUIu_NJn9b17mKzRqiX-UpXmt-&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Shrewsbury International School Bangkok',
    'Latitude': '13.709251',
    'Longitude': '100.510117',
    'Website': 'https://www.shrewsbury.ac.th/riverside/index/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcJAFE_oNiDIiumpIZNBtseu7apf0uEDNzMd-Mr_io35-dPE8-IFTtWs6xYxnLpI2G_wXCCaryB7BsyIsz579RCWEjgA6jErplLmXrDm-tx9uPIWfJSUUeHWevDZffldU6lYhcn5H5VDV3ALtUMZPI1xko59ykVGsRSLkmW79V2LY8Bm&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Harrow International School Bangkok',
    'Latitude': '13.9049799',
    'Longitude': '100.5834389',
    'Website': 'http://www.harrowschool.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcJBSOTbQYo4K2MW7CQ4VGq3YeKQnia9r49t4o08E7DZPgRcZck0T8otxo2NdQ7GJlegJZXIZWKkRcycp881q49iNl99XAvD1fvUCzzrkuxC5oXm9Rs7lzp4Yo0urhwefi1e7Z76KGwYDpYA1kWx3MNMtuggEI385FDDsK05SNpjBN5T&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'International Community School Bangkok',
    'Latitude': '13.6670036',
    'Longitude': '100.6518173',
    'Website': 'http://www.ics.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcJRzGppA7jTcU8IhAfKi07yk2oK16QupoTxdOxZnVfvity2KxKj1dNmaC-NdFzF5u-tgaRCslwFd6b29AmizAMhNmOQ3-oup74GnXiY4NbAAk5MaOTiBCg7Fzjw299rqQ5K0avebItOdl7fdDL5dWFbUC_LfIFGkkCsNLae9knA2gRB&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Brighton College International School Bangkok',
    'Latitude': '13.75434',
    'Longitude': '100.6717698',
    'Website': 'https://brightoncollege.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcJZcCsb7S41SpMPdfDkk8OWAnHqDTZDfaG6i79PgqOumtFySkDa3iQbDOKhW2G2m3m3ruEDZl_D3X6zoU1lgsXpSQXW397hULLYfrb1kC5JM3l3sbhBRETqT2dUUMiRVah79TxX9AUOLfdBtygewKO892sXpjH5K4Vbmy2LByTq309K&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'St.Andrews International School Bangkok',
    'Latitude': '13.7243794',
    'Longitude': '100.5968223',
    'Website': 'https://www.nordangliaeducation.com/our-schools/bangkok?utm_source=google&utm_medium=organic&utm_campaign=Yext_GBM_SEA009_10524854&y_source=1_MTA1MjQ4NTQtNzE1LWxvY2F0aW9uLndlYnNpdGU%3D',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcIEe8TUqQvAK0F9HaWL47JtWX-PRHl8rx8tT8obbihaTLky9vTRqhB7Fb9saa5pjXutD0bXHL4H3qVw8zNeqL2hi6fkySgvPyRqHmQTN8VPlSFbUUPVrvwc19BoPaWtTQXFzaThxZywzZ3ClKE1Cg5lc76NM5ouIPLZn9HbmJcJjF4l&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Bangkok Prep School',
    'Latitude': '13.7149999',
    'Longitude': '100.6015163',
    'Website': 'https://www.bangkokprep.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcL5S2z2hP9bLLvfl8P-HXbV9WhHe_73xuNlZJyJjWgIgB90_f78d-TKWwG43Fo3HmlpfCG3D-mQy0YtactZOfIeNknHDW6Lllrrwdki9DA9DuxmRcVRpEjFXyLLUqU28ppuq7VB_kuNA607MHLTbHccZ2tdmp83S-TFYDT-NHf9tRRu&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Concordian International School Bangkok',
    'Latitude': '13.6382728',
    'Longitude': '100.6740613',
    'Website': 'https://www.concordian.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcKKjAZC0xFjVigy1yTBeYoHcxhtgIczbbvdFkerIOkxZxKw76BIkH64iPkuQP75RvohzQVRY6au_-7_jmCaI1UO6uEFeuic_lBZfOkZi3scYITa80_tv1RQ-he18qwNQs2P8Ftmtbfb7PPtoyx811kfP8MQ3Ranyg4fG7RM402bmTxk&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Ruamrudee International School Bangkok',
    'Latitude': '13.7838152',
    'Longitude': '100.7292359',
    'Website': 'https://www.rism.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcK98EJKoHX1KuSmPGLSLLEb1-_k7Ut7uOxVlBDltTIxq_8p4Jgz9kB8MEmumy_JPsRWv1i1IYCWXh2TWQwuw06CVGuEN3v302840mtvFSLtxB_WQqJiJu6aoxaRgEs-2tYOtOMPYO4KRiQZ27oe3lp_wRuOSStCZK9r_LycwYMxbfxG&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'KIS International School Bangkok',
    'Latitude': '13.7713099',
    'Longitude': '100.5891821',
    'Website': 'http://www.kis.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcI1ELFPREOC2xolgNm7MuMyFF3CJ3XfgtYIHivbbljU5VdctNBB-MY0_Nf9G_GTUilY6YBdMTZ7cS-L6MektUmOS0eRgMrD2MR7QhpNqVt1fVZqBcEzsCB4XdBqFogf2t9Y4kcoWL1dJZMT0ZGI3YgJUiBsQlyUFieaojQASh5nO6EA&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'St.Andrews Sukhumvit 107 Shool Bangkok',
    'Latitude': '13.6590406',
    'Longitude': '100.6016179',
    'Website': 'http://www.standrewssukhumvit.com/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcLEEzZlkyJ-NOHV6KCYMuZGeHmOkdvUExGygYImJNZw4mPbb51VYf1drFnX51T7gc2SBwMJZsy6p0LPGlOCbNPOm0uBHxT66wLVZ18Y3vit6yQTJWQOGLpuKAl_HWUvNL3Pz8TWWOR5hq8RtB4lTlgKqXz74OzCniIFxmyR4XQa-Kty&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Bromsgrove International School Bangkok',
    'Latitude': '13.8187359',
    'Longitude': '100.797328',
    'Website': 'http://www.bromsgrove.ac.th/boarding-school-thailand/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcLoQFVb3xtTuW4D1o757-4xUx6VvoDXyVpLmK3ubinFRPKIVi9mwydXZjeSc7zhx_2Z3MCVp7dH9-avtvdzayyp094DRQdILUCp9XVaOlb1nZR5pEEFcGUlaCXvUfShJlGIHtbu7SxFs5y2B5oJRPtTpPiwuhXyPL8CUp_lPkeX0RK-&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': "The Regent's International School Bangkok",
    'Latitude': '13.7674219',
    'Longitude': '100.59577',
    'Website': 'https://www.regents.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcLisjA3Gh9nJ-nWov6Z7Bi4yAttcDapJSL4PsnHYaWL_mAHOH0baJ5yU5PQ37ZlyfOw9xy3vMln5K3-oW7z2Vct3xItXBG5uYFqQG215F_cmVTkxWDupw5NnQ2S-16c-Dx0Oz0KCBTV7JoEsYq-kRFDa9cj_30Fck1TjJClonajdm51&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Berkeley International School Bangkok',
    'Latitude': '13.6735489',
    'Longitude': '100.6144224',
    'Website': 'http://www.berkeley.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcK6W-F2W_V-qo8oTPVl925R5zthCESS4EdGKFt2yHko7Vfzo2WhYK_yG3jfEcoDZjjx6W_qlapfKNfeEA-Sp1B5DGvBnrQg8FNZNHLH2TF8S3TqJqcrNZXMF1LXQ8xjzH7qNDJ9m2CBUhFkZmDrw_uBJWcWD2n51v0UG1x4IaVsYOIU&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Singapore International School of Bangkok',
    'Latitude': '13.7704447',
    'Longitude': '100.6026044',
    'Website': 'https://sisb.ac.th/singapore-international-school-pracha-uthit-campus/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcLFTS6F6ZmaZe-LIbt6A38_8WbKJJ1ns-nFb9XK-92Wog8NIz4rofm7sd4PP856MEMPy2zO_lBqaJYLOTkrIRNOUoOZd9eFL2JMNej_nUcgAcMh2r2iUAXhIH9xx0Y_xPdcntPedzjD5qnyVdK_FoPKdUdlyhxerziQ-SBAplYb_Niu&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'The American School of Bangkok',
    'Latitude': '13.7563309',
    'Longitude': '100.5017651',
    'Website': 'http://www.bangkok.go.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcLoNHJrNKWmYTtsBeQKz4K7aHVAwuUrsfnt0Ltgt-ou2TULeiJkS5fidpycGZMYq5Y71ETQWTbOk11scVop18S3A7405ukji4eGv1YqqO-iTQKELxa59zPl_6Sl8ZFnSyWVeb8sNyAkSAfVvTxlDjuPSSBgZuOOgYEiRS4kv3I7mwGD&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Charter International School Bangkok',
    'Latitude': '13.7111747',
    'Longitude': '100.6943264',
    'Website': 'http://www.charter.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcLSMeu64SIKfMNrYAp46XA7e_Gc_z4Z-NUUek7cb_TCPgDhT_ONJk6_zvi86cmPR9pRwP7Nc2HySeOj-AvfverLWqGQXNHkYbxDSBqf0qsowgYIZdVJSL0psWHx28DXDFzmPos93Kd3c2_pw6GmfB1ggWfe90Jnt5eJsJ1toXWuDwKX&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': "St.Stephen's International School Bangkok",
    'Latitude': '13.8349203',
    'Longitude': '100.5587086',
    'Website': 'http://www.sis.edu/bangkok',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcI74nyXv1Qz_NJtyf0TpMkSN6LTFxbEK1A61wkltJB5wyhWfawEbj5dprJnzJvCyrVTWWD_yNn5XvfOOMrQUYSfRV7ntnMp8HTt--9K1x0jHCEjq3FdpMdcZl5lZ2DLit7K6U4nL4AcbscQCLmVX3FxondotLNNf_GahjXT7yJQZD9g&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Canadian International School Bangkok',
    'Latitude': '13.7762804',
    'Longitude': '100.4963455',
    'Website': 'https://www.canadianschool.com/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcJTVKWC7hgV4P6TNia-2CsDd7KeN7N0LNjYwSR6PfRUDf09yNxU2dTbCTnAlBZpWEV_zkSe2HRq-dXvdneguRvV677ayIq0ku6kGGmXt52ivdZQ-gTVPwwYtQeF6FdZjhIF6T0VV5TgXB8Pmwu8xcGI0WeyILYy3sDlRgMWgzHhNY6T&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Anglo Singapore International School Bangkok',
    'Latitude': '13.6879703',
    'Longitude': '100.6090378',
    'Website': 'https://anglosingapore.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcIUMn1hrCXByy54OOSG5n9WUWMovbaUP8-FOwzD-NmKyJICf6GCJSKvkzzXKn55FXSkfOx8CIO7-jN_29jdBB3GPMmNo1f6ZEunYaFc_FUEXC8GH6fBogiE7aoGUxiiDfUQspD7otSJyzE2d0JDwVoqX5xJyPR6dRQKP_d1P0w_fwQu&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Garden International School Bangkok',
    'Latitude': '13.715204',
    'Longitude': '100.545965',
    'Website': 'http://gardenbangkok.com/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcKbyoGcNpQlUfk0IX49gX7LlA55aM0ZgkY7rVQprEpiuW6ESk6FMTB8sENDpKMg64Kb560mPNYalv6SmkZrfX1jhPXgMn9m8EgSDjUg4AUjR6re6hvK_Rub1tWK6Sg0jUFxf235ItB3smrJcuiP1kzKGBiiAYUVKrAkbCkI8V6_iFMV&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Wells International School Bangkok',
    'Latitude': '13.7273221',
    'Longitude': '100.5770463',
    'Website': 'https://wells.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcJ46ApdjzCbpKhajhFAukU3CFAHiM13I1uYub8qxugs_i6b5AoeGJ0494bkdGEjeCxmPEfVZCjfM8gPzILSfrCmyR9cHCi9WAm_j2F3mXbI6W4HSzdjp40x430hkl_bJOWdw7-UphBVkTRxdo3m-DNt0deRYDoumj14HYyk01fmS0iB&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Ascot International School Bangkok',
    'Latitude': '13.7623362',
    'Longitude': '100.6870136',
    'Website': 'https://www.ascot.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcIoIK32qK5Xtuf06NBbl0_qUzH52uBTAlrXVBw8KauXl8xw__wQ28MxGiYCCDjJ4w7Z_OJthM3UN02WLchTWTWyL7p5L66tk8IomwbCfBVqih7ysIX7IzamllcDddCABnUsv2dd06xkRA7pB4OHBk7nQnJBBGxvQt74InV6i303SvxU&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'RBIS-Rasami British International School Bangkok',
    'Latitude': '13.7693714',
    'Longitude': '100.5469764',
    'Website': 'http://www.rbis.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcI4t1OsDZ0cAgc75P0gOLtoKkReMi1iYo2kO-jGbTdtH_wfzFfFLdSImC4uwkvBEmz_K9NUyUGuKzT-YaVMSdFO_8WJOirGh3qfhGlmvQN4fTRO8E2sVhx9F0ebjk2tH6i-7-edwiK8efawrbtl-chNqqKOZUW42sNb8ZB4kh_s20OA&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Bangkok Christian International School',
    'Latitude': '13.7342278',
    'Longitude': '100.6315207',
    'Website': 'http://www.bcis.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcLkWqxvDATfLSsf4cveHBdN-xI3MCEwyMTAxl_iS5vlyy5gP4LHXAA_1qBiRVmi_RSGxtXbN5m7QiCy1gEbCE7svJtN2o6vySuzFFVXExb1VIAJicInd5l56e4-nBr3K410efqP31LEfxXf5zwhHA0XHMMAH55HBFWS-tV82-KwhlDP&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Keera-Pat International School Bangkok',
    'Latitude': '13.8451022',
    'Longitude': '100.6324747',
    'Website': 'https://kpis.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcJT3ava1tCXQaxpy_2Y3cy-cAlV4fUxZRNdccKwSEqcIrWqHqC04FmMZ5JjqR2aNG0d4P5nuT4lhC95XQYE0R65OPiG1i51lQt78yapTnOXv-29W6KHPVG_q2eS74K4PFdLK420vAG-HcRqbQMSm9JpMgPR5UynGhrEMA5DbuYQ6cX5&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Morden International School Bangkok',
    'Latitude': '13.7448284',
    'Longitude': '100.5717935',
    'Website': 'http://www.misb.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcLZG0adEuK7qmtErc7iqbas5l72ELN_-3AO2o_a89iFdXwhON4I_RCCBkAOX_roRW0iqdqRBinlo00eE6BAVYfQkql4EfZyfhYhsHYX_twA7d_FAhKUVwmdfAMnfj_gaI1iPBRbB2vORyWUWTRKgchLj-ypv5PK1xBZuS3Axuqdc-QQ&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Trinity International School Bangkok',
    'Latitude': '13.722674',
    'Longitude': '100.57496',
    'Website': 'http://www.trinity.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcLPjmOby1upCg7YViwagdjd0yErQ8zRL_qSDPb5QqreGfBrbeFbwJDyoIbZ877d0BQ3jMmp9ahg-1aglk7FSboqaT-zlyNsMdyHwb9Px1H7O8KHClc2VdGXPOIWaL6AGeti22bGwZeb_Jkoccv1437ZxAfdI8hh6sCTYyZGjQCYg9Y&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Pan-Asia International School Bangkok',
    'Latitude': '13.7032782',
    'Longitude': '100.6865583',
    'Website': 'http://www.pais.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcIs89J4KMJNSRaBdoRVGUhCzOy7eYEqwaA4Sm0NDwMLGF6DNBq0rfKdNwD8BYVRMkXbd15BXls-JWsjUpglCMrFp1k7a9uZIJao-RnLtcGZKP2PbP8i_is48NqFDp1FCa9-p6uyoJujTGGzUvd4Q3UiIoXci-ptvBtN-XssUYsHLKX8&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'International Pioneers School Bangkok',
    'Latitude': '13.7222948',
    'Longitude': '100.5010652',
    'Website': 'https://www.ips.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcLntZYgyINrZcQkpk7TJ9qj4oCpt2WBKEj6-h8yUwxASiy2Xeh2CC8ZnnRgmTmaLQBuApsm9Q20_oL3QjQPeuhinCmKxW33BFOJ1Qpb6fL5pUQ_5fJbSp6NlLFOIIZ0UTK8PctTFL_XwdPJSCPaDIoxKTnqqb3yDK4cjuFyOQDNOo48&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Traill International School Bangkok',
    'Latitude': '13.7513243',
    'Longitude': '100.6142789',
    'Website': 'http://www.traillschool.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcJ6kx37L6_ECJp0HbCYm5wWZwP45cgijImQy-GGmvjjw3aSs_wM0s8E3VpW68pAHVQz5uAfj3UOfjnz_8W0QpcVN4wFjkHB7XquyUj_-wbdVgpreywBPm8-GFot0D7I3qNjmu66p2iWtuK9i0E2BHHH6DWgyBbzzwS7gUk3pfQEpeV9&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Heathfield International School Bangkok',
    'Latitude': '13.7833437',
    'Longitude': '100.686121',
    'Website': 'http://www.heathfield.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcJPIBILv8e0X4IpCGRKy4Ln5ahZ0lcv5NpnbOx223AqMI0juWzELk8CkEyysxdcHVW3LdIV3PpSN8D_fs_PwlpA5_LehhU3uQEQtfULrB6L8F8x5e-up22YizuKgcudFDrQW9z7S3OVLJktWFCv_YYLH7aFkcg_2JaP3ssrB9KlV8Yu&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Ramkhamhaeng Advent International School Bangkok',
    'Latitude': '13.7684494',
    'Longitude': '100.6583869',
    'Website': 'http://www.rais.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcKKwMsvj6nItaep89CavFRaO_VOXFSQvdVGZYz_f8hjAeBLdBE_2w7PuAF2hCiWLjmrK_aUefuZylX4NgSous7xWMxPAY65GRbDmWkWi9vS-FfPmctl6Y859pcX3eHjTCtVHBlWp1t6VmhdlUCRiYMI9mkTaRT0FFDVxgYsJcCgfwD_&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Thai-Singapore International School Bangkok',
    'Latitude': '13.6464244',
    'Longitude': '100.64008',
    'Website': 'http://www.tsis.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcLBsZWrJzcUkdMnBCKkKYvuI7dUyZ5ObjGFeH27gDgWA67HzJ-LVLCqajm_6EhLhY4osWEDekWpdKXX3sGujJlT23XODoWNHpioIRp01F2j4yeBjJZ9rukZUNQ0xoIZ93JmGl_2rlyADMlkIVeOkNfsHeU0eMpjSmoSh3tsb6h__LFr&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Ekkamai International School Bangkok',
    'Latitude': '13.7308164',
    'Longitude': '100.5921479',
    'Website': 'http://www.eis.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcLkgEgUlDuDxMG8ymBgs34EnvvHtXr3KPUW8JCQqIMFPGHQklBAQwMg7MN178KHebt7Byx6GqkqYi6BCbkOE1z1xAy-G2wV6x5f3lIxSPgWnn5g1yrc91YYxBuluRUVOxFj42P4RwTyU9dqRjbaY8bd6gtpA7sMjLMhJIwi-15LJDkd&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Niva International School Bangkok',
    'Latitude': '13.8024142',
    'Longitude': '100.6291464',
    'Website': 'https://www.niva.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcIO5fWbF-uLKneT8NLQRgW4GAwK2QHFxp9JyNDbwI2rKHnNJa9X0sbRyL_-zoGnpka6iynL-3FNLiOtxVN8zsjG_qLXeN8zLjkyPNDUulg5winLb-r4gm7vW5HKMRKE0zZINI-Ds3cwA-nFa91UN1tMziNMxE44tJyaTxjyZplnCVTN&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'New Sathorn International School Bangkok',
    'Latitude': '13.7012349',
    'Longitude': '100.5363066',
    'Website': 'https://www.nsis.ac.th/html/home.php',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcID_5MZ0LOteJUE5XMZThD0NB0xrgnJJXUYkGQ4KiBgE-QDu91Y3aDoXwo5_4rfA200Fqs0m7K06Nz3UeIxHAJrlt0-PVPErk5MakTwIPW8xsyjbAIrROFJYzFVGDTDGmk6sgqMV6qJyjN9a-0W1UoKyLF_chY3gEikhLql8YgEoP8q&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Kincaid International School of Bangkok',
    'Latitude': '13.7232957',
    'Longitude': '100.6605967',
    'Website': 'http://kincaidbangkok.com/',
    },

    {
    'Location': 'Thai-Chinese International School Bangkok',
    'Latitude': '13.6274052',
    'Longitude': '100.6990674',
    'Website': 'http://www.tcis.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcLNB-kNnl3t8BFaGey6qqvYNypGIV0T87QLYuqknSi8QIgwrmmktl-2zWioT2O2IrPcDfdUzfWTwDIvsI61619tM7PK7x8774JjB3mgkMncqmUuBWbr3ZJpLnKDjA_Z9uFlBHe9W2a38o-qVldE5d5CjFKKmbhgU73weaQRNHT6Jgwa&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': "King's College Bangkok",
    'Latitude': '13.6916337',
    'Longitude': '100.5277282',
    'Website': 'http://www.kingsbangkok.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcJP4W_265kYF41ayY1k23HF4xUcLQAlh-SoIKRIuq-BfkU33xnth88ZiMqOYbc0-tc4TdCgCQlf6vt0AJLBTovBNdClkvFTFCCU-VyKfO4ObHmAqKNcfQf7oWI-pSGgunOMhBz8eiwK7hGO0ljTG1VSwEwVGFLYNdBmE1SfRiZ_ANI2&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Wellington College Bangkok',
    'Latitude': '13.7440145',
    'Longitude': '100.6716032',
    'Website': 'http://www.wellingtoncollege.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcKCKCvBp5ab6Gi8D-I_ugdQ6bb1Yo6kNlr9Gge59Ie_uEqKf16WlRL_UGBgFDQnL07QdYM3x2g6WhjPB5UGHAifkD3tzFVG6-5Hv4MBAAVk8JA1TYkFHU-svykVDFph7SHAfEIdalTOps5T50imlqMeDweKMEKKvoSCYk_WgQJbJ-DO&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Basis International School Bangkok',
    'Latitude': '13.664277',
    'Longitude': '100.4340891',
    'Website': 'http://basis.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcI5LMuaN6HtOwxViaKV_XNe2UeTt2MOCF5DE6RFhoTYMlidKEi-YoHB2Ial-vWeV229i0oeNKHnEaUfUqn29fEJnk5chm7o6BjHgsyMnetQDGAORjuoDyHjj3uPgo1wCD1UMo9ntJZ9Uh_E6kwm92zXdSF2aGgBoDiOPJ2J8ZdnHAsm&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Shrewsbury City Campus Bangkok',
    'Latitude': '13.7520197',
    'Longitude': '100.5774866',
    'Website': 'https://www.shrewsbury.ac.th/city',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcLpRgCLJGVxhXqznih9j7-wa0Pt3P-sDQ2E5BF1S4Pd5MsRK8p6_e-2B2GlGtnbXPouGx7BOTXGvWT8fNzx2SqO00QqBmAKAkQOKbgdp7DnHh2DyuUrnjK1JWxt8-8Sw9FJ8nzEKp3u3Tm59OAdgaI2_X1YMwG6ep4vG-b0m5UqWSSI&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Denla British School Bangkok',
    'Latitude': '13.9114858',
    'Longitude': '100.4511118',
    'Website': 'http://www.dbsbangkok.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcLeeYSl5AHAl1fZWXOaYy-sG1GoIY656hi65bgMApZmCt9xq1WsPzVO3im4dOSsLOiC-kQPr7YlRVTJIJAjwEYZH9yBNQ_yXLYv9UKHC3zIb_fWt_S1yf5jf1mI2f-bB05yExVWpach9pIZRwI585kvpTUDXhv2L8YxUHv-ivLD0E1E&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Verso School Bangkok',
    'Latitude': '13.633318',
    'Longitude': '100.7326451',
    'Website': 'http://www.verso.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcJOJFI1cZojApfTvCG1Atly6vMM_nel02n-2pLVmY7zzDRqrNY6RSVrE9GvVHilvyB8ZXjLxLi5WSYZEXUQvVpHhn2yXmz7cT5qCE1p8h7Btx6i3Ql5jNfwfshwGLsvdf71LGMySxhAXBfhcX_SHNBpPWL_VTFX67FfOl1FMJuBkk8m&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Dprep Bangkok School ',
    'Latitude': '13.6434669',
    'Longitude': '100.6782441',
    'Website': 'https://www.dprep.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcIxHcqZBXVCJBBsvhfgHRhhZ40b6s10CXOoPVd3XhFykp27hD1fSCnX-if-XFx6MXXxXXJSuxdEWTeqY8Xz30YN4MIQdhIEy8Psi4bsjItib-ix3utkeZffCiEHlJGrFZiOqxri1Um75TP0sGkITUXyWlk-TYEx_Qp3d8GwkbNG3iRy&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Raffles American International School Bangkok',
    'Latitude': '13.664716',
    'Longitude': '100.6590705',
    'Website': 'http://www.ras.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcKiy_KlmO1QrffvoODWefdUsnfYdx3vqjeG3_Ep-Lncs-sKg8xkAsfH5Af1YX1VjDPmY_FFRh6FqCq3AWqch8j00-g9xLOqEEsJZ_kJr3MkdYBfD6UMrLId2rQevkj0-y5POfJn6ltSXdwzT79pz_QZlcZY9kBEKj6twi5ImoHAe_TJ&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Ruamrudee International School Ratchapruek Campus Bangkok',
    'Latitude': '13.8394235',
    'Longitude': '100.4553922',
    'Website': 'http://www.risr.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcJp5twKeikCgHAUo2nzvRUwU6mrUO_cq1-dzMlObuDTs7Lr7gS-g4p2pEQ0T93e9Js0cfAzE-QcEIpAJG8zi664X08LO0JcxEaVdNkGDU-dT0zy8m4NMpJFfcyh0iWDMamaFuQlwQi5lBiJKUrc09eJ54OVcsYN6Sxo1pny8DhEW40L&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    },

    {
    'Location': 'Mandarin International School Bangkok',
    'Latitude': '13.7641339',
    'Longitude': '100.6609741',
    'Website': 'http://www.mandarin.ac.th/',
    'Image URL': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference=Aaw_FcLzKWPBjPlAGgcg_blQEHgrRtYISdQ_TqEdMZ0vOsV0eoQFvLURrp4eHuogJGL8RyBo2JmvnYGd3ijqf4ybBEXX9Dauv0HXKsFenn5iPEPTxGhRmZddDNqZ1Mv609oBSZMXC-zyLHhF7OVvxQan82_jJ3LKUJdUj9L8kWxLIO7nCuQo&key=AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    }

]

df = pd.DataFrame(coordinates_data)
df.to_excel('mydata_output.xlsx', index=False)