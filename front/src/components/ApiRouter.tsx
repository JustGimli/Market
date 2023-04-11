import { useState } from "react";
import { Route, Routes } from "react-router";
import { privRoutes, publRoutes } from "../routes";

export default function AppRouter() {
    const isAuth = useState(true); // mobx

    return (
        <>
            <Routes>
                {isAuth
                    ? privRoutes.map(({ path, Component }) => (
                          <Route
                              key={path}
                              path={path}
                              element={<Component />}
                          />
                      ))
                    : publRoutes.map(({ path, Component }) => (
                          <Route
                              key={path}
                              path={path}
                              element={<Component />}
                          />
                      ))}
            </Routes>
        </>
    );
}
