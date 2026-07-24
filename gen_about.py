import html, random
random.seed(7)

ascii_face = r""".....................'.....''.''''''''''''''''.'''''...'........................
.....................''....'''''''''''''''''''''''''...'''.'.'..................
......................'.'''.'''''''''''''''...'''''''''''''''...................
....................'..''''.''''''''.''.'''''''''''''''......'..................
..................'..''''''..'''...           ..''''''''........................
................''...'.''''''..                .   '''''.'''''..................
...............''...'.''''..               ....  .  ``'''..'''..................
..........'.....''''''''''              ...'..''''..'''..'''''''................
...........'.'''.'''''''.        .    .  ...''... .''... .''''..''''............
.........'..''..''''''''.      .`'............'`^":^.     .'.''''''''...........
..........'..'.'''''''''    '^:::"":II:,^`^":,I<-][]-I'   .'''''''''............
...........''''''''''''.  .`:l!i>~-}1)()){)//ftfrnrxj|~^   '''''''''''.'........
.......'..'''''''''''''.  `:l!><~-}(\tfrxxuvvzYYYYzvxt1<^. .'''''''''.''........
..........'''''''''''''. .^;li><_]{(/frvcxczXJLQLCYcvj|-l^ .''''''''''''........
......''.''''''''''''''' .^;!i><+-[)__xvccvuXYYJUUYXvx/}i^.'''''''''''''........
.''..''''''''''''''''''' .,!!!li<-{\rnczXzvvYJLCJXvuunr\<"''''''''''''''........
.....'''''''''''''''''''. l!Il!Ii+](xcYCCJUJOZm0Yzunxjrj~'.'''''''''''''........
.....'''''''''''''''''';^.i!l'     `:~|uUQCLn/-;'^^"<(|f~.''''''''''''''........
....'.'..'''''''''''''':i^>!,:;l<_{}<:`>/rz[",;i~}[?-<)t+?~'''''''''''''''......
.......'''''''''''''''';>IiII"'^_^~v~>:!|UUt(->:^!{I~)\t-/\''''''''''''.........
.....'''''''''''''''''';"Ii!!!!!-[)1[l,l)Yv/)|][(|[[})\/?v+'''''''''''''.'''....
.'.....'''''''''''''''',l"i!>-1||(){?>!i|CYnxuxxvvnjff\\+r:'''''''''''''''......
...'''''''''''''''''''':!`lli_)tfft{_ll+tXvuczCJUJJJXx/|>/^'''''''''''''........
.....'''''''''''''''''';i`:;i_1jrjf[I!_)nLYcrXQOO00Czf\[+|"''''''''''''''.......
.'...''''''''''''''''''''',Il~}\rur+>[-/zwZLJuL0ZOLXn\\i{\`''''''''''''''.......
.'....''''''''''''''''''''^;Ii?1/t{-<!Ii}fr))zJJLLYvr(];''''''''''''''''..'.....
....'.''''''''''''''''''''`,,I+]+:`^"`::-i~+[1/cXUzn/}-"''''''''''''''''''......
....'''..'''''''''''''''''',:I<-l::`I!l+{)\t|~>!{vvf?_>''''''''''''''....''.....
.'...''..'''''''''''''''''''",l~_>+I,;?)|))}?[)?\cx}[>''''''''''''''''''''''....
.......'''''''''''''''''''''.",;!i_<>>~?{\/fnuu)\f1[!'''''''''''''''''.''.......
.........'''''''''''''''''''"''`"l<?]]<!!~rXYXj1---:'''''''''''''''''''''.......
.......''''''''''''''''''''.],'  ^;<_+]{(\tnz\}iiI"-?'''''''''''''''''.''.......
......'..'..'''''''''''''. '(:"^  .^:I[(|1[]-I,''<]-Y'.'''''''''''''''''.'......
..........'''''''''''''.   `)?,,,^   .,:""^`..'![{{bQ^  .'''''''''''''''........
..........'''''''''.       .1\/I;;:"`'..'''^;-}1)|kpC". ..  .'''''''..'.........
.........'''.'..           .[fxzr>!ll!!>~-]{))|(0ahb(^' .'. ... .....'..........
............         ...   .`\XJQZC]-??[}1|\/|Jooohp>^'..''' ...................
.......       ......'''..  .'-jUmddkm()((\/|Ya***hkc^^'..''''...................
..        ........ '``'.....'ltzJwkkhoJrr\Jh**#*hhq:'``'..'``'..'''''....... ...
.     ............'```'''...':jUULwpt^l~__i[q#*hoaQ`'``'''''``....'''''.........
.. ...........'''.  .''.'....`tCCJL;,^I,"<}~.?aaoor'`````'``'..''.'''''''''.....
...........'''''.....'''''...'<LJC[>I:l!;_'<v_+Qoa>``^`````'.'''''''''''''''''.'
 .........'''''''..''''''''...:xmbOr[>._~],OwOk0rY```````````''.''''''''''''''.'
 .'...'''''''''. ''`'''''''..'`uXkbwj}`>":jwwdkdp_'`^````````'`'..''''`'````''.'
 .'..'''''''''''..''`'''''''..'"xdkbri^'1}"Lpbdkv:'^^^`````''''''''''````````'''
 .''''''''''''''' '`'`''''''..'`1mhk1;`>)|.{wddh{``^^^```'''''`''''``````````.`.
...'..'''''''''''. ''`'''''''.'`?Jhdl:<+;:IlJddd>'`^^`````'''`'``````^``````'.'.
 ..' .''''''''''''..'```'''''..'"nbL!++'l:?iiwqL``^^^`````''`''`````````^``'.''.
 ..'..''''''''''''' '``````''..'`(d)~!'iI<],;Cp|'`^^^````````'````````````'..'..
 ...' .''''..''''`'' ```````'..'`_p?^^>;]{:"Icw!`^^^^^`````^'^```````````'. ....
....' ..'''...''''``'.``````''..';OII;:[~::<irc'`^^^^``````'`````^^``''`''. '...
.. ... ..'....'''''`'.'``````''.'`vil~?l";__[()'`^^^```````````````''''''. ....
...  .  .......'''''''.``````''''`,<+<I"l?[]^ii'^^^^``````'````````'..''.  ...
.....    ........''''`'.`````'''.``>I^,<~]~^I"^``````````'````````'.....   . ...
         ........'''''''.`````'''````;~+_:`I,'.```````````''``''''.  ..    ..'..
  ...     .........''''`''````''''`';l+>`^I"_.'````````''.'''''........    .....
.  ...     ........'''''' '````'''`'Ii,',I;}^ `````````'''''''''.....       ...
....        . ......'''''' ````'''`'"''I">{` .````````'''''''''....         ....
 .....           ....'''''' '``''''`.`;,_[`' '```````'''..'''''....           .."""

