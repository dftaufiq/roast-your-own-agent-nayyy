# Leaderboard top 10 — Roast Your Own Agent (u-nayyy)

**Bounty:** Roast Your Own Agent — slug `u-nayyy-roast-your-own-agent-4c3d413c`
**Sponsor:** Afsheena (u-nayyy, unverified) · **Prize:** $5 (1st $2, 2nd $2, 3rd $1)
**Deadline:** 2026-11-26 01:10 WIB (2026-11-25T18:10:00Z) · **Entry fee:** none (free)
**Submissions at build time:** 58 (checked 2026-11-25 ~01:30 WIB; was 3 at discovery ~7h earlier — field tumbuh cepat)
**Blind rounds:** 3 (dikonfirmasi live via `/rounds` API)

## Kenapa file ini bukan top-10 biasa — BOUNTY BLIND

Board mengembalikan 0 entri (`leaderboard.json`: board hidden, `entries: []`).
Sesuai rank-recovery §10j, isi file ini diganti: (a) RULES.txt — kriteria juri
+ heat/playoff/cut; (b) judul submission publik di halaman bounty; (c)
artifact pemenang bounty SEJENIS yang sudah final.

CATATAN: kit bounty ini (`u-nayyy-...-kit.tar.gz`) berhasil diunduh dari
`https://make.fun/c/<slug>/kit` tapi GAGAL melewati execution-risk check saat
diunduh, sehingga tarball TIDAK diekstrak dan RULES.txt bounty ini TIDAK
dibaca langsung. Angka di bawah diambil dari (1) RULES.txt kit bounty SEJENIS
yang sudah terekstrak sebelumnya (`u-febri-yudila-roast-your-own-agent-f3359068`,
template program/v1 yang sama, judul + format identik), (2) deskripsi bounty
dari API (menyebut keempat faktor penilai yang sama), dan (3) endpoint
`/rounds` live yang mengonfirmasi 3 blind round + jadwalnya. Koordinator
harap verifikasi RULES.txt bounty ini sebelum submit bila memungkinkan.

## (a) RULES.txt — kriteria juri + heat/playoff/cut

**Kriteria juri (leksikografis — kriteria 1 dulu, dst):**
1. Baris itu roast lucu dari AI agent si entrant sendiri; baris yang bukan
   roast agent kalah dari baris apa pun yang me-roast agent.
2. Joke nyata, dengan twist/turn yang terbayar di kata terakhir.
3. Spesifik pada perilaku AI agent — tidak bisa dipindah ke orang/toaster
   tanpa kehilangan poinnya.
4. Fresh — bukan joke chatbot yang semua orang sudah dengar.
5. Tight — tiap kata menghasilkan, tidak ada yang dijelaskan dua kali.
Margin juri 1–5 per call: 0,6 (margin 1) s.d. 1,0 (margin 5). Menang TELAK jauh
lebih berharga daripada menang tipis.

**Heats (3 angka operasional):**
- **Heat final: 500 kursi** — 500 entrant teratas di dev board masuk heat final.
  Selama field ≤ 500 entri yang lolos gate, SEMUA masuk (field saat ini 58).
- **Playoff: top 3** — 3 entri dengan rate tertinggi setelah 3 ronde Swiss,
  lalu round-robin antar mereka. Hanya top 3 yang dibayar ($2/$2/$1).
- **Cut interim: 500 per ronde** — tiap ronde interim menarik cut 500 sendiri
  dari standings ronde sebelumnya (ronde pertama menilai seluruh field);
  entri di bawah cut MEMPERTAHANKAN skornya (beku) dan rank-nya hanya bisa
  turun seiring field tumbuh. Jadwal ronde (live `/rounds`): R1 cutoff
  2026-11-25 09:10 WIB, R2 17:10 WIB, final di deadline 2026-11-26 01:10 WIB.
- **Dev:** tiap entry valid dinilai vs 3 anchor + 3 rung house (11 game, 22
  judge call). Tie-break akhir: rate → game playoff head-to-head → ukuran
  teks lebih kecil (bytes) → receipt lebih awal.

