package com.example.demo.controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.UserDto;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
@RestController

public class TestController {
    @GetMapping(value = "/test")
    public UserDto test(){

        UserDto dto = new UserDto();
        dto.setAge(17);
        dto.setName("Jane");

        return dto;

    }

    @RequestMapping(value = "/json_test", method = RequestMethod.GET)
    public String test(@RequestParam("id") String id){

        JsonObject obj = new JsonObject();
        obj.addProperty("title", "산사와 아가씨");
        obj.addProperty("content", "로맨틱 코메디");

        JsonObject data = new JsonObject();
        data.addProperty("time", "토일 8시");
        obj.add("data", data);

        return obj.toString();

    }

    @RequestMapping(value = "/product", method = RequestMethod.GET)
    public String testProduct(@RequestParam("id") String id){

        JsonObject obj = new JsonObject();
        obj.addProperty("item_nm", "수제 햄버거");
        obj.addProperty("item_detail", "소고기 패티와 토마토가 들어 있는 햄버거");
        obj.addProperty("item_reg_date", "2022/04/22");
        obj.addProperty("item_price", "4000");

        return obj.toString();

    }

    @RequestMapping(value = "/productlist", method = RequestMethod.GET)
    public String productList(){

        JsonObject obj1 = new JsonObject();
        obj1.addProperty("item_nm", "수제 햄버거");
        obj1.addProperty("item_detail", "소고기 패티와 토마토가 들어 있는 햄버거");
        obj1.addProperty("item_reg_date", "2022/04/22");
        obj1.addProperty("item_price", "4000");

        JsonObject obj2 = new JsonObject();
        obj2.addProperty("item_nm", "카레라이스");
        obj2.addProperty("item_detail", "매운 3분 카레라이스");
        obj2.addProperty("item_reg_date", "2022/03/10");
        obj2.addProperty("item_price", "8000");

        JsonObject obj3 = new JsonObject();
        obj3.addProperty("item_nm", "라면");
        obj3.addProperty("item_detail", "소고기 라면");
        obj3.addProperty("item_reg_date", "2021/09/10");
        obj3.addProperty("item_price", "1500");

        JsonArray infoArray = new JsonArray();
        infoArray.add(obj1);
        infoArray.add(obj2);
        infoArray.add(obj3);

        return infoArray.toString();
    }



}
