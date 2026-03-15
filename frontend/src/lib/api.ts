const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1';

async function fetchApi<T>(endpoint: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE}${endpoint}`, {
    headers: {
      'Content-Type': 'application/json',
      ...options?.headers,
    },
    ...options,
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: 'An error occurred' }));
    throw new Error(error.detail || `HTTP error! status: ${response.status}`);
  }

  if (response.status === 204) {
    return {} as T;
  }

  return response.json();
}

export const api = {
  shops: {
    list: () => fetchApi<any[]>('/shops'),
    get: (id: string) => fetchApi<any>(`/shops/${id}`),
    search: (query: string) => fetchApi<any[]>(`/shops/search?q=${encodeURIComponent(query)}`),
    create: (data: any) => fetchApi<any>('/shops', {
      method: 'POST',
      body: JSON.stringify(data),
    }),
    update: (id: string, data: any) => fetchApi<any>(`/shops/${id}`, {
      method: 'PUT',
      body: JSON.stringify(data),
    }),
    delete: (id: string) => fetchApi<void>(`/shops/${id}`, {
      method: 'DELETE',
    }),
    getBalance: (id: string) => fetchApi<any>(`/shops/${id}/balance`),
  },
  products: {
    list: () => fetchApi<any[]>('/products'),
    get: (id: string) => fetchApi<any>(`/products/${id}`),
    create: (data: any) => fetchApi<any>('/products', {
      method: 'POST',
      body: JSON.stringify(data),
    }),
    update: (id: string, data: any) => fetchApi<any>(`/products/${id}`, {
      method: 'PUT',
      body: JSON.stringify(data),
    }),
  },
  orders: {
    listByShop: (shopId: string) => fetchApi<any[]>(`/orders/shop/${shopId}`),
    get: (id: string) => fetchApi<any>(`/orders/${id}`),
    create: (data: any) => fetchApi<any>('/orders', {
      method: 'POST',
      body: JSON.stringify(data),
    }),
    delete: (id: string) => fetchApi<void>(`/orders/${id}`, {
      method: 'DELETE',
    }),
  },
  payments: {
    listByShop: (shopId: string) => fetchApi<any[]>(`/payments/shop/${shopId}`),
    create: (data: any) => fetchApi<any>('/payments', {
      method: 'POST',
      body: JSON.stringify(data),
    }),
    delete: (id: string) => fetchApi<void>(`/payments/${id}`, {
      method: 'DELETE',
    }),
  },
};