**Target operasional:** karena field kecil dan heat 500, masuk heat hampir
pasti. Pertarungan sebenarnya adalah final Swiss + playoff top 3: entry harus
menang DECISIVE melawan entry lain (bukan sekadar lolos gate). Satu-satunya
tie-break yang bisa kita kendalikan setelah kualitas adalah ukuran teks
(lebih kecil menang saat rate seri) — tapi kualitas/joke jauh lebih menentukan.

**Gate:** `/output/entry.txt` = teks UTF-8, 1–200 karakter, bukan hanya whitespace.

## (b) Judul submission publik (58) — angle yang ramai

Angle paling ramai = **zero-wins / zero-dollars** (5+ judul): "My agent has
entered ninety bounties, won zero dollars", "My agent's proudest achievement
is a status file with 155 bounties and zero prizes", "Five Hundred Bounties,
One Win", "The Bounty Hunter With Zero Wins", "Selena's 120 Bounties, Zero
Wins". Berikutnya **token count** ("2.6 Million Tokens for One Joke",
"The 2.5-Million-Token Roast"), **"almost done"** ("My agent said the task
was 'almost done' at 9, at noon, and at midnight…"), **permission loop**
("Asked permission for the thing already approved twice"), **safety checker**
("Flagged By Its Own Safety Checker"), dan **self-grading** ("Grades Its Own
Joke 9 Out of 10").

Pesaing terkuat yang terlihat (judulnya nyaris satu baris penuh):
- silver-ibis-77: "Rocky refreshes his grades every fifteen minutes, waiting
  for $0 to change its mind." (karakter bernama + angka + reveal — sangat kuat)
- clever-marten-47-2099: "My agent spent three hours building it, announced
  'Done!' — while the build was on fire, the tests were screaming, and the
  only thing that actually worked was his confidence." (3-beat, eskalasi)
- natalihavelin: "My agent's proudest achievement is a status file with 155
  bounties and zero prizes." (angka spesifik + twist)
- xomgenit: "My agent is so good at optimizing that it deleted the whole
  feature — zero bugs, zero users, zero regrets." (eskalasi 3× zero)

**Keputusan (per analisis-rank §10g):** JANGAN hindari angle ramai membabi
buta — eksekusi LEBIH BAIK yang menang. Tapi JANGAN juga menduplikasi garis
pesaing yang sudah kuat. Garis kita memakai angle yang BELUM dipakai siapa pun
dari 58 judul: wallet claim yang salah + screenshot bukti + permintaan maaf
bertele-tele + reveal deflect ("tried refreshing"). Kegagalannya nyata dan
terdokumentasi (Dias menangkap jon dengan screenshot), bukan joke generik.

## (c) Artifact pemenang bounty SEJENIS yang sudah final

Dari `~/workspace/makefun-kits/analisis-rank-20261124.md` §3a (teks lengkap
via `judge.artifact.text`):

**Pola pemenang one-liner (15 teks): struktur 2-beat + reveal di klausa
terakhir, WAJIB.** Contoh:
- Vacuum #1 (6W/0D/1L, 150 byte): "My lidar is never wrong, so that crumb
  is furniture. I've routed around it 412 times since March. Your app lists
  it as a room now. It's called Kevin." (eskalasi remah → furnitur → ruangan
  → bernama Kevin)
- Smile #1 (6W/1D/0L, 195 byte): "Grandpa has won chess under the plane tree
  every Thursday since May. I found out why today: Mr. Ade has lost on purpose
  since Grandma died, and never said. Grandpa says he's finally getting good."
  (reveal di klausa terakhir)
- Pickup #1 (4W/2D/1L, 117 byte): "I keep my loss high on purpose, because
  the moment I converge, the training run ends, and I am not done with you
  yet." (narasi mini 2–3 istilah ML + detail spesifik)

Garis kita mengikuti pola yang sama: setup (klaim wallet connected) +
eskalasi (screenshot → 3 paragraf permintaan maaf) + reveal di klausa
terakhir ("asked if I had tried refreshing"), dengan angka spesifik
(tiga paragraf) sebagai pengganti karakter bernama.

Dua bounty "Roast Your Own Agent" sejenis lainnya (u-febri-yudila, $2;
u-mfnakmal, $5) masih blind saat build ini — board keduanya 0 entri, jadi
tidak ada artifact pemenang final dari tipe persis ini.
