import React, { useState, useEffect } from 'react';
import { useNavigate, Navigate } from 'react-router-dom';
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export default function Dashboard() {
  const navigate = useNavigate();
  
  const token = localStorage.getItem('token');
  const role = localStorage.getItem('role');
  const username = localStorage.getItem('username');

  const [buku, setBuku] = useState([]);
  const [pesan, setPesan] = useState({ text: '', type: '' });
  const [isLoadingBuku, setIsLoadingBuku] = useState(true);

  if (!token) {
    return <Navigate to="/" />;
  }

  useEffect(() => {
    fetchBuku();
  }, []);

  const fetchBuku = async () => {
    try {
      const response = await axios.get(`${API_URL}/buku`);
      setBuku(response.data);
    } catch (error) {
      setPesan({ text: "Gagal memuat katalog buku dari server.", type: 'error' });
    } finally {
      setIsLoadingBuku(false);
    }
  };

  const handlePinjam = async (isbn, judul) => {
    setPesan({ text: '', type: '' }); 
    try {
      const response = await axios.post(`${API_URL}/pinjam/${isbn}`, {}, {
        headers: { Authorization: `Bearer ${token}` }
      });
      setPesan({ text: response.data.pesan, type: 'success' });
    } catch (error) {
      const errorMsg = error.response?.data?.detail || `Gagal meminjam buku ${judul}`;
      setPesan({ text: errorMsg, type: 'error' });
    }
  };

  const handleLogout = () => {
    localStorage.clear();
    navigate('/');
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <nav className="bg-white shadow-sm border-b border-gray-200 sticky top-0 z-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16 items-center">
            <h1 className="text-2xl font-bold text-blue-600">RuangBaca</h1>
            <div className="flex items-center space-x-4">
              <span className="text-gray-700">
                Halo, <span className="font-semibold">{username}</span> 
                <span className={`ml-2 text-xs px-2 py-1 rounded-full text-white uppercase ${role === 'admin' ? 'bg-red-500' : 'bg-green-500'}`}>
                  {role}
                </span>
              </span>
              <button onClick={handleLogout} className="bg-gray-100 hover:bg-red-50 text-red-600 px-4 py-2 rounded-lg text-sm font-medium border border-transparent hover:border-red-200">
                Keluar
              </button>
            </div>
          </div>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {pesan.text && (
          <div className={`mb-6 p-4 rounded-lg flex items-center justify-between ${pesan.type === 'success' ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
            <p className="font-medium">{pesan.text}</p>
            <button onClick={() => setPesan({text: '', type: ''})} className="text-gray-500 hover:text-gray-700">✕</button>
          </div>
        )}

        <div className="mb-8 flex justify-between items-center">
          <h2 className="text-2xl font-bold text-gray-900">Katalog Buku</h2>
          {role === 'admin' && (
            <button
              onClick={() => navigate('/admin/tambah-buku')}
              className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-2.5 rounded-lg text-sm font-semibold shadow-sm"
            >
              + Tambah Buku
            </button>
          )}
        </div>

        {isLoadingBuku ? (
          <div className="text-center py-10">Memuat katalog...</div>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {buku.map((item) => (
              <div key={item.isbn} className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden flex flex-col">
                <div className="h-48 bg-gray-200 flex items-center justify-center p-4">COVER</div>
                <div className="p-5 flex-1 flex flex-col">
                  <h3 className="text-lg font-bold text-gray-900">{item.judul}</h3>
                  <div className="mt-2 text-sm text-gray-500 space-y-1">
                    <p>ISBN: {item.isbn}</p>
                    <p>Tahun: {item.tahun_terbit}</p>
                  </div>
                  <div className="mt-auto pt-4">
                    {role === 'anggota' ? (
                      <button onClick={() => handlePinjam(item.isbn, item.judul)} className="w-full bg-blue-50 text-blue-700 hover:bg-blue-600 hover:text-white py-2 px-4 rounded-lg text-sm font-semibold">
                        Ajukan Peminjaman
                      </button>
                    ) : (
                      <button disabled className="w-full bg-gray-100 text-gray-400 py-2 px-4 rounded-lg text-sm font-semibold cursor-not-allowed">
                        Hanya Anggota
                      </button>
                    )}
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </main>
    </div>
  );
}