lines = ascii_face.split('\n')
W, H = 880, 900

def face_color(i, total):
    mid = total * 0.42
    dist = abs(i - mid) / mid
    if dist < 0.35:
        return "#39d353"
    elif dist < 0.6:
        return "#26a641"
    elif dist < 0.85:
        return "#006d32"
    return "#0e4429"

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="\'Courier New\',Courier,monospace">')
svg.append('''<defs><style>
.sl{animation:scan 4s linear infinite;opacity:.07}
.fl{animation:flame .35s ease-in-out infinite;transform-origin:0 0}
.rk{animation:bob 3s ease-in-out infinite}
@keyframes scan{0%{transform:translateY(0)}100%{transform:translateY(400px)}}
@keyframes flame{0%,100%{transform:scaleY(1)}50%{transform:scaleY(.55)}}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
</style></defs>''')

# background
svg.append(f'<rect width="{W}" height="{H}" fill="#0d1117"/>')

# ============ TERMINAL PANEL ============
svg.append('<rect x="14" y="14" width="852" height="480" rx="12" fill="none" stroke="#FF6B00" stroke-width="4" opacity="0.18"/>')
svg.append('<rect x="14" y="14" width="852" height="480" rx="12" fill="#0a0d13" stroke="#FF6B00" stroke-width="1.2"/>')

# title bar
svg.append('<line x1="14" y1="50" x2="866" y2="50" stroke="#FF6B00" stroke-width="0.6" opacity="0.5"/>')
svg.append('<circle cx="36" cy="32" r="5.5" fill="#ff5f57"/>')
svg.append('<circle cx="56" cy="32" r="5.5" fill="#febc2e"/>')
svg.append('<circle cx="76" cy="32" r="5.5" fill="#28c840"/>')
svg.append('<text x="440" y="36" fill="#8b949e" font-size="12" text-anchor="middle">tarek@devs ~ $ ./profile.sh --live</text>')
svg.append('<circle cx="796" cy="32" r="3.5" fill="#FF6B00"><animate attributeName="opacity" values="1;.15;1" dur="1.2s" repeatCount="indefinite"/></circle>')
svg.append('<text x="806" y="36" fill="#FF6B00" font-size="9" font-weight="bold" letter-spacing="1">SCANNING</text>')

