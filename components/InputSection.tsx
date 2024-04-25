import { Input } from "antd";
import React, { Dispatch, SetStateAction, useState } from "react";

interface InputSectionProps {
	title: string;
	placeholder: string;
	data: string;
	setData: Dispatch<SetStateAction<string>>;
}

function InputSection({ setData, title, placeholder }: InputSectionProps) {
	const { TextArea } = Input;

	const [inputValue, setInputValue] = useState("");

	return (
		<div className="mb-3">
			<h2 className="italic underline mb-1">{title}</h2>
			<TextArea
				className=" bg-slate-700 placeholder:text-slate-500 &:focus:{box-shadow:0 0 0 2px rgba(0, 0, 255, 0.2) }"
				rows={4}
				placeholder={placeholder}
				onChange={(e) => setInputValue(e.target.value)}
			/>
		</div>
	);
}

export default InputSection;
