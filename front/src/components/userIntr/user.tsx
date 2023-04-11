import $api from "../../utils/api/api";

export default function User() {
    $api.get("/users/");

    return <></>;
}