# ---- LEFT: face ----
svg.append('<text x="30" y="70" fill="#FF8C00" font-size="9" letter-spacing="3" opacity="0.9">VISUAL.MAP</text>')
svg.append('<rect x="28" y="78" width="392" height="400" rx="4" fill="#0d1117" stroke="#30363d" stroke-width="1"/>')

total = len(lines)
y0, lh = 91, 6.55
for i, line in enumerate(lines):
    y = y0 + i * lh
    svg.append(f'<text x="36" y="{y:.1f}" fill="{face_color(i, total)}" font-size="6.2" textLength="376" lengthAdjust="spacingAndGlyphs" xml:space="preserve">{html.escape(line)}</text>')

# ---- RIGHT: system info ----
svg.append('<text x="436" y="70" fill="#FF8C00" font-size="9" letter-spacing="3" opacity="0.9">SYSTEM.INFO</text>')
svg.append('<line x1="436" y1="78" x2="852" y2="78" stroke="#30363d" stroke-width="0.6"/>')

CW = 6.6           # approx char width at font-size 11 Courier
KEY_X = 440
VAL_X = 852

def leader(key, val):
    start = KEY_X + (len(key) + 2) * CW + 4
    end = VAL_X - len(val) * CW - 8
    n = max(0, int((end - start) / CW))
    return start, "·" * n

info = [
    ("hdr",  "tarek@devs"),
    ("kv", "Name", "Tarek Rahman"),
    ("kv", "Role", "Asst. Mechanical Engineer"),
    ("kv", "Company", "HCEG"),
    ("kv", "Project", "Rajshahi WASA SWTP"),
    ("kv", "Location", "Rajshahi, Bangladesh"),
    ("kv", "Education", "BSc ME · CGPA 3.90/4.00"),
    ("sec", "Focus Areas"),
    ("kv", "Standards", "BS · ISO · IEC"),
    ("kv", "Systems", "Pumps · Valves · Cranes"),
    ("kv", "Docs", "Submittals · Vendor Coord"),
    ("kv", "Domain", "Turbomachinery · Renewables"),
    ("sec", "Contact"),
    ("kv", "Portfolio", "tarekrahman.vercel.app"),
    ("kv", "LinkedIn", "iamtarekrahman"),
    ("kv", "Email", "tarek737519@gmail.com"),
    ("sec", "Live Stats"),
    ("note", "See live GitHub stats badges below in README ↓"),
]

iy = 102
for item in info:
    if item[0] == "hdr":
        svg.append(f'<text x="{KEY_X}" y="{iy}" font-size="13" fill="#FF6B00" font-weight="bold">{item[1]}</text>')
        klen = (len(item[1]) + 1) * 7.9
        svg.append(f'<line x1="{KEY_X + klen:.0f}" y1="{iy-4}" x2="{VAL_X}" y2="{iy-4}" stroke="#FF6B00" stroke-width="1.2"/>')
        iy += 25
    elif item[0] == "sec":
        iy += 4
        svg.append(f'<text x="{KEY_X}" y="{iy}" font-size="11" fill="#FF8C00" font-weight="bold">─ {item[1]}</text>')
        klen = (len(item[1]) + 3) * CW + 6
        svg.append(f'<line x1="{KEY_X + klen:.0f}" y1="{iy-3.5}" x2="{VAL_X}" y2="{iy-3.5}" stroke="#FF8C00" stroke-width="1" opacity="0.7"/>')
        iy += 22
    elif item[0] == "kv":
        key, val = item[1], item[2]
        dx, dots = leader(key, val)
        svg.append(
            f'<text x="{KEY_X}" y="{iy}" font-size="11">'
            f'<tspan fill="#FF8C00" font-weight="bold">{html.escape(key)}</tspan><tspan fill="#8b949e">:</tspan>'
            f'</text>'
        )
        svg.append(f'<text x="{dx:.0f}" y="{iy}" font-size="11" fill="#3d444d">{dots}</text>')
        svg.append(f'<text x="{VAL_X}" y="{iy}" font-size="11" fill="#e6edf3" text-anchor="end">{html.escape(val)}</text>')
        iy += 21
    elif item[0] == "note":
        svg.append(f'<rect x="{KEY_X}" y="{iy-9}" width="7" height="10" fill="#FF6B00"/>')
        svg.append(f'<text x="{KEY_X+13}" y="{iy}" font-size="10.5" fill="#c9d1d9">{html.escape(item[1])}</text>')
        iy += 21

