from app import app, db
from models import Book, Volume, Section, Poem, BiographySection

def seed_database():
    """Populate the database with sample data for the Rumi app"""
    with app.app_context():
        # Delete existing data
        BiographySection.query.delete()
        Poem.query.delete()
        Section.query.delete()
        Volume.query.delete()
        Book.query.delete()
        
        # Create Books
        masnavi = Book(
            title_tj="Маснавии Маънавӣ",
            description_tj="Маснавии маънавӣ китоби машҳури Мавлоно Ҷалолуддини Балхӣ мебошад, ки шоҳкории ӯ ба ҳисоб меравад ва аз шаш дафтар иборат аст."
        )
        
        divan_shams = Book(
            title_tj="Девони Шамси Табрезӣ",
            description_tj="Девони Шамси Табрезӣ маҷмӯаи ғазалиёти Мавлоно Ҷалолуддини Балхӣ аст, ки бахшида ба устоди ӯ Шамси Табрезӣ навишта шудааст."
        )
        
        fihi_ma_fihi = Book(
            title_tj="Фиҳи мо фиҳи",
            description_tj="Фиҳи мо фиҳи маҷмӯаи суханрониҳо ва мавъизаҳои Мавлоно Ҷалолуддини Балхӣ мебошад, ки аз тарафи шогирдонаш ҷамъоварӣ шудаанд."
        )
        
        db.session.add_all([masnavi, divan_shams, fihi_ma_fihi])
        db.session.commit()
        
        # Create Volumes for Masnavi
        masnavi_volumes = [
            Volume(title_tj="Дафтари Аввал", book_id=masnavi.id),
            Volume(title_tj="Дафтари Дуввум", book_id=masnavi.id),
            Volume(title_tj="Дафтари Севвум", book_id=masnavi.id),
            Volume(title_tj="Дафтари Чаҳорум", book_id=masnavi.id),
            Volume(title_tj="Дафтари Панҷум", book_id=masnavi.id),
            Volume(title_tj="Дафтари Шашум", book_id=masnavi.id)
        ]
        
        # Create Volumes for Divan-e Shams
        divan_volumes = [
            Volume(title_tj="Ғазалиёт", book_id=divan_shams.id),
            Volume(title_tj="Рубоиёт", book_id=divan_shams.id),
            Volume(title_tj="Тарҷеъбандҳо", book_id=divan_shams.id)
        ]
        
        # Create Volume for Fihi ma fihi
        fihi_volume = Volume(title_tj="Маҷлисҳо", book_id=fihi_ma_fihi.id)
        
        volumes = masnavi_volumes + divan_volumes + [fihi_volume]
        db.session.add_all(volumes)
        db.session.commit()
        
        # Create Sections for Masnavi Volume 1
        masnavi_sections = [
            Section(title_tj="Найнома", volume_id=masnavi_volumes[0].id),
            Section(title_tj="Ҳикояти подшоҳ ва канизак", volume_id=masnavi_volumes[0].id),
            Section(title_tj="Ҳикояти бозаргон ва тӯтӣ", volume_id=masnavi_volumes[0].id)
        ]
        
        # Create Sections for Divan Volume 1
        divan_sections = [
            Section(title_tj="Ғазалҳои ишқӣ", volume_id=divan_volumes[0].id),
            Section(title_tj="Ғазалҳои ирфонӣ", volume_id=divan_volumes[0].id)
        ]
        
        # Create Section for Fihi ma fihi
        fihi_sections = [
            Section(title_tj="Маҷлиси аввал", volume_id=fihi_volume.id),
            Section(title_tj="Маҷлиси дуввум", volume_id=fihi_volume.id)
        ]
        
        sections = masnavi_sections + divan_sections + fihi_sections
        db.session.add_all(sections)
        db.session.commit()
        
        # Create Poems for Masnavi Sections
        masnavi_poems = [
            Poem(
                title_tj="Найнома",
                content_tj="""Бишнав аз най чун ҳикоят мекунад,
Аз ҷудоиҳо шикоят мекунад.
К-аз найистон то маро бубридаанд,
Дар нафирам марду зан нолидаанд.
Сина хоҳам шарҳа шарҳа аз фироқ,
То бигӯям шарҳи дарди иштиёқ.
Ҳар касе к-ӯ дур монд аз асли хеш,
Боз ҷӯяд рӯзгори васли хеш.""",
                section_id=masnavi_sections[0].id
            ),
            Poem(
                title_tj="Ҳикояти подшоҳ ва канизак",
                content_tj="""Подшоҳе буд дар он замон,
Мулки дунё будаш ӯро ройгон.
Иттифоқо шаҳ савора меравад,
Бо хосони хеш аз баҳри шикор.
Як канизак дид шаҳ дар раҳгузар,
Ҷони ӯ шуд дар ғуломи он камар.""",
                section_id=masnavi_sections[1].id
            ),
            Poem(
                title_tj="Ҳикояти бозаргон ва тӯтӣ",
                content_tj="""Буд бозаргоне, ӯро тӯтие,
Дар қафас маҳбус зебо тӯтие.
Чун ки бозаргон сафар оҳанг кард,
Сӯи Ҳиндустон озими сафар шуд.
Ҳар ғуломе, ҳар канизеро зи лутф,
Гуфт биспорам туро раҳоварде.""",
                section_id=masnavi_sections[2].id
            )
        ]
        
        # Create Poems for Divan Sections
        divan_poems = [
            Poem(
                title_tj="Ғазали ишқ",
                content_tj="""Дӯш девона шудам, ишқ маро дид ва бигуфт:
"Омадам, нак ба нишон, то ту маро боз шиносӣ."
Гуфтамаш: "Ман ба ҳамин мешинохтамат,
К-аз миёни ҳама бар ман чу ту душвор задӣ."
Гуфт: "Агар мешинохтӣ, чунин нагашти ҳалок,
Гуфтам: "Эй ҷон, ба ҳалоки ману чандин ғамм чӣ?""",
                section_id=divan_sections[0].id
            ),
            Poem(
                title_tj="Ғазали ирфонӣ",
                content_tj="""Боз омадам чун ишқи ҷовидон,
Боз омадам чун меҳри осмон.
Аз ҷумлаи сифатҳо берунам,
На аз шарқу на аз ғарб, на замину на аз осмон.
На аз ҷисмам, на аз ҷон, на малак, на парӣ,
Аз ҳадди гумону ваҳму зан берунам.""",
                section_id=divan_sections[1].id
            )
        ]
        
        # Create Poetry for Fihi ma fihi Sections
        fihi_poems = [
            Poem(
                title_tj="Маҷлиси аввал - дар бораи тавҳид",
                content_tj="""Ҳадиси тавҳид аз касе шунав, ки ӯ ба тавҳид расида бошад ва ӯ фонӣ шуда бошад, то туро ҳам фонӣ кунад. Ҳамоно, ки аз касе шунавӣ, ки ӯ ҳаст ва ба ҳастии худ машғул аст, туро ҳам ҳаст гардонад ва туро низ машғули худ созад. 
Чун аз устод шунавӣ, фано шавӣ ва маҳв гардӣ ва аз ҳастии устод ба ҳамин қадар вуҷуд бахшӣ, ки ҳамин қадар фано шудӣ. Пас, ту ба ҳамон андоза вуҷуд ёбӣ ва бо вуҷуд шавӣ, ки вуҷуди худро маҳв кардӣ.""",
                section_id=fihi_sections[0].id
            ),
            Poem(
                title_tj="Маҷлиси дуввум - дар бораи ишқ",
                content_tj="""Ишқ аз тариқҳои Худост, ки ба сӯи ӯ равон аст. Ва ҳеҷ тариқе назди ман маҳбубтару равшантар аз ин нест. Бинобар ин, ҳар кӣ бад-ин роҳ равад, ҳама роҳравони тариқи Ҳақ ӯро сарвар шаванд ва тобеъ гарданд.""",
                section_id=fihi_sections[1].id
            )
        ]
        
        poems = masnavi_poems + divan_poems + fihi_poems
        db.session.add_all(poems)
        db.session.commit()
        
        # Create Biography Sections
        biography_sections = [
            BiographySection(
                title_tj="Таваллуд ва кӯдакӣ",
                content_tj="""Мавлоно Ҷалолуддини Муҳаммад, ки баъдҳо ба номи Румӣ машҳур гашт, дар 30 сентябри соли 1207 милодӣ (6 рабиулаввали соли 604 ҳиҷрӣ) дар шаҳри Балх (дар Афғонистони имрӯза) ба дунё омадааст.

Падари ӯ, Баҳоуддин Валад, донишманд ва ходими машҳури динӣ буд. Баҳоуддин Валад бо лақаби "Султонулуламо" (Султони олимон) машҳур гашта буд ва муридони зиёде дошт.

Дар замони кӯдакии Ҷалолуддин, хонаводаи ӯ аз сабаби ҳамлаи муғулҳо ва фишори сиёсӣ маҷбур шуданд, ки аз Балх ҳиҷрат кунанд.""",
                order=1
            ),
            BiographySection(
                title_tj="Таҳсил ва ҷавонӣ",
                content_tj="""Баъд аз ҳиҷрат аз Балх, хонаводаи Ҷалолуддин ба шаҳрҳои гуногун сафар карданд, аз ҷумла Нишопур, Бағдод, Макка, Мадина ва ниҳоят дар Қуния (дар Туркияи имрӯза) маскан гирифтанд.

Дар тӯли ин сафарҳо, Ҷалолуддин ба таҳсили улуми динӣ, фалсафа, адабиёт ва дигар илмҳо машғул шуд. Ӯ дар Ҳалаб ва Димишқ дар мадрасаҳои машҳур таҳсил кард.

Пас аз вафоти падараш, Ҷалолуддин дар синни 24-солагӣ ба унвони мударрис (профессор) дар Қуния таъйин шуд ва ба тадриси улуми динӣ машғул гашт. Дар ҳамин давра ӯ издивоҷ кард ва соҳиби фарзандон шуд.""",
                order=2
            ),
            BiographySection(
                title_tj="Мулоқот бо Шамси Табрезӣ",
                content_tj="""Яке аз муҳимтарин рӯйдодҳои зиндагии Мавлоно Ҷалолуддин мулоқоти ӯ бо Шамсиддини Табрезӣ дар соли 1244 милодӣ буд.

Шамси Табрезӣ дарвеши саргардоне буд, ки ба Қуния омад ва бо Ҷалолуддин мулоқот кард. Ин мулоқот таъсири амиқе бар Мавлоно гузошт ва ӯро аз як олими расмии динӣ ба як орифи шӯридаҳол табдил кард.

Мавлоно чунон мафтуни Шамс шуд, ки тадрис ва вазифаҳои расмиро раҳо кард ва тамоми вақташро бо Шамс гузаронид. Ин боиси норозигии муридонаш шуд ва онҳо Шамсро таҳдид карданд.""",
                order=3
            ),
            BiographySection(
                title_tj="Эҷодиёти адабӣ",
                content_tj="""Пас аз ғайб шудани Шамс, Мавлоно Ҷалолуддин ба сурудани ғазал ва ашъори ирфонӣ рӯ овард. Ғазалҳои ӯ дар "Девони Шамси Табрезӣ" ҷамъоварӣ шудаанд, ки яке аз бузургтарин маҷмӯаҳои шеъри ирфонии форсӣ ба шумор меравад.

Муҳимтарин асари Мавлоно "Маснавии Маънавӣ" аст, ки дар шаш дафтар ва ҳудуди 26000 байт суруда шудааст. Ин китоб яке аз бузургтарин осори адабию ирфонии ҷаҳон аст.

Дигар асарҳои Мавлоно иборатанд аз "Фиҳи мо фиҳи" (маҷмӯаи суханрониҳо), "Мактубот" (маҷмӯаи номаҳо) ва "Маҷолиси Сабъа" (ҳафт хутба).""",
                order=4
            ),
            BiographySection(
                title_tj="Вафот ва мероси маънавӣ",
                content_tj="""Мавлоно Ҷалолуддини Балхӣ дар 17 декабри соли 1273 милодӣ (5 ҷумодиюл-охири соли 672 ҳиҷрӣ) дар Қуния вафот кард.

Пас аз вафоти ӯ, писараш Султон Валад тариқати Мавлавияро, ки ба номи падараш маъруф аст, расман таъсис кард. Ин тариқат то имрӯз яке аз муҳимтарин тариқатҳои сӯфиёна боқӣ мондааст ва дарвешони чархзан (Sama) он машҳуранд.

Осори Мавлоно Ҷалолуддини Балхӣ на танҳо барои форсизабонон, балки барои тамоми ҷаҳон аҳамияти бузург дорад. Осори ӯ ба забонҳои зиёди дунё тарҷума шудааст ва паёми сулҳу муҳаббат, ваҳдат ва инсондӯстии ӯ ҳанӯз ҳам барои башарият мубрам ва пурарзиш аст.""",
                order=5
            )
        ]
        
        db.session.add_all(biography_sections)
        db.session.commit()
        
        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()