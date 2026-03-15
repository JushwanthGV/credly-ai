"use client";

import { useState, useEffect } from "react";
import { api } from "@/lib/api";
import { Shop, ShopCreate } from "@/lib/api-types";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent } from "@/components/ui/card";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogFooter,
} from "@/components/ui/dialog";
import { Plus, Search, Phone, MapPin } from "lucide-react";

export default function Home() {
  const [shops, setShops] = useState<Shop[]>([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [isLoading, setIsLoading] = useState(true);
  const [isAddDialogOpen, setIsAddDialogOpen] = useState(false);
  const [newShop, setNewShop] = useState<ShopCreate>({ name: "", phone: "" });
  const [isSubmitting, setIsSubmitting] = useState(false);

  useEffect(() => {
    loadShops();
  }, []);

  async function loadShops() {
    try {
      const data = searchQuery
        ? await api.shops.search(searchQuery)
        : await api.shops.list();
      setShops(data);
    } catch (error) {
      console.error("Failed to load shops:", error);
    } finally {
      setIsLoading(false);
    }
  }

  useEffect(() => {
    const debounce = setTimeout(() => {
      loadShops();
    }, 300);
    return () => clearTimeout(debounce);
  }, [searchQuery]);

  async function handleAddShop(e: React.FormEvent) {
    e.preventDefault();
    setIsSubmitting(true);
    try {
      await api.shops.create(newShop);
      setIsAddDialogOpen(false);
      setNewShop({ name: "", phone: "" });
      loadShops();
    } catch (error) {
      console.error("Failed to add shop:", error);
      alert("Failed to add shop. Please try again.");
    } finally {
      setIsSubmitting(false);
    }
  }

  function formatCurrency(amount: number): string {
    return new Intl.NumberFormat("en-IN", {
      style: "currency",
      currency: "INR",
      minimumFractionDigits: 0,
    }).format(amount);
  }

  return (
    <div>
      <div className="space-y-4">
        <div className="relative">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400" />
          <Input
            placeholder="Search shops..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="pl-10 h-12"
          />
        </div>

        <Button
          onClick={() => setIsAddDialogOpen(true)}
          className="w-full h-12 text-base"
        >
          <Plus className="mr-2 h-5 w-5" />
          Add Shop
        </Button>

        {isLoading ? (
          <div className="text-center py-8 text-gray-500">Loading...</div>
        ) : shops.length === 0 ? (
          <div className="text-center py-8 text-gray-500">
            No shops found. Add your first shop!
          </div>
        ) : (
          <div className="space-y-3">
            {shops.map((shop) => (
              <Card
                key={shop.id}
                className="cursor-pointer hover:shadow-md transition-shadow"
              >
                <CardContent className="p-4">
                  <div className="flex justify-between items-start">
                    <div>
                      <h3 className="font-semibold text-lg">{shop.name}</h3>
                      {shop.phone && (
                        <div className="flex items-center text-sm text-gray-500 mt-1">
                          <Phone className="h-3 w-3 mr-1" />
                          {shop.phone}
                        </div>
                      )}
                      {shop.address && (
                        <div className="flex items-center text-sm text-gray-500 mt-1">
                          <MapPin className="h-3 w-3 mr-1" />
                          {shop.address}
                        </div>
                      )}
                    </div>
                    <div className="text-right">
                      <div
                        className={`text-lg font-bold ${
                          shop.balance > 0 ? "text-red-600" : "text-green-600"
                        }`}
                      >
                        {formatCurrency(shop.balance)}
                      </div>
                      <div className="text-xs text-gray-500">Balance</div>
                    </div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        )}
      </div>

      <Dialog open={isAddDialogOpen} onOpenChange={setIsAddDialogOpen}>
        <DialogContent>
          <DialogHeader>
            <DialogTitle>Add New Shop</DialogTitle>
          </DialogHeader>
          <form onSubmit={handleAddShop}>
            <div className="space-y-4 py-4">
              <div>
                <label className="text-sm font-medium">Shop Name *</label>
                <Input
                  value={newShop.name}
                  onChange={(e) =>
                    setNewShop({ ...newShop, name: e.target.value })
                  }
                  placeholder="Enter shop name"
                  required
                  className="mt-1"
                />
              </div>
              <div>
                <label className="text-sm font-medium">Phone Number</label>
                <Input
                  value={newShop.phone}
                  onChange={(e) =>
                    setNewShop({ ...newShop, phone: e.target.value })
                  }
                  placeholder="Enter phone number"
                  className="mt-1"
                />
              </div>
            </div>
            <DialogFooter>
              <Button
                type="button"
                variant="outline"
                onClick={() => setIsAddDialogOpen(false)}
              >
                Cancel
              </Button>
              <Button type="submit" disabled={isSubmitting}>
                {isSubmitting ? "Adding..." : "Add Shop"}
              </Button>
            </DialogFooter>
          </form>
        </DialogContent>
      </Dialog>
    </div>
  );
}
