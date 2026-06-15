export interface Product {
  id: number;
  slug: string;
  name: string;
  description: string;
  longDescription?: string;
  price: number;
  image: string;
  pdf: string;
  previews?: string[];
  included?: string[];
}