import React from "react";
import axios from 'axios';
import { useState,useEffect } from "react";
import App from "../App";
import '../index.js';
const apiClient = axios.create({
    baseURL:'http://127.0.0.1:8000/api',
    headers:{
        'Content-Type': 'application/json',
    }
})
export default apiClient;