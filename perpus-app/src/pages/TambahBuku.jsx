import React, { useState, useEffect } from 'react';
import { useNavigate, Navigate } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export default function TambahBuku() {
  const token = localStorage.getItem('token');
  const role = localStorage.getItem('role');
  const navigate = useNavigate();

  // Redirect jika bukan admin
  if (!token || role !== 'admin') {
    return <Navigate to="/dashboard" />;
  }

  const { register, handleSubmit, formState: { errors, isSubmitting }, reset } = useForm();
  const [kategoriList, setKategoriList] = useState([]);
  const [pesan, setPesan] = useState({ text: '', type: '' });
  const [loadingKategori, setLoadingKategori] = useState(true);

  useEffect(() => {
    fetchKategori();
  }, []);

  const fetchKategori = async () => {
    try {
      const response = await axios.get(`${API_URL}/kategori`);
      setKategoriList(response.data);
    } catch (error) {
      setPesan({ text: 'Gagal memuat daftar kategori', type: 'error' });
    } finally {
      setLoadingKategori(false);
    }
  };

  const onSubmit = async (data) => {
    setPesan({ text: '', type: '' });
    try {
      const params = new URLSearchParams();
      params.append('isbn', data.isbn);
      params.append('judul', data.judul);
      params.append('tahun_terbit', data.tahun_terbit);
      params.append('id_kategori', data.id_kategori);

      const response = await axios.post(`${API_URL}/buku`, params, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          Authorization: `Bearer ${token}`,
        },
      });
      setPesan({ text: response.data.pesan, type: 'success' });
      reset();
    } catch (error) {
      const errorMsg = error.response?.data?.detail || 'Gagal menambahkan buku. Periksa kembali data.';
      setPesan({ text: errorMsg, type: 'error' });
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-4">
      <div className="max-w-2xl mx-auto">
        <div className="mb-6 flex items-center justify-between">
          <button
            onClick={() => navigate('/dashboard')}
            className="text-blue-600 hover:underline flex items-center gap-1"
          >
            ← Kembali ke Dashboard
          </button>
          <h1 className="text-2xl font-bold text-gray-800">Tambah Buku Baru</h1>
        </div>

        {pesan.text && (
          <div
            className={`mb-4 p-4 rounded-lg flex items-center justify-between ${
              pesan.type === 'success' ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
            }`}
          >
            <p className="font-medium">{pesan.text}</p>
            <button onClick={() => setPesan({ text: '', type: '' })} className="text-gray-500 hover:text-gray-700">
              ✕
            </button>
          </div>
        )}

        <form
          onSubmit={handleSubmit(onSubmit)}
          className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 space-y-5"
        >
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">ISBN *</label>
            <input
              {...register('isbn', { required: 'ISBN wajib diisi' })}
              placeholder="Contoh: 978-3-16-148410-0"
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
            />
            {errors.isbn && <p className="text-red-500 text-sm mt-1">{errors.isbn.message}</p>}
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Judul Buku *</label>
            <input
              {...register('judul', { required: 'Judul wajib diisi' })}
              placeholder="Masukkan judul buku"
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
            />
            {errors.judul && <p className="text-red-500 text-sm mt-1">{errors.judul.message}</p>}
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Tahun Terbit *</label>
            <input
              type="number"
              {...register('tahun_terbit', {
                required: 'Tahun terbit wajib diisi',
                min: { value: 1000, message: 'Tahun minimal 1000' },
                max: { value: new Date().getFullYear(), message: `Tahun maksimal ${new Date().getFullYear()}` },
              })}
              placeholder="Contoh: 2023"
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
            />
            {errors.tahun_terbit && <p className="text-red-500 text-sm mt-1">{errors.tahun_terbit.message}</p>}
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Kategori *</label>
            {loadingKategori ? (
              <p className="text-gray-400 text-sm">Memuat kategori...</p>
            ) : (
              <select
                {...register('id_kategori', { required: 'Pilih kategori' })}
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none bg-white"
              >
                <option value="">-- Pilih Kategori --</option>
                {kategoriList.map((kat) => (
                  <option key={kat.id_kategori} value={kat.id_kategori}>
                    {kat.nama_kategori}
                  </option>
                ))}
              </select>
            )}
            {errors.id_kategori && <p className="text-red-500 text-sm mt-1">{errors.id_kategori.message}</p>}
          </div>

          <button
            type="submit"
            disabled={isSubmitting || loadingKategori}
            className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-lg transition-colors disabled:bg-blue-400 disabled:cursor-not-allowed"
          >
            {isSubmitting ? 'Menyimpan...' : 'Tambahkan Buku'}
          </button>
        </form>
      </div>
    </div>
  );
}