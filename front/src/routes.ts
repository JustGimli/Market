import Accaunt from "./pages/accaunt";
import Home from "./pages/home";
import { PUBLIC_ROUTES, USER_ROUTE } from "./utils/consts";

export const  publRoutes = [
    {
    path: PUBLIC_ROUTES,
    Component: Home
    }
]

export const privRoutes = [
    {
        path: USER_ROUTE,
        Component: Accaunt
    }
]