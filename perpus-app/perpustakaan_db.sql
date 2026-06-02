-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 05 Bulan Mei 2026 pada 05.09
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `perpustakaan_db`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `anggota`
--

CREATE TABLE `anggota` (
  `id_anggota` int(11) NOT NULL,
  `nama_anggota` varchar(255) NOT NULL,
  `no_telepon` varchar(20) DEFAULT NULL,
  `alamat` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `anggota`
--

INSERT INTO `anggota` (`id_anggota`, `nama_anggota`, `no_telepon`, `alamat`) VALUES
(1, 'Harjo Winarsih', '(0992) 226-2094', 'Jl. Astana Anyar No. 488, Tangerang, Banten 68429'),
(2, 'Cut Talia Rahimah', '+62 (356) 009 4176', 'Jl. M.H Thamrin No. 90, Sorong, SB 16664'),
(3, 'Anastasia Adriansyah', '+62 (048) 527-9421', 'Gang Ronggowarsito No. 53, Tanjungbalai, Kalimantan Selatan 92775'),
(4, 'drg. Cahyo Narpati', '+62 (45) 673 0253', 'Gang Ahmad Dahlan No. 16, Pagaralam, DKI Jakarta 18678'),
(5, 'Dr. Dewi Rajasa', '+62 (778) 041 3002', 'Gg. Kutisari Selatan No. 78, Lhokseumawe, KR 09591'),
(6, 'Candra Sihombing', '+62-725-680-7729', 'Gang Cikutra Timur No. 642, Padang, Kepulauan Riau 41314'),
(7, 'Farah Mahendra, M.TI.', '(0135) 591-8188', 'Gg. Peta No. 279, Padangpanjang, Bali 17115'),
(8, 'Dt. Paiman Yuliarti, M.Ak', '+62 (445) 752 5938', 'Gg. Jayawijaya No. 8, Langsa, JB 55658'),
(9, 'Capa Narpati', '082 033 7849', 'Gg. Rajiman No. 55, Tarakan, Sulawesi Barat 90528'),
(10, 'Ajeng Anggraini, S.Pd', '+62 (020) 725 4420', 'Jl. Ciumbuleuit No. 45, Bengkulu, Kepulauan Riau 75509'),
(11, 'Lala Putra', '+62 (22) 342 8396', 'Gg. Ciwastra No. 9, Sabang, SU 35000'),
(12, 'Asmianto Oktaviani', '+62 (403) 159 5509', 'Jl. Cempaka No. 030, Bekasi, Sulawesi Barat 30501'),
(13, 'Sakura Pertiwi', '(012) 699 9955', 'Gang S. Parman No. 50, Pontianak, AC 14915'),
(14, 'Elma Natsir, S.I.Kom', '+62-908-590-2630', 'Jl. Sukajadi No. 44, Banjarmasin, BB 42347'),
(15, 'Maria Wijayanti', '+62 (0037) 627-3638', 'Gang Erlangga No. 58, Singkawang, DI Yogyakarta 66333'),
(16, 'Uli Purnawati', '(045) 984 4224', 'Jl. Raya Ujungberung No. 98, Pematangsiantar, Sumatera Utara 89852'),
(17, 'Dewi Natsir', '+62 (025) 562 8772', 'Gang Suniaraja No. 5, Bima, Jawa Barat 60523'),
(18, 'dr. Galur Andriani', '+62 (706) 170 6707', 'Gang Cikapayang No. 35, Sukabumi, BA 90994'),
(19, 'R. Viktor Narpati', '+62-0033-481-4479', 'Gg. Raya Ujungberung No. 5, Mojokerto, Nusa Tenggara Barat 83863'),
(20, 'Nabila Waluyo', '+62 (0074) 737-1214', 'Jalan Moch. Ramdan No. 6, Kupang, SR 00274'),
(21, 'Warta Hastuti', '+62 (356) 097 9252', 'Gang Ciumbuleuit No. 6, Cimahi, PA 48917'),
(22, 'Kasiran Astuti', '+62 (0119) 596-9749', 'Gang Peta No. 15, Banjarbaru, Kepulauan Riau 93011'),
(23, 'Dina Samosir, S.I.Kom', '+62 (85) 779-4664', 'Gg. Lembong No. 7, Tomohon, JK 69876'),
(24, 'Aswani Wijayanti', '(0862) 496 9986', 'Jalan Gardujati No. 905, Metro, KT 28900'),
(25, 'Yance Padmasari', '+62-620-281-5887', 'Jl. Monginsidi No. 247, Batam, Sumatera Barat 07311'),
(26, 'Ghaliyati Anggraini', '+62-0768-926-8784', 'Gg. Monginsidi No. 04, Ternate, SB 27972'),
(27, 'Saadat Namaga', '(075) 512-3359', 'Jl. Asia Afrika No. 35, Yogyakarta, BT 23907'),
(28, 'Estiawan Aryani', '0813778802', 'Gang Rajiman No. 1, Malang, Lampung 72790'),
(29, 'Novi Rahmawati', '+62 (016) 395 3318', 'Gang Sukabumi No. 04, Bandar Lampung, Kalimantan Tengah 00061'),
(30, 'Hj. Yessi Sinaga', '(052) 579 0550', 'Gg. Jend. Sudirman No. 3, Denpasar, Papua Barat 27133'),
(31, 'Elisa Iswahyudi, S.Ked', '+62-038-053-9483', 'Jl. Pelajar Pejuang No. 9, Kota Administrasi Jakarta Barat, Sumatera Barat 77054'),
(32, 'Dipa Wasita', '(008) 241 1034', 'Jl. Sadang Serang No. 55, Surakarta, Kalimantan Utara 36416'),
(33, 'Icha Irawan', '(014) 542 7433', 'Gg. Cihampelas No. 9, Bandung, NB 93010'),
(34, 'Cahyadi Haryanti', '+62 (002) 370-6521', 'Jalan Bangka Raya No. 50, Mojokerto, Jawa Tengah 55243'),
(35, 'T. Candra Safitri, S.I.Kom', '+62-87-802-6254', 'Gg. Rajawali Barat No. 376, Tual, JK 30362'),
(36, 'drg. Tina Gunarto', '(0929) 590 2480', 'Jl. Peta No. 3, Lhokseumawe, GO 13428'),
(37, 'KH. Akarsana Agustina', '+62 (070) 484-2075', 'Gg. Ciwastra No. 33, Blitar, Sulawesi Tenggara 78347'),
(38, 'Pangestu Sihotang', '+62-260-703-7399', 'Gg. Moch. Ramdan No. 68, Cilegon, PB 48141'),
(39, 'Farah Hidayanto', '+62 (985) 655 2644', 'Gang Siliwangi No. 761, Bengkulu, Jawa Tengah 32563'),
(40, 'drg. Eli Wijayanti, S.Pd', '+62 (064) 685 7113', 'Jl. Stasiun Wonokromo No. 67, Tasikmalaya, Bali 95905'),
(41, 'dr. Ayu Purnawati, S.Pd', '(0730) 157-7672', 'Gang K.H. Wahid Hasyim No. 4, Langsa, Banten 66281'),
(42, 'Edward Hidayat, M.Ak', '+62 (071) 634 6307', 'Gg. Peta No. 499, Bekasi, Lampung 64817'),
(43, 'Tgk. Jaya Prastuti', '(028) 782-0913', 'Jalan Cikapayang No. 19, Blitar, JK 62377'),
(44, 'Puti Dewi Iswahyudi, M.Pd', '+62 (012) 548 6556', 'Gg. Setiabudhi No. 1, Denpasar, JB 58288'),
(45, 'Harto Kurniawan, M.M.', '+62-57-282-6383', 'Jl. Soekarno Hatta No. 82, Kediri, AC 87054'),
(46, 'Sutan Jaeman Tampubolon, S.Pd', '+62 (017) 286-4576', 'Gg. Peta No. 01, Banjar, Sumatera Barat 54339'),
(47, 'Putri Rahmawati', '+62-903-655-3648', 'Gg. Indragiri No. 29, Langsa, NT 02544'),
(48, 'Shania Latupono', '+62 (809) 542-8586', 'Gang Soekarno Hatta No. 08, Kediri, GO 58932'),
(49, 'Mustika Wasita, M.Ak', '+62 (597) 650-7829', 'Gg. Bangka Raya No. 29, Balikpapan, BB 88499'),
(50, 'Ika Yolanda', '+62 (062) 460-3375', 'Gg. Medokan Ayu No. 2, Banjarbaru, SR 71059'),
(51, 'Drs. Elvin Wulandari', '(095) 010-7171', 'Jl. Cihampelas No. 262, Surabaya, Sumatera Barat 58523'),
(52, 'Ayu Kusumo', '+62 (007) 518-8698', 'Gang Cikutra Barat No. 5, Depok, SS 36923'),
(53, 'Jono Rajata', '(076) 092 7800', 'Gang Pasirkoja No. 28, Langsa, AC 59669'),
(54, 'R. Naradi Dabukke, S.H.', '+62-64-666-3554', 'Gang Moch. Toha No. 65, Balikpapan, AC 01609'),
(55, 'Radit Pranowo, M.M.', '0804574419', 'Jalan Sentot Alibasa No. 125, Blitar, KS 79385'),
(56, 'drg. Gandewa Hasanah', '+62 (0822) 189 9888', 'Jl. Dr. Djunjunan No. 950, Sorong, SG 07563'),
(57, 'Marsito Wacana', '+62 (18) 488 3492', 'Gang Pasirkoja No. 2, Cilegon, BB 05716'),
(58, 'Lidya Mangunsong', '+62 (690) 457 8657', 'Jl. Veteran No. 760, Palopo, NB 66452'),
(59, 'Amalia Saptono', '+62 (02) 574 9581', 'Gang HOS. Cokroaminoto No. 975, Sawahlunto, BE 58759'),
(60, 'Kuncara Mulyani', '(0328) 166 2711', 'Jalan Ahmad Yani No. 09, Metro, BE 63174'),
(61, 'Halim Hutapea, M.Ak', '(0977) 097 5156', 'Jalan Wonoayu No. 98, Singkawang, SU 55702'),
(62, 'Putri Anggriawan, M.TI.', '+62 (63) 394-6092', 'Gang Wonoayu No. 41, Tegal, DKI Jakarta 11106'),
(63, 'R.M. Prakosa Maulana, S.Ked', '086 062 5278', 'Jalan Cikutra Timur No. 24, Malang, Kepulauan Riau 49583'),
(64, 'Jaga Palastri', '(0255) 057 3823', 'Jalan Astana Anyar No. 117, Banjarmasin, Kalimantan Barat 07194'),
(65, 'Ira Tamba, M.Kom.', '+62 (12) 909-8244', 'Gang Dr. Djunjunan No. 901, Tarakan, NB 39328'),
(66, 'Novi Januar', '087 277 2689', 'Gg. Rajawali Barat No. 0, Manado, Kepulauan Bangka Belitung 26617'),
(67, 'Ibrani Winarno, S.Kom', '+62 (048) 085-8801', 'Jalan Bangka Raya No. 909, Tanjungbalai, Maluku 47597'),
(68, 'Anita Prasasta', '+62 (076) 692 6201', 'Jl. Jend. Sudirman No. 56, Tanjungbalai, JK 06563'),
(69, 'Vanesa Gunawan', '(050) 505-0741', 'Jl. Merdeka No. 513, Bandung, KS 19600'),
(70, 'Sarah Safitri', '(023) 883-9638', 'Gg. K.H. Wahid Hasyim No. 71, Ambon, Sulawesi Utara 99450'),
(71, 'Maya Saputra, S.Pd', '+62 (0053) 753-9909', 'Jalan W.R. Supratman No. 889, Ternate, SS 02829'),
(72, 'Mutia Suryono', '(065) 462-9429', 'Gg. S. Parman No. 219, Kota Administrasi Jakarta Utara, SN 62832'),
(73, 'Joko Firmansyah', '+62-58-792-6313', 'Gg. Siliwangi No. 404, Surakarta, Banten 66453'),
(74, 'Zalindra Prayoga', '+62 (607) 484 1311', 'Gg. Sukabumi No. 18, Banjar, KI 38356'),
(75, 'Yusuf Nurdiyanti', '+62 (0818) 743-4321', 'Jl. R.E Martadinata No. 51, Solok, JI 68571'),
(76, 'Dt. Ridwan Aryani, S.E.', '0850242795', 'Jl. PHH. Mustofa No. 15, Tangerang, KB 39893'),
(77, 'drg. Ina Waluyo', '+62 (040) 940 8149', 'Jalan Pelajar Pejuang No. 2, Metro, SU 21500'),
(78, 'KH. Lanang Latupono, S.IP', '+62-221-451-4144', 'Gang Ir. H. Djuanda No. 67, Makassar, JI 39325'),
(79, 'drg. Hani Dabukke, M.Kom.', '+62 (0049) 449 2373', 'Gg. Laswi No. 9, Tangerang, Gorontalo 08529'),
(80, 'R.M. Mulyono Haryanto', '+62 (767) 826 9195', 'Jl. Suryakencana No. 45, Manado, SU 24411'),
(81, 'Galiono Ramadan', '(0833) 129-9188', 'Jalan Lembong No. 168, Parepare, BA 39005'),
(82, 'Qori Nasyidah, M.Ak', '+62 (058) 659 7589', 'Jalan Wonoayu No. 401, Tegal, SS 42846'),
(83, 'Margana Sihotang', '+62 (0896) 694 8815', 'Jalan Cempaka No. 385, Bitung, PA 06431'),
(84, 'Gadang Rahimah', '(0207) 817-4774', 'Jalan Jend. A. Yani No. 174, Cirebon, Banten 87581'),
(85, 'Karsana Uyainah', '(0401) 382-6435', 'Jl. Kutai No. 7, Padang Sidempuan, Sumatera Utara 73947'),
(86, 'Teddy Utami', '(061) 253-8787', 'Gg. Pacuan Kuda No. 221, Tangerang Selatan, Lampung 03664'),
(87, 'Paris Salahudin', '(077) 517-5473', 'Gang Moch. Toha No. 48, Kota Administrasi Jakarta Timur, SB 01924'),
(88, 'Irfan Padmasari', '(0085) 649 8779', 'Gang Moch. Toha No. 22, Surabaya, Maluku 91004'),
(89, 'Natalia Kusmawati, S.Ked', '+62-0392-225-5671', 'Jl. Kendalsari No. 8, Bukittinggi, PA 85528'),
(90, 'Mala Prasasta, S.E.I', '+62 (63) 577 9819', 'Gg. Sukabumi No. 040, Semarang, Riau 37430'),
(91, 'dr. Daruna Nashiruddin, S.Pd', '(0726) 792 5129', 'Jl. Jakarta No. 8, Balikpapan, KB 95780'),
(92, 'drg. Pandu Mangunsong, S.Sos', '+62 (467) 912 7759', 'Jl. Cihampelas No. 07, Mataram, JB 86460'),
(93, 'Omar Kusmawati', '(076) 534 8751', 'Gg. Erlangga No. 99, Lubuklinggau, Jawa Timur 61966'),
(94, 'Putu Haryanti', '+62 (057) 869-4475', 'Gg. Tubagus Ismail No. 751, Kediri, PA 55316'),
(95, 'Abyasa Suartini', '+62 (0618) 299-2806', 'Jl. Joyoboyo No. 4, Magelang, Jawa Barat 64820'),
(96, 'Tina Nasyidah', '+62 (83) 138-2604', 'Jalan H.J Maemunah No. 97, Banda Aceh, Nusa Tenggara Barat 40852'),
(97, 'Tgk. Gamani Pradana, M.M.', '+62 (016) 042-6722', 'Jl. Rajawali Barat No. 984, Yogyakarta, DKI Jakarta 00877'),
(98, 'Nadine Simbolon', '+62 (06) 411 6584', 'Gg. Pelajar Pejuang No. 805, Blitar, Lampung 42718'),
(99, 'R. Patricia Saragih, M.Kom.', '(051) 772-8988', 'Gang Pacuan Kuda No. 69, Binjai, LA 42029'),
(100, 'Makara Hardiansyah', '(043) 950 2294', 'Jl. Waringin No. 0, Manado, JA 31983');

-- --------------------------------------------------------

--
-- Struktur dari tabel `buku`
--

CREATE TABLE `buku` (
  `isbn` varchar(20) NOT NULL,
  `judul` varchar(255) NOT NULL,
  `tahun_terbit` int(11) DEFAULT NULL,
  `id_kategori` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `buku`
--

INSERT INTO `buku` (`isbn`, `judul`, `tahun_terbit`, `id_kategori`) VALUES
('978-0-04-613945-2', 'Autem Exercitationem Illo Accusantium Cum Fuga', 2005, 3),
('978-0-04-998552-0', 'Porro Fugit', 2005, 6),
('978-0-06-531501-1', 'Labore Optio Voluptas Amet', 2017, 9),
('978-0-09-451556-7', 'Occaecati Ipsum', 2016, 10),
('978-0-12-801811-8', 'Rerum Earum', 1998, 6),
('978-0-14-086727-5', 'Non Explicabo Nihil', 2006, 10),
('978-0-14-534705-5', 'Optio Est Odit', 1992, 7),
('978-0-14-826407-6', 'Repellat Delectus Suscipit', 2008, 8),
('978-0-15-604495-0', 'Tenetur Totam', 1990, 9),
('978-0-16-605731-5', 'Hic Autem', 1990, 1),
('978-0-17-368989-9', 'Earum Labore Distinctio Maxime Cupiditate', 1995, 4),
('978-0-207-31237-3', 'Ab Possimus Ipsum', 2013, 3),
('978-0-223-03054-1', 'Deserunt Ipsum Ullam', 2021, 9),
('978-0-237-16886-5', 'Eveniet Iure Doloremque Aspernatur Quia', 1996, 6),
('978-0-254-54410-9', 'Provident Amet Maiores', 2007, 1),
('978-0-302-56900-9', 'Voluptatibus Ex Expedita Cumque Porro Corporis', 2005, 5),
('978-0-316-33147-0', 'Suscipit Inventore', 2004, 10),
('978-0-330-23807-6', 'Sed Labore Cupiditate', 2016, 8),
('978-0-332-66498-9', 'Harum Blanditiis Eveniet', 2003, 5),
('978-0-372-79293-2', 'Sunt Deleniti Praesentium Assumenda', 2020, 4),
('978-0-421-23253-2', 'Et Dolore', 2008, 3),
('978-0-443-88825-0', 'Repudiandae Illum Accusantium Minima', 2021, 1),
('978-0-458-07856-1', 'Corporis Et Doloribus Placeat Enim', 2010, 2),
('978-0-488-20760-3', 'Dolor Maxime Aliquid', 2013, 9),
('978-0-492-49823-3', 'Harum Quod At Architecto Accusantium Aperiam', 1993, 6),
('978-0-498-24244-1', 'Harum Officia', 2021, 3),
('978-0-499-98826-3', 'Aut Qui', 1998, 2),
('978-0-502-16000-6', 'Vitae Aliquid Incidunt Dignissimos', 2015, 9),
('978-0-506-76409-5', 'Dignissimos Pariatur Temporibus', 2005, 8),
('978-0-511-39431-7', 'Repellat Eum Distinctio At Maiores Rem', 1990, 1),
('978-0-519-14891-2', 'Molestiae Unde Facilis Laboriosam', 2023, 8),
('978-0-526-90295-8', 'Nisi Vitae Iste', 2020, 7),
('978-0-528-19273-9', 'Reiciendis Pariatur Voluptatem Veritatis Numquam', 2004, 5),
('978-0-539-90441-3', 'Dignissimos Fugit Rerum Suscipit', 2005, 5),
('978-0-543-36067-0', 'Possimus Molestias', 2000, 8),
('978-0-559-50677-2', 'Aliquid Nihil Quam Possimus', 1992, 1),
('978-0-571-19264-9', 'Dolores Adipisci', 2007, 8),
('978-0-617-76011-5', 'Quisquam Quis', 2011, 8),
('978-0-618-26076-8', 'Laboriosam Esse Voluptates Consectetur', 2013, 3),
('978-0-623-07658-3', 'Modi Quia Ipsam', 1999, 7),
('978-0-632-93607-6', 'Animi Illo', 1996, 10),
('978-0-643-35785-3', 'Quibusdam Nulla Illo Aspernatur', 2010, 2),
('978-0-646-27637-3', 'Autem Expedita Omnis Quibusdam Animi', 2005, 3),
('978-0-664-01301-1', 'Tempore Animi Non Similique Est', 2019, 8),
('978-0-664-46144-7', 'Ea Hic Unde', 2005, 2),
('978-0-7009-4892-5', 'Error', 2004, 4),
('978-0-7012-0364-1', 'Harum Numquam Occaecati', 2018, 7),
('978-0-7038-7122-0', 'Earum Odit Repellat Iste Natus', 1992, 3),
('978-0-7416-6667-3', 'Culpa Hic Officiis', 1992, 1),
('978-0-7520-1995-6', 'Neque Quos', 1993, 7),
('978-0-7523-6381-3', 'Ut Qui Maxime', 2014, 8),
('978-0-7662-4407-8', 'Autem Ratione Alias', 1999, 1),
('978-0-7704-4282-8', 'Voluptatem Molestiae Itaque', 2000, 10),
('978-0-7767-8781-7', 'Sapiente Omnis', 1994, 6),
('978-0-7860-5617-0', 'Ad Dolore Deleniti', 2006, 10),
('978-0-8463-7063-5', 'Repellendus Ipsum Sapiente Aperiam Minima', 2004, 10),
('978-0-85571-233-4', 'Saepe Beatae Ullam', 1996, 5),
('978-0-86300-156-7', 'Explicabo Deleniti Sit Ducimus Quasi', 2012, 8),
('978-0-87537-254-9', 'Fuga Unde Repellendus Autem', 1996, 7),
('978-0-906535-99-8', 'Ea Deserunt Sed Iure', 2006, 4),
('978-0-915276-77-6', 'Quibusdam Nihil Nesciunt', 2015, 3),
('978-0-924106-05-7', 'Occaecati Doloremque Corporis', 2021, 10),
('978-0-931219-56-6', 'Accusantium Consequatur Recusandae Facilis', 2006, 1),
('978-0-9694307-8-0', 'Ipsam Autem', 2002, 8),
('978-1-02-753343-6', 'Iure Aliquam Commodi Doloribus Explicabo', 2001, 10),
('978-1-05-032321-9', 'Asperiores Vero Nihil', 2001, 3),
('978-1-05-790743-6', 'Dolore Aliquam Odio Esse Illo', 2002, 2),
('978-1-05-858595-4', 'Quisquam Consequatur Repudiandae Mollitia Tempora Blanditiis', 2015, 6),
('978-1-164-26238-1', 'Eveniet Iste Amet Excepturi', 2006, 8),
('978-1-168-79251-8', 'Omnis Suscipit Ea', 2017, 8),
('978-1-183-98755-5', 'Minus Suscipit Temporibus Odit', 2014, 10),
('978-1-187-91799-2', 'Eius Ipsum Rem Aperiam', 2011, 3),
('978-1-211-02953-0', 'Tempore Quo Tenetur Dolorum', 2019, 9),
('978-1-239-61328-5', 'Ex Maxime', 2004, 8),
('978-1-273-09238-1', 'Maiores Modi Autem Quisquam', 2004, 7),
('978-1-278-61814-2', 'Voluptas Maxime Perspiciatis Repudiandae', 2017, 5),
('978-1-290-90136-9', 'Corporis Ex Est', 2011, 9),
('978-1-324-88064-6', 'Odio Minus Exercitationem Maiores', 2011, 6),
('978-1-332-67051-2', 'Neque Porro Accusamus', 1999, 8),
('978-1-339-36542-8', 'Placeat Commodi Aspernatur Eligendi Corrupti', 1996, 3),
('978-1-382-06374-6', 'Totam Deserunt Ea', 2022, 10),
('978-1-382-99470-5', 'Asperiores Cum Minus Facilis', 1991, 6),
('978-1-390-80297-9', 'Nulla Maxime Quibusdam', 2002, 9),
('978-1-391-03322-8', 'Mollitia Earum Excepturi Accusantium Illum Incidunt', 1993, 6),
('978-1-4264-6085-2', 'Velit Dolorum Maxime Explicabo Quasi', 2001, 10),
('978-1-4439-8383-9', 'Eaque Similique Autem', 1991, 7),
('978-1-4870-7444-9', 'Facilis Provident Velit', 2021, 3),
('978-1-5294-5495-6', 'Quo Tenetur Repudiandae', 2003, 3),
('978-1-5417-3794-5', 'Qui Quas Fugiat Enim', 2009, 3),
('978-1-55367-688-1', 'Sit Doloribus Laborum Sint Ea', 1991, 3),
('978-1-55772-565-3', 'Eius Ab Aperiam', 2008, 7),
('978-1-55896-427-3', 'Iure Vitae Et', 2003, 10),
('978-1-61552-337-5', 'Maiores Suscipit Qui Expedita Aliquam', 1992, 4),
('978-1-61954-645-5', 'Accusamus Voluptatem Ea', 2002, 5),
('978-1-69365-769-6', 'Vero Porro Architecto Aliquam', 2023, 8),
('978-1-69404-164-7', 'Inventore Molestiae Repellendus Aliquam', 2011, 2),
('978-1-69430-013-3', 'Libero Laboriosam', 2005, 3),
('978-1-69939-374-1', 'Doloremque Dignissimos', 2017, 8),
('978-1-71004-634-2', 'Delectus Explicabo Laudantium Voluptates Autem', 2009, 5),
('978-1-71383-815-9', 'Ducimus Consequatur Similique', 1993, 4),
('978-1-71538-829-4', 'Voluptatibus Perferendis', 2005, 5),
('978-1-75299-268-3', 'Eligendi Assumenda Quis Et Alias Explicabo', 2012, 1),
('978-1-79091-537-8', 'Totam Quasi Soluta Eius Id', 2024, 6),
('978-1-79713-341-6', 'Veniam Voluptas Aspernatur', 1994, 8),
('978-1-80451-812-0', 'Modi Consequatur Laudantium Minima', 2001, 4),
('978-1-80604-429-0', 'Exercitationem Fugiat Aspernatur', 2007, 2),
('978-1-82544-124-7', 'Culpa Libero Harum', 2009, 6),
('978-1-86411-106-4', 'Fugiat Praesentium', 2004, 8),
('978-1-882074-41-9', 'Accusantium Vitae', 2019, 2),
('978-1-907155-13-0', 'Labore Beatae Aperiam Dolorem Voluptatibus Ad', 1990, 2),
('978-1-938445-73-6', 'Officia Iure Ab Eos Aperiam', 2012, 5),
('978-1-943401-90-1', 'Voluptatem Dolores', 2004, 7),
('978-1-944008-36-9', 'Suscipit Excepturi Ullam Quae Ab', 2017, 3),
('978-1-951019-49-5', 'Autem Temporibus Repellendus', 2001, 9),
('978-1-955998-95-6', 'Officiis Odio Fugiat Eum Incidunt', 2021, 6),
('978-1-965709-96-2', 'Alias Minus Et Illo Accusamus Ad', 2003, 2),
('978-1-9763-1425-4', 'Architecto Quia Aliquid', 2001, 1),
('978-1-9778-3219-1', 'Perspiciatis Voluptatibus Soluta Harum Qui', 2018, 2),
('978-1-994899-80-1', 'Reiciendis Nihil Porro Optio Repudiandae', 2023, 6),
('978-1-997987-90-1', 'Ex Atque Eligendi Excepturi Quas', 1997, 6);

-- --------------------------------------------------------

--
-- Struktur dari tabel `buku_penulis`
--

CREATE TABLE `buku_penulis` (
  `isbn` varchar(20) NOT NULL,
  `id_penulis` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `buku_penulis`
--

INSERT INTO `buku_penulis` (`isbn`, `id_penulis`) VALUES
('978-0-04-613945-2', 25),
('978-0-04-613945-2', 47),
('978-0-04-998552-0', 18),
('978-0-06-531501-1', 20),
('978-0-09-451556-7', 13),
('978-0-09-451556-7', 45),
('978-0-12-801811-8', 11),
('978-0-14-086727-5', 26),
('978-0-14-086727-5', 29),
('978-0-14-534705-5', 35),
('978-0-14-826407-6', 42),
('978-0-15-604495-0', 18),
('978-0-15-604495-0', 22),
('978-0-16-605731-5', 32),
('978-0-17-368989-9', 11),
('978-0-17-368989-9', 38),
('978-0-207-31237-3', 46),
('978-0-223-03054-1', 15),
('978-0-237-16886-5', 1),
('978-0-237-16886-5', 32),
('978-0-254-54410-9', 41),
('978-0-302-56900-9', 19),
('978-0-302-56900-9', 25),
('978-0-316-33147-0', 42),
('978-0-316-33147-0', 43),
('978-0-330-23807-6', 2),
('978-0-332-66498-9', 3),
('978-0-372-79293-2', 6),
('978-0-372-79293-2', 16),
('978-0-421-23253-2', 45),
('978-0-443-88825-0', 7),
('978-0-443-88825-0', 46),
('978-0-458-07856-1', 28),
('978-0-458-07856-1', 38),
('978-0-488-20760-3', 11),
('978-0-488-20760-3', 13),
('978-0-492-49823-3', 43),
('978-0-498-24244-1', 14),
('978-0-498-24244-1', 43),
('978-0-499-98826-3', 38),
('978-0-502-16000-6', 20),
('978-0-502-16000-6', 49),
('978-0-506-76409-5', 26),
('978-0-511-39431-7', 30),
('978-0-511-39431-7', 31),
('978-0-519-14891-2', 34),
('978-0-519-14891-2', 40),
('978-0-526-90295-8', 47),
('978-0-528-19273-9', 11),
('978-0-528-19273-9', 45),
('978-0-539-90441-3', 21),
('978-0-539-90441-3', 38),
('978-0-543-36067-0', 28),
('978-0-543-36067-0', 31),
('978-0-559-50677-2', 11),
('978-0-559-50677-2', 34),
('978-0-571-19264-9', 11),
('978-0-617-76011-5', 28),
('978-0-618-26076-8', 8),
('978-0-618-26076-8', 28),
('978-0-623-07658-3', 21),
('978-0-623-07658-3', 28),
('978-0-632-93607-6', 25),
('978-0-643-35785-3', 16),
('978-0-643-35785-3', 20),
('978-0-646-27637-3', 33),
('978-0-646-27637-3', 46),
('978-0-664-01301-1', 2),
('978-0-664-01301-1', 5),
('978-0-664-46144-7', 34),
('978-0-7009-4892-5', 34),
('978-0-7012-0364-1', 40),
('978-0-7012-0364-1', 42),
('978-0-7038-7122-0', 21),
('978-0-7038-7122-0', 22),
('978-0-7416-6667-3', 3),
('978-0-7416-6667-3', 19),
('978-0-7520-1995-6', 23),
('978-0-7523-6381-3', 30),
('978-0-7662-4407-8', 43),
('978-0-7704-4282-8', 30),
('978-0-7704-4282-8', 48),
('978-0-7767-8781-7', 8),
('978-0-7767-8781-7', 10),
('978-0-7860-5617-0', 11),
('978-0-7860-5617-0', 27),
('978-0-8463-7063-5', 4),
('978-0-85571-233-4', 18),
('978-0-85571-233-4', 28),
('978-0-86300-156-7', 41),
('978-0-87537-254-9', 2),
('978-0-906535-99-8', 12),
('978-0-915276-77-6', 32),
('978-0-915276-77-6', 45),
('978-0-924106-05-7', 10),
('978-0-924106-05-7', 18),
('978-0-931219-56-6', 3),
('978-0-9694307-8-0', 21),
('978-1-02-753343-6', 16),
('978-1-05-032321-9', 47),
('978-1-05-790743-6', 11),
('978-1-05-790743-6', 27),
('978-1-05-858595-4', 6),
('978-1-05-858595-4', 8),
('978-1-164-26238-1', 16),
('978-1-168-79251-8', 38),
('978-1-168-79251-8', 41),
('978-1-183-98755-5', 31),
('978-1-183-98755-5', 34),
('978-1-187-91799-2', 3),
('978-1-211-02953-0', 44),
('978-1-211-02953-0', 45),
('978-1-239-61328-5', 16),
('978-1-239-61328-5', 33),
('978-1-273-09238-1', 42),
('978-1-273-09238-1', 44),
('978-1-278-61814-2', 44),
('978-1-290-90136-9', 19),
('978-1-290-90136-9', 40),
('978-1-324-88064-6', 16),
('978-1-324-88064-6', 40),
('978-1-332-67051-2', 1),
('978-1-332-67051-2', 27),
('978-1-339-36542-8', 31),
('978-1-382-06374-6', 26),
('978-1-382-06374-6', 48),
('978-1-382-99470-5', 2),
('978-1-382-99470-5', 7),
('978-1-390-80297-9', 5),
('978-1-391-03322-8', 26),
('978-1-4264-6085-2', 22),
('978-1-4439-8383-9', 46),
('978-1-4870-7444-9', 3),
('978-1-4870-7444-9', 7),
('978-1-5294-5495-6', 7),
('978-1-5294-5495-6', 18),
('978-1-5417-3794-5', 38),
('978-1-55367-688-1', 22),
('978-1-55367-688-1', 36),
('978-1-55772-565-3', 7),
('978-1-55772-565-3', 21),
('978-1-55896-427-3', 29),
('978-1-61552-337-5', 2),
('978-1-61552-337-5', 3),
('978-1-61954-645-5', 30),
('978-1-69365-769-6', 1),
('978-1-69365-769-6', 16),
('978-1-69404-164-7', 15),
('978-1-69430-013-3', 11),
('978-1-69430-013-3', 15),
('978-1-69939-374-1', 8),
('978-1-71004-634-2', 22),
('978-1-71383-815-9', 6),
('978-1-71538-829-4', 17),
('978-1-71538-829-4', 37),
('978-1-75299-268-3', 23),
('978-1-75299-268-3', 44),
('978-1-79091-537-8', 18),
('978-1-79713-341-6', 39),
('978-1-80451-812-0', 22),
('978-1-80604-429-0', 13),
('978-1-80604-429-0', 27),
('978-1-82544-124-7', 8),
('978-1-86411-106-4', 7),
('978-1-86411-106-4', 16),
('978-1-882074-41-9', 10),
('978-1-882074-41-9', 22),
('978-1-907155-13-0', 4),
('978-1-907155-13-0', 26),
('978-1-938445-73-6', 34),
('978-1-943401-90-1', 18),
('978-1-944008-36-9', 25),
('978-1-944008-36-9', 47),
('978-1-951019-49-5', 6),
('978-1-951019-49-5', 15),
('978-1-955998-95-6', 45),
('978-1-965709-96-2', 42),
('978-1-9763-1425-4', 4),
('978-1-9763-1425-4', 38),
('978-1-9778-3219-1', 4),
('978-1-994899-80-1', 6),
('978-1-994899-80-1', 37),
('978-1-997987-90-1', 19),
('978-1-997987-90-1', 47);

-- --------------------------------------------------------

--
-- Struktur dari tabel `denda`
--

CREATE TABLE `denda` (
  `id_denda` int(11) NOT NULL,
  `id_peminjaman` int(11) DEFAULT NULL,
  `nominal_denda` decimal(10,2) NOT NULL,
  `status_pembayaran` enum('Belum Lunas','Lunas') DEFAULT 'Belum Lunas'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `denda`
--

INSERT INTO `denda` (`id_denda`, `id_peminjaman`, `nominal_denda`, `status_pembayaran`) VALUES
(1, 6, 16000.00, 'Lunas'),
(2, 9, 16000.00, 'Belum Lunas'),
(3, 14, 14000.00, 'Belum Lunas'),
(4, 15, 20000.00, 'Belum Lunas'),
(5, 16, 26000.00, 'Lunas'),
(6, 18, 10000.00, 'Belum Lunas'),
(7, 20, 26000.00, 'Lunas'),
(8, 23, 4000.00, 'Belum Lunas'),
(9, 25, 28000.00, 'Lunas'),
(10, 26, 10000.00, 'Lunas'),
(11, 27, 2000.00, 'Lunas'),
(12, 28, 10000.00, 'Lunas'),
(13, 30, 28000.00, 'Belum Lunas'),
(14, 32, 18000.00, 'Belum Lunas'),
(15, 34, 14000.00, 'Belum Lunas'),
(16, 37, 10000.00, 'Lunas'),
(17, 38, 16000.00, 'Lunas'),
(18, 39, 24000.00, 'Lunas'),
(19, 41, 26000.00, 'Belum Lunas'),
(20, 42, 14000.00, 'Belum Lunas'),
(21, 43, 10000.00, 'Lunas'),
(22, 45, 24000.00, 'Belum Lunas'),
(23, 47, 28000.00, 'Lunas'),
(24, 48, 28000.00, 'Lunas'),
(25, 50, 24000.00, 'Lunas'),
(26, 51, 22000.00, 'Belum Lunas'),
(27, 60, 8000.00, 'Belum Lunas'),
(28, 61, 28000.00, 'Belum Lunas'),
(29, 63, 16000.00, 'Belum Lunas'),
(30, 66, 2000.00, 'Lunas'),
(31, 67, 6000.00, 'Belum Lunas'),
(32, 68, 6000.00, 'Belum Lunas'),
(33, 69, 8000.00, 'Belum Lunas'),
(34, 70, 22000.00, 'Belum Lunas'),
(35, 72, 8000.00, 'Lunas'),
(36, 73, 28000.00, 'Belum Lunas'),
(37, 74, 8000.00, 'Lunas'),
(38, 76, 18000.00, 'Belum Lunas'),
(39, 78, 8000.00, 'Lunas'),
(40, 81, 8000.00, 'Belum Lunas'),
(41, 87, 22000.00, 'Lunas'),
(42, 89, 14000.00, 'Lunas'),
(43, 90, 4000.00, 'Lunas'),
(44, 91, 12000.00, 'Belum Lunas'),
(45, 93, 8000.00, 'Belum Lunas'),
(46, 95, 2000.00, 'Lunas'),
(47, 99, 28000.00, 'Belum Lunas'),
(48, 100, 20000.00, 'Belum Lunas'),
(49, 103, 20000.00, 'Lunas'),
(50, 105, 10000.00, 'Lunas'),
(51, 108, 4000.00, 'Lunas'),
(52, 111, 16000.00, 'Lunas'),
(53, 112, 8000.00, 'Lunas'),
(54, 113, 12000.00, 'Lunas'),
(55, 116, 2000.00, 'Belum Lunas'),
(56, 119, 26000.00, 'Lunas'),
(57, 120, 4000.00, 'Lunas'),
(58, 122, 28000.00, 'Belum Lunas'),
(59, 125, 22000.00, 'Belum Lunas'),
(60, 128, 6000.00, 'Belum Lunas'),
(61, 129, 2000.00, 'Lunas'),
(62, 133, 18000.00, 'Lunas'),
(63, 135, 14000.00, 'Belum Lunas'),
(64, 136, 22000.00, 'Lunas'),
(65, 137, 2000.00, 'Lunas'),
(66, 138, 8000.00, 'Lunas'),
(67, 139, 2000.00, 'Lunas'),
(68, 140, 20000.00, 'Lunas'),
(69, 142, 2000.00, 'Belum Lunas'),
(70, 144, 24000.00, 'Lunas'),
(71, 145, 6000.00, 'Lunas'),
(72, 147, 14000.00, 'Lunas'),
(73, 148, 14000.00, 'Lunas'),
(74, 150, 16000.00, 'Lunas');

-- --------------------------------------------------------

--
-- Struktur dari tabel `kategori`
--

CREATE TABLE `kategori` (
  `id_kategori` int(11) NOT NULL,
  `nama_kategori` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `kategori`
--

INSERT INTO `kategori` (`id_kategori`, `nama_kategori`) VALUES
(1, 'Fiksi'),
(2, 'Sains'),
(3, 'Sejarah'),
(4, 'Teknologi'),
(5, 'Filsafat'),
(6, 'Biografi'),
(7, 'Sastra'),
(8, 'Agama'),
(9, 'Seni'),
(10, 'Komik');

-- --------------------------------------------------------

--
-- Struktur dari tabel `peminjaman`
--

CREATE TABLE `peminjaman` (
  `id_peminjaman` int(11) NOT NULL,
  `id_anggota` int(11) DEFAULT NULL,
  `isbn` varchar(20) DEFAULT NULL,
  `tanggal_pinjam` date NOT NULL,
  `tenggat_kembali` date NOT NULL,
  `tanggal_dikembalikan` date DEFAULT NULL,
  `status_peminjaman` enum('Dipinjam','Dikembalikan','Terlambat') DEFAULT 'Dipinjam'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `peminjaman`
--

INSERT INTO `peminjaman` (`id_peminjaman`, `id_anggota`, `isbn`, `tanggal_pinjam`, `tenggat_kembali`, `tanggal_dikembalikan`, `status_peminjaman`) VALUES
(1, 20, '978-0-664-46144-7', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(2, 38, '978-1-382-06374-6', '2026-05-04', '2026-05-11', '2026-05-06', 'Dikembalikan'),
(3, 53, '978-0-543-36067-0', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(4, 48, '978-1-907155-13-0', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(5, 90, '978-1-187-91799-2', '2026-05-04', '2026-05-11', '2026-05-09', 'Dikembalikan'),
(6, 2, '978-1-4870-7444-9', '2026-05-04', '2026-05-11', '2026-05-19', 'Terlambat'),
(7, 6, '978-1-278-61814-2', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(8, 70, '978-1-61552-337-5', '2026-05-04', '2026-05-11', '2026-05-10', 'Dikembalikan'),
(9, 50, '978-1-79091-537-8', '2026-05-04', '2026-05-11', '2026-05-19', 'Terlambat'),
(10, 33, '978-0-254-54410-9', '2026-05-04', '2026-05-11', '2026-05-06', 'Dikembalikan'),
(11, 16, '978-0-85571-233-4', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(12, 3, '978-1-69365-769-6', '2026-05-04', '2026-05-11', '2026-05-09', 'Dikembalikan'),
(13, 49, '978-1-02-753343-6', '2026-05-04', '2026-05-11', '2026-05-09', 'Dikembalikan'),
(14, 86, '978-0-9694307-8-0', '2026-05-04', '2026-05-11', '2026-05-18', 'Terlambat'),
(15, 46, '978-1-5417-3794-5', '2026-05-04', '2026-05-11', '2026-05-21', 'Terlambat'),
(16, 79, '978-1-391-03322-8', '2026-05-04', '2026-05-11', '2026-05-24', 'Terlambat'),
(17, 75, '978-0-915276-77-6', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(18, 96, '978-0-506-76409-5', '2026-05-04', '2026-05-11', '2026-05-16', 'Terlambat'),
(19, 30, '978-0-458-07856-1', '2026-05-04', '2026-05-11', '2026-05-06', 'Dikembalikan'),
(20, 79, '978-0-511-39431-7', '2026-05-04', '2026-05-11', '2026-05-24', 'Terlambat'),
(21, 47, '978-1-965709-96-2', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(22, 3, '978-0-16-605731-5', '2026-05-04', '2026-05-11', '2026-05-09', 'Dikembalikan'),
(23, 82, '978-0-7416-6667-3', '2026-05-04', '2026-05-11', '2026-05-13', 'Terlambat'),
(24, 19, '978-0-372-79293-2', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(25, 50, '978-1-61954-645-5', '2026-05-04', '2026-05-11', '2026-05-25', 'Terlambat'),
(26, 29, '978-0-7860-5617-0', '2026-05-04', '2026-05-11', '2026-05-16', 'Terlambat'),
(27, 69, '978-1-164-26238-1', '2026-05-04', '2026-05-11', '2026-05-12', 'Terlambat'),
(28, 63, '978-1-4264-6085-2', '2026-05-04', '2026-05-11', '2026-05-16', 'Terlambat'),
(29, 33, '978-1-994899-80-1', '2026-05-04', '2026-05-11', '2026-05-05', 'Dikembalikan'),
(30, 58, '978-0-488-20760-3', '2026-05-04', '2026-05-11', '2026-05-25', 'Terlambat'),
(31, 19, '978-1-239-61328-5', '2026-05-04', '2026-05-11', '2026-05-11', 'Dikembalikan'),
(32, 78, '978-0-15-604495-0', '2026-05-04', '2026-05-11', '2026-05-20', 'Terlambat'),
(33, 75, '978-0-646-27637-3', '2026-05-04', '2026-05-11', '2026-05-08', 'Dikembalikan'),
(34, 65, '978-1-168-79251-8', '2026-05-04', '2026-05-11', '2026-05-18', 'Terlambat'),
(35, 59, '978-0-12-801811-8', '2026-05-04', '2026-05-11', '2026-05-11', 'Dikembalikan'),
(36, 37, '978-0-458-07856-1', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(37, 26, '978-1-86411-106-4', '2026-05-04', '2026-05-11', '2026-05-16', 'Terlambat'),
(38, 99, '978-0-519-14891-2', '2026-05-04', '2026-05-11', '2026-05-19', 'Terlambat'),
(39, 62, '978-1-79091-537-8', '2026-05-04', '2026-05-11', '2026-05-23', 'Terlambat'),
(40, 23, '978-0-06-531501-1', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(41, 37, '978-0-526-90295-8', '2026-05-04', '2026-05-11', '2026-05-24', 'Terlambat'),
(42, 31, '978-1-69939-374-1', '2026-05-04', '2026-05-11', '2026-05-18', 'Terlambat'),
(43, 29, '978-1-69939-374-1', '2026-05-04', '2026-05-11', '2026-05-16', 'Terlambat'),
(44, 45, '978-0-372-79293-2', '2026-05-04', '2026-05-11', '2026-05-09', 'Dikembalikan'),
(45, 99, '978-1-211-02953-0', '2026-05-04', '2026-05-11', '2026-05-23', 'Terlambat'),
(46, 72, '978-0-502-16000-6', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(47, 62, '978-0-7009-4892-5', '2026-05-04', '2026-05-11', '2026-05-25', 'Terlambat'),
(48, 14, '978-1-61954-645-5', '2026-05-04', '2026-05-11', '2026-05-25', 'Terlambat'),
(49, 10, '978-0-511-39431-7', '2026-05-04', '2026-05-11', '2026-05-11', 'Dikembalikan'),
(50, 21, '978-1-239-61328-5', '2026-05-04', '2026-05-11', '2026-05-23', 'Terlambat'),
(51, 7, '978-1-943401-90-1', '2026-05-04', '2026-05-11', '2026-05-22', 'Terlambat'),
(52, 8, '978-0-499-98826-3', '2026-05-04', '2026-05-11', '2026-05-07', 'Dikembalikan'),
(53, 10, '978-1-69365-769-6', '2026-05-04', '2026-05-11', '2026-05-05', 'Dikembalikan'),
(54, 64, '978-0-498-24244-1', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(55, 5, '978-1-273-09238-1', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(56, 62, '978-1-168-79251-8', '2026-05-04', '2026-05-11', '2026-05-05', 'Dikembalikan'),
(57, 80, '978-0-506-76409-5', '2026-05-04', '2026-05-11', '2026-05-07', 'Dikembalikan'),
(58, 37, '978-0-492-49823-3', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(59, 49, '978-1-05-858595-4', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(60, 74, '978-0-12-801811-8', '2026-05-04', '2026-05-11', '2026-05-15', 'Terlambat'),
(61, 58, '978-1-55772-565-3', '2026-05-04', '2026-05-11', '2026-05-25', 'Terlambat'),
(62, 54, '978-1-938445-73-6', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(63, 15, '978-1-382-06374-6', '2026-05-04', '2026-05-11', '2026-05-19', 'Terlambat'),
(64, 14, '978-1-71004-634-2', '2026-05-04', '2026-05-11', '2026-05-07', 'Dikembalikan'),
(65, 77, '978-1-4870-7444-9', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(66, 63, '978-0-87537-254-9', '2026-05-04', '2026-05-11', '2026-05-12', 'Terlambat'),
(67, 58, '978-0-7416-6667-3', '2026-05-04', '2026-05-11', '2026-05-14', 'Terlambat'),
(68, 30, '978-0-14-534705-5', '2026-05-04', '2026-05-11', '2026-05-14', 'Terlambat'),
(69, 11, '978-1-79713-341-6', '2026-05-04', '2026-05-11', '2026-05-15', 'Terlambat'),
(70, 60, '978-0-7767-8781-7', '2026-05-04', '2026-05-11', '2026-05-22', 'Terlambat'),
(71, 25, '978-0-617-76011-5', '2026-05-04', '2026-05-11', '2026-05-05', 'Dikembalikan'),
(72, 16, '978-1-55772-565-3', '2026-05-04', '2026-05-11', '2026-05-15', 'Terlambat'),
(73, 99, '978-1-882074-41-9', '2026-05-04', '2026-05-11', '2026-05-25', 'Terlambat'),
(74, 98, '978-1-339-36542-8', '2026-05-04', '2026-05-11', '2026-05-15', 'Terlambat'),
(75, 43, '978-1-290-90136-9', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(76, 71, '978-0-207-31237-3', '2026-05-04', '2026-05-11', '2026-05-20', 'Terlambat'),
(77, 21, '978-0-254-54410-9', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(78, 41, '978-1-938445-73-6', '2026-05-04', '2026-05-11', '2026-05-15', 'Terlambat'),
(79, 94, '978-0-539-90441-3', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(80, 32, '978-1-69430-013-3', '2026-05-04', '2026-05-11', '2026-05-07', 'Dikembalikan'),
(81, 2, '978-0-7662-4407-8', '2026-05-04', '2026-05-11', '2026-05-15', 'Terlambat'),
(82, 66, '978-0-04-613945-2', '2026-05-04', '2026-05-11', '2026-05-07', 'Dikembalikan'),
(83, 51, '978-0-632-93607-6', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(84, 19, '978-1-71004-634-2', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(85, 72, '978-0-618-26076-8', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(86, 4, '978-1-79713-341-6', '2026-05-04', '2026-05-11', '2026-05-05', 'Dikembalikan'),
(87, 7, '978-0-7416-6667-3', '2026-05-04', '2026-05-11', '2026-05-22', 'Terlambat'),
(88, 5, '978-0-643-35785-3', '2026-05-04', '2026-05-11', '2026-05-06', 'Dikembalikan'),
(89, 3, '978-0-617-76011-5', '2026-05-04', '2026-05-11', '2026-05-18', 'Terlambat'),
(90, 83, '978-0-9694307-8-0', '2026-05-04', '2026-05-11', '2026-05-13', 'Terlambat'),
(91, 9, '978-1-239-61328-5', '2026-05-04', '2026-05-11', '2026-05-17', 'Terlambat'),
(92, 18, '978-0-316-33147-0', '2026-05-04', '2026-05-11', '2026-05-06', 'Dikembalikan'),
(93, 84, '978-0-511-39431-7', '2026-05-04', '2026-05-11', '2026-05-15', 'Terlambat'),
(94, 88, '978-1-882074-41-9', '2026-05-04', '2026-05-11', '2026-05-10', 'Dikembalikan'),
(95, 58, '978-1-4264-6085-2', '2026-05-04', '2026-05-11', '2026-05-12', 'Terlambat'),
(96, 56, '978-1-4870-7444-9', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(97, 59, '978-0-499-98826-3', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(98, 89, '978-0-8463-7063-5', '2026-05-04', '2026-05-11', '2026-05-10', 'Dikembalikan'),
(99, 94, '978-1-69404-164-7', '2026-05-04', '2026-05-11', '2026-05-25', 'Terlambat'),
(100, 57, '978-1-944008-36-9', '2026-05-04', '2026-05-11', '2026-05-21', 'Terlambat'),
(101, 63, '978-1-05-790743-6', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(102, 30, '978-0-526-90295-8', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(103, 98, '978-0-519-14891-2', '2026-05-04', '2026-05-11', '2026-05-21', 'Terlambat'),
(104, 49, '978-1-71383-815-9', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(105, 13, '978-0-646-27637-3', '2026-05-04', '2026-05-11', '2026-05-16', 'Terlambat'),
(106, 70, '978-1-290-90136-9', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(107, 31, '978-0-04-613945-2', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(108, 69, '978-0-14-534705-5', '2026-05-04', '2026-05-11', '2026-05-13', 'Terlambat'),
(109, 20, '978-0-664-01301-1', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(110, 14, '978-0-511-39431-7', '2026-05-04', '2026-05-11', '2026-05-09', 'Dikembalikan'),
(111, 66, '978-0-09-451556-7', '2026-05-04', '2026-05-11', '2026-05-19', 'Terlambat'),
(112, 19, '978-1-71383-815-9', '2026-05-04', '2026-05-11', '2026-05-15', 'Terlambat'),
(113, 30, '978-0-8463-7063-5', '2026-05-04', '2026-05-11', '2026-05-17', 'Terlambat'),
(114, 25, '978-0-646-27637-3', '2026-05-04', '2026-05-11', '2026-05-08', 'Dikembalikan'),
(115, 60, '978-0-915276-77-6', '2026-05-04', '2026-05-11', '2026-05-06', 'Dikembalikan'),
(116, 6, '978-1-955998-95-6', '2026-05-04', '2026-05-11', '2026-05-12', 'Terlambat'),
(117, 5, '978-0-617-76011-5', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(118, 40, '978-1-71383-815-9', '2026-05-04', '2026-05-11', '2026-05-10', 'Dikembalikan'),
(119, 11, '978-1-4439-8383-9', '2026-05-04', '2026-05-11', '2026-05-24', 'Terlambat'),
(120, 89, '978-0-254-54410-9', '2026-05-04', '2026-05-11', '2026-05-13', 'Terlambat'),
(121, 12, '978-1-80604-429-0', '2026-05-04', '2026-05-11', '2026-05-09', 'Dikembalikan'),
(122, 46, '978-0-7767-8781-7', '2026-05-04', '2026-05-11', '2026-05-25', 'Terlambat'),
(123, 43, '978-0-646-27637-3', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(124, 96, '978-1-164-26238-1', '2026-05-04', '2026-05-11', '2026-05-06', 'Dikembalikan'),
(125, 57, '978-0-8463-7063-5', '2026-05-04', '2026-05-11', '2026-05-22', 'Terlambat'),
(126, 64, '978-1-5417-3794-5', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(127, 69, '978-0-915276-77-6', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(128, 10, '978-0-7520-1995-6', '2026-05-04', '2026-05-11', '2026-05-14', 'Terlambat'),
(129, 13, '978-0-559-50677-2', '2026-05-04', '2026-05-11', '2026-05-12', 'Terlambat'),
(130, 40, '978-1-391-03322-8', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(131, 86, '978-1-86411-106-4', '2026-05-04', '2026-05-11', '2026-05-09', 'Dikembalikan'),
(132, 17, '978-0-931219-56-6', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(133, 97, '978-1-332-67051-2', '2026-05-04', '2026-05-11', '2026-05-20', 'Terlambat'),
(134, 5, '978-0-499-98826-3', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(135, 70, '978-0-223-03054-1', '2026-05-04', '2026-05-11', '2026-05-18', 'Terlambat'),
(136, 12, '978-1-71383-815-9', '2026-05-04', '2026-05-11', '2026-05-22', 'Terlambat'),
(137, 87, '978-0-618-26076-8', '2026-05-04', '2026-05-11', '2026-05-12', 'Terlambat'),
(138, 78, '978-0-207-31237-3', '2026-05-04', '2026-05-11', '2026-05-15', 'Terlambat'),
(139, 7, '978-0-421-23253-2', '2026-05-04', '2026-05-11', '2026-05-12', 'Terlambat'),
(140, 26, '978-0-86300-156-7', '2026-05-04', '2026-05-11', '2026-05-21', 'Terlambat'),
(141, 71, '978-0-8463-7063-5', '2026-05-04', '2026-05-11', '2026-05-07', 'Dikembalikan'),
(142, 3, '978-0-543-36067-0', '2026-05-04', '2026-05-11', '2026-05-12', 'Terlambat'),
(143, 23, '978-0-7860-5617-0', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(144, 91, '978-0-237-16886-5', '2026-05-04', '2026-05-11', '2026-05-23', 'Terlambat'),
(145, 13, '978-1-339-36542-8', '2026-05-04', '2026-05-11', '2026-05-14', 'Terlambat'),
(146, 33, '978-1-05-032321-9', '2026-05-04', '2026-05-11', '2026-05-06', 'Dikembalikan'),
(147, 38, '978-0-85571-233-4', '2026-05-04', '2026-05-11', '2026-05-18', 'Terlambat'),
(148, 36, '978-1-55896-427-3', '2026-05-04', '2026-05-11', '2026-05-18', 'Terlambat'),
(149, 30, '978-1-79091-537-8', '2026-05-04', '2026-05-11', '0000-00-00', 'Dipinjam'),
(150, 37, '978-0-12-801811-8', '2026-05-04', '2026-05-11', '2026-05-19', 'Terlambat');

-- --------------------------------------------------------

--
-- Struktur dari tabel `penulis`
--

CREATE TABLE `penulis` (
  `id_penulis` int(11) NOT NULL,
  `nama_penulis` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `penulis`
--

INSERT INTO `penulis` (`id_penulis`, `nama_penulis`) VALUES
(1, 'Sadina Kusmawati, S.T.'),
(2, 'Dt. Nasim Adriansyah, S.T.'),
(3, 'Waluyo Samosir'),
(4, 'Ir. Farhunnisa Prasetya, M.Farm'),
(5, 'Rahmi Pradana'),
(6, 'Mumpuni Mandasari'),
(7, 'Daruna Yuniar'),
(8, 'Sabar Wibowo, S.Pt'),
(9, 'Chelsea Napitupulu'),
(10, 'KH. Mustika Dabukke'),
(11, 'Harsana Mandasari'),
(12, 'Dagel Adriansyah'),
(13, 'Ifa Waluyo'),
(14, 'Galih Usada'),
(15, 'Siska Ardianto'),
(16, 'Mitra Ardianto'),
(17, 'drg. Jais Usamah'),
(18, 'Patricia Sitompul'),
(19, 'Nadia Hassanah'),
(20, 'R.M. Pangestu Riyanti, M.Farm'),
(21, 'Sarah Uwais'),
(22, 'R. Rachel Saragih'),
(23, 'Ratih Marpaung'),
(24, 'Gada Wulandari'),
(25, 'Dina Waskita'),
(26, 'Tgk. Praba Maheswara'),
(27, 'Empluk Budiyanto, S.T.'),
(28, 'Ir. Cahyo Mayasari'),
(29, 'Bambang Mangunsong'),
(30, 'Unjani Gunawan'),
(31, 'Arsipatra Susanti'),
(32, 'Tira Thamrin'),
(33, 'Naradi Wijaya'),
(34, 'Tgk. Umay Saragih, M.TI.'),
(35, 'Ir. Gasti Kuswoyo, M.Ak'),
(36, 'Wawan Wijayanti'),
(37, 'Yoga Wijayanti'),
(38, 'Viktor Winarno'),
(39, 'Kairav Nasyiah, S.IP'),
(40, 'Kamaria Namaga'),
(41, 'Wisnu Tamba'),
(42, 'Eli Wahyuni'),
(43, 'Lintang Suryono'),
(44, 'Qori Situmorang'),
(45, 'Najib Putra'),
(46, 'Yuni Utami'),
(47, 'Rizki Prasasta'),
(48, 'Hj. Sari Mayasari, M.TI.'),
(49, 'Lili Widodo'),
(50, 'Cut Amelia Purwanti');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `anggota`
--
ALTER TABLE `anggota`
  ADD PRIMARY KEY (`id_anggota`);

--
-- Indeks untuk tabel `buku`
--
ALTER TABLE `buku`
  ADD PRIMARY KEY (`isbn`),
  ADD KEY `id_kategori` (`id_kategori`);

--
-- Indeks untuk tabel `buku_penulis`
--
ALTER TABLE `buku_penulis`
  ADD PRIMARY KEY (`isbn`,`id_penulis`),
  ADD KEY `id_penulis` (`id_penulis`);

--
-- Indeks untuk tabel `denda`
--
ALTER TABLE `denda`
  ADD PRIMARY KEY (`id_denda`),
  ADD KEY `id_peminjaman` (`id_peminjaman`);

--
-- Indeks untuk tabel `kategori`
--
ALTER TABLE `kategori`
  ADD PRIMARY KEY (`id_kategori`);

--
-- Indeks untuk tabel `peminjaman`
--
ALTER TABLE `peminjaman`
  ADD PRIMARY KEY (`id_peminjaman`),
  ADD KEY `id_anggota` (`id_anggota`),
  ADD KEY `isbn` (`isbn`);

--
-- Indeks untuk tabel `penulis`
--
ALTER TABLE `penulis`
  ADD PRIMARY KEY (`id_penulis`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `anggota`
--
ALTER TABLE `anggota`
  MODIFY `id_anggota` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT untuk tabel `denda`
--
ALTER TABLE `denda`
  MODIFY `id_denda` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=75;

--
-- AUTO_INCREMENT untuk tabel `kategori`
--
ALTER TABLE `kategori`
  MODIFY `id_kategori` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT untuk tabel `peminjaman`
--
ALTER TABLE `peminjaman`
  MODIFY `id_peminjaman` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=151;

--
-- AUTO_INCREMENT untuk tabel `penulis`
--
ALTER TABLE `penulis`
  MODIFY `id_penulis` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `buku`
--
ALTER TABLE `buku`
  ADD CONSTRAINT `buku_ibfk_1` FOREIGN KEY (`id_kategori`) REFERENCES `kategori` (`id_kategori`) ON DELETE SET NULL;

--
-- Ketidakleluasaan untuk tabel `buku_penulis`
--
ALTER TABLE `buku_penulis`
  ADD CONSTRAINT `buku_penulis_ibfk_1` FOREIGN KEY (`isbn`) REFERENCES `buku` (`isbn`) ON DELETE CASCADE,
  ADD CONSTRAINT `buku_penulis_ibfk_2` FOREIGN KEY (`id_penulis`) REFERENCES `penulis` (`id_penulis`) ON DELETE CASCADE;

--
-- Ketidakleluasaan untuk tabel `denda`
--
ALTER TABLE `denda`
  ADD CONSTRAINT `denda_ibfk_1` FOREIGN KEY (`id_peminjaman`) REFERENCES `peminjaman` (`id_peminjaman`) ON DELETE CASCADE;

--
-- Ketidakleluasaan untuk tabel `peminjaman`
--
ALTER TABLE `peminjaman`
  ADD CONSTRAINT `peminjaman_ibfk_1` FOREIGN KEY (`id_anggota`) REFERENCES `anggota` (`id_anggota`) ON DELETE CASCADE,
  ADD CONSTRAINT `peminjaman_ibfk_2` FOREIGN KEY (`isbn`) REFERENCES `buku` (`isbn`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
