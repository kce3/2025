import React, { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { motion } from "framer-motion";

const menuOptions = {
  아침: ["샐러드", "계란후라이", "토스트", "죽"],
  점심: ["비빔밥", "김치찌개", "제육볶음", "돈까스"],
  저녁: ["삼겹살", "된장찌개", "칼국수", "불고기"],
  디저트: ["케이크", "빙수", "과일", "아이스크림"],
};

const prices = {
  샐러드: 6000,
  계란후라이: 4000,
  토스트: 5000,
  죽: 7000,
  비빔밥: 8000,
  김치찌개: 7500,
  제육볶음: 8500,
  돈까스: 9000,
  삼겹살: 12000,
  된장찌개: 7000,
  칼국수: 8000,
  불고기: 11000,
  케이크: 6000,
  빙수: 7000,
  과일: 5000,
  아이스크림: 4000,
};

const MealPlanner = () => {
  const [screen, setScreen] = useState("intro");
  const [selectedMeals, setSelectedMeals] = useState({});
  const [total, setTotal] = useState(0);

  useEffect(() => {
    const timer = setTimeout(() => setScreen("main"), 3000);
    return () => clearTimeout(timer);
  }, []);

  const handleChoice = (mealType, choiceType) => {
    if (choiceType === "추천") {
      const randomMenu =
        menuOptions[mealType][
          Math.floor(Math.random() * menuOptions[mealType].length)
        ];
      setSelectedMeals((prev) => ({ ...prev, [mealType]: randomMenu }));
      setTotal((prev) => prev + prices[randomMenu]);
    } else {
      const menu = prompt(`${mealType} 메뉴를 직접 입력해주세요: ${menuOptions[mealType].join(", ")}`);
      if (menu && prices[menu]) {
        setSelectedMeals((prev) => ({ ...prev, [mealType]: menu }));
        setTotal((prev) => prev + prices[menu]);
      } else if (menu) {
        alert("해당 메뉴는 목록에 없습니다!");
      }
    }
  };

  if (screen === "intro") {
    return (
      <div className="flex items-center justify-center h-screen bg-gradient-to-r from-yellow-200 to-orange-200">
        <motion.h1
          className="text-4xl font-bold text-orange-800"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 2 }}
        >
          🍽️ 질환별 맞춤 식단 추천 웹사이트
        </motion.h1>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-b from-orange-50 to-yellow-100 p-6">
      <h2 className="text-3xl font-bold text-center text-orange-700 mb-6">
        오늘의 식단을 정해볼까요?
      </h2>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
        {Object.keys(menuOptions).map((mealType) => (
          <Card key={mealType} className="rounded-2xl shadow-lg">
            <CardContent className="p-6">
              <h3 className="text-xl font-semibold text-orange-600 mb-4">{mealType}</h3>
              <div className="flex gap-4">
                <Button onClick={() => handleChoice(mealType, "추천")}>
                  추천받기
                </Button>
                <Button onClick={() => handleChoice(mealType, "직접선택")}>
                  직접 선택
                </Button>
              </div>
              {selectedMeals[mealType] && (
                <motion.div
                  className="mt-4 p-3 rounded-xl bg-orange-100 text-orange-900 font-bold text-center text-lg"
                  initial={{ scale: 0 }}
                  animate={{ scale: 1 }}
                >
                  ✅ 선택한 메뉴: {selectedMeals[mealType]} ({prices[selectedMeals[mealType]]}원)
                </motion.div>
              )}
            </CardContent>
          </Card>
        ))}
      </div>

      <div className="mt-8 text-center text-2xl font-bold text-orange-800">
        총 합계: {total}원
      </div>
    </div>
  );
};

export default MealPlanner;