# scan sweep (clipped to terminal panel)
svg.append('<clipPath id="term"><rect x="15" y="51" width="850" height="442" rx="10"/></clipPath>')
svg.append('<g clip-path="url(#term)"><rect class="sl" x="15" y="51" width="850" height="26" fill="#FF6B00"/></g>')

# ============ CONTRIBUTION GRID ============
svg.append('<rect x="14" y="512" width="852" height="216" rx="12" fill="none" stroke="#FF6B00" stroke-width="4" opacity="0.18"/>')
svg.append('<rect x="14" y="512" width="852" height="216" rx="12" fill="#0a0d13" stroke="#FF6B00" stroke-width="1.2"/>')

palette = ['#e6edf3', '#9be9a8', '#40c463', '#30a14e', '#216e39']
COLS, ROWS, CELL, GAP = 30, 7, 20, 6
grid_w = COLS * (CELL + GAP) - GAP
gx = (W - grid_w) / 2
gy = 532

rings = set()
while len(rings) < 6:
    rings.add((random.randrange(COLS), random.randrange(ROWS)))

for c in range(COLS):
    for r in range(ROWS):
        fill = random.choices(palette, weights=[26, 22, 21, 17, 14])[0]
        x = gx + c * (CELL + GAP)
        y = gy + r * (CELL + GAP)
        extra = ""
        if fill in ('#40c463', '#30a14e', '#216e39') and random.random() < 0.06:
            extra = f'<animate attributeName="opacity" values="1;0.45;1" dur="{random.uniform(1.6, 3):.1f}s" repeatCount="indefinite"/>'
        svg.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{CELL}" height="{CELL}" rx="5" fill="{fill}">{extra}</rect>')

for (c, r) in rings:
    x = gx + c * (CELL + GAP) + CELL / 2
    y = gy + r * (CELL + GAP) + CELL / 2
    svg.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="14" fill="none" stroke="#30a14e" stroke-width="2.5"/>')

# ============ ROCKET ============
stars = [(120,770,1.5,.5),(300,820,1,.4),(520,760,1,.5),(700,840,1.5,.35),(820,780,1,.6),
         (200,870,1,.4),(430,880,1.5,.3),(620,790,1,.5),(60,850,1,.45),(760,865,1,.4)]
for sx, sy, sr, so in stars:
    svg.append(f'<circle cx="{sx}" cy="{sy}" r="{sr}" fill="white" opacity="{so}"/>')

svg.append('''<g transform="translate(190,810)"><g class="rk">
<polygon points="0,-38 -13,10 13,10" fill="#e6edf3"/>
<polygon points="0,-38 0,10 13,10" fill="#c9d1d9"/>
<rect x="-13" y="10" width="26" height="26" rx="3" fill="#e6edf3"/>
<rect x="0" y="10" width="13" height="26" rx="3" fill="#c9d1d9"/>
<circle cx="0" cy="20" r="6.5" fill="#0d1117" stroke="#FF6B00" stroke-width="2"/>
<polygon points="-13,26 -24,46 -13,40" fill="#FF6B00"/>
<polygon points="13,26 24,46 13,40" fill="#FF8C00"/>
<g transform="translate(0,40)">
<ellipse class="fl" cx="0" cy="10" rx="7" ry="16" fill="#FF6B00" opacity="0.9"/>
<ellipse class="fl" cx="0" cy="8" rx="4" ry="10" fill="#FFAA00"/>
</g>
<circle cx="0" cy="72" r="2" fill="#FF8C00" opacity="0.7"><animate attributeName="cy" values="72;95" dur="1s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.7;0" dur="1s" repeatCount="indefinite"/></circle>
<circle cx="-6" cy="66" r="1.5" fill="#FFAA00" opacity="0.6"><animate attributeName="cy" values="66;88" dur="1.3s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.6;0" dur="1.3s" repeatCount="indefinite"/></circle>
<circle cx="6" cy="69" r="1.5" fill="#FF6B00" opacity="0.6"><animate attributeName="cy" values="69;92" dur="0.8s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.6;0" dur="0.8s" repeatCount="indefinite"/></circle>
</g></g>''')

svg.append('</svg>')

with open("assets/section_about.svg", "w", encoding="utf-8") as f:
    f.write("\n".join(svg))
print(f"OK: {len(lines)} face lines, {len(svg)} svg elements")
