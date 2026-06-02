import React, { useState, useEffect } from 'react';
import { useNavigate, Navigate } from 'react-router-dom';
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export default function DaftarPeminjaman() {
  const token = localStorage.getItem('token');
  const role = localStorage.getItem('role');
  const navigate = useNavigate();

  // Redirect jika bukan admin
  if (!token || role !== 'admin') {
    return <Navigate to="/dashboard" />;
  }

  const [peminjaman, setPeminjaman] = useState([]);
  const [pesan, setPesan] = useState({ text: '', type: '' });
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    fetchPeminjaman();
  }, []);

  const fetchPeminjaman = async () => {
    try {
      const response = await axios.get(`${API_URL}/admin/peminjaman`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setPeminjaman(response.data);
    } catch (error) {
      setPesan({ text: 'Gagal memuat data peminjaman.', type: 'error' });
    } finally {
      setIsLoading(false);
    }
  };

  const handleUpdateStatus = async (id_peminjaman, status_baru) => {
    setPesan({ text: '', type: '' });
    try {
      const params = new URLSearchParams();
      params.append('status_baru', status_baru);

      const response = await axios.put(
        `${API_URL}/admin/peminjaman/${id_peminjaman}/status`,
        params,
        {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setPesan({ text: response.data.pesan, type: 'success' });
      // Refresh data setelah update
      fetchPeminjaman();
    } catch (error) {
      const errorMsg =
        error.response?.data?.detail || 'Gagal mengubah status peminjaman.';
      setPesan({ text: errorMsg, type: 'error' });
    }
  };

  const getStatusColor = (status) => {
    switch (status) {
      case 'Menunggu':
        return 'bg-yellow-100 text-yellow-800';
      case 'Dipinjam':
        return 'bg-blue-100 text-blue-800';
      case 'Dikembalikan':
        return 'bg-green-100 text-green-800';
      case 'Ditolak':
        return 'bg-red-100 text-red-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-4">
      <div className="max-w-7xl mx-auto">
        {/* Header + Navigasi */}
        <div className="mb-6 flex items-center justify-between">
          <button
            onClick={() => navigate('/dashboard')}
            className="text-blue-600 hover:underline flex items-center gap-1"
          >
            ← Kembali ke Dashboard
          </button>
          <h1 className="text-2xl font-bold text-gray-800">
            Verifikasi Peminjaman
          </h1>
          <div className="w-20" /> {/* Spacer agar judul tetap di tengah */}
        </div>

        {/* Notifikasi */}
        {pesan.text && (
          <div
            className={`mb-4 p-4 rounded-lg flex items-center justify-between ${
              pesan.type === 'success'
                ? 'bg-green-100 text-green-800'
                : 'bg-red-100 text-red-800'
            }`}
          >
            <p className="font-medium">{pesan.text}</p>
            <button
              onClick={() => setPesan({ text: '', type: '' })}
              className="text-gray-500 hover:text-gray-700"
            >
              ✕
            </button>
          </div>
        )}

        {/* Tabel */}
        {isLoading ? (
          <div className="text-center py-10 text-gray-500">
            Memuat data peminjaman...
          </div>
        ) : peminjaman.length === 0 ? (
          <div className="text-center py-10 text-gray-500">
            Belum ada data peminjaman.
          </div>
        ) : (
          <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
            <div className="overflow-x-auto">
              <table className="min-w-full divide-y divide-gray-200">
                <thead className="bg-gray-50">
                  <tr>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      ID
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Anggota
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Buku (ISBN)
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Status
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Aksi
                    </th>
                  </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                  {peminjaman.map((item) => (
                    <tr key={item.id_peminjaman} className="hover:bg-gray-50">
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        #{item.id_peminjaman}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-700">
                        {/* Asumsi backend mengembalikan relasi peminjam */}
                        {item.peminjam?.nama_anggota || `ID: ${item.id_anggota}`}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-700">
                        {/* Asumsi backend mengembalikan relasi buku */}
                        {item.buku?.judul || item.isbn}
                        <div className="text-xs text-gray-400">
                          {item.isbn}
                        </div>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <span
                          className={`px-2 py-1 inline-flex text-xs leading-5 font-semibold rounded-full ${getStatusColor(
                            item.status_peminjaman
                          )}`}
                        >
                          {item.status_peminjaman}
                        </span>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm">
                        {item.status_peminjaman === 'Menunggu' && (
                          <div className="flex gap-2">
                            <button
                              onClick={() =>
                                handleUpdateStatus(
                                  item.id_peminjaman,
                                  'Dipinjam'
                                )
                              }
                              className="bg-green-600 hover:bg-green-700 text-white px-3 py-1 rounded-md text-xs font-medium"
                            >
                              Setujui
                            </button>
                            <button
                              onClick={() =>
                                handleUpdateStatus(
                                  item.id_peminjaman,
                                  'Ditolak'
                                )
                              }
                              className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded-md text-xs font-medium"
                            >
                              Tolak
                            </button>
                          </div>
                        )}
                        {item.status_peminjaman === 'Dipinjam' && (
                          <button
                            onClick={() =>
                              handleUpdateStatus(
                                item.id_peminjaman,
                                'Dikembalikan'
                              )
                            }
                            className="bg-blue-600 hover:bg-blue-700 text-white px-3 py-1 rounded-md text-xs font-medium"
                          >
                            Tandai Dikembalikan
                          </button>
                        )}
                        {(item.status_peminjaman === 'Dikembalikan' ||
                          item.status_peminjaman === 'Ditolak') && (
                          <span className="text-gray-400 text-xs">
                            Tidak ada aksi
                          </span>
                        )}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}