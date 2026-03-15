export interface Shop {
  id: string;
  name: string;
  phone?: string;
  address?: string;
  balance: number;
  created_at: string;
  updated_at: string;
}

export interface ShopCreate {
  name: string;
  phone?: string;
  address?: string;
}

export interface Product {
  id: string;
  name: string;
  unit_price: number;
  is_active: boolean;
  created_at: string;
}

export interface OrderItem {
  id: string;
  order_id: string;
  product_id: string;
  quantity: number;
  unit_price: number;
  total: number;
}

export interface Order {
  id: string;
  shop_id: string;
  total: number;
  status: string;
  notes?: string;
  created_at: string;
  items: OrderItem[];
}

export interface OrderCreate {
  shop_id: string;
  items: { product_id: string; quantity: number }[];
  notes?: string;
}

export interface Payment {
  id: string;
  shop_id: string;
  amount: number;
  payment_method?: string;
  notes?: string;
  created_at: string;
}

export interface PaymentCreate {
  shop_id: string;
  amount: number;
  payment_method?: string;
  notes?: string;
}

export interface Balance {
  shop_id: string;
  total_orders: number;
  total_payments: number;
  balance: number;
}